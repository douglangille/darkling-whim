# Quick Reference: Why Custom Workflow is Required

## The Problem
Your site uses these custom Jekyll plugins:
```yaml
plugins:
  - jekyll-paginate-v2    ❌ NOT supported by GitHub Pages
  - jekyll-archives       ❌ NOT supported by GitHub Pages  
  - jekyll-redirect-from  ❌ NOT supported by GitHub Pages
  - jekyll-sitemap        ✅ Supported
  - jekyll-gist           ✅ Supported
  - jekyll-include-cache  ✅ Supported
```

## The Solution
Use GitHub Actions workflow to build with custom plugins, then deploy.

## Setup Required (ONE TIME)
1. Go to: Repository Settings → Pages
2. Under "Build and deployment" section
3. Change **Source** from "Deploy from a branch" to **"GitHub Actions"**
4. Save

## What This Enables
- ✅ All custom plugins work correctly
- ✅ Advanced pagination (jekyll-paginate-v2)
- ✅ Automatic tag/category archives (jekyll-archives)
- ✅ URL redirects (jekyll-redirect-from)
- ✅ Deploys to https://douglangille.ca

## Workflow Location
`.github/workflows/jekyll-deploy.yml`

## Triggers
- Push to `main` branch (automatic)
- Manual trigger via Actions tab (workflow_dispatch)

## Build Process
1. Checkout code
2. Setup Ruby 3.3
3. Install all gems (including custom plugins)
4. Build site with Jekyll
5. Upload built site as artifact
6. Deploy artifact to GitHub Pages

## Status Check
After configuration, check the Actions tab:
- Build job should succeed ✅
- Deploy job should succeed ✅
- Site updates at https://douglangille.ca ✅
