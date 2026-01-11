# Workbench

Personal knowledge management system integrating IT work, creative writing, life planning, and hobby farm operations.

## Domain Structure

- **`_!nbox`**: Universal inbox for rapid capture
- **`_plan`**: Strategic planning (quarterly/annual), productivity systems, execution frameworks
- **`_work`**: IT management (NSCC), professional projects, career development
- **`_tech`**: Technology stack, AI tooling, dev environment, system optimization
- **`_writing`**: Fiction projects, story universes, writing craft and workflows
- **`_life`**: Personal health, counselling, relationships, recipes, reference archives
- **`_farm`**: Hobby farm logs, animal care, property management
- **`_drafts`**: Active works in progress across all domains
- **`_posts`**: Published content ready for site deployment
- **`story-engine`**: Perplexity-based writing toolset and AI assistants

## Philosophy

This workbench follows a "workbench, not warehouse" principle—active tools and current projects, with minimal archival clutter. Content flows through capture (`_!nbox`), development (`_drafts`), and either storage (domain folders) or publication (`_posts`).

## Reference Archives

The `_life/` folder contains frozen reference archives (changingminds.org, creatingminds.org) that serve as deep knowledge bases. **These archives are read-only and never modified.** When content is needed for active work, extract and create new notes in the appropriate domain folder (`_writing`, `_work`, `_tech`, etc.) with links back to archive sources for provenance.

## Build Configuration

Non-Jekyll folders (prefixed with `_`) are excluded in `_config.yml` and `netlify.toml` to prevent publication of private content while maintaining the Jekyll site structure.
