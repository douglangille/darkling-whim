# AI Tool Stack Rationalization - Dec 31, 2025

## Context
Year-end review and optimization of AI tool ecosystem to address conversation sprawl and clarify tool-specific roles.

## Current Tool Stack

### Main Tools
1. **Gemini (Free Tier)** - Mobile devices
   - Generous multimodal capabilities at free tier
   - Primary chatbot with accumulated context
   - Auto-expunge after 3 months
   - Custom instructions for thread hygiene and drift management

2. **Perplexity Pro** (1-year free via PayPal)
   - Primary workbench for deep work
   - Wired to GitHub repo for long context
   - Access to multiple models
   - Spaces with custom instructions
   - Strategy: Delete threads when done, rely on GitHub for long-tail context

### Niche/Single-Use Tools
3. **Claude (Free Tier)**
   - Prose generation and creativity
   - Artifacts capability
   - Severely rate-limited (strategic use only)
   - Strategy: Immediate deletion after extracting output

4. **Mistral (Free Tier)**
   - Same use case as Claude
   - Uncensored content generation (horror, adult themes)
   - Critical for fiction writing needs
   - Strategy: Immediate deletion after extracting output

5. **ChatGPT (Free)** - *Repositioned*
   - Previously on Plus subscription (too expensive for value)
   - Conversational jack-of-all-trades
   - Canvas feature for brainstorming
   - Rate-limited and frustrating at free tier
   - **New Role**: Creative brainstorming tool (not prose generation)
   - Strategy: Immediate deletion after extracting brainstorm

## Core Problem: Conversation Sprawl

### Root Issue
- Conversations accumulate quickly across platforms
- Even quarterly purging creates significant sprawl depth
- Too much accumulated context "removes the color and everything turns brown"
- Balance needed between useful context retention and overwhelming accumulation

### Custom Instructions Strategy (Gemini)
Key principles implemented:
- **Bottom Line Upfront**: One crisp, decisive opening sentence
- **Inverted Pyramid**: Lead with important facts, use bullets/bold headers
- **Decisive Transparency**: Provide most likely answer immediately, state confidence level
- **Thread Hygiene & Drift Guard**: 
  - Interrupt when conversation shifts topics
  - Suggest moving to new thread
  - Provide "Roll-Up" summary in code block for easy copy-paste
  - Suggest deletion if no long-term value
- **Strategic Constraints**:
  - No forced frameworks unless uniquely applicable
  - No default fiction mode
  - Challenge assumptions only when strategically significant

## Retention Strategy by Tool

### Gemini (Selective Retention)
**Keep conversations that:**
- Build reusable context (preferences, workflows, recurring problems)
- Have reference value (would actually scroll back to consult)
- Tied to active projects not archived elsewhere

**Delete immediately:**
- One-off questions
- Quick factual lookups
- Anything with Roll-Up summary saved elsewhere

### Perplexity Pro
- Delete threads when complete
- GitHub handles long-tail context

### Claude/Mistral/ChatGPT (Single-Use Tier)
- Extract output/brainstorm
- Save to appropriate location (GitHub, notes)
- Delete thread immediately

## Key Insights

1. **ChatGPT's Repositioning**: Moved from "trying to do everything" to focused creative brainstorming niche alongside Claude/Mistral in single-use tier

2. **The Context Paradox**: Accumulated context improves conversational ability but eventually degrades quality ("everything turns brown")

3. **Tool Boundaries Matter**: Each tool now has clear, non-overlapping role that plays to its strengths at free/Pro tier pricing

4. **Immediate Deletion ≠ Lost Value**: Single-use tools provide value through extraction and proper archiving, not conversation history

5. **Sustainable Sprawl Management**: Quarterly purging was too aggressive; selective retention with clear criteria is more sustainable

## Decision Framework

**When evaluating whether to keep a conversation:**
1. Would I reference this again?
2. Does it build context that improves future interactions?
3. Is it already archived elsewhere?
4. Does it relate to active work?

If no to all four → delete immediately
