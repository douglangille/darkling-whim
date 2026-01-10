---
title: 2026 AI Stack Architecture & Workflow
updated: 2026-01-10
---

## Overview

This stack intentionally separates tools by **role**, **device**, and **data permanence** to contain chat sprawl, reduce parasocial drift, and maintain a vendor-agnostic knowledge base through GitHub MCP.

## Core Philosophy

- **Treat LLMs as compute tools, not companions**
- **Enforce intentional sessions via GitHub MCP**
- **Avoid native apps for free-tier LLMs to minimize parasocial engagement**
- **Use GitHub repo as vendor-agnostic creative datalake**
- **Reserve live camera/multimodal features for situational needs only**

---

## Subscription & Tool Strategy

### Current Paid/Free Access

**Perplexity Pro (Free for 1 year via PayPal)**
- Multi-model access: GPT-5 / GPT-5.2, Claude Sonnet, Gemini Pro, Sonar
- Web + citation-backed retrieval
- File uploads, long-context summarization
- Works on mobile and browser
- GitHub MCP integration for archival workflow

**ChatGPT, Gemini, Claude, Mistral (Free tiers)**
- Free GPT-5 or variant access (limited usage, possible throttling)
- Browser-only use for creative tasks, multi-step reasoning, or situational needs
- No native app required; used surgically
- Gemini mobile app exception for ephemeral/disposable queries

### Decision Principles

- **Single dedicated app: Perplexity Pro (mobile + web)**
- All other tools used **surgically in browser at free tier**
- Avoid parasocial loops; enforce chat hygiene via **GitHub MCP**
- Use live camera features only when truly necessary
- No paid subscriptions beyond free Perplexity Pro year

---

## Devices and Roles

### iPhone – Ephemeral AI
- **Primary Tool**: Perplexity Pro app
  - Voice queries, image uploads, multi-model access
  - Fast, instrumental workflow for daily living
  - Research with citations
- **Secondary Tool**: Gemini app (optional)
  - Activity auto-deletes after 3 months
  - Disposable queries, quick ideas, throwaway brainstorming
  - Acts as containment zone for "petting the AI"
- **Not Installed**: ChatGPT, Claude, Mistral native apps
  - Prevents addictive conversational loops
  - Forces intentional browser-based sessions when needed

### iPad – Exploration AI
- **Tool**: Perplexity Pro for research
- **Tool**: Gemini app (primarily invoked via Safari/Feedeed share sheet)
  - Content-first exploration—summaries, critiques, questions about articles
  - Browser-centric; AI is a processor of pages, not a destination for chatting
  - Minimizes standalone "New Chat" usage to avoid rambling and attachment
- **Browser Access**: ChatGPT, Claude, Mistral for specific tasks only

### Mac – Archival and Prose AI
- **Primary**: Perplexity Pro with GitHub MCP integration
  - Research engine and archival front-end
  - Structured outputs stored in GitHub
  - Multi-model experimentation via Perplexity's model selection
- **Browser-based free tier**: Claude, ChatGPT, Gemini, Mistral
  - Claude: Premium prose / structural editing engine (used sparingly)
  - Mistral: Uncensored fiction lab for creative drafts
  - ChatGPT: Creative brainstorming / narrative ideation
  - Gemini: Large context drafts / structured summaries
- **Intent**: Serious projects, keepers, and versioned work only

---

## GitHub MCP as RAG Layer

### Core Function
- Stores all notes, prompts, outputs
- Enforces conversation discipline: no sprawling threads
- Provides versioning and retrieval
- Acts as **system of record**, decoupled from LLMs
- Vendor-agnostic creative datalake for future-proofing

### Chat Flow Pattern
1. **Capture / store** output in GitHub (MCP)
2. **Retrieve context** selectively for new prompts
3. **Query LLM** (Perplexity mobile or browser-based free LLMs)
4. **Store results** back in GitHub
5. Optional **iteration**: multi-model comparisons in Perplexity

### Advantages
- Forces lean prompts
- Encourages modular reuse of content (scenes, character notes, worldbuilding)
- Maintains intentionality
- Preserves vendor-agnostic context for future-proofing

### Repository Structure Recommendations

```
_writing/
  scenes/
  characters/
  worldbuilding/
_tech/
  ai-tools/
  prompts/
    templates/
_plan/
  outputs/
    [dated entries with metadata]
```

**Organization principles:**
- Modular scene/character directories for easy retrieval
- Prompt templates for recurring creative patterns
- Output versioning to track narrative iterations
- Metadata tagging (YAML frontmatter) for semantic retrieval

---

## Model Selection by Task

| Task | Recommended Tool | Notes |
|------|-----------------|-------|
| Research, citations, long-context summarization | **Perplexity Pro** | Multi-model access, web grounding |
| Creative brainstorming / narrative ideation | **ChatGPT Free (browser)** or Perplexity Pro | Conversational fluency |
| Large context drafts / structured summaries | **Gemini Free (browser)** | 1M+ token context |
| Analytical, multi-step reasoning | **Claude Free (browser)** | 200K context, reasoning depth |
| Uncensored fiction / character dialogue | **Mistral Free (browser)** | Experimental generation |
| Character dialogue experimentation | **ChatGPT Free** | Conversational tone |
| Analytical writing critique | **Claude Free** | Editorial precision |

### Notes
- Multi-model access in Perplexity Pro greatly increases value for research + creative work
- Free tiers of ChatGPT, Gemini, Claude, Mistral are sufficient for targeted, intentional use
- Paid subscriptions for these tools are unnecessary in this workflow

---

## Tool Specialization

