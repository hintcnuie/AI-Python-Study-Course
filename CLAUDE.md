# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A static HTML/CSS/JS personal handmade-craft blog website — "璐璐手作小屋" (Lulu's Handmade Cottage). Built as a university course assignment for a female college student. No frameworks, no build tools, no server — purely static files meant to be opened directly in a browser.

## Commands

There is no build/lint/test toolchain in this project. To preview:

```bash
open index.html   # macOS — opens in default browser
# or simply double-click index.html in Finder
```

To verify JS syntax after editing `js/main.js`:

```bash
node --check js/main.js
```

## Architecture

### Page template

Every page follows the same structure (in order):

1. **Announcement bar** — scrolling text banner (`<div class="announcement-bar">`)
2. **Navbar** — sticky logo + 8 nav links with mobile hamburger toggle (`<nav class="navbar">`)
3. **Main content** — either `hero` + `section` blocks (homepage) or `page-header` + `page-content` (sub-pages)
4. **Footer** — 4-column grid: about, quick nav, contact info, friend links; plus copyright bar
5. **Back-to-top button** — fixed bottom-right, appears on scroll > 400px
6. **Music toggle button** — fixed bottom-right (above back-to-top), dynamically injected by JS
7. **`<script src="../js/main.js">`** — always the last element before `</body>`

### CSS (`css/style.css`)

- Single stylesheet, shared by every page (~1200 lines)
- CSS custom properties defined in `:root` for colors, shadows, radii, transitions
- No CSS preprocessor or utility framework
- Layout patterns: `.card-grid` (auto-fill grid), `.detail-layout` (2-column for product detail), `.about-preview` (2-column for about), `.article-full` (centered max-width for diary posts)
- Responsive breakpoints at 768px and 480px
- Pink-warm-beige color palette: primary `#E8917E`, accent `#8BA888`, bg `#FFFBF7`

### JS (`js/main.js`)

Single JS file included on every page. Handles:

- Mobile nav toggle (hamburger menu)
- Active nav link detection from current URL
- Back-to-top button visibility + smooth scroll
- Guestbook form → localStorage read/write + render
- Contact form submission toast
- Gallery filter buttons (category show/hide)
- Link exchange / newsletter form toasts
- **Background music player** — Web Audio API, C-major scale, triangle wave + sparkle overtone, plays short ascending mini-melodies / chords / single notes at background volume (gain 0.10). Toggle button injected into DOM at load. State persisted via `localStorage` key `lulu_music`.

### Site structure (8 channels, each ≥ 3 pages)

| Channel | Directory | Sub-pages |
|---------|-----------|-----------|
| Home | `/` | index.html |
| About | `about/` | index, story, hobby |
| Dolls | `dolls/` | index, detail1, detail2, detail3 |
| Frames | `frames/` | index, detail1, detail2, detail3 |
| Gallery | `gallery/` | index, doll, frame |
| Diary | `diary/` | index, post1, post2, post3 |
| Guestbook | `guestbook/` | index, contact, messages |
| Links | `links/` | index, apply, recommend |

### Naming conventions (from course requirements)

- All file and folder names: **lowercase English only** (or lowercase + digits). No Chinese, punctuation, or special characters.
- Homepage must be `index.html` or `index.htm`.
- All links must use **relative paths**.
- Max directory depth: 3 levels.

## Privacy rule

The site author's full name (叶璐璐) must NOT appear anywhere. Use **璐璐** (given name only) in all visible text, meta tags, alt attributes, and footer copyright. This applies to all future edits.

## Known quirks

- Sub-page HTML files duplicate the full template (navbar, announcement bar, footer) rather than using includes. Editing a shared element means touching ~25 HTML files.
- The guestbook stores data in `localStorage` under key `lulu_guestbook` — no backend, no persistence across browsers.
- Detail pages (`dolls/detail*.html`, `frames/detail*.html`) have inline-minified footer/nav HTML rather than the indented format used on other pages.
- `images/works/` contains the 6 product photos (doll1-3.jpg, frame1-3.jpg, gallery1-2.jpg). Root-level `IMG_*.JPG` files appear to be raw camera imports, unused by the site.
- The `music/` directory contains only a README — the actual audio is generated procedurally via Web Audio API, no MP3 file needed.
