---
title: "Past Summits"
summary: "Annual summits of the International Contact Research Network."
date: 2026-09-18
type: "page"
markup: "html"
---
<style>
.article-container {
    max-width: 1140px;
}

.events-page {
    max-width: 1100px;
    margin: 0 auto;
}

.events-tabs {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 2.5rem;
}

.events-tab {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 0.95rem;
    font-weight: 500;
    color: #666;
    padding: 0.5rem 1.25rem;
    border-radius: 999px;
    transition: color 0.2s ease, background-color 0.2s ease;
}

.events-tab:hover {
    color: #007bff;
}

.events-tab.is-active {
    color: #007bff;
    background-color: rgba(0, 123, 255, 0.1);
}

.events-panel {
    display: none;
}

.events-panel.is-active {
    display: block;
}

.events-heading {
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 0.25rem 1rem;
    padding-bottom: 1.25rem;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid #d5d5d5;
}

.dark .events-heading {
    border-bottom-color: #495057;
}

.events-heading .events-year {
    font-family: 'Montserrat', sans-serif;
    font-size: 2.5rem;
    font-weight: 500;
    line-height: 1;
    color: #1a1a1a;
}

.events-heading .events-subtitle {
    font-size: 1rem;
    color: #666;
}

.dark .events-heading .events-year {
    color: #f1f3f5;
}

.events-section-label {
    margin-bottom: 0.5rem;
}

.events-concluded-label {
    margin-top: 0;
    margin-bottom: 0.25rem;
}

.events-organisers-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    gap: 1.5rem;
    margin: 0 0 3rem;
}

.events-organiser-card {
    text-align: center;
    width: 230px;
}

.events-organiser-card .events-organiser-avatar {
    width: 150px;
    height: 150px;
    max-width: 100%;
    object-fit: cover;
    margin-bottom: 0.5rem;
}

.events-organiser-name {
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    font-weight: 500;
}

.events-organiser-org,
.events-organiser-role {
    font-family: 'Montserrat', sans-serif;
    font-size: 0.7rem;
    color: #666;
    margin-top: 0.15rem;
}

.events-organiser-role .role-line {
    display: block;
    margin-top: 0.35rem;
}

.dark .events-organiser-org,
.dark .events-organiser-role {
    color: #adb5bd;
}

.events-contributors {
    line-height: 1.6;
    margin: 0 0 3rem;
}

.events-keynote-title {
    flex: 1;
    min-width: 220px;
    align-self: center;
    text-align: left;
    margin: 0;
}

.events-recap {
    line-height: 1.7;
    margin-bottom: 2rem;
    white-space: pre-line;
}

.events-photo-feature {
    margin: 0 0 1.25rem;
}

.events-photo-feature img {
    width: 100%;
    max-height: 480px;
    object-fit: cover;
    border-radius: 6px;
    display: block;
}

.events-photo-feature figcaption {
    font-size: 0.85rem;
    color: #777;
    margin-top: 0.4rem;
    text-align: center;
}

.dark .events-photo-feature figcaption {
    color: #adb5bd;
}

.events-gallery {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
    margin-bottom: 1rem;
}

@media (max-width: 500px) {
    .events-gallery {
        grid-template-columns: 1fr;
    }
}

.events-gallery-item {
    margin: 0;
}

.events-gallery-item.is-extra {
    display: none;
}

.events-gallery-item img {
    width: 100%;
    height: 360px;
    object-fit: cover;
    border-radius: 6px;
    display: block;
}

.events-gallery-item.is-square img {
    object-fit: contain;
    background: #f0f0f0;
}

.dark .events-gallery-item.is-square img {
    background: #2b2f33;
}

.events-gallery-item figcaption {
    font-size: 0.85rem;
    color: #777;
    margin-top: 0.4rem;
    text-align: center;
}

.dark .events-gallery-item figcaption {
    color: #adb5bd;
}

.events-gallery-toggle {
    display: block;
    margin: 0 auto 1.5rem;
    background: none;
    border: 1px solid #d5d5d5;
    border-radius: 999px;
    padding: 0.5rem 1.25rem;
    font-size: 0.85rem;
    color: #666;
    cursor: pointer;
    transition: color 0.2s ease, border-color 0.2s ease;
}

.events-gallery-toggle:hover {
    color: #007bff;
    border-color: #007bff;
}

.events-gallery-toggle.is-hidden {
    display: none;
}