### Perplexity Pro
- **Role**: Research engine, archival front-end, primary mobile AI
- **Strengths**: Multi-model access, citations, GitHub MCP integration
- **Device**: iPhone (primary), iPad, Mac
- **Use Cases**: Daily research, cited responses, instrumental queries, multi-model experimentation

### Gemini
- **Role**: Ephemeral assistant for disposable thinking, content exploration
- **Strengths**: Long context (1M+ tokens), auto-delete settings, share sheet integration
- **Device**: iPhone (containment), iPad (content processor)
- **Use Cases**: Throwaway brainstorming, article summaries, quick questions

### Claude
- **Role**: Premium prose / structural editing engine
- **Strengths**: Reasoning depth, editorial precision, 200K context
- **Device**: Mac (browser only)
- **Use Cases**: High-fidelity prose, analytical writing, structural editing

### Mistral
- **Role**: Uncensored fiction lab
- **Strengths**: Creative freedom, experimental generation
- **Device**: Mac (browser only)
- **Use Cases**: Uncensored creative drafts, dialogue experimentation

### ChatGPT
- **Role**: Creative brainstorming / narrative ideation
- **Strengths**: Conversational fluency, GPT-5 access (free tier)
- **Device**: Mac (browser only)
- **Use Cases**: Character dialogue, narrative exploration, quick creative iterations

---

## Workflow Integration Pattern

### Pre-Session
1. Pull relevant context from GitHub (character notes, world rules, previous scenes)
2. Review quarterly planning notes if relevant
3. Select appropriate LLM based on task matrix above

### Generation Session
1. Use focused prompt + retrieved context
2. For creative work: experiment with multiple models via Perplexity or browser tabs
3. Maintain session intentionality—avoid conversational drift
4. Keep each session scoped to specific outcome

### Post-Session
1. Commit output to GitHub with descriptive metadata
2. Tag outputs for quarterly retrospectives
3. Delete ephemeral chat threads (except Gemini auto-delete)
4. Update relevant project documentation

### Review Cycle
- Weekly: Review outputs against planning cadence
- Quarterly: Assess tool effectiveness, update task routing if needed
- Annually: Evaluate subscription value (Perplexity Pro renewal decision)

---

## Behavioral & Cognitive Boundaries

### Intentional Usage
- **Device selection encodes intent**: Mac + Perplexity = keeper work; iPhone Gemini = disposable
- **Session containment**: One focused task per chat; archive and move on
- **No chat sprawl**: Delete threads after archiving outputs to GitHub
- **No native apps for free-tier tools**: Prevents addictive engagement patterns

### Parasocial Risk Mitigation
- **Browser-only access** for ChatGPT, Claude, Mistral creates friction barrier
- **GitHub MCP** forces explicit capture decisions (not passive accumulation)
- **Gemini auto-delete** (3 months) prevents emotional attachment to conversation history
- **Perplexity instrumental design** emphasizes research over conversation

### Multimodal Feature Discipline
- **Reserve camera/vision features** for farm/household tasks with genuine visual context needs
- **Avoid casual camera use** for queries that can be text-based
- **iPhone Perplexity**: voice and image for instrumental daily tasks only

---

## Future-Proofing Strategy

### Vendor Independence
- **GitHub-centric storage** means any LLM can be swapped without losing work
- **Modular prompt templates** transferable across models
- **Metadata tagging** enables future semantic search regardless of tool changes

### Subscription Reassessment (2027)
When free Perplexity Pro year ends:
- Evaluate whether paid renewal justifies cost vs. browser-based free tiers
- Assess maturity of free-tier ecosystem (may be sufficient by then)
- Consider alternative paid options if significant features emerge
- GitHub MCP ensures continuity regardless of decision

### RAG Enhancement Readiness
- Organized GitHub structure enables **future vector search** integration
- YAML frontmatter supports **semantic retrieval** tool adoption
- Modular content organization works with emerging **RAG tools**

---

## Risk Mitigation

### Browser Friction vs. Usage Value
- **Monitor**: Does browser-only access for free tools create excessive friction?
- **Decision rule**: If avoiding valuable creative sessions due to browser overhead, consider:
  - Single additional native app (Claude) with strict usage rules
  - Time-boxed sessions (Pomodoro-style boundaries)
- **Current stance**: Maintain browser-only for all except Perplexity Pro + Gemini ephemeral

### Quarterly Review Questions
1. Is GitHub MCP capturing all keeper work effectively?
2. Are free-tier rate limits causing workflow disruption?
3. Is Perplexity Pro providing sufficient value for primary use?
4. Are browser-based tools meeting creative workflow needs?
5. Is device-based intentionality working as designed?

---

## Summary Architecture

**One Paid App**: Perplexity Pro (free 1 year) – primary mobile, archival integration, multi-model research

**Browser-Based Free Tier**: ChatGPT, Gemini, Claude, Mistral – surgical, situational, ephemeral

**System of Record**: GitHub MCP – vendor-agnostic datalake, versioning, intentionality enforcement

**Device Intent Encoding**:
- **iPhone**: Instrumental AI (Perplexity) + disposable queries (optional Gemini)
- **iPad**: Content exploration (Perplexity + Gemini via share sheet)
- **Mac**: Archival work (Perplexity + GitHub MCP) + creative sessions (browser LLMs)

**Workflow Discipline**:
- Capture → retrieve → generate → store
- Clean sessions, delete sprawl
- Metadata for retrieval
- Quarterly reassessment

This architecture balances **cost-effectiveness, vendor independence, creative flexibility,** and **parasocial risk mitigation** while maintaining the "workbench, not warehouse" philosophy across all systems.
