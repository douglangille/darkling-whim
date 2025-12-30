Here are your two saveable notes as downloadable markdown files:

```markdown
# AI Tool Stack (Late 2025)

**Last Updated:** December 30, 2025

## Current Configuration

### Primary Tools
- **Perplexity Pro** - Search, research, analysis, and synthesis with citations
  - Use for: Multi-source research, fact-checking, deep dives, comparative analysis
  - Strength: Real-time web access with transparent sourcing
  
- **Gemini (Free)** - Hands-free, live camera + voice assistant
  - Use for: Equipment troubleshooting, hobby farm issues, real-time visual problem-solving
  - Strength: Free live camera mode, conversational quality, natural voices
  
- **ChatGPT** - Deprioritized
  - Status: No longer worth paid subscription
  - Reason: Feature differentiation has eroded; competitors offer better value
  - Kept as fallback only

### Tool Selection Principle
Use specialized tools for specific jobs rather than forcing one LLM to handle everything. Match the tool to the task type.

## Search Workflow (Free-Only Strategy)

**I will not pay for a search engine.**

- **Google Search** - Quick, utilitarian lookups
  - Fast results for straightforward queries
  - Accept mediocre quality as trade-off for speed
  
- **Perplexity Pro** - Research-heavy, synthesis, or citation-needed queries
  - Use when multiple sources need comparison
  - Use when answer quality matters more than speed
  
- **DuckDuckGo** - Rare, highly sensitive queries only
  - Minimal use; quality is poor
  - Keep as privacy escape hatch for specific cases

## Decision Points

### When to Use Which Tool
- **Perplexity**: "Why is X happening?", "Compare A vs B", "What are the latest developments in Y?"
- **Gemini**: "What's wrong with this equipment?" (camera pointed at it), hands-free troubleshooting
- **Google Search**: "What time does X close?", "Weather forecast", quick factual lookups
- **DuckDuckGo**: Searches I don't want in Google's profile

### Why This Matters
OpenAI's consumer value proposition has weakened. Google can cross-subsidize Gemini indefinitely. Perplexity has a focused, sustainable business model. Using the right tool for each job maximizes utility while minimizing costs.

## Review Cycle
Re-evaluate this stack quarterly or when major platform changes occur.
```