.dark .events-gallery-toggle {
    border-color: #495057;
    color: #adb5bd;
}

.dark .events-gallery-toggle:hover {
    color: #64b5f6;
    border-color: #64b5f6;
}

.events-link {
    font-size: 0.9rem;
}

.events-placeholder {
    text-align: center;
    color: #777;
    padding: 3rem 1rem;
    font-size: 1.05rem;
}

.dark .events-tab {
    color: #adb5bd;
}

.dark .events-tab:hover {
    color: #64b5f6;
}

.dark .events-tab.is-active {
    color: #64b5f6;
    background-color: rgba(100, 181, 246, 0.15);
}

.dark .events-heading .events-subtitle {
    color: #adb5bd;
}

.dark .events-placeholder {
    color: #adb5bd;
}
</style>

<div class="events-page">

<div class="events-tabs" role="tablist">
    <button type="button" class="events-tab is-active" data-year="2024" role="tab" aria-selected="true">2024</button>
    <button type="button" class="events-tab" data-year="2025" role="tab" aria-selected="false">2025</button>
    <button type="button" class="events-tab" data-year="2026" role="tab" aria-selected="false">2026</button>
</div>

<div id="events-2024" class="events-panel is-active">

<div class="events-heading">
    <span class="events-year">2024</span>
    <span class="events-subtitle">30&ndash;31 May &middot; Birkbeck, University of London</span>
</div>

<h2 class="events-section-label">Organisers</h2>

<div class="events-organisers-grid">
{{< organiser "michele" >}}
{{< organiser "libby" >}}
{{< organiser "lukas" >}}
</div>

<h2 class="events-section-label events-concluded-label">Recap</h2>

<div class="events-recap">
We just completed the inaugural summit of the new international Contact Research Network - thanks to the amazing colleagues who spent the last 2 days with us in London at Birkbeck!

Our conversations highlighted some priorities and opportunities for future research:
Contact interventions can promote understanding in schools (Lindsey), at work (Libby) and in conflict situations (Orkun), and reduce political polarisation (Michèle).
Contact in everyday life may also promote understanding, yet we need to further explore how to create successful interactions (Stefania, Deborah &amp; Patrick).
There are promising opportunities to use new technologies to promote contact and better intergroup relations - from VR to chatbots (Lukas).

We were particularly excited to also hear from early career researchers who will help shape the future of our research field (Jie, Zackary, Diana, Emine and Ditte).

We struck up various new collaborations and can't wait to see them play out - and to have further contact researchers join us on the journey ahead.
</div>

<div class="events-gallery" data-gallery="2024" data-visible="6">
    <figure class="events-gallery-item">
        <img src="/media/events/2024/organisers.jpg" alt="The three summit organisers, Michèle Birtel, Libby Drury and Lukas Wallrich, at Birkbeck">
        <figcaption>Libby, Michèle &amp; Lukas</figcaption>
    </figure>
    <figure class="events-gallery-item">
        <img src="/media/events/2024/dinner.jpg" alt="Summit participants at the group dinner">
        <figcaption>The group at dinner</figcaption>
    </figure>
</div>
<button type="button" class="events-gallery-toggle is-hidden" data-gallery-toggle="2024">Show more</button>

</div>

<div id="events-2025" class="events-panel">

<div class="events-heading">
    <span class="events-year">2025</span>
    <span class="events-subtitle">2&ndash;3 June &middot; Mary O&rsquo;Brien Room, Lady Margaret Hall, University of Oxford</span>
</div>

<figure class="events-photo-feature">
    <img src="/media/events/2025/group.jpg" alt="Summit participants outside Lady Margaret Hall, University of Oxford">
    <figcaption>The group at Lady Margaret Hall</figcaption>
</figure>

<h2 class="events-section-label">Organisers</h2>

<div class="events-organisers-grid">
{{< organiser "shelley" >}}
{{< organiser "lukas" >}}
</div>

<h2 class="events-section-label">Keynote Speaker</h2>

<div class="events-organisers-grid">
{{< organiser "stefania" >}}
<p class="events-contributors events-keynote-title">Keynote lecture: Social cohesion through positive and negative intergroup contact: Retracing the generative and stressful journey of minority academic dissent</p>
</div>

<h2 class="events-section-label events-concluded-label">Recap</h2>

<div class="events-recap">
We had a fantastic day at this year's ICRN Summit, held at the University of Oxford.

