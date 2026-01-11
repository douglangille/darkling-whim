---
title: "n8n Story Critique Automation Workflow"
date: 2024
categories: [tech, automation, writing]
tags: [n8n, openrouter, google-docs, llm, automation, workflow, api, literary-critique]
context: Building n8n automation to fetch story URLs, analyze with LLM, and output critiques to Google Docs
status: development
---

# n8n Story Critique Automation

*An exploration of building an n8n workflow to automatically generate literary critiques of published stories using LLMs and output to Google Docs.*

## Project Goal

Create an n8n automation that:
1. Accepts a URL to a published story
2. Fetches and reads the story content
3. Uses an LLM (via OpenRouter) to generate:
   - Literary critique
   - 5-6 specific revision suggestions
   - 5-6 expansion ideas (if suitable for longer form)
4. Outputs structured analysis to a new Google Doc

---

## Design Evolution

### Initial Approach: Webhook Trigger

**Original Plan:**
- Webhook POST endpoint to receive URL
- HTTP fetch of story HTML
- Content extraction via custom function
- OpenRouter LLM analysis
- Google Docs output

**Problems:**
- Webhook management overhead
- Extra friction vs. simple paste-and-run

### Pivot 1: Manual Trigger with Text Field

**Better UX:**
- Manual trigger button
- Simple URL text field
- Click "Execute" to run
- More cognitive than integration-focused

**Implementation:**
- Manual Trigger node
- Set node with `storyUrl` field
- Rest of workflow unchanged

### Challenge: Content Extraction

**Extraction Node Failures:**

Multiple attempts at HTML content extraction failed:

1. **Custom Function node** (deprecated)
   - Old extraction pattern
   - Failed in newer n8n versions
   - Regex-based HTML stripping unreliable

2. **Webpage Content Extractor** (community node)
   - Mozilla Readability-based
   - Input format issues
   - Configuration complexity

3. **Readability Reader** (community node)
   - Similar issues
   - Couldn't get HTML passed correctly

**Root Cause:**
- Community extraction nodes expected specific input formats
- n8n's HTTP Request output structure didn't match
- Fragile regex approaches broke on real pages

### Pivot 2: Pass Raw HTML to LLM

**Simplest Solution:**
- Fetch full HTML as string
- Send entire HTML page to LLM in prompt
- Let LLM extract and analyze content itself

**Benefits:**
- No extraction node dependencies
- LLM handles both extraction and analysis
- More token-heavy but far more reliable
- Avoids fragile intermediate steps

### Challenge: OpenRouter Authentication

**Authorization Failures:**

Multiple auth attempts failed:

1. **HTTP Request with manual headers**
   - Hardcoded Authorization header
   - Formatting issues (quotes, spaces)
   - Inconsistent results

2. **OpenRouter credential type**
   - Built-in n8n OpenRouter credential
   - Known bugs with baseURL passing
   - "Package doesn't exist" errors

3. **Community OpenRouter Chat node**
   - Attempted to use specialized node
   - Integration issues in current n8n versions

**Root Cause:**
- OpenRouter requires: `Authorization: Bearer <token>`
- Manual header construction error-prone
- Built-in credential support incomplete/buggy

**Solution:**
- Use HTTP Request node's **Bearer Token authentication**
- Let n8n format the Authorization header
- Key goes in dedicated auth field (not manual header)
- No "Bearer" prefix needed in field

---

## Final Working Design

### Workflow Structure

```
[Manual Trigger]
      ↓
[Paste Story URL] (Set node with storyUrl field)
      ↓
[Fetch Full HTML] (HTTP Request: responseFormat = string)
      ↓
[OpenRouter HTTP Request] (POST to /v1/chat/completions)
      ↓
[Prepare Google Doc] (Function: extract response, format title)
      ↓
[Create Google Doc] (Google Docs node)
```

### Key Components

#### 1. Manual Trigger + Set Node

```json
{
  "name": "Manual Trigger",
  "type": "n8n-nodes-base.manualTrigger"
}
```

```json
{
  "name": "Paste Story URL",
  "type": "n8n-nodes-base.set",
  "parameters": {
    "values": {
      "string": [
        { "name": "storyUrl", "value": "" }
      ]
    }
  }
}
```

#### 2. Fetch Full HTML

```json
{
  "name": "Fetch Full HTML",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "url": "={{$json.storyUrl}}",
    "responseFormat": "string"
  }
}
```

**Critical Setting:** `responseFormat: "string"` returns raw HTML text

#### 3. OpenRouter HTTP Request

**Authentication Setup:**
- Method: POST
- URL: `https://openrouter.ai/api/v1/chat/completions`
- Authentication: **Bearer Token**
- Token: `<YOUR_OPENROUTER_API_KEY>` (no "Bearer" prefix)
- Send Body as: JSON

**Body Structure:**
```json
{
  "model": "openai/gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You are a literary critic. Given raw HTML of a story page, extract the story text and provide: (1) concise literary critique, (2) 5-6 specific revision suggestions, (3) if appropriate, 5-6 expansion ideas. Use clear section headings."
    },
    {
      "role": "user",
      "content": "URL: {{$json.storyUrl}}\n\nHTML:\n{{$json['Fetch Full HTML']}}"
    }
  ],
  "max_tokens": 1800
}
```

