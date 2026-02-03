# GitHub Pages Deployment Setup

## Why Custom Workflow is Needed

This site uses custom Jekyll plugins that are **not supported** by GitHub's built-in Pages deployment:

1. **jekyll-paginate-v2** - Advanced pagination with multiple collections
2. **jekyll-archives** - Automatic tag and category archive pages  
3. **jekyll-redirect-from** - URL redirect functionality

GitHub Pages' built-in Jekyll processor only supports [a limited set of plugins](https://pages.github.com/versions/). To use custom plugins, you must build the site using GitHub Actions and deploy the resulting static files.

## Required GitHub Pages Configuration

**CRITICAL:** For the workflow to deploy successfully, GitHub Pages must be configured to use GitHub Actions as the deployment source.

### Configuration Steps:

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Build and deployment**, set:
   - **Source**: GitHub Actions (NOT "Deploy from a branch")
   
That's it! Once this is configured, the workflow in `.github/workflows/jekyll-deploy.yml` will:
- Build the site with all custom plugins
- Upload the built site as an artifact
- Deploy to GitHub Pages

## Current Status

- ✅ Workflow file exists and is correctly configured
- ✅ Site builds successfully with custom plugins
- ⚠️  **ACTION REQUIRED**: Verify GitHub Pages is set to "GitHub Actions" source

## Workflow Details

The workflow (`.github/workflows/jekyll-deploy.yml`):
- Triggers on push to `main` branch
- Uses Ruby 3.3
- Builds with all Gemfile plugins
- Deploys to your custom domain: https://douglangille.ca

## Troubleshooting

If deployment fails:
1. Check that Pages source is set to "GitHub Actions" (not "Deploy from a branch")
2. Verify the workflow has proper permissions (`pages: write`, `id-token: write`)
3. Check workflow run logs in the Actions tab

## Alternative: Use Supported Plugins Only

If you wanted to avoid the custom workflow, you'd need to:
- Replace `jekyll-paginate-v2` with `jekyll-paginate` (v1)
- Remove `jekyll-archives` (or implement manually)
- Remove `jekyll-redirect-from` (or use other redirect methods)

This is **not recommended** as it would break existing functionality.
