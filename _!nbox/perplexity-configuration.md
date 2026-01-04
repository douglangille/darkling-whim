# Perplexity Pro Configuration Guide

## Account Settings
- Subscription: Perplexity Pro
- Primary use: Research, writing, planning, brainstorming

---

## Writing Studio Space Setup

### Space Configuration
**Name**: Writing Studio (or similar)

**Connected Resources**:
- GitHub MCP connection to writing repos
- Bootstrap file with custom instructions
- System prompt for persistent persona

**Default Settings**:
- **Model**: Claude Sonnet 4.5
- **Sources**: None (toggle to Web when research needed)
- **Instructions**: [Your bootstrap prompt - paste from your existing setup]

### When to Use Writing Studio
- Creative writing (fiction, blog posts)
- Brainstorming story ideas or post concepts
- Generating prompts for other tools (if needed)
- Iterative revision with MCP context

---

## Model Selection Guide

| Model | Best For | When to Use |
|-------|----------|-------------|
| Claude Sonnet 4.5 | Creative writing, prose, brainstorming | Writing Studio, uncensored content, complex reasoning |
| GPT-4o | Balanced research/writing | Mixed tasks, when Claude unavailable |
| Sonar (default) | Quick lookups, general queries | Fast searches, basic questions |

---

## Source Control Strategy

### Choose Sources: None
**Use for**:
- Fast brainstorming without research delay
- Prose generation
- Prompt creation
- Conversational thinking (journaling via dictation)

**Why**: Skips web research, acts like ChatGPT for speed

### Choose Sources: Web
**Use for**:
- Research queries
- Fact-checking
- Troubleshooting (appliance fixes, IT issues)
- When citations needed

### Choose Sources: Internal
**Auto-enabled** when MCP/files connected
- Queries GitHub repos via MCP
- Searches uploaded files in Spaces
- RAG functionality for your content

---

## iOS App Settings (iPhone 13)

### Default Configuration
Settings > Search > **Default to "Choose sources: None"**

### Quick Workflows
**Dictation for Reflection**:
1. Open Perplexity app
2. Tap microphone
3. Speak stream-of-consciousness
4. Read structured response
5. No need to save - process = value

**Troubleshooting with Photos**:
1. New thread
2. Toggle sources: Web (on)
3. Upload photo of issue
4. Dictate question
5. Get multimodal analysis

---

## Labs Usage Guide

### Accessing Labs
- MacBook web only (best for MCP workflows)
- Click Labs tab > New project

### Common Project Types

**Podcast Script Generation**:
```
Create a 15-minute podcast script (two hosts) explaining 
the key ideas from [GitHub repo link / uploaded files]. 
Conversational tone, suitable for listening during chores.
```

**Deep Research Reports**:
```
Research [topic] and create a structured report with:
- Executive summary
- Key findings
- Recommendations
- Cited sources
```

**Asset Creation**:
```
Analyze this spreadsheet and create:
- Summary dashboard
- Key metrics chart
- Exportable insights document
```

### Labs Limitations
- Creates **scripts**, not audio files (need external TTS or NotebookLM)
- 5-30 minutes per project execution
- Outputs in Assets tab (download individually)

---

## MCP GitHub Connection

### Setup (MacBook Only)
1. Install PerplexityXPC helper app
2. Connect GitHub repos in Space settings
3. Grant repo access permissions

### Capabilities
- Read file contents across repos
- Search by filename, tag, content
- Context-aware responses using repo history
- Can write files back to repos (when prompted)

### Example Queries in MCP-Connected Space
- "Find all posts tagged 'Haley' in this repo"
- "Summarize changes in the last 5 commits"
- "Create a style guide based on my existing blog posts"
- "Concatenate all stories in /fiction folder into one markdown file"

---

## Voice Features (Rarely Used)

### When to Use Dictation (Preferred)
- Reflection/journaling
- Brainstorming while walking
- Quick queries when hands busy
- Maintains tool relationship (not parasocial)

### When to Use Interactive Voice (Optional)
- Real-time troubleshooting conversations
- Complex multi-turn problem solving
- Testing only - not primary workflow

**Note**: Interactive voice mode creates more rapport/relationship feel; 
dictation maintains clearer tool boundary for AUDHD brain.

---

## Spaces Strategy

### Current Spaces
1. **Writing Studio** - MCP GitHub, Claude default, creative work
2. **Planning** (optional) - Quarterly/annual goal tracking
3. **[Project-specific]** - As needed, not permanent

### Space vs. Regular Thread
**Use Space when**:
- Need persistent MCP connection
- Custom system prompt required
- Collaborative (share with team)
- Long-term project (quarterly planning)

**Use Regular Thread when**:
- One-off query
- Quick research
- No need for context continuity

---

## Reading Theme (For Reference)
While Perplexity UI font can't be changed, maintain consistency elsewhere:

**Target Settings**:
- Font: Serif (Iowan-style)
- Background: Sepia/warm
- Size: 175% (comfortable at arm's length)
- Apps: feeeed, Apple Books, Safari Reader

---

## Troubleshooting Common Issues

**Sources not working in Space**:
- Check MCP connection in Space settings
- Verify GitHub permissions
- Try "Sources: Internal" toggle

**Labs not generating audio**:
- Labs creates scripts only
- Use external TTS (ElevenLabs) or NotebookLM for audio

**Model changes not persisting**:
- Model sets per Space, not globally
- Set default in Space settings for consistency

---

**Last Updated**: December 27, 2025
