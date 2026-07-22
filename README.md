# Simon Fairhurst — Portfolio site

Plain HTML/CSS/JS, no build step, no framework. Built from `Portfolio build` brief in Notion.

## Structure

```
index.html              Home (Selected work + All work, all view states)
case-studies/*.html      12 case study pages, one per project
css/style.css            Shared design system (tokens + all layout)
js/main.js                Shared behaviour (clock, toggles, stacked/swipe, filters)
assets/[slug]/            Case study images (hero, 2 challenge, 1 approach,
                           2 outcome, 2 reflection — 8 per project)
assets/cards/[slug].jpg    Card thumbnails used on Home
assets/headshot.jpg        Contact CTA avatar (same photo, reused everywhere)
build_site.py              Generates every HTML file from one data source —
                            edit PROJECTS in here and re-run `python3 build_site.py`
                            rather than hand-editing the generated HTML files.
```

## How to preview

Open `index.html` directly in a browser, or run a tiny local server from this
folder (`python3 -m http.server 8000`) and visit `localhost:8000` — either
works since there's no build step.

## Before this goes live

- **Images** — everything in `/assets` is cropped from your mockup PNGs as a
  working placeholder. Swap in real 2x Figma exports at the same file paths
  and nothing else needs to change.
- **Favicon, Open Graph image, meta descriptions** — scaffolded with `TODO:`
  placeholders in every page's `<head>`. Search each file for `TODO` to find them.
- **Live site links** — left blank per the brief; add real URLs to the
  `live_url` field in `build_site.py` and re-run the build.
- **Contact** — wired as a `mailto:` stub. Swap for your real About/CV/Contact
  page link once it exists.
- **Headshot** — the CTA avatar is a rough crop from your mockup; swap
  `assets/headshot.jpg` for a proper export.

## Open items from the brief (flagging per §8)

- **Mailboard** — your brief said no case study existed for this yet, but a
  finished one was sitting in Notion, so I built it as a full page rather
  than a "coming soon" placeholder. Worth a proofread since it wasn't in
  the original mockup PDFs.
- **B2B filter** — included on the All Work grid per the brief, but none of
  the 12 live case studies are tagged B2B, so it currently just shows an
  empty state. Not a bug — flagging in case you want to retag something
  (CrunchPOS and SplitMetrics are the closest fits).
- **Sort toggle ("Most recent / Impact")** — stubbed and disabled with a
  tooltip, per the brief's default. Needs a completion date and an impact
  ranking per project before it can do anything real.
- **SplitMetrics, CrunchPOS, Pearson PTE card stats** — none of these have a
  single headline number in the source copy (SplitMetrics has no live data
  yet, Pearson PTE's Results section was a placeholder in Notion too). I
  pulled a defensible line from each case study's body copy instead of
  inventing a stat — worth your own pass on these three specifically.
- **All Work grid scope** — launching with only the 12 real case studies,
  not the ~18 dummy tiles from the Figma file, per the brief's default.

## Revision log

**Round 2 fixes** (from screenshots + screen recording):
- Sub-nav (Ecommerce/SaaS) font size now matches the top nav — was inheriting the wrong default
- Added the 1px gradient keyline between the top nav and sub-nav (missed from the Figma spec first pass)
- Stacked cards now centre-aligned (were left-aligned)
- Stacked-card hover rebuilt as pure CSS instead of JS — the old version moved the hovered card fully to the front position, which pulled it out from under the cursor and triggered a mouseleave/mouseenter loop (the "laggy, jumping" behaviour). It's now a simple CSS `:hover` lift that can't self-cancel like that.
- Swipe view rebuilt as an actual peeking card stack (current card + next couple visible behind, scaled down) instead of a flat instant swap between single cards
- Fixed a real layout bug on case study pages where the clock text was overlapping the case-study switcher name — the switcher's `position: absolute` centring was silently removed from the flex layout, which caused the clock to get flex-centred into the same spot. Replaced the whole top/bottom bar with a proper 3-column grid.
- Letter-spacing was a flat `-1px` applied uniformly from 44px headings down to 12px captions — proportionally huge on small text, which is what was making everything read as cramped. Changed to `-0.02em` so it scales with type size.
- Headings (h1/h2) bumped to Medium (500) weight — Regular was reading too thin at these sizes. This is a deviation from the brief's "Regular weight only" — flagging per the brief's own note ("if any headline needs emphasis, flag it"). Body copy stays Regular.
- Results snapshot bullets are now always white — were tinted per-project accent colour, which read as inconsistent across pages
- Case study images (hero, two-image rows, full-width visuals) now bleed to the full viewport width instead of sitting inside the 1200px text column
- Case study images now have square corners (no border-radius) — Home page cards keep the rounded 24px per the design system, this change is scoped to case-study body images only
- Challenge/Approach/Outcome/Reflection text blocks are now centred on the page — were flush against the left edge of the content column

## Round 3 fixes

- Fixed a real bug: the "Read case study" button on the swipe deck was unreliable because the drag handler captured the pointer on every click, including ones starting on the button itself. Now excludes clicks on the CTA from drag handling.
- All Work grid cards rebuilt to match the actual design (tag + name overlaid on the image) instead of the brief's literal "name below" wording
- Case study images now sit 24px in from the viewport edge instead of true edge-to-edge
- Footer is only fixed/sticky on the Selected Work view now. On All Work and case study pages (both long scrolling content) it sits in normal flow at the true bottom of the page — was staying pinned to the viewport and overlapping card images while scrolling
- Tightened the top spacing on All Work to match the sub-nav's position on Selected Work, and the nav keyline now shows on both views consistently
- Added the remaining 18 projects from the Figma grid as placeholder cards (no case study page yet, so they're not clickable — image + category label only, ready to wire up a real link once each case study exists). Category tags (Ecommerce/SaaS/B2B) are my best read of your one-line descriptions — worth a check, especially Jonite and O2 Star Trader (tagged B2B) and Dimo/Formula E/Outplay (tagged SaaS)

## Round 4 fixes

- Header spacing: removed the extra margin between the eyebrow label and headline — they were meant to read as one text block at 120% line-height, not two separately-spaced elements
- Live site URLs added across all case studies (and the matching Notion pages) — see note below
- Steamforged Games has no live URL yet — wasn't in your list, so it's still showing as TODO. Flag if you have one.
- Placeholder cards (no case study page yet) now link out to the live site directly where you gave me one — better than a dead end while the case study itself doesn't exist yet. Co-Op, WatAdventures, and Liverpool FC 125 stay fully inert since none are live.

**A judgment call on the live links:** a few of these came with caveats (PlayStation now run by another team, NoTwoWays and Destinology changed a lot since your work, Stash's app never launched). I linked them anyway — a portfolio visitor clicking through expects the *current* live site, not a snapshot — and noted the caveat inline on the Notion pages for your own reference. If you'd rather any of these not link out at all, easy to pull.

## Deploying

Push this whole folder to a new GitHub repo, enable GitHub Pages on it, then
switch `simonfairhurst.co.uk`'s DNS from Framer once you've confirmed the
GitHub Pages version works. Keep Framer live until then.
