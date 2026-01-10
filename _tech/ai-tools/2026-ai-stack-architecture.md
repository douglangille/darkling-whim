---
title: 2026 AI Stack Architecture & Workflow
updated: 2026-01-10
experiment: Perplexity-only native app strategy
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
- **Browser-only use across all devices**
- Used surgically for creative tasks, multi-step reasoning, or situational needs
- No native apps installed

### Decision Principles

- **Single dedicated app: Perplexity Pro (iPhone + iPad + Mac)**
- **All other tools strictly browser-only at free tier**
- Avoid parasocial loops; enforce chat hygiene via **GitHub MCP**
- Use live camera features only when truly necessary
- No paid subscriptions beyond free Perplexity Pro year

### Experiment Notes (Jan 10, 2026)

**Hypothesis**: Perplexity-only native app strategy will:
- Maximize intentionality by creating friction for all non-research AI usage
- Test whether multi-model access in Perplexity Pro can cover most creative needs
- Eliminate "Gemini containment zone" in favor of pure browser discipline
- Provide clean baseline to assess actual tool usage patterns

**What Changed**:
- Removed Gemini native app from iPhone/iPad
- All ChatGPT, Gemini, Claude, Mistral usage now browser-based across all devices
- Perplexity Pro becomes sole native AI app on all devices

**Success Metrics**:
- Does browser friction prevent valuable work or just reduce parasocial drift?
- Can Perplexity Pro's multi-model access satisfy creative brainstorming needs?
- Do browser-based tools get used intentionally or avoided entirely?
- Does iPhone Perplexity handle daily living queries effectively without Gemini backup?

**Review Date**: End of Q1 2026 (March 31, 2026)

---

## Devices and Roles

### iPhone – Instrumental AI
- **Only Installed App**: Perplexity Pro
  - Voice queries, image uploads, multi-model access
  - Fast, instrumental workflow for daily living
  - Research with citations
  - Multi-model experimentation (GPT-5, Claude, Gemini, Sonar)
- **Browser Access**: ChatGPT, Gemini, Claude, Mistral (for specific tasks only)
- **Not Installed**: All other AI native apps
  - Prevents addictive conversational loops
  - Forces intentional browser-based sessions when needed

### iPad – Research & Exploration AI
- **Only Installed App**: Perplexity Pro
  - Primary research tool
  - Multi-model queries for content exploration
  - Share sheet integration for article processing
- **Browser Access**: ChatGPT, Gemini, Claude, Mistral (for specific creative tasks)
  - Content-first exploration—summaries, critiques, questions about articles
  - Browser-centric; AI is a processor of pages, not a destination for chatting

### Mac – Archival and Prose AI
- **Primary App**: Perplexity Pro with GitHub MCP integration
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
3. **Query LLM** (Perplexity app or browser-based free LLMs)
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
| Research, citations, long-context summarization | **Perplexity Pro (app)** | Multi-model access, web grounding |
| Quick daily queries, voice interaction | **Perplexity Pro (app)** | iPhone/iPad convenience |
| Creative brainstorming / narrative ideation | **Perplexity Pro** or ChatGPT Free (browser) | Test multi-model in Perplexity first |
| Large context drafts / structured summaries | **Gemini Free (browser)** | 1M+ token context |
| Analytical, multi-step reasoning | **Perplexity Pro** or Claude Free (browser) | Claude Sonnet in Perplexity or browser |
| Uncensored fiction / character dialogue | **Mistral Free (browser)** | Experimental generation |
| Character dialogue experimentation | **ChatGPT Free (browser)** | Conversational tone |
| Analytical writing critique | **Claude Free (browser)** | Editorial precision |

### Notes
- **Try Perplexity Pro's multi-model access first** before reaching for browser tools
- Multi-model access in Perplexity Pro may cover most creative needs during experiment
- Free tiers of ChatGPT, Gemini, Claude, Mistral available when browser-based focus is beneficial
- Paid subscriptions for other tools remain unnecessary in this workflow

---

## Tool Specialization

### Perplexity Pro (Native App - All Devices)
- **Role**: Primary AI interface, research engine, archival front-end, multi-model experimentation
- **Strengths**: Multi-model access (GPT-5, Claude Sonnet, Gemini Pro, Sonar), citations, GitHub MCP integration
- **Device**: iPhone, iPad, Mac (only installed native AI app)
- **Use Cases**: Daily research, cited responses, instrumental queries, creative brainstorming, multi-model comparison

### Gemini (Browser Only)
- **Role**: Large context processing for specialized needs
- **Strengths**: Long context (1M+ tokens), structured summaries
- **Device**: Mac browser (primary), iPad/iPhone browser (situational)
- **Use Cases**: Massive document analysis, article summaries when share sheet not sufficient

### Claude (Browser Only)
- **Role**: Premium prose / structural editing engine
- **Strengths**: Reasoning depth, editorial precision, 200K context
- **Device**: Mac browser (primary)
- **Use Cases**: High-fidelity prose, analytical writing, structural editing

### Mistral (Browser Only)
- **Role**: Uncensored fiction lab
- **Strengths**: Creative freedom, experimental generation
- **Device**: Mac browser only
- **Use Cases**: Uncensored creative drafts, dialogue experimentation

