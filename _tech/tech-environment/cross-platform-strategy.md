# Cross-Platform Workflows

## Migration: Gemini → ChatGPT

### Rationale

- User prefers ChatGPT for synthesis
- Plans to do most work in ChatGPT going forward
- Has existing Gemini conversations to continue

### Rejected Tools

- **Echoes**: Paid (cost concern)
- **TopicsGPT**: Deprecated (unavailable)

### Export Tools Explored

- RevivalStack's AI Chat Exporter (Tampermonkey script)
- Chrome plugins:
  - "Gemini Exporter"
  - "AI Exporter"

### Preferred Approach

**Plugin-only exporters**:
- Allow Markdown output
- No script manager required (Tampermonkey avoided)
- Low-friction solution

### Format Choice

**Markdown (`.md`)**:
- Readability
- Structural integrity
- Standard for import/export

### Decisions

- No Echoes (cost)
- No TopicsGPT (deprecated)
- Plugin-only Gemini exporters preferred
- Markdown chosen as export/import format

### Open Loops

- User may request reusable ChatGPT prompt template for continuing Gemini conversations
- User may want support cleaning up exported Markdown for use in ChatGPT
- User may want walkthrough or hands-on help with specific plugins or workflows

### Discardables

- Detailed exploration of JSON, PDF, or TXT formats (unnecessary for current workflow)
- Script-based solutions (not preferred unless necessary)

## AI Tool Emulation

### NotebookLM in ChatGPT

- Structured prompts + vault context
- Comparison of tools and limitations provided

### Perplexity-Style Behavior

- Scaffolding for citations + research flows
- Custom instructions for Perplexity-style article prompt
- Tailored to user's voice and writing style for blog generation

### Feature Comparison Table

Provided real-time comparison across:
- ChatGPT
- Claude
- Gemini
- Grok
- Mistral

### Creative Writing Comparison

Evaluated which chatbot best for creative writing:
- Claude: Second-best for longform narrative
- ChatGPT: Best all-around (chosen)

### Value-Driven Decision

User emphasized preference for value; concluded ChatGPT provides best all-around deal.

### Custom Instructions Workflow

1. User requested Perplexity-style article prompt
2. Assistant delivered fully structured, reusable version
3. User requested drop-in version for Custom Instructions
4. User rejected generic version
5. Requested rework aligned with user's voice/style
6. Final version delivered and accepted

### Decisions

- ChatGPT = most cost-effective, all-around assistant
- Claude acknowledged but not primary
- Custom instructions can emulate Perplexity-style with slight trade-offs
- ChatGPT capable of acting as both NotebookLM and Perplexity with scaffolding

### Open Loops

- Create hybrid Claude + ChatGPT creative writing workflow
- Build downloadable Custom GPT profile with logo and Perplexity blog-style settings
- Generate Apple Notes/Markdown export versions of blog prompt or research summaries

### Discardables

- Original generic Perplexity-style prompt (rejected as too clunky for drop-in use)
