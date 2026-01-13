---
date: 2026-01-13
tags: [project, vibe-coding, python, fitbit, healthkit, automation, api]
status: low-priority-idea
---

# Custom Fitbit to HealthKit Sync Tool

## Project Status: LOW PRIORITY

**Reason:** Perplexity HealthKit integration is non-functional. Project blocked until AI analysis layer works properly.

## Project Concept

Build a custom Python-based sync tool to replace third-party middleware and provide complete control over the Fitbit → Apple Health → AI Analysis → Workbench data pipeline.

## Current Blocker (January 2026)

**Perplexity HealthKit integration doesn't work:**
- Platform detection bug (appears on wrong platforms)
- No authorization flow exists
- No official documentation
- Feature appears incomplete/experimental

**Impact on project:**
- Main value proposition was Perplexity integration
- Building custom tool now would just replicate existing "Sync Fitbit to Health" app
- Without AI analysis layer, limited benefit over current $0 solution

**Revisit when:**
- Perplexity HealthKit properly launches (check quarterly)
- OR alternative AI analysis tools mature (Gemini, Claude, ChatGPT)
- OR clear need emerges for custom automation beyond current stack

## Motivation (When Unblocked)

- Eliminate third-party app dependencies
- Customizable data transformation and formatting
- Direct GitHub integration for automated commits
- Learning opportunity with HealthKit APIs and OAuth flows
- Future-proof solution under personal control
- Enable AI-powered health insights automation

## Technical Architecture (Proposed)

### Components

1. **Fitbit API Integration**
   - OAuth 2.0 authentication
   - Pull health metrics (steps, heart rate, sleep, calories, etc.)
   - Historical data import capability

2. **HealthKit Integration**
   - Apple HealthKit framework access
   - Write data to Apple Health database
   - Options: PyObjC bindings or native Swift

3. **AI Analysis Integration**
   - Format data for AI analysis (Perplexity, Gemini, etc.)
   - Trigger analysis via API when available
   - Generate markdown reports

4. **GitHub Automation**
   - Auto-commit health reports to Workbench repo
   - Structured markdown output for _life/health folder
   - Maintain health timeline and metrics

5. **Scheduling**
   - cron job or launchd for automated daily syncs
   - Manual trigger option for on-demand syncs

## Development Approach (Future)

- **Vibe coding** with Gemini CLI + VS Code integration
- AI-assisted development for OAuth flows and API interactions
- Iterative feature development
- Focus on markdown output formatting for Workbench compatibility

## Potential Features

- Configurable sync intervals
- Selective metric syncing
- Data validation and error handling
- Backup/export functionality
- Health trend analysis and anomaly detection
- Customizable report templates
- Integration with multiple AI analysis platforms

## Tech Stack

- **Language**: Python
- **APIs**: Fitbit Web API, Apple HealthKit, Perplexity API (when available)
- **Libraries**: requests, PyObjC (or Swift for HealthKit)
- **Scheduling**: launchd (macOS)
- **Version Control**: Git/GitHub

## Benefits (When Functional)

- Complete data pipeline control
- Eliminates subscription costs
- Customized to exact workflow needs
- Open source potential (help others in same situation)
- Portfolio/demonstration piece
- Aligns with "workbench, not warehouse" philosophy
- Automated AI-powered health insights

## Current Reality Check

**What works now:**
- Fitbit Inspire 3 collects data
- "Sync Fitbit to Health" app syncs to Apple Health ($0, one-tap)
- Apple Health stores data passively
- Manual markdown health notes in Workbench

**What doesn't work:**
- Perplexity HealthKit integration (non-functional)
- Automated AI analysis and report generation
- Direct GitHub automation pipeline

**Decision:** Current stack is adequate until AI analysis layer properly launches. Don't build custom tool prematurely.

## Status

**Low priority idea** - 2026-01-13  
**Next review:** April 2026 (quarterly check-in with Perplexity HealthKit status)

## Related

- See: `_life/health/2026-01-13-perplexity-healthkit-integration.md` for current status
- See: `_life/health/health-tech-stack.md` for working health workflow
- See: `_tech/ai-tools/perplexity-configuration.md` for technical details about HealthKit bug