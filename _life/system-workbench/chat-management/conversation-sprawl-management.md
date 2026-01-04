# Conversation Sprawl Management Strategy

## The Problem
- Conversations accumulate quickly across platforms
- Even quarterly purging creates significant depth
- Too much context "removes the color and everything turns brown"
- Balance needed: useful context vs. overwhelming accumulation

## The Solution: Tiered Retention Strategy

### Tier 1: Accumulated Context (Gemini)
**Keep If:**
1. Would I reference this again?
2. Does it build context that improves future interactions?
3. Is it already archived elsewhere? (If yes → delete)
4. Does it relate to active work?

**Delete If:** No to all four questions above

**Auto-Expunge:** 3 months (set in Gemini settings)

### Tier 2: Workbench Context (Perplexity Pro)
**Strategy:** Delete all threads after completion
**Long-tail Context:** Managed via GitHub repo integration
**No accumulation needed:** External context system handles persistence

### Tier 3: Single-Use Tools (Claude/Mistral/ChatGPT)
**Strategy:** Immediate deletion after extraction
**Workflow:**
1. Generate output/brainstorm
2. Extract and save to appropriate location (GitHub, notes app, project files)
3. Delete thread immediately
4. No exceptions

## Thread Hygiene Practices

### The Roll-Up
- Request summary at conversation end
- Delivered in code block for easy copy-paste
- Captures key insights/decisions
- Archive before deletion if valuable

### Drift Guard
- Interrupt when topic shifts
- Prompt to create new thread for new topic
- Prevents multi-topic sprawl in single conversation

### Quarterly Review
- Too aggressive for everything
- Better: Selective retention with clear criteria
- Review Gemini threads quarterly, apply retention criteria
- Single-use tools handle themselves via immediate deletion

## Anti-Patterns to Avoid

❌ Keeping "just in case" conversations
❌ Accumulating single-use tool threads
❌ Letting multi-topic conversations sprawl
❌ Forgetting to extract before deletion
❌ Building dependency on ChatGPT conversation history
