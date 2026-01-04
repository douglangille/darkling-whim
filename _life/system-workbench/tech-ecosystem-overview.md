# Doug's Minimalist Tech Ecosystem

**Date**: December 27, 2025  
**Status**: Optimized for AUDHD, Low Friction, Zero Tool Sprawl

## Philosophy
- One AI tool (Perplexity Pro)
- Clear device boundaries
- Process over artifact
- Intentional friction where helpful
- Minimize guilt-inducing "should use" apps

---

## The Stack

### Single AI Hub
**Perplexity Pro** - Replaces ChatGPT, Gemini, Claude, Mistral, NotebookLM (mostly)

**Exception**: NotebookLM kept *only* for one-click podcast generation from GitHub content

---

## Device Roles & Setup

### iPhone 13 (iOS 26.2)
**Role**: Communication + Dictation Hub

**Core Apps**:
- Perplexity (installed) - dictation, troubleshooting, quick queries
- Outlook - work + personal iCloud mail
- Apple Calendar - unified personal/work view
- Apple Reminders - execution tasks
- Spotify - podcasts + occasional audiobooks (15 hrs/month)
- Safari - friction backdoor for rare needs
- Messages/Phone - core comms

**Deleted for Minimalism**:
- YouTube (moved to iPad)
- Feeed (moved to iPad)
- Apple Books (moved to iPad)
- Libby (not used enough - 1-2 audiobooks/year)
- Apple Mail (redundant with Outlook)
- Apple Journal (guilt generator, replaced by Perplexity dictation)

**Settings**:
- Perplexity default: "Choose sources: None" for fast responses
- Keep phone as pure utility device, not consumption

---

### iPad mini 6 (iPadOS 26.2)
**Role**: Consumption Zone

**Access**: Perplexity web only (no app installed)

**Core Apps**:
- feeeed - RSS/newsletter reading
- Apple Books - long-form reading, sideloaded epubs/PDFs
- YouTube - intentional video watching
- Music/Spotify - media consumption
- Safari - web browsing with uBlock
- Productivity apps (Calendar, Outlook, Office, OneDrive, Teams) - light work

