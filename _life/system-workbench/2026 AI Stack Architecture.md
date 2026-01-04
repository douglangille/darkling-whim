Title: 2026 AI Stack Architecture

## Overview

This stack intentionally separates tools by **role**, **device**, and **data permanence** to contain chat sprawl and reduce parasocial drift.

## Devices and Roles

- **iPhone – Ephemeral AI**
  - Tool: Gemini app
  - Settings: Activity kept but auto-deletes after 3 months [file:49][web:75]
  - Intent: Disposable queries, quick ideas, throwaway brainstorming
  - No Perplexity, Claude, or Mistral installed
  - Acts as a containment zone for chat sprawl and “petting the AI”

- **iPad – Exploration AI**
  - Tool: Gemini app, primarily invoked via Safari/Feedeed share sheet
  - Intent: Content-first exploration—summaries, critiques, questions about articles
  - Browser-centric; AI is a processor of pages, not a destination for chatting
  - Minimizes standalone “New Chat” usage to avoid rambling and attachment

- **Mac – Archival and Prose AI**
  - Tool: Perplexity with GitHub/MCP integration for research and structured outputs [memory:24]
  - Tools: Claude and Mistral for high-fidelity and uncensored prose
  - Intent: Serious projects, keepers, and versioned work only

## Tool Specialization

- **Perplexity** – Research engine and archival front-end
- **Gemini** – Ephemeral assistant for disposable thinking
- **Claude** – Premium prose / structural editing engine (used sparingly)
- **Mistral** – Uncensored fiction lab for creative drafts

This architecture encodes intent into the combination of device and tool: if it happens on Mac + Perplexity, it is by definition “keeper” work; if it happens on mobile Gemini, it is by definition temporary.
