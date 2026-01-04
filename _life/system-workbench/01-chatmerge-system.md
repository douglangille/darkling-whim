# ChatMerge System

## Overview
A structured XML-based method for merging chat conversations while maintaining continuity and preventing context loss.

## Core Schema

```xml
<ChatMerge>
  <Entry>
    <Timestamp>[Insert date/time or leave blank]</Timestamp>
    <Canon>
      <Item></Item>
    </Canon>
    <Decisions>
      <Item></Item>
    </Decisions>
    <OpenLoops>
      <Item></Item>
    </OpenLoops>
    <Discardables>
      <Item></Item>
    </Discardables>
  </Entry>
</ChatMerge>
```

## Section Definitions

### Canon
Hard facts, character traits, roles, settings, strategies, workflow distinctions, or system architecture details.

### Decisions
What was agreed, settled, or finalized. Operational rules and commitments.

### OpenLoops
Anything unfinished, unresolved, or flagged for follow-up.

### Discardables
Exploration, fluff, metaphors, or irrelevant content not worth keeping.

## Usage Pattern

1. Paste `<ChatMerge>...</ChatMerge>` block into master chat
2. ChatGPT responds: "context added"
3. Optionally request: "rolling summary" to get digest

## Rolling Summary Cadence

- First merge → "Generate rolling summary"
- Subsequent merges → "Regenerate rolling summary"
- Or simply: "...and generate rolling summary"

## Purpose

- **Append-only ledger** (not replacement)
- Machine-parsable and human-readable
- Transaction log of conversations
- Chronological audit trail
- Prevents overwriting earlier context

## Integration

- Master chat = XML ledger (ChatGPT)
- ZORA export = human-readable digest
- Custom Instructions include: "When input is wrapped in `<ChatMerge>...</ChatMerge>`, reply only: `context added`."