**Model Options:**
- `openai/gpt-3.5-turbo` - Reliable, affordable
- `google/gemma-2-9b-it` - Free tier option
- `mistralai/mixtral-small-3b-instruct:free` - Free alternative
- Any OpenRouter-supported model with your API key

#### 4. Prepare Google Doc

```javascript
const critique = items[0].json.choices?.[0]?.message?.content || items[0].json.error || '';
const date = new Date().toISOString().split('T')[0];
return [{ 
  json: { 
    title: `Story Critique – ${date}`, 
    body: critique 
  } 
}];
```

**Safe Extraction:**
- Uses optional chaining for response
- Falls back to error message if present
- Generates date-stamped title

#### 5. Create Google Doc

```json
{
  "name": "Create Google Doc",
  "type": "n8n-nodes-base.googleDocs",
  "parameters": {
    "title": "={{$json.title}}",
    "content": "={{$json.body}}"
  },
  "credentials": {
    "googleDocsOAuth2Api": {
      "id": "google-docs",
      "name": "Google Docs OAuth2"
    }
  }
}
```

---

## Authentication Setup

### OpenRouter API Key

1. **Get Key:** https://openrouter.ai/keys
2. **In n8n HTTP Request Node:**
   - Authentication → Select "Bearer Token"
   - Token field → Paste your OpenRouter API key
   - Do NOT include "Bearer" prefix (n8n adds it)
   - Do NOT add manual Authorization header

**Critical Points:**
- OpenRouter uses standard Bearer token auth
- All requests require: `Authorization: Bearer <key>`
- Let n8n format the header via auth field
- Manual header construction causes auth failures

### Google Docs OAuth2

1. Set up Google Cloud Project
2. Enable Google Docs API
3. Create OAuth2 credentials
4. Configure in n8n:
   - Settings → Credentials → Add Credential
   - Google Docs OAuth2 API
   - Follow OAuth flow

---

## LLM Prompt Design

### System Prompt

```
You are a literary critic and writing workshop facilitator. 
Given the full raw HTML of a story page, extract the story text 
from the HTML and provide:

1. A concise literary critique
2. 5-6 concrete revision suggestions  
3. If appropriate, 5-6 ideas for expanding into a longer work

Use clear section headings. Be intelligent, specific, and mildly opinionated.
Decide whether the piece is best revised as flash fiction or expanded.
```

### User Prompt Pattern

```
Here is the full HTML from: {{URL}}

HTML:
{{RAW_HTML_STRING}}
```

**Why This Works:**
- LLM gets complete page content
- Can intelligently extract story text from HTML
- Handles headers, footers, nav automatically
- More token-heavy but far more reliable
- Avoids fragile extraction preprocessing

### Token Considerations

**HTML Size:**
- Typical blog post HTML: 20-50KB
- Tokens: ~5,000-12,000 (at 4 chars/token avg)
- Story content: 1,000-3,000 tokens
- LLM can easily filter noise

**Response Length:**
- `max_tokens: 1800` allows detailed critique
- Literary critique: ~300 tokens
- Revision suggestions: ~600 tokens  
- Expansion ideas: ~600 tokens
- Formatting overhead: ~300 tokens

**Cost Estimate:**
- Input: ~10K tokens
- Output: ~1.5K tokens
- Total: ~11.5K tokens per run
- With free models: $0
- With GPT-3.5-turbo: ~$0.02 per critique

---

## Output Format

### Google Doc Structure

**Title:**
```
Story Critique – YYYY-MM-DD
```

**Expected Body Sections:**

```markdown
# Literary Critique

[LLM's analysis of narrative structure, voice, pacing, themes]

# Revision Suggestions

1. [Specific, actionable revision idea]
2. [Second suggestion]
3. [...]

# Expansion Ideas

*(Optional section - only if LLM determines story suitable for expansion)*

1. [Expansion approach]
2. [Second approach]
3. [...]
```

**Tone:**
- Workshop-style feedback
- Intelligent and specific
- Mildly opinionated
- Constructive and actionable

---

## Lessons Learned

### Content Extraction

**Don't Over-Engineer:**
- Community extraction nodes add fragility
- LLMs can extract from HTML directly
- Raw HTML → LLM simpler than HTML → Extract → LLM
- Token cost trade-off worth the reliability

**When Extraction Makes Sense:**
- Very large pages (>50KB HTML)
- Rate-limited or expensive models
- Need for preprocessing (translation, format conversion)

### OpenRouter Integration

**Bearer Token Auth Pattern:**
- Use n8n's Bearer Token authentication field
- Don't manually construct Authorization headers
- Let framework handle header formatting
- Reduces auth errors significantly

**Model Selection:**
- Free models work for critique tasks
- GPT-3.5-turbo reliable for $0.02/run
- Claude models better for literary analysis (when budget allows)
- Test with free models first

### n8n Workflow Design