**Reading Theme** (Unified across all apps):
- Font: Serif (Iowan-style)
- Background: Sepia/warm
- Size: 175% equivalent (comfortable at arm's length)
- Justification: On in Books, comfortable spacing in all

**Deleted**:
- iMovie (not used)
- Microsoft Loop (no inking support)
- Perplexity app (web sufficient, enforces intentional use)

---

### MacBook Air M1 (macOS 26.2)
**Role**: Creation Workhorse

**Access**: Perplexity web only (for MCP GitHub connection)

**Core Tools**:
- Perplexity Pro (web) with GitHub MCP
- Writing Studio Space (see below)
- Calibre - ebook library/conversion (epub → PDF for LLM ingestion)
- VSCode/dev tools
- Apple Notes - ephemeral capture only

**MCP Setup**:
- GitHub connection for RAG on all repos
- Enables context-aware writing, planning, and brainstorming

---

## Perplexity Optimization

### Writing Studio Space (MacBook)
**Configuration**:
- GitHub MCP connected to writing repos
- Default model: Claude Sonnet 4.5 (superior prose generation)
- Bootstrap file with system prompt loaded
- Sources: None (default for fast brainstorming)
- Switch to "Sources: Web" only when research needed

**Use Cases**:
- Creative writing (fiction, blog posts)
- Brainstorming and ideation
- Prompt generation for external tools if needed
- Revision and critique workflows

### Perplexity Labs (MacBook)
**Features**:
- Deep Research: autonomous multi-source reports (LMS, IT, healthspan topics)
- Script generation: podcast scripts from GitHub repos (requires external TTS)
- Mindmaps and structured outputs
- Chart/asset generation
- One-off project automation (5-30 min self-supervised work)

**Limitation**: Labs creates *scripts*, not audio files - use NotebookLM for actual podcast generation

### iOS Quick Settings
- "Choose sources: None" - fast ChatGPT-like responses without research lag
- Model selector: Claude Sonnet 4.5 for prose, "Best" for mixed tasks
- Voice mode: rarely used; dictation preferred for maintaining tool relationship vs. parasocial risk

---

## Workflow Transformations

### Journaling → Perplexity Dictation
- **Old**: Apple Journal (guilt generator, unused)
- **New**: Ad-hoc Perplexity threads via dictation
- **Insight**: The *process* of articulating thoughts = journaling; artifact optional
- **Benefit**: No guilt, natural reflection, structured AI responses aid metacognition

### Planning Systems
**Weekly Execution**:
- Apple Reminders (task completion, dopamine hits)

**Quarterly Planning**:
- Perplexity threads or dedicated "Planning" Space
- Dictate goals/reflections → AI structures priorities
- Export to GitHub via MCP as markdown artifact

**Forever Notes Framework**:
- Abandoned (didn't work for AUDHD brain)
- Apple Notes now = ephemeral capture only (article links, quick scratchpad)

### Reading Workflow
**Three Unified Frames**:
1. **Safari Reader** - one-off web articles, distraction removal
2. **Apple Books** - long-form, sideloaded content, LLM-ready PDFs
3. **feeeed** - RSS/ongoing sources, built-in summaries

**Decision Tree**:
- Random web article → Safari Reader (read & forget) or share to Notes for later
- Evergreen/reference → Apple Books
- Ongoing source → feeeed (no auto-send to LLM - intentional friction)

### Podcast Generation (Hybrid Approach)
**Perplexity Labs**: Create podcast *scripts* from GitHub repos via MCP
**NotebookLM**: One-click audio generation from content
- Drag/drop story files into NotebookLM
- Or: use Perplexity to concatenate tagged stories → single file → NotebookLM
- Output: MP3 for consumption on iPad/iPhone

**Spotify Audiobooks**: 15 hours/month = 1-2 books, sufficient for light use

---

## What Was Deleted & Why

| App | Device | Reason |
|-----|--------|--------|
| YouTube | iPhone | Distraction tool disguised as utility; moved to iPad for intentional watching |
| Feeed | iPhone | RSS belongs on consumption device (iPad) |
| Apple Books | iPhone | Reading = iPad activity |
| Libby | iPhone | 1-2 audiobooks/year doesn't justify app; Spotify Premium covers this |
| Apple Mail | iPhone | Redundant with Outlook; no Apple Intelligence on iPhone 13 |
| Apple Journal | iPhone | Guilt generator; replaced by Perplexity dictation-as-reflection |
| iMovie | iPad | Unused; video editing not part of workflow |
| Loop | iPad | No inking support; web access sufficient |
| Perplexity app | iPad | Web-only enforces intentional use; no need for app |

---

## Key Insights & Principles

### AUDHD Optimization
- **Context boundaries**: Phone = comms, iPad = consume, Mac = create
- **Friction design**: Safari as "backdoor" slows impulsive browsing
- **Dopamine awareness**: Removed apps that trigger research/learning loops vs. execution
- **Visual consistency**: Unified serif/sepia reading theme reduces cognitive load

### AI Relationship Management
- **Dictation > Interactive voice**: Maintains tool relationship, avoids parasocial trap
- **Process = journaling**: Articulation to AI is reflection; no artifact guilt
- **Conversational AI as metacognition**: Perplexity threads naturally facilitate thinking

### Minimalism
- One AI hub eliminates decision fatigue
- Clear device roles prevent context switching
- Ephemeral Notes = no maintenance burden
- Tool sprawl only allowed when dramatically better (NotebookLM podcasts)

---

## Next Actions (From Dec 27, 2025)
1. Test Writing Studio Space on MacBook with GitHub MCP
2. Generate first podcast script in Labs from blog repo
3. Test NotebookLM podcast generation with Haley stories
4. Use Perplexity for quarterly planning thread (Q1 2026)

---

**Last Updated**: December 27, 2025  
**Review Cycle**: Quarterly or when friction emerges
