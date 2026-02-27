# Agents

Guidelines for AI agents working on this codebase.

## Project

Static personal blog at sreekar.coffee. One CSS file (`styles.css`) shared across all pages. No build step, no framework, no JS.

## Rules

- **Only edit `styles.css`** for design changes — never touch HTML structure
- **No new dependencies** — no npm, no frameworks, no external CSS libraries
- **No new files** unless explicitly requested
- Preserve the dot grid background on `html`, warm cream palette, and handwritten font pairing (Caveat + Kalam)
- Keep the single-breakpoint mental model: tablet ≤768px, mobile ≤480px

## Adding a new blog post

1. Copy the closest existing post in `blog/` as a template
2. Update title, date (`.date`), and content
3. Add a link entry at the top of `blog/index.html`
4. No CSS changes needed — all posts share `styles.css`

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
