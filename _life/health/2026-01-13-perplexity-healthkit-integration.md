---
date: 2026-01-13
tags: [health, perplexity, healthkit, fitbit, workflow, mcp]
status: on-hold
---

# Perplexity HealthKit Integration Discovery

## Current Status: NON-FUNCTIONAL

**Discovered:** January 13, 2026  
**Status:** Awaiting official release - feature incomplete/broken

### What We Discovered

HealthKit integration exists in Perplexity's toolkit but is **not properly implemented**:

**Platform Availability Bug:**
- HealthKit appears as source option in **macOS Safari** (where it can't work - no HealthKit on macOS)
- HealthKit does NOT appear in **iOS/iPadOS Safari** (where it should work - HealthKit exists on these platforms)
- This is completely backwards from expected behavior

**No Authorization Flow:**
- No way to configure or authorize HealthKit access on any platform
- No connector in Settings → Connectors page
- Selecting HealthKit as source produces errors
- Tool exists in MCP but can't be initialized

**No Official Documentation:**
- No entries in Perplexity support center
- Feature appears to be incomplete/experimental
- Possibly intended for native macOS app (as some docs suggested) but implemented incorrectly in browser

## Original Plan (ON HOLD)

### Proposed Data Pipeline (When Working)
```
Fitbit → Sync App → Apple Health → Perplexity HealthKit → Workbench Repo
```

### Components

1. **Fitbit Inspire 3**: Primary data collection hardware
2. **Sync Fitbit to Health** (by Yoshifumi Kanno): Middleware app for data transfer
   - One-tap manual sync
   - 10+ health categories supported
   - No subscription fees
   - Aligns with intentional tool usage philosophy
3. **Apple Health**: Consolidated data store (already reinstalled)
4. **Perplexity HealthKit**: AI-powered analysis layer ⚠️ NOT WORKING YET
5. **GitHub Workbench**: Permanent markdown-based record

## Potential Benefits (When Released)

- Transform Apple Health from passive data silo to actionable AI interface
- AI-generated insights without manual dashboard checking
- Maintains GitHub-centric workflow
- Enables automated weekly/monthly health reports in markdown format
- Natural language queries about health trends and correlations

## What We're Doing Instead

### Current Implementation
1. ✅ Apple Health reinstalled (serves as data consolidation layer)
2. ✅ "Sync Fitbit to Health" app installed and configured
3. ✅ Daily manual sync established (morning coffee ritual)
4. ⏸️ **Perplexity HealthKit integration on hold** until properly released
5. ✅ Continue manual health tracking in Workbench markdown files

### When to Revisit

**Check quarterly** (next: April 2026):
- Has HealthKit appeared as connector in Perplexity Settings?
- Has official documentation been published?
- Does it work on iOS/iPadOS where it should?
- Has authorization flow been implemented?

**How to test:**
1. Open Perplexity on iPhone/iPad Safari
2. Check if HealthKit appears as source option
3. Try to authorize access through iOS Health app
4. Attempt simple query: "What's my average step count this week?"

## Documentation Updates

**Tech Stack Documentation:**
- See `_tech/ai-tools/perplexity-configuration.md` for technical details about the bug
- See `health-tech-stack.md` (this folder) for updated workflow without HealthKit integration

**Related Project Ideas:**
- Custom Fitbit → HealthKit sync tool with direct Perplexity integration
- See `_tech/projects/2026-01-13-fitbit-healthkit-sync-project.md` if still exists

## Key Insight

**Don't build around non-existent features.**

The entire workflow redesign was based on Perplexity HealthKit integration being functional. Since it's not:

- Apple Health remains data consolidation layer only
- Don't check Apple Health as dashboard (still avoid the app)
- Fitbit remains primary interface for daily monitoring
- Manual markdown health notes continue in Workbench
- Revisit when feature properly launches

**This aligns with ADHD-friendly simplicity:**
- Don't add tools before they're proven to work
- Don't build infrastructure around vapor features
- Maintain working stack until better option actually exists

---

**Next Review:** April 2026 (quarterly check-in)