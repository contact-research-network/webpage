import pandas as pd
import requests
from datetime import datetime
import re
import unicodedata
import json
import os
import time
from urllib.parse import quote

list_duration = 3 # how many years should be included prior to the current year
records_file = 'publication_records.json' # last good Crossref records, kept when a request fails
crossref_fields = ['DOI', 'title', 'author', 'container-title', 'group-title', 'created', 'published', 'published-online', 'published-print']
crossref_pause = 0.4 # seconds between requests, to stay below Crossref's limit of 3 per second
crossref_attempts = 6

# Authors who share a surname and first initial with a member but are a different person
non_members = {'b keith payne'}

def download_csv(url):
    return pd.read_csv(url)

def crossref_get(url, params, email):
    # Returns the response message, or None if Crossref cannot provide it
    for attempt in range(crossref_attempts):
        time.sleep(crossref_pause)
        wait = 2 ** attempt
        try:
            response = requests.get(url, params={**params, 'mailto': email}, timeout=60)
            if response.status_code == 200:
                return response.json()['message']
            if response.status_code != 429 and response.status_code < 500:
                return None
            retry_after = response.headers.get('Retry-After', '')
            wait = int(retry_after) if retry_after.isdigit() else wait
        except (requests.RequestException, ValueError, KeyError) as error:
            print('Crossref request failed:', error)
        time.sleep(min(wait, 60))
    return None

def trim_record(item):
    record = {field: item[field] for field in crossref_fields if field in item}
    if 'author' in record:
        record['author'] = [{key: author[key] for key in ('given', 'family', 'name', 'ORCID') if key in author}
                            for author in record['author']]
    return record

def fetch_publications(orcid, email):
    # Returns all works for an ORCID, or None if any page could not be retrieved
    current_year = datetime.now().year
    params = {
        'filter': f"orcid:{orcid},from-pub-date:{current_year-list_duration-1}-01-01,until-pub-date:{current_year}-12-31",
        'select': ','.join(crossref_fields),
        'rows': 1000,
        'cursor': '*',
    }
    items = []
    while True:
        message = crossref_get('https://api.crossref.org/works', params, email)
        if message is None:
            return None
        items.extend(message['items'])
        if not message['items'] or len(items) >= message['total-results']:
            return items if len(items) >= message['total-results'] else None
        params['cursor'] = message['next-cursor']

def load_records():
    if os.path.exists(records_file):
        with open(records_file, encoding='utf-8') as file:
            return json.load(file)
    return {'orcids': {}, 'items': {}}

def save_records(records):
    with open(records_file, 'w', encoding='utf-8') as file:
        json.dump(records, file, ensure_ascii=False, indent=1, sort_keys=True)

def update_member_records(records, orcids, email):
    # Replaces a member's stored works only after a complete, non-empty response
    works_by_orcid, kept = {}, []
    for orcid in dict.fromkeys(filter(None, map(clean_orcid, orcids))):
        print('Retrieving publications for ORCID:', orcid)
        items = fetch_publications(orcid, email)
        stored = records['orcids'].get(orcid, [])
        if items is None or (not items and stored):
            works_by_orcid[orcid] = stored
            kept.append(orcid)
            continue
        records['items'].update({item['DOI'].lower(): trim_record(item) for item in items})
        works_by_orcid[orcid] = sorted(item['DOI'].lower() for item in items)
    records['orcids'] = works_by_orcid
    if kept:
        print(f"::warning::Kept stored publications for {len(kept)} ORCIDs after Crossref failures: {', '.join(kept)}")

def format_author_list(authors):
    if len(authors) > 1:
        # Join all but the last author with a comma, then add the last author with an ampersand
        authors_str = ', '.join(authors[:-1]) + ' & ' + authors[-1]
    else:
        # If there's only one author, no need for a comma or an ampersand
        authors_str = authors[0] if authors else ''
    return authors_str

