# On a Darkling Whim

**Live Site**: [https://douglangille.ca](https://douglangille.ca)

## About

On a Darkling Whim is Doug Langille's creative writing portfolio featuring original stories and poems exploring cosmic horror, dark fantasy, and psychological unease.

**Subtitle**: "Untethered tales, beautifully scarred"

**Description**: Stories and poems by Doug Langille: dark around the edges, wonder with teeth.

This Jekyll site uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme.

## Site Structure

- **Stories & Poems** (`_posts/`): Fiction and poetry organized by publication date
- **About** (`_pages/profile/about.md`): Author bio and writing philosophy
- **Now** (`_pages/profile/now.md`): Current creative projects and reading list
- **AI** (`_pages/profile/ai.md`): How AI is used in the writing process

The About, Now and AI pages are maintained in the forge vault (`writing/darkling-whim/pages/`) and overwritten by its deploy, which replaces `_pages/profile/` each time. Edit them there, not here.
- **Assets** (`assets/`): Images, CSS customizations, and other media

## The Haley-verse

An interconnected story universe exploring cosmic horror, power dynamics, and survival at the edges. Multiple stories across the site feature recurring characters and themes, particularly centered around Haley Madigan.

## Local Development

### Prerequisites

- Ruby 3.3 or higher
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

The site uses **custom Jekyll plugins** (jekyll-paginate-v2, jekyll-archives, jekyll-redirect-from) that require a GitHub Actions workflow for building and deployment.

**Important**: GitHub Pages must be configured to use "GitHub Actions" as the deployment source (Settings → Pages → Source: GitHub Actions).

The workflow automatically builds and deploys to GitHub Pages when changes are pushed to the `main` branch. Custom domain `douglangille.ca` is configured through GitHub Pages settings with DNS managed via Cloudflare.

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

Edit other files in `_pages/` to update static content. The About, Now and AI pages are in `_pages/profile/` and come from the forge vault (see above), so edit them there.

## Configuration

Site settings are in `_config.yml`, including:
- Site title, subtitle, and description
- Author bio and social links
- Theme customization
- Tag-based archives (categories disabled)
- Pagination settings (12 posts per page)

## Writing Approach

Stories are built through collaboration between human vision and AI assistance. AI handles mechanical drafting based on structured frameworks, which are then extensively revised for voice and craft. Every story published reflects authorial decisions, distinctive voice, and creative control.

See the [About page](https://douglangille.ca/about/) for full disclosure on writing process and philosophy.

## License

© 2013-2026 Doug Langille. Content rights reserved. Theme licensed under MIT.
