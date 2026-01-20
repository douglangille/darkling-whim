# On a Darkling Whim

**Live Site**: [https://douglangille.ca](https://douglangille.ca)

## About

On a Darkling Whim is Doug Langille's creative writing portfolio featuring original stories and poems exploring cosmic horror, dark fantasy, and psychological unease.

**Subtitle**: "Untethered tales, beautifully scarred"

**Description**: Stories and poems by Doug Langille: dark around the edges, wonder with teeth.

This Jekyll site uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme and is deployed via Netlify.

## Site Structure

- **Stories & Poems** (`_posts/`): Fiction and poetry organized by publication date
- **About** (`_pages/about.md`): Author bio and writing philosophy
- **Now** (`_pages/now.md`): Current creative projects and reading list
- **Assets** (`assets/`): Images, CSS customizations, and other media

## The Haley-verse

An interconnected story universe exploring cosmic horror, power dynamics, and survival at the edges. Multiple stories across the site feature recurring characters and themes, particularly centered around Haley Madigan.

## Local Development

### Prerequisites

- Ruby 3.1 or higher
- Bundler

### Setup

1. Install dependencies:
   ```bash
   bundle install
   ```

2. Serve the site locally:
   ```bash
   bundle exec jekyll serve
   ```

3. Visit `http://localhost:4000` in your browser

## Deployment

The site automatically deploys to Netlify when changes are pushed to the `main` branch.

## Content Management

### Publishing Stories & Poems

Create files in `_posts/` with the format `YYYY-MM-DD-title.md`:

```markdown
---
title: "Your Story Title"
date: YYYY-MM-DD
excerpt: "A compelling hook for the story."
header:
  overlay_image: /assets/images/your-image.jpg
  overlay_filter: 0.5
tags:
  - flash-fiction
  - haley-verse
---

Your story content here.
```

### Managing Pages

Edit files in `_pages/` to update static content:
- `about.md` - Author bio and writing philosophy (rarely changes)
- `now.md` - Current projects and reading list (update regularly)

## Configuration

Site settings are in `_config.yml`, including:
- Site title, subtitle, and description
- Author bio and social links
- Theme customization
- Tag-based archives (categories disabled)
- Pagination settings (12 posts per page)

## Writing Philosophy

All stories on this site are drafted entirely by hand with no AI involvement in the creative process. AI serves only as a line editor for spelling and grammar, and occasionally as a critic for craft development.

## License

© 2013-2026 Doug Langille. Content rights reserved. Theme licensed under MIT.
