# NotebookLM Integration Guide

## Why NotebookLM Stays in the Stack

**Single use case**: One-click podcast generation from text sources

**Justification**: Dramatically better than Perplexity Labs (which only creates *scripts*, not audio)

**Not tool sprawl**: Specialized tool for one specific job

---

## Setup

**Device**: Use on MacBook or iPad (web-based, no app needed)

**Access**: https://notebooklm.google.com

---

## Supported Source Types

NotebookLM accepts:
- PDFs
- Text files (.txt)
- Markdown files (.md)
- Word documents (.docx)
- Google Docs
- Web URLs (single page, not crawling)
- Google Sheets
- Slides

**Does NOT**:
- Directly connect to GitHub repos
- Crawl/spider linked pages
- Follow tag archives automatically

---

## Workflows for Your Content

### Workflow 1: Individual Story Files
**Best for**: Discrete stories, blog posts

1. Export/download story files from GitHub to Mac
2. Go to NotebookLM > Create new notebook
3. **Drag and drop** all story files into the notebook
4. Click **Generate podcast**
5. Download MP3 file
6. Transfer to iPad/iPhone → listen in Spotify or Files app

**Pros**: Simple, no pre-processing  
**Cons**: Many files = many sources in one notebook

---

### Workflow 2: Concatenated File via Perplexity
**Best for**: Series of stories (e.g., all Haley stories)

1. **In Perplexity Writing Studio** (MacBook, GitHub MCP connected):
   ```
   Find all stories in this repo tagged 'Haley' and concatenate 
   them into a single markdown document with clear headings 
   between stories. Format for podcast consumption.
   ```

2. Copy the concatenated markdown output
3. Save as `haley-stories.md` locally
4. Go to NotebookLM > Create new notebook
5. Upload `haley-stories.md` as single source
6. Click **Generate podcast**
7. Download MP3 → transfer → listen

**Pros**: One source, easier to manage  
**Cons**: Extra Perplexity step (but low friction)

---

### Workflow 3: Published Posts as URLs
**Best for**: Already published blog posts

1. Go to NotebookLM > Create new notebook
2. For each published post:
   - Copy the URL
   - Click **Add source** > **Website URL**
   - Paste URL
3. Repeat for all posts you want in the podcast
4. Click **Generate podcast**
5. Download MP3 → transfer → listen

**Pros**: No file downloads needed  
**Cons**: One URL at a time (can't batch, can't crawl tag archives)

---

## Podcast Generation Settings

NotebookLM typically offers:
- **Length**: Auto (based on content) or custom
- **Tone**: Conversational, explanatory (usually auto-selected)
- **Voices**: Two hosts (male/female, auto-assigned)

**No advanced customization**: It's intentionally simple - one click, done.

---

## Output & Consumption

### Download
- MP3 file (usually 10-20 MB per 15-20 min episode)
- Downloads to Mac/iPad Downloads folder

### Transfer to iPhone/iPad
- AirDrop from Mac to iPad/iPhone
- Upload to iCloud Drive → download on iOS
- Use Files app to access locally

### Playback Options
- **Spotify**: Upload to your podcast library (if supported)
- **Apple Books**: Import as audiobook
- **Files app + built-in player**: Simplest
- **VLC or other audio app**

---

## When to Use NotebookLM vs. Perplexity

| Task | Use NotebookLM | Use Perplexity |
|------|----------------|----------------|
| Generate audio podcast from text | ✅ Yes | ❌ No (scripts only) |
| Analyze/query content | ❌ No | ✅ Yes (MCP RAG) |
| Create podcast script for editing | ❌ No | ✅ Yes (Labs) |
| Multi-source research synthesis | ❌ No | ✅ Yes (Deep Research) |
| Quick one-click audio overview | ✅ Yes | ❌ No |

---

## Limitations & Workarounds

### No GitHub Integration
**Workaround**: Use Perplexity to concatenate repo files → export → upload to NotebookLM

### No URL Crawling
**Workaround**: Add each post URL individually, or use concatenated file method

### No Voice Customization
**Workaround**: Accept auto-generated voices, or use Labs script + external TTS (ElevenLabs) for full control

### Limited Editing
**Workaround**: If podcast needs editing, use Perplexity Labs for script first, revise, then manual TTS

---

## Example Projects

### Project 1: Haley Story Collection
**Sources**: 
- All Haley story files (drag-drop), OR
- One concatenated `haley-stories.md` (via Perplexity)

**Output**: 30-45 min podcast overviewing the series

**Use**: Listen on iPad during farm work

---

### Project 2: Blog Post Retrospective
**Sources**:
- URLs of published blog posts from past quarter

**Output**: 20 min podcast summarizing key themes/ideas

**Use**: Quarterly review while walking

---

### Project 3: Writing Research
**Sources**:
- PDFs of craft books
- Markdown notes from writing research

**Output**: Podcast explaining key craft concepts

**Use**: Reinforce learning while doing chores

---

## Maintenance

**Frequency**: Use as-needed, no ongoing setup

**Notebook Management**:
- Delete old notebooks after consuming podcast
- Or keep for reference/re-generation

**No Integration Required**: Standalone tool, no Perplexity sync needed

---

## Decision Point: Keep or Remove?

**Keep if**:
- You regularly want audio overviews of your writing
- One-click podcast from files is valuable
- Listening > reading for consumption/review

**Remove if**:
- You never actually listen to generated podcasts
- Spotify audiobooks + text reading is sufficient
- Tool guilt > actual utility

**Current Status**: Keep for specialized podcast generation (Dec 27, 2025)

---

**Last Updated**: December 27, 2025  
**Review**: After generating 3-5 podcasts, assess actual usage
