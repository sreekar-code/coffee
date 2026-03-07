# Agents

Guidelines for AI agents working on this codebase.

## Project

Static personal blog at sreekar.coffee. One CSS file (`styles.css`) shared across all pages. No build step, no framework, no JS. Open source.

## Rules

- **CSS changes go in `styles.css` only** — never inline styles in HTML
- **HTML edits only when explicitly requested** — e.g. adding a link, fixing content, not restructuring layout
- **No new dependencies** — no npm, no frameworks, no external CSS libraries
- **No new files** unless explicitly requested
- Preserve the dot grid background on `html`, warm cream palette, and handwritten font pairing (Caveat + Kalam)
- Keep the two-breakpoint model: tablet ≤768px, mobile ≤480px
- Do not remove the `p:has(> img)` photo frame styling — it handles image rotation and hover behaviour

## Navigation pattern

All pages share the same nav structure:
```
Home   Blog   Twitter
```
- Home and Blog are internal links; Twitter links externally to `https://x.com/sreekar_1729` (opens in new tab)
- The current page is rendered as plain text (no link)

## Footer

Source (GitHub repo) and RSS links appear on the **home page only** (`index.html`). Blog listing and post pages have no footer.

## Adding a new blog post

1. Copy `blog/cup-1.html` as a template
2. Update `<title>`, `<h1>`, `<p class="date">`, and content
3. Add a link entry at the top of `blog/index.html`
4. No CSS changes needed — all posts share `styles.css`
5. Pushing the new file to `main` auto-updates `rss.xml` via GitHub Actions

## RSS

- Feed: `rss.xml` (do not edit manually — it is generated)
- Generator: `generate_rss.py` — parses `<h1>`, `<p class="date">`, and first `<p>` inside `<section>` from each post
- Workflow: `.github/workflows/update-rss.yml` triggers on `blog/**.html` pushes, commits updated feed with `[skip ci]`
- To regenerate locally: `python3 generate_rss.py`

## Design tokens

| Token         | Value                          |
|---------------|--------------------------------|
| Background    | `#F8F2E8`                      |
| Text          | `#2C1A0E`                      |
| Accent        | `#8B4513`                      |
| Accent hover  | `#C4783A`                      |
| Muted text    | `#9A6040`                      |
| Dot grid      | `rgba(100, 55, 20, 0.15)` 24px |
| Display font  | Caveat (headings, title)       |
| Body font     | Kalam (all body text)          |

## Git

- Remote: `git@github.com:sreekar-code/coffee.git`
- Branch: `main`
- Always preview on `python3 -m http.server 3000` before pushing