A huge thank you to Shelley McKeown Jones for hosting us, and to Stefania Paolini, who delivered a brilliant keynote address, with Sylvie Graf offering insightful reflections as discussant. The event featured 24 engaging presentations, as well as vibrant networking and idea exchange throughout the day.

Key highlights:
&bull; 33 in-person and 23 online participants
&bull; A special session focused on shaping the ICRN&rsquo;s vision, mission, and future activities
&bull; Some sessions, including the keynote, were recorded and will be shared once finalised

We were also pleased to welcome Stefania Paolini as our new Chair. We warmly thank Michèle Denise Birtel for her dedicated leadership over the past year.

During the meeting, Stefania (Paolini), Lukas (Wallrich) and Rita (Guerra), in their roles as network chairs and secretary, suggested a blueprint for the ICRN network&rsquo;s governance and constitution moving forward, anchored on the guiding principles of &lsquo;diversity of people&rsquo;, &lsquo;diversity of ideas&rsquo;, &lsquo;respectful and equitable cooperation&rsquo;, and &lsquo;high ethical standards&rsquo;. The Oxford meeting acted as a kickstart to the conversation about these themes and the future of the network, which we hope to progress with in the remainder of the year, involving all members of the network irrespective of their attendance of the last Summit. So watch this space and remain engaged in upcoming consultation efforts.
</div>

<div class="events-gallery" data-gallery="2025" data-visible="6">
    <figure class="events-gallery-item is-square">
        <img src="/media/events/2025/talks.jpg" alt="Presenters at the 2025 summit">
        <figcaption>Presentations throughout the day</figcaption>
    </figure>
</div>
<button type="button" class="events-gallery-toggle is-hidden" data-gallery-toggle="2025">Show more</button>

</div>

<div id="events-2026" class="events-panel">

<div class="events-heading">
    <span class="events-year">2026</span>
    <span class="events-subtitle">5&ndash;7 July &middot; FernUniversit&auml;t Campus Centre, Karlsruhe, Germany</span>
</div>

<figure class="events-photo-feature">
    <img src="/media/events/2026/group2.jpg" alt="Summit participants at the FernUniversität Campus Centre, Karlsruhe">
    <figcaption>The group in Karlsruhe</figcaption>
</figure>

<h2 class="events-section-label">Organisers</h2>

<div class="events-organisers-grid">
{{< organiser "emine" >}}
{{< organiser "maria-therese" >}}
{{< organiser "patrick" >}}
</div>

<h2 class="events-section-label">Keynote Speaker</h2>

<p class="events-contributors">Prof. Cara McInnis<br>Professor, Acadia University<br>Keynote lecture: Art Imitates Life: Reflexive Reflections on My Intergroup Contact Era</p>

<h2 class="events-section-label">Contributors</h2>

<p class="events-contributors">Stefania Paolini, Lukas Wallrich, Libby Drury, Molly Adams, Rita Guerra, Jie Huang, Shelley McKeown Jones, Oliver Christ, Mathias Kauff, Sarina Sch&auml;fer, Jil Ullenboom, Lydia Tschekorsky Orloff, and Sebastian Emrys Kalkuhl.</p>

<h2 class="events-section-label events-concluded-label">Recap</h2>

<div class="events-recap">
We had our third annual ICRN Summit this July, and it really was a wonderful few days. From July 5th&ndash;7th, we gathered at the FernUniversit&auml;t Campus Centre in Karlsruhe, Germany. 53 researchers joined us in person and 20 more joined online, coming together from across the field to share ideas, data, and a lot of coffee.

The Summit opened with an optional mentoring session, where more experienced researchers offered guidance and support to students and early-career members, and everyone had a chance to connect one-on-one before the formal programme began. Over the three days, we hosted 24 research presentations covering everything from predictors of contact and contact willingness to contact dynamics over time and the effects of contact on outcomes beyond prejudice. We were lucky to have Cara McInnis deliver this year's keynote lecture, "Art Imitates Life: Reflexive Reflections on My Intergroup Contact Era," which set a thoughtful tone for the rest of the Summit. Slides from presenters who agreed to share are available on <a href="https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Flink.sbstck.com%2Fredirect%2Fe56a122a-3a10-4115-a088-35562bf75d95%3Fj%3DeyJ1IjoiNHFxaDNlIn0.G8VaxZFSVKH5GJC6HyJJ3gK0dUPpi_VqngCBZDCJufw&data=05%7C02%7Cjie.huang3%40durham.ac.uk%7C9300d8071de94414e66808dee3c71e55%7C7250d88b4b684529be44d59a2d8a6f94%7C0%7C0%7C639198641538727831%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=mnxlUgzcVOIcA1CtVvlYHXcRU%2BKu6CO9PUtrtWXJxAw%3D&reserved=0" target="_blank" rel="noopener">OSF</a>.

