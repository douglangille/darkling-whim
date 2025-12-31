# AI Tool Stack Reference

## Main Tools

### Gemini (Free Tier)
- **Platform**: Mobile devices (iPhone/iPad)
- **Primary Use**: Main conversational chatbot with multimodal capabilities
- **Context Strategy**: Selective retention with 3-month auto-expunge
- **Retention Criteria**:
  - Builds reusable context (preferences, workflows)
  - Has reference value (would consult again)
  - Tied to active projects
- **Delete**: One-offs, quick lookups, Roll-Up archived elsewhere

### Perplexity Pro
- **Platform**: All devices (primary workbench)
- **Primary Use**: Research, deep work, complex queries
- **Integration**: GitHub repo for long context
- **Features**: Multiple models, Spaces with custom instructions
- **Context Strategy**: Delete threads when done, GitHub handles long-tail

## Single-Use Tools (Immediate Deletion)

### Claude (Free Tier)
- **Primary Use**: Prose generation, creative writing
- **Feature**: Artifacts
- **Limitation**: Severely rate-limited (strategic use only)
- **Workflow**: Generate prose → Extract → Delete thread

### Mistral (Free Tier)
- **Primary Use**: Uncensored prose (horror, adult themes)
- **Workflow**: Generate prose → Extract → Delete thread

### ChatGPT (Free Tier)
- **Primary Use**: Creative brainstorming, Canvas ideation
- **Secondary**: Conversational framework exploration
- **Limitation**: Rate-limited at free tier
- **Workflow**: Brainstorm → Extract ideas → Delete thread
- **Not For**: Polished prose (use Claude instead)

## Tool Selection Decision Tree

**Need accumulated context?** → Gemini
**Research/deep work?** → Perplexity Pro
**Polished prose?** → Claude
**Uncensored content?** → Mistral
**Creative brainstorming?** → ChatGPT
