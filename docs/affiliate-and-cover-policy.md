# Affiliate links and book covers

Checked against the linked primary sources on 2026-09-17. Marketplace-specific Amazon rules must be checked before activation.

## GitHub presentation

A book guide begins with its title, a modest cover image when the rights record is approved, and one related Amazon text link immediately underneath when configured. The link is labeled “affiliate link” and has a nearby disclosure. The rest of the page provides original educational material and usable resources.

[GitHub's advertising policy](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies#10-advertising-on-github) allows project-related images, links, and promotional text in READMEs. It also says advertising must not be the primary focus. There is no safe-harbor rule based on a number of links or words. We do not claim GitHub has preapproved this repository.

No banners, repeated purchase calls, unrelated products, promotional issues in other projects, or purchased/fake engagement. GitHub Pages has separate terms; this project does not enable Pages.

## Amazon configuration

The owner will provide the marketplace and their product links later. Until then, the repository has no active affiliate links and does not guess a tag or use someone else's.

Before activation, the owner must confirm that the repository URL is included in their Amazon account's site list and that their account/marketplace permits the intended placement. Influencer status does not itself establish approval for every external placement.

Use an owner-supplied Special Link for the matching title and edition. Keep its Amazon destination obvious. Do not publish stale prices, availability, copied customer reviews, or star ratings. Do not put affiliate links inside AI skill instructions, where they could be repeated in generated output without context.

The disclosure alongside configured links is: **As an Amazon Associate I earn from qualifying purchases.** Also label the link itself as an affiliate link. See the [Amazon operating agreement](https://affiliate-program.amazon.com/help/operating/agreement) and [program policies](https://affiliate-program.amazon.com/help/operating/policies).

## Cover rights and sources

A cover found online is not automatically licensed for reuse. Author/publisher promotional assets need a documented permission basis appropriate to this use. Amazon product images have their own acquisition, linking, storage, and display conditions; a scraped image URL or an affiliate tag is not permission to commit the image to Git.

Prefer a cover asset supplied or expressly allowed by the rights holder for an editorial guide. Record source URL, edition, credit, permitted use, permission evidence, and date in `.github/library/covers.json`. Keep any private permission correspondence outside the public repository and publish only the necessary evidence summary.

Do not alter a cover, remove a credit, imply endorsement, or include third-party art in the MIT license. Do not reproduce a publisher's workbook or diagrams as if they were our original templates.

Open Library provides a documented cover-embedding service for public pages. A `service-embed` record uses a direct `covers.openlibrary.org` image URL and credits the corresponding book record, following [its cover guidelines](https://openlibrary.org/dev/docs/api/covers). This is a documented service-display basis, not a claim that the artwork is public domain or that we hold a copyright license. Keep the image small, unmodified, and relevant to the guide; do not store or redistribute it as an MIT-licensed project asset.

If neither an approved asset nor a documented service embed is available, retain the cover slot and show a brief pending note in the draft. Do not disguise a generated title card as the real cover. Published guides require a documented cover-display basis and a truthful source-check record. A human-review credit requires actual human review.

If Amazon-supplied imagery is considered later, first verify the applicable [Program IP License](https://affiliate-program.amazon.com/help/operating/policies), including image handling and the principal-purpose conditions for API content. Static GitHub rendering and caching may not fit those conditions; licensed publisher artwork is the planned route.

## Current state

Affiliate account details: deferred by the owner. The Mom Test uses a verified Open Library thumbnail with a service-embedding record. Its buying-options link goes to the author's website until the owner's affiliate URL is supplied; no affiliate tag is invented.
