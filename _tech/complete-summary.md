# AI Tool Stack Integration Summary
**Date:** January 11-12, 2026

## Overview
Evaluated and implemented a three-tool AI stack for creative writing workflows with private GitHub repo: **Perplexity Pro (GitHub MCP)**, **Gemini CLI**, and **GitHub Copilot Chat**. Removed redundant Gemini Code Assist.

## Tools Evaluated & Decisions

### 1. Gemini CLI (Implemented)
**Purpose:** Local batch operations, multi-file analysis, consistency checks
- **Free Tier:** 1,000 requests/day, 60/min, 1M token context
- **Installation:** `brew install gemini-cli` (macOS)
- **VSCode Integration:** `/ide enable` (one-time setup) for workspace context
- **Key Features:**
  - Local clone speed beats Perplexity MCP latency
  - Batch scene analysis, consistency checks
  - Non-interactive scripting: `gemini -p "command" --output-format json`
  - Shell/file operations, MCP extensibility
  - Auto-detects open files, workspace, GEMINI.md context files
- **Best For:** Heavy lifting on local repos (__inbox triage, multi-scene diffs)
- **Usage Estimate:** 8% (reserve tool)

### 2. GitHub Copilot Chat (Primary Tool - 70%)
**License:** Two-year Copilot for Education (verified)
- **Access:** Full Copilot Pro features in VSCode
- **Models:** GPT, Claude, Gemini (multi-model support)
- **Strengths:** 
  - Inline completions and prose tweaks
  - Agent mode with workspace context
  - Real-time editing in open files
  - Instant repo awareness
- **Best For:** Daily workbench editing, scene expansions, README management
- **Usage Estimate:** 70% (default workhorse)

### 3. Perplexity Pro with GitHub MCP (Secondary - 20%)
**Purpose:** Exploratory research, long-tail thinking, repo synthesis
- **Models:** GPT-5/4.x, Claude Sonnet/Opus, Gemini 2.5+
- **Strengths:**
  - Conversational depth across full repo
  - Search grounding for research
