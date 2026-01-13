---
date: 2026-01-13
tags: [health, perplexity, healthkit, fitbit, workflow, mcp]
---

# Perplexity HealthKit Integration Discovery

## New Capability

Perplexity Mac app now has HealthKit access through Local Model Context Protocol (MCP).

- Privacy-first architecture keeps health data local during processing
- Enables conversational queries and AI-powered analysis of Apple Health data
- Available exclusively through macOS Mac App Store version
- Part of broader Local MCP functionality for files, databases, apps, and services

## Current Situation

- Previously deleted Apple Health in favor of all-in Fitbit ecosystem
- Have existing health folder in Workbench repo for manual tracking
- Need Fitbit app for device management (non-negotiable)

## Proposed Data Pipeline

Fitbit → Sync App → Apple Health → Perplexity MCP → Workbench Repo

### Components

1. **Fitbit**: Primary data collection hardware
2. **Sync Fitbit to Health** (by Yoshifumi Kanno): Middleware app for data transfer
   - One-tap manual sync
   - 10+ health categories supported
   - No subscription fees
   - Aligns with intentional tool usage philosophy
3. **Apple Health**: Consolidated data store
4. **Perplexity MCP**: AI-powered analysis layer
5. **GitHub Workbench**: Permanent markdown-based record

## Benefits

- Transforms Apple Health from passive data silo to actionable interface
- AI-generated insights augment existing manual tracking
- Maintains GitHub-centric workflow
- Reduces digital clutter (potentially eliminate separate Fitbit dashboard reliance)
- Enables automated weekly/monthly health reports in markdown format

## Next Steps

- Install "Sync Fitbit to Health" app
- Configure sync permissions
- Establish routine for data sync (e.g., morning coffee ritual)
- Test Perplexity HealthKit queries via Mac app
- Develop templates for health reports in Workbench format

## Related

- See: [[2026-01-13-fitbit-healthkit-sync-project.md]] for custom tool project idea
