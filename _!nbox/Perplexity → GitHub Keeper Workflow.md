Title: Perplexity → GitHub Keeper Workflow

## Goal

Turn Perplexity into the front-end for durable knowledge that ultimately lives in a GitHub-backed notes or workbench repository.

## Workflow

1. **Do the heavy thinking in Perplexity on Mac:**
   - Ask for structured, sectioned summaries.
   - Refine until the output reads like a self-contained document.

2. **Export from Perplexity:**
   - Use the export option to get Markdown (preferred for Git) [web:11].
   - Check headings, code blocks, and lists for clarity.

3. **Commit to GitHub via MCP or locally:**
   - File path: `!nbox/`
   - Filename pattern: `YYYYMMDD_Title.md`
   - Example: `20251229_Petting-the-AI-Stack-Design.md` [memory:24]

4. **Later processing:**
   - Periodically empty `!nbox` by:
     - Linking or moving processed notes into permanent folders (e.g., `ai/`, `writing/`, `systems/`).
     - Tagging or cross-referencing in your broader notes system.

## Rules of Thumb

- If a Perplexity output **isn’t** worth exporting and committing, it probably belongs in the Gemini layer instead.
- The act of opening the Mac and using Perplexity should itself be treated as a decision: “I intend this to be potentially permanent.”
