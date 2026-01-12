# Inbox Processing Guidelines

## Purpose

The `_!nbox` folder serves as a **temporary intake queue** for unprocessed content. Files here should not remain permanently—this is a workbench, not a warehouse.

## Processing Workflow

### 1. Intake
Drop files here for analysis and sorting:
- Exported chat transcripts
- Legacy documents from old file systems
- Clipped articles or PDFs
- Notes that need organization
- Any content requiring review

### 2. Analysis
Each file should be evaluated for:
- **Relevance**: Does this support active work or reference needs?
- **Destination**: Which collection does this belong in?
- **Format**: Should this be converted to Markdown or kept as-is?
- **Value**: Keep, archive, or delete?

### 3. Destination Collections

- `_work` - Professional materials (presentations, resumes, work artifacts)
- `_tech` - Technical notes, tutorials, IT documentation
- `_writing` - Fiction development, story notes, writing craft
- `_life` - Personal reference, health tracking, general notes
- `_farm` - Farming operations, animal care, land management
- `_plan` - Goals, quarterly planning, tracking systems
- `_posts` - Blog-ready content for publication
- `_drafts` - In-progress writing for the blog
- `story-engine` - Story universe development materials

### 4. Processing Decisions

**KEEP** if:
- Active reference material for current projects
- Synthesized knowledge worth preserving
- Presentations or artifacts representing your expertise
- Notes that inform ongoing work

**CONVERT** if:
- PDF/Office docs that should become searchable Markdown
- Dense documents better represented as concise summaries
- Chat transcripts containing reusable insights

**DELETE** if:
- Outdated or superseded information
- Plugin READMEs for software no longer used
- Duplicate versions of the same content
- "Just in case" hoarding with no clear use case
- Recovery codes or credentials (should be in password manager)

### 5. Completion
Once processed, files should be:
- Moved to their destination collection with proper front matter
- Deleted if determined to be clutter
- Never left to accumulate in `_!nbox`

## File Naming Conventions

When moving to collections, prefer:
- Descriptive, lowercase names with hyphens: `my-document-name.md`
- ISO date prefixes when relevant: `2026-01-11-topic-name.md`
- No special characters except hyphens and underscores

## Front Matter Requirements

When converting to Markdown, include:
```yaml
---
title: "Descriptive Title"
date: YYYY-MM-DD
categories: [relevant, tags]
---
```

See collection-specific READMEs for additional metadata requirements.

## Batch Processing

Process in themed batches:
- One batch of work/professional materials
- Another batch of writing/fiction notes  
- A batch of technical documentation

This reduces context switching and makes decisions easier.

---

**Remember**: The inbox is for *processing*, not *storage*. Keep it empty or nearly empty.