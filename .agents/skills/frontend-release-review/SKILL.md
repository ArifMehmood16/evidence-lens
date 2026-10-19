---
name: frontend-release-review
description: Review an EvidenceLens frontend release for public versus private indexing, accessibility, SEO, mobile behavior, and performance. Use when frontend routes, metadata, assets, or deployment behavior change.
license: Apache-2.0
---

# Review a frontend release

Read the frontend section of ../../../docs/engineering-standards.md. Use the selected framework's routing, metadata, image, and accessibility capabilities before adding custom equivalents.

1. Classify routes: public indexable pages, intentionally non-indexable public pages, authenticated practitioner content, and staging. Authentication controls private access; noindex and robots.txt do not.
2. For indexable pages, inspect rendered titles, descriptions, canonical URLs, one main H1 and logical heading hierarchy, clean slugs, internal links, accurate structured data, and Open Graph metadata/images. The sitemap contains only canonical, indexable public URLs.
3. Inspect robots/noindex behavior deliberately. Do not remove noindex from private or staging content. Crawlers need access to observe noindex; robots blocking alone does not reliably prevent URL indexing.
4. Check keyboard navigation, focus, labels, contrast, responsive layout, error/loading states, and image alternatives. Decorative images use empty alt text. Check applicable WCAG 2.2 AA criteria with automation plus manual interaction.
5. Check broken links and asset sizes. Use responsive compressed images and measure Core Web Vitals under representative conditions. Label lab results; field results require actual traffic.
6. Verify HTTPS and deployment-specific metadata. Search Console verification requires the real property and authorized access. Do not claim it is complete from configuration alone.
7. Report findings with affected routes and evidence. Propose useful content/community distribution for backlinks; do not purchase links, send messages, or publish outreach without authorization.

If no frontend exists, maintain acceptance criteria rather than generating an unsolicited website.