Alongside the formal talks, the Summit featured a poster session, open unconferencing discussions where participants shaped the agenda in real time, and open collaboration space for building new partnerships and research ideas. As always, the goal wasn't just to present finished work, but to spark the kind of conversations that lead to it.

This year, we also introduced our first-ever Early Career Researcher Awards. Matilde Tassinari won Best Blitz Presentation, with Mamoru Sakura as runner-up. Zaya Da Silva won Best Poster, and Aaron Lauterbach won Best Oral Presentation, with Marta Sih Wei Macaluso as runner-up. Congratulations to all five for such strong work!

Beyond the research, the Summit made plenty of room for connecting outside the sessions too. On the first evening, we headed to dinner together, and on the second day we swapped the conference room for a picnic in the Castle Gardens. We also introduced something new this year: Contact Bingo, a game we developed ourselves to get people talking, laughing, and making new connections across the group.

None of this happens without a lot of work behind the scenes. A special thank you to this year's organisers, Emine Bilgen, Maria-Therese Friehs, and Patrick Kotzur, for putting the Summit together, and to the wider committee and everyone who contributed along the way.

A big thank-you to Mark Rubin for sharing a lovely Bluesky thread capturing the atmosphere of the Summit &mdash; check it out <a href="https://bsky.app/profile/markrubin.bsky.social/post/3mpvuk6kqqc2r" target="_blank" rel="noopener">here</a>.

The Summit continues to grow each year, and we're already looking forward to seeing where the ICRN community takes it next.
</div>

<div class="events-gallery" data-gallery="2026" data-visible="6">
    <figure class="events-gallery-item is-square">
        <img src="/media/events/2026/collage.jpg" alt="Moments from the 2026 summit: presentations, unconferencing, the picnic and dinner">
        <figcaption>Moments from the Summit</figcaption>
    </figure>
</div>
<button type="button" class="events-gallery-toggle is-hidden" data-gallery-toggle="2026">Show more</button>

</div>

</div>

<script>
(function () {
    var tabs = document.querySelectorAll('.events-tab');
    var panels = document.querySelectorAll('.events-panel');

    tabs.forEach(function (tab) {
        tab.addEventListener('click', function () {
            var year = tab.getAttribute('data-year');

            tabs.forEach(function (t) {
                t.classList.remove('is-active');
                t.setAttribute('aria-selected', 'false');
            });
            tab.classList.add('is-active');
            tab.setAttribute('aria-selected', 'true');

            panels.forEach(function (p) {
                p.classList.remove('is-active');
            });
            document.getElementById('events-' + year).classList.add('is-active');
        });
    });

    var galleries = document.querySelectorAll('.events-gallery');

    galleries.forEach(function (gallery) {
        var id = gallery.getAttribute('data-gallery');
        var visible = parseInt(gallery.getAttribute('data-visible'), 10) || 6;
        var items = gallery.querySelectorAll('.events-gallery-item');
        var toggle = document.querySelector('[data-gallery-toggle="' + id + '"]');

        if (items.length <= visible) {
            if (toggle) {
                toggle.classList.add('is-hidden');
            }
            return;
        }

        items.forEach(function (item, index) {
            if (index >= visible) {
                item.classList.add('is-extra');
            }
        });

        if (toggle) {
            toggle.classList.remove('is-hidden');
            toggle.textContent = 'Show ' + (items.length - visible) + ' more';

            toggle.addEventListener('click', function () {
                var expanded = gallery.classList.toggle('is-expanded');

                if (expanded) {
                    items.forEach(function (item) { item.classList.remove('is-extra'); });
                    toggle.textContent = 'Show less';
                } else {
                    items.forEach(function (item, index) {
                        item.classList.toggle('is-extra', index >= visible);
                    });
                    toggle.textContent = 'Show ' + (items.length - visible) + ' more';
                }
            });
        }
    });
})();
</script>
