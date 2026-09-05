---
title: "Connect with us"
layout: "contact"
design:
  columns: '1'
---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">

<style>
.contact-connect {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.contact-connect p {
    white-space: nowrap;
}

@media (max-width: 600px) {
    .contact-connect p {
        white-space: normal;
    }
}

.contact-connect p {
    margin-bottom: 1.5rem;
}

.contact-social-links {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 2.5rem;
    margin-bottom: 2rem;
}

.contact-social-links a {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    color: #1a1a1a;
    text-decoration: none;
    transition: color 0.2s ease, transform 0.2s ease;
}

.contact-social-links a:hover {
    color: #06805E;
    transform: translateY(-2px);
}

.contact-social-links i {
    font-size: 2rem;
    line-height: 1;
}

.contact-social-links span {
    font-size: 0.9rem;
}

.contact-divider {
    border: none;
    border-top: 1px solid #d5d5d5;
    background: none;
    background-image: none;
    height: 0;
    margin: 0.5rem auto 1.5rem;
    max-width: 260px;
}

.dark .contact-social-links a {
    color: #f1f3f5;
}

.dark .contact-social-links a:hover {
    color: #64b5f6;
}

.dark .contact-divider {
    border-top-color: #495057;
    background: none;
    background-image: none;
}
</style>

<div class="contact-connect">

<p>Follow our <a href="https://contactresearch.substack.com/" target="_blank" rel="noopener">latest news</a> and research on social media, or <a href="get_involved">get involved</a> with the network.</p>

<div class="contact-social-links">
    <a href="https://bsky.app/profile/contactresearch.bsky.social" target="_blank" rel="noopener" aria-label="Bluesky">
        <i class="ti ti-brand-bluesky" aria-hidden="true"></i>
        <span>Bluesky</span>
    </a>
    <a href="https://www.linkedin.com/company/international-contact-research-network" target="_blank" rel="noopener" aria-label="LinkedIn">
        <i class="ti ti-brand-linkedin" aria-hidden="true"></i>
        <span>LinkedIn</span>
    </a>
    <a href="https://www.youtube.com/@ContactResearchNetwork" target="_blank" rel="noopener" aria-label="YouTube">
        <i class="ti ti-brand-youtube" aria-hidden="true"></i>
        <span>YouTube</span>
    </a>
</div>

<hr class="contact-divider">

<p>Questions? Email us at <a href="mailto:contactresearchnetwork@gmail.com">contactresearchnetwork@gmail.com</a></p>

</div>