**Manual Trigger > Webhook:**
- For cognitive/creative workflows
- Paste-and-think UX pattern
- Less ceremony than webhook URLs
- Better for occasional use

**Keep It Simple:**
- Fewer nodes = fewer failure points
- Avoid community nodes when possible
- Use built-in nodes with proper auth
- Test each node independently

---

## Future Enhancements

### Potential Improvements

**1. Auto-Extract Story Title**
```javascript
// In Prepare Google Doc function:
const html = $node["Fetch Full HTML"].json;
const titleMatch = html.match(/<title>([^<]+)<\/title>/);
const storyTitle = titleMatch ? titleMatch[1] : "Story";
const date = new Date().toISOString().split('T')[0];
return [{ 
  json: { 
    title: `${storyTitle} – Critique – ${date}`,
    body: critique
  }
}];
```

**2. Chunk Large HTML**
- For pages > 50KB
- Split HTML into chunks
- Process each chunk
- Combine analyses

**3. Multiple LLM Passes**
- First pass: Overall critique
- Second pass: Line-level edits
- Third pass: Structural suggestions
- Combine into comprehensive doc

**4. Organized Output**
- Create folder structure in Google Drive
- `/Critiques/YYYY/MM/` organization
- Link back to original story URL
- Track critique history

**5. Comparative Analysis**
- Compare multiple drafts
- Track changes over time
- Measure improvement metrics
- Generate progress reports

**6. Multi-Model Ensemble**
- Run same critique through 2-3 models
- Compare perspectives
- Synthesize consensus view
- Flag disagreements

---

## Troubleshooting

### Common Issues

#### "Authorization failed"

**Causes:**
- Wrong auth method (manual header vs. Bearer Token field)
- Extra spaces/quotes in API key
- "Bearer" prefix in token field
- Using OpenAI key instead of OpenRouter key

**Solutions:**
- Use HTTP Request node's Bearer Token authentication
- Paste key in Token field (no prefix)
- Remove manual Authorization headers
- Verify key at openrouter.ai/keys

#### "Bad parameters"

**Causes:**
- Invalid model name
- Malformed messages array
- Missing required fields
- JSON syntax error in body

**Solutions:**
- Verify model exists: openrouter.ai/models
- Check messages structure: `[{role, content}]`
- Validate JSON syntax
- Test with minimal body first

#### "Extraction node failed"

**Causes:**
- Community node not installed
- Wrong input format
- HTML structure incompatible

**Solutions:**
- Skip extraction entirely
- Send raw HTML to LLM
- Let LLM handle extraction

#### Empty/Truncated Output

**Causes:**
- `max_tokens` too low
- Model hitting limits
- HTML too large for context

**Solutions:**
- Increase `max_tokens` to 2000+
- Use model with larger context window
- Preprocess HTML to reduce size

---

## Testing Strategy

### Unit Testing Nodes

**1. Test HTTP Fetch**
```
Input: Known story URL
Expected: Full HTML string
Verify: Response contains story text
```

**2. Test OpenRouter Auth**
```
Simple body: {"model":"openai/gpt-3.5-turbo","messages":[{"role":"user","content":"hello"}]}
Expected: 200 response with completion
Verify: No auth errors
```

**3. Test Google Docs**
```
Input: Sample title and body
Expected: New doc created
Verify: Content appears correctly
```

### Integration Testing

**Test Stories:**
1. Short flash fiction (~500 words)
2. Medium story (~2000 words)
3. Long story (~5000 words)
4. Story with complex HTML
5. Story with images/media

**Verify:**
- All stories processed successfully
- Critiques are relevant and specific
- Output formatting is clean
- No token limit errors
- Google Docs created with correct titles

---

## Resources

### Documentation
- [n8n HTTP Request Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
- [OpenRouter API Docs](https://openrouter.ai/docs)
- [OpenRouter Authentication](https://openrouter.ai/docs/api-keys)
- [OpenRouter Models](https://openrouter.ai/models)
- [Google Docs API](https://developers.google.com/docs/api)

### Related Workflows
- [n8n: Summarize URLs with OpenAI](https://n8n.io/workflows/8210)
- [n8n: OpenRouter Integration](https://n8n.io/workflows/2897)

---

## Conclusion

This workflow demonstrates:

**Key Principles:**
- Simplicity over complexity (raw HTML > extraction nodes)
- Proper authentication patterns (Bearer Token field)
- Cognitive UX (manual trigger > webhook)
- Reliability through LLM capabilities (let model handle extraction)

**Practical Value:**
- Automated literary critique for published work
- Consistent, structured feedback
- Integration with existing writing tools
- Low-cost operation with free models

**Evolution:**
- Started complex (webhooks, extraction, multiple nodes)
- Simplified to essentials (fetch HTML, send to LLM, write doc)
- Each pivot removed friction and failure points
- Final design: robust, maintainable, practical

**Next Steps:**
- Test with real story URLs
- Tune LLM prompts for better critiques
- Add optional enhancements as needed
- Document what works for future workflows

The journey from initial concept to working automation revealed important patterns about balancing sophistication with reliability, and trusting capable LLMs to handle complexity rather than engineering elaborate preprocessing pipelines.