### ChatGPT (Browser Only)
- **Role**: Creative brainstorming / narrative ideation (when Perplexity insufficient)
- **Strengths**: Conversational fluency, GPT-5 access (free tier)
- **Device**: Mac browser (primary)
- **Use Cases**: Character dialogue, narrative exploration, quick creative iterations

---

## Workflow Integration Pattern

### Pre-Session
1. Pull relevant context from GitHub (character notes, world rules, previous scenes)
2. Review quarterly planning notes if relevant
3. Select appropriate LLM based on task matrix above
4. **Default to Perplexity Pro first during experiment**

### Generation Session
1. Use focused prompt + retrieved context
2. For creative work: test multi-model in Perplexity before opening browser tabs
3. Maintain session intentionality—avoid conversational drift
4. Keep each session scoped to specific outcome
5. Note when browser tool is chosen over Perplexity (track pattern for review)

### Post-Session
1. Commit output to GitHub with descriptive metadata
2. Tag outputs for quarterly retrospectives
3. Delete ephemeral chat threads
4. Update relevant project documentation
5. **Log experiment observations** (browser friction vs. value, Perplexity coverage)

### Review Cycle
- Weekly: Review outputs against planning cadence
- Quarterly: Assess tool effectiveness, update task routing if needed
- **Q1 2026 Experiment Review**: Evaluate Perplexity-only app strategy
- Annually: Evaluate subscription value (Perplexity Pro renewal decision)

---

## Behavioral & Cognitive Boundaries

### Intentional Usage
- **Single native app = maximum intentionality**: Perplexity for all device-based AI interaction
- **Session containment**: One focused task per chat; archive and move on
- **No chat sprawl**: Delete threads after archiving outputs to GitHub
- **Browser friction as feature**: Forces evaluation of whether task truly needs AI

### Parasocial Risk Mitigation
- **Browser-only access** for all free-tier LLMs creates maximum friction barrier
- **No native app fallbacks** prevents switching apps to continue conversations
- **GitHub MCP** forces explicit capture decisions (not passive accumulation)
- **Perplexity instrumental design** emphasizes research over conversation
- **Experiment tests whether app availability = parasocial risk** or if discipline is sufficient

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
- **Experiment learnings will inform subscription decision**

### RAG Enhancement Readiness
- Organized GitHub structure enables **future vector search** integration
- YAML frontmatter supports **semantic retrieval** tool adoption
- Modular content organization works with emerging **RAG tools**

---

## Risk Mitigation

### Experiment-Specific Risks
- **Risk**: Excessive browser friction prevents valuable creative work
  - **Mitigation**: Track when browser is avoided vs. genuinely not needed
  - **Decision point**: If valuable work is consistently skipped, reassess single-app strategy
- **Risk**: Perplexity Pro multi-model access insufficient for creative needs
  - **Mitigation**: Document specific creative tasks where browser tools are required
  - **Decision point**: If pattern emerges, consider targeted app exceptions
- **Risk**: iPhone lacks quick disposable query option without Gemini
  - **Mitigation**: Use Perplexity Pro for quick queries; assess if friction is beneficial or harmful
  - **Decision point**: If daily utility suffers, reconsider Gemini containment app

### Browser Friction vs. Usage Value
- **Monitor**: Does browser-only access create friction that improves intentionality or reduces utility?
- **Current stance**: Test Perplexity-only native app strategy through Q1 2026
- **Decision rule**: Review experiment results end of March 2026

### Quarterly Review Questions
1. Is GitHub MCP capturing all keeper work effectively?
2. Are free-tier rate limits causing workflow disruption?
3. Is Perplexity Pro providing sufficient value as sole native app?
4. Are browser-based tools meeting creative workflow needs?
5. Is single-app strategy working as designed or creating harmful friction?
6. **Experiment-specific**: How often was browser avoided due to friction vs. genuine non-need?
7. **Experiment-specific**: Did Perplexity Pro's multi-model access reduce reliance on browser tools?

---

## Summary Architecture

**One Native App (All Devices)**: Perplexity Pro (free 1 year) – sole AI app on iPhone, iPad, Mac

**Browser-Based Free Tier (All Devices)**: ChatGPT, Gemini, Claude, Mistral – surgical, situational, intentional

**System of Record**: GitHub MCP – vendor-agnostic datalake, versioning, intentionality enforcement

**Device Intent Encoding**:
- **iPhone**: Perplexity Pro only (instrumental AI, voice/image, multi-model queries)
- **iPad**: Perplexity Pro only (research, content exploration via share sheet)
- **Mac**: Perplexity Pro (archival + GitHub MCP) + browser LLMs (creative sessions)

**Workflow Discipline**:
- Capture → retrieve → generate → store
- Clean sessions, delete sprawl
- Metadata for retrieval
- Quarterly reassessment
- **Experiment tracking through Q1 2026**

**Experiment Status**: Active (Jan 10 - Mar 31, 2026)
- Testing Perplexity-only native app strategy
- All other AI tools strictly browser-based
- Review findings end of Q1 2026 to inform permanent architecture

This architecture balances **cost-effectiveness, vendor independence, creative flexibility,** and **parasocial risk mitigation** while maintaining the "workbench, not warehouse" philosophy across all systems. The Perplexity-only experiment tests whether maximum app friction optimizes intentionality without sacrificing utility.
