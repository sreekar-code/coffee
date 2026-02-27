# sreekar.coffee

A personal coffee blog documenting AeroPress brewing experiments — recipes, tasting notes, café visits, and coffee rabbit holes.

## Stack

- Vanilla HTML + CSS (no frameworks)
- [Umami](https://umami.is) for privacy-friendly analytics
- Static hosting

## Structure

```
├── index.html          # Home
├── socials.html        # Socials
├── styles.css          # All styles (single shared sheet)
├── images/
└── blog/
    ├── index.html      # Post listing
    ├── cup-*.html      # Brewing logs
    └── notes-*.html    # Coffee notes
```

## Design

Coffee journal aesthetic — warm cream background (`#F8F2E8`), dot grid, handwritten fonts (Caveat + Kalam), minimal layout. No build step, no dependencies.

## Local dev

```bash
python3 -m http.server 3000
```
