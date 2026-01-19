# On a Darkling Whim

**Live Site**: [https://douglangille.ca](https://douglangille.ca)

## About

On a Darkling Whim is Doug Langille's creative writing portfolio featuring original stories and poems with a dark, speculative edge. The site tagline says it best: "dark around the edges, wonder with teeth."

This Jekyll site uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme and is deployed via GitHub Pages.

## Site Structure

- **Stories & Poems** (`_posts/`): Fiction and poetry organized by publication date
- **Perspectives** (`_pages/perspectives/`): Essays and commentary on writing craft
- **Now** (`_pages/now/`): Current projects and status updates
- **Assets** (`assets/`): Images, CSS customizations, and other media

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

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch via GitHub Actions (`.github/workflows/`).

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
---

Your story content here.
```

### Managing Pages

Edit files in `_pages/` to update static content like the Now page or Perspectives section.

## Configuration

Site settings are in `_config.yml`, including:
- Site title, subtitle, and description
- Author bio and social links
- Theme customization
- Pagination and archive settings

## License

© 2013-2026 Doug Langille. Content rights reserved. Theme licensed under MIT.