def get_year(item):
    fields = ['published-print', 'published-online', 'published', 'created']
    for field in fields:
        if field in item and 'date-parts' in item[field] and item[field]['date-parts'][0][0]:
            year = item[field]['date-parts'][0][0]
            if re.match(r'^\d{4}$', str(year)):
                return year
    return None 

def extract_year_ref(reference):
    match = re.search(r'\((\d{4})\)', reference)
    if match:
        return int(match.group(1))
    return None

def name_parts(name):
    # Lower-case words without diacritics, so that Uluğ matches Ulug
    name = unicodedata.normalize('NFKD', name.translate(str.maketrans('łŁıđĐøØ', 'lLidDoO')))
    name = ''.join(char for char in name if not unicodedata.combining(char))
    return re.findall(r'[a-z]+', name.casefold())

def surname_key(surname):
    # Also treats transliterated umlauts as equal, so that Schaefer matches Schäfer
    return re.sub(r'([aou])e', r'\1', ''.join(name_parts(surname)))

def clean_orcid(orcid):
    match = re.search(r'\d{4}-\d{4}-\d{4}-\d{3}[\dX]', str(orcid).upper())
    return match.group() if match else None

def index_members(group_members):
    names_by_orcid, given_names_by_surname, given_names_by_surname_word = {}, {}, {}
    for _, member in group_members.fillna('').iterrows():
        surname, given_names = member['Last name'], name_parts(member['First name'])
        if given_names:
            given_names_by_surname.setdefault(surname_key(surname), []).append(given_names)
            for word in name_parts(surname):
                if len(word) > 3: # Skips particles such as van and da
                    given_names_by_surname_word.setdefault(word, []).append(given_names)
        orcid = clean_orcid(member['ORCiD'])
        if orcid:
            names_by_orcid.setdefault(orcid, set()).update(name for name in given_names + name_parts(surname) if len(name) > 1)
    return names_by_orcid, given_names_by_surname, given_names_by_surname_word

def given_names_match(author_given, member_given):
    return author_given[0][0] == member_given[0][0] or any(len(name) > 1 and name in author_given for name in member_given)

def full_words_match(full_name, given_names_by_surname_word):
    # Catches surnames recorded differently, such as Lytkina for Widmer-Lytkina
    return any(len(name) > 1 and name != word and name in full_name
               for word in set(full_name)
               for member_given in given_names_by_surname_word.get(word, [])
               for name in member_given)

def is_member(author, names_by_orcid, given_names_by_surname, given_names_by_surname_word):
    author_given = name_parts(author.get('given', ''))
    full_name = author_given + name_parts(author['family'])
    if ' '.join(full_name) in non_members:
        return False
    # Crossref occasionally attaches an ORCID to the wrong co-author, so part of the name must agree too
    if names_by_orcid.get(clean_orcid(author.get('ORCID')), set()) & set(full_name):
        return True
    if full_words_match(full_name, given_names_by_surname_word):
        return True
    return bool(author_given) and any(given_names_match(author_given, member_given)
                                      for member_given in given_names_by_surname.get(surname_key(author['family']), []))