```markdown
# Privacy Harm Reduction Strategy

**Last Updated:** December 30, 2025

## Core Philosophy

**Goal:** Minimize high-value data streams into major platforms, not achieve absolute privacy.

Accept some data leakage where utility is genuinely high, but protect the most invasive collection points: email content, document storage, browsing history, location patterns, and core productivity data.

## Current Stance

### What I Keep Outside Big Tech
- **No Gmail** - Google account uses `me@douglangille.ca` (portable identity)
- **No Chrome** - Safari for personal, Edge for work
- **No Google Drive** - iCloud for storage
- **No Google Maps** - Apple Maps exclusively
- **No Gmail inbox mining** - Email stays on personal infrastructure

### Where I Accept Google's Presence
- **YouTube** (with search/watch history disabled)
- **Gemini** (for live camera troubleshooting utility)
- **Google Home** (legacy device; minimize where possible)
- **Google Search** (utilitarian queries only)

### Browser & Platform Strategy
- **Personal browsing:** Safari
- **Work browsing:** Edge
- **Maps:** Apple Maps
- **Cloud storage:** iCloud
- **Email:** Own domain, not Gmail

## Privacy Audit Checklist

### High-Priority Platforms to Review

#### Microsoft
- [ ] **M365 (Work)**: Activity history, diagnostics, what syncs to personal account
- [ ] **Personal Microsoft Account**: Disable activity history, browsing/search history, ad personalization, location history, set diagnostics to "Required only"

#### LinkedIn
- [ ] Hide connections list (set to "Only You")
- [ ] Disable search engine indexing of profile
- [ ] Set email/phone visibility to "Connections only" or "Nobody"
- [ ] Disable interest-based advertising and data sharing
- [ ] Enable security alerts for unauthorized changes
- [ ] Use private browsing when researching people

#### GitHub
- [ ] Review public repository visibility
- [ ] Use GitHub noreply email for commits
- [ ] Audit what shows on public profile
- [ ] Verify 2FA enabled

#### Dropbox
- [ ] Audit publicly shared links
- [ ] Revoke unused third-party app integrations
- [ ] Enable 2FA if not already active
- [ ] Review and disable old file request links

#### Apple
- [ ] Review what's syncing to iCloud
- [ ] Audit Location Services permissions app-by-app
- [ ] Verify "Ask App Not to Track" is enabled
- [ ] Confirm Safari privacy features active (hide IP, prevent cross-site tracking)

#### Facebook
- [ ] Clear and disconnect "Off-Facebook Activity"
- [ ] Disable all ad personalization in Accounts Center
- [ ] Set friends list to "Only Me"
- [ ] Disable search engine indexing
- [ ] Turn off Location History (delete first)
- [ ] Remove all third-party app integrations
- [ ] Disable Active Status in Messenger
- [ ] Minimal profile (remove workplace, education, hometown, relationship, interests)
- [ ] Use messenger.com in browser instead of app when possible

#### Substack
- [ ] Review author profile visibility
- [ ] Check what subscriber analytics I'm collecting
- [ ] Export subscriber list regularly (backup/portability)
- [ ] Consider whether subscription reading list should be public
- [ ] Turn off platform recommendation emails

#### Google (Ongoing Maintenance)
- [ ] Verify YouTube search/watch history remains off
- [ ] Disable Web & App Activity
- [ ] Disable Location History
- [ ] Turn off Ad Personalization
- [ ] Set auto-delete to shortest timeframe (3 months) for anything kept on

### Other Services to Consider
- Amazon (if used): browsing history, Alexa recordings, ad settings
- Spotify/streaming: listening history, ad personalization
- ISP/DNS: Consider encrypted DNS via iCloud Private Relay or Cloudflare
- Smart home devices: Minimize data collection settings

## Facebook & Messenger Strategy

### Why I Keep It
Messenger access to certain family and friends who won't migrate to other platforms. "Lazy human connection infrastructure."

### Harm Reduction Approach
1. **Aggressive privacy lockdown** (see checklist above)
2. **Behavior modeling over time:**
   - For people I talk to regularly: initiate and continue conversations via **iMessage/SMS**
   - Reply to Messenger messages with "just texted you"
   - Let Messenger become passive/legacy channel without forcing anyone to switch
   - Keep Facebook contacts available but underused

### Expected Outcome
High-value relationships naturally migrate to iMessage/SMS. Facebook loses behavioral data about communication frequency and relationship strength. Messenger remains as compatibility layer only.

## Content & Platform Ownership

### Home Base
- **Jekyll blog + douglangille.ca** = Canonical identity and creative writing home
- **GitHub repo** = Backup of all Substack posts (exit strategy)

### Professional Presence
- **Substack** = Professional content archive + light brand management
- **LinkedIn** = Primary engagement/distribution for professional writing

### Comment Strategy
- **Writing blog:** Intentionally no comments
- **If professional content migrates to Jekyll:**
  - Option 1: GitHub-backed comments (utterances/giscus)
  - Option 2: Use LinkedIn as discussion surface
  - **Never:** Disqus (privacy nightmare)

### Subscriber Strategy
- No pressure to grow Substack subscribers currently
- Engagement happens primarily via LinkedIn
- Revisit "Why subscribe?" only when there's clear, sustainable value proposition

## Review Cycle

Conduct full privacy audit **annually** or when:
- Major platform policy changes occur
- New service added to regular workflow
- Preparing to migrate away from a platform
- Privacy regulations change

---

**Next Review Due:** December 2026
```