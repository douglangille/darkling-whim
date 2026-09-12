---
permalink: /style-guide/
title: "Style Guide"
excerpt: "Internal reference: exercises every color token and mode-sensitive component on the site, for checking light/dark rendering."
author_profile: false
sitemap: false
search: false
share: false
comments: false
---

Internal reference page — not linked in nav. Exists to exercise every color token and hand-derived light/dark override in `main.scss` in one place, so both modes can be checked at a glance without hunting through posts. See `darkling-whim/DESIGN.md` for the token table and the math behind each derived value.

## Typography

# Heading 1 — Special Elite
## Heading 2 — Special Elite
### Heading 3 — Special Elite

Body copy is Cutive, 1rem, 1.75 line-height, with letter/word-spacing opened up to counter Cutive's naturally tight default set. This paragraph exists to check that the body font, text color, line spacing, and letter/word-spacing all read correctly against the background in both modes — it should feel like open, readable prose, not a jammed-together block or the flat gray of a system sans stack.

Here's a [default link](#), a [visited-style link](#) for comparison, and inline `code, styled as monospace`.

## Links (hover the ones below to check `--accent-text-color`)

- [Standard link](#) — uses `--link-color`
- **Bold link inside a sentence:** the quick brown fox jumps over the [lazy dog](#) here.

Crimson is used *almost* exclusively as hover/interactive color, never decoration — check that a link's resting color matches body text, not crimson, until you hover it.

## Buttons

Exercises `.btn` — the one deliberate exception to "crimson only on hover," a solid crimson fill. Should stay legible (white text) in both modes without needing a mode-specific variant, since white-on-crimson clears 9.29:1 regardless of page background.

<a href="#" class="btn">Read Now</a>
<button>A button element</button>

## Notices

Bare `.notice` / `.markdown-alert` — the theme's default gray-tinted notice, used in `_pages/writings.md` and several pre-2026 posts. Its background is derived from the page background (`--notice-bg`), so it should look like a subtle tint of the page, not a jarring fixed gray box in dark mode.

{% capture notice-text %}
This is a default notice. It should have a subtle background tinted from the page background, a muted link color for [links like this one](#), and — if it contains a blockquote — a colored left border.

> A blockquote inside the notice, to check `--notice-blockquote-border`.

Some `inline code` inside the notice, to check `--notice-code-bg`.
{% endcapture %}
<div class="notice" markdown="1">{{ notice-text | markdownify }}</div>

## Table (checks `--border-color-strong`)

| Column A | Column B | Column C |
|---|---|---|
| Row one | Some value | Another value |
| Row two | Some value | Another value |
| Row three | Some value | Another value |

## Form focus states (checks `--focus-shadow-text` / `--focus-shadow-accent`, and the footer/form background fix)

Click into each field below — the focus ring should be visible and appropriately subtle in both modes, and the form's own background should read as a faint tint of the page, not a fixed light-gray box.

<form>
  <div class="field">
    <label for="sg-text">Text input</label><br>
    <input type="text" id="sg-text" placeholder="Click to test focus ring">
  </div>
  <br>
  <div class="field">
    <label for="sg-textarea">Textarea</label><br>
    <textarea id="sg-textarea" placeholder="Click to test focus ring"></textarea>
  </div>
  <br>
  <div class="field">
    <label for="sg-select">Select</label><br>
    <select id="sg-select">
      <option>Option one</option>
      <option>Option two</option>
    </select>
  </div>
</form>

## Search toggle and hamburger icon (both check `--accent-text-color`)

The magnifying glass and (on narrow viewports) the hamburger icon in the masthead — hover the search icon and confirm it shifts to crimson rather than disappearing; the hamburger's resting color should already be legible crimson against the masthead background in both modes.

## Masthead / navigation

Check the site title, subtitle, nav links, and their hover states at the top of this page against `--masthead-link-color` / `--masthead-link-color-hover`.

## Code block

```python
def check_dark_mode(background_color, text_color):
    """Code blocks use --code-background-color; .highlight itself is intentionally un-themed."""
    contrast = calculate_contrast(background_color, text_color)
    return contrast >= 4.5  # WCAG AA minimum
```

## Muted text (checks `--muted-text-color`)

This sentence, the page footer below, and the search-results excerpt styling all use the muted text token — it should read as a clearly de-emphasized gray relative to body text, in both modes, without dropping so low it's hard to read. (Dark mode runs closer to the AA floor here than light mode — 3.98:1 in the footer specifically — a known soft spot in the palette, not something this page fixes.)

---

**Checklist**: toggle your OS light/dark setting (or use browser devtools' rendered emulation) and confirm every section above holds up in both modes — particularly the notice, the form background and focus ring, the footer at the very bottom of this page, table borders, and the navicon/search-icon, since those are the hand-derived tokens rather than direct variable substitutions. See `darkling-whim/DESIGN.md` for the exact values each should resolve to.