def format_citation(items, group_members):
    print('Generating reference list')
    member_index = index_members(group_members)
    # Remove duplicates and sort by creation date
    unique_items = {item['DOI']: item for item in items}
    sorted_items = sorted(unique_items.values(), key=lambda x: x['created']['timestamp'], reverse=True)

    # Remove duplicate titles and retain newest version
    unique_titles = {}

    for item in sorted_items:
        title = item.get('title', [''])[0].strip().lower()
        timestamp = item['created']['timestamp']

        if title not in unique_titles or timestamp > unique_titles[title]['created']['timestamp']:
            unique_titles[title] = item

    sorted_items = sorted(unique_titles.values(), key=lambda x: x['created']['timestamp'], reverse=True)

    keyword_pattern = re.compile(r'contact|friendship|intergroup', re.IGNORECASE)

    contact_research = []
    other_research = []

    for item in sorted_items:
        authors = []
        for author in item.get('author', []):
          if 'family' in author:
              family_name = author['family']
              author_str = f"{family_name}, {' '.join([i[0]+'.' for i in author.get('given', '').split()])}"
              if is_member(author, *member_index):
                  author_str = f"<span class='member'>{author_str}</span>"
              authors.append(author_str)
          elif 'name' in author:
              name = author['name']
              if name in group_members['Last name'].values:
                  name = f"<span class='member'>{name}</span>"
              authors.append(name)

        if not authors:
            continue
        
        authors_str = format_author_list(authors)
        title = item.get('title', [''])[0]
        container_title = item.get('container-title', [''])[0] if item.get('container-title', ['']) else ''
        if not container_title:
            container_title = item.get('group-title', ['']) if item.get('group-title', ['']) else ''
        container_format = f"*{container_title}*" if container_title else ''
        year = get_year(item)
        
        if year < datetime.now().year - list_duration:
            continue
        
        doi_url = f"https://doi.org/{item['DOI']}"
        
        # Ensure the title ends with exactly one period
        final_title = title if title.endswith(('.', '!', '?')) else title + '.'
        
        entry = f"- {authors_str} ({year}). **{final_title}** {container_format} [{doi_url}]({doi_url})"
        
        # Decide which list to append to based on title keywords
        if keyword_pattern.search(title):
            contact_research.append(entry)
        else:
            other_research.append(entry)
    
    contact_research = sorted(contact_research, key=extract_year_ref, reverse=True)
    other_research = sorted(other_research, key=extract_year_ref, reverse=True)

    return contact_research, other_research
  
def process_manual_additions(records, addition_df, email):
    print('Processing manual additions')
    dois = addition_df['DOI'].astype(str).str.strip().str.lower()
    out_dois = set(dois[addition_df['Action'] == 'out'])
    in_dois = set(dois[addition_df['Action'] == 'in'])

    # Only DOIs that are not stored yet need a request
    for doi in sorted(in_dois - set(records['items'])):
        message = crossref_get(f"https://api.crossref.org/works/{quote(doi)}", {}, email)
        if message:
            records['items'][doi] = trim_record(message)

    # Keep only records that are still in use, leaving out DOIs marked as 'out'
    member_dois = {doi for works in records['orcids'].values() for doi in works}
    records['items'] = {doi: item for doi, item in records['items'].items() if doi in member_dois | in_dois}
    return [item for doi, item in records['items'].items() if doi not in out_dois]

def main(email, orcid_url, additions_url):
    orcid_df = download_csv(orcid_url)
    addition_df = download_csv(additions_url)
    records = load_records()
    update_member_records(records, orcid_df['ORCiD'], email)
    all_items = process_manual_additions(records, addition_df, email)
    save_records(records)

    if all_items:
        contact_research, other_research = format_citation(all_items, orcid_df)
        with open("content/publication_list/_index.md", "w") as file:
            file.write("# Contact Research by Network Members\n")
            file.write("\n\n Note that this list is automatically generated and may not be exhaustive (or entirely accurate). Authors <span class='member'>highlighted like this</span> are members of the International Contact Research Network.\n\n")
            file.write("\n\n".join(contact_research))
            file.write("\n\n# Other Research by Network Members\n")
            file.write("\n".join(other_research))
            
if __name__ == "__main__":
    main('lukas.wallrich@gmail.com', 
      'https://docs.google.com/spreadsheets/d/e/2PACX-1vRquajekw2qmXA6XhKsf5YQ4z4llRTrFuqkZzjQTS3TCh1MLUV-uQeLddmTeXceABCrdRXpjGDWbJp5/pub?gid=569779606&single=true&output=csv',
      'https://docs.google.com/spreadsheets/d/e/2PACX-1vQbvk04Bi6A5a3BHxZ-b4FDZubqUxXR7wUnC33PMjnXmVhcDf40otCapWI9ioN2hLalDGqI1B-K7Z8t/pub?output=csv')
