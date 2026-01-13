---
date: 2026-01-13
tags: [project, vibe-coding, python, fitbit, healthkit, automation, api]
status: idea
---

# Custom Fitbit to HealthKit Sync Tool

## Project Concept

Build a custom Python-based sync tool to replace third-party middleware and provide complete control over the Fitbit → Apple Health → Perplexity → Workbench data pipeline.

## Motivation

- Eliminate third-party app dependencies
- Customizable data transformation and formatting
- Direct GitHub integration for automated commits
- Learning opportunity with HealthKit APIs and OAuth flows
- Future-proof solution under personal control

## Technical Architecture

### Components

1. **Fitbit API Integration**
   - OAuth 2.0 authentication
   - Pull health metrics (steps, heart rate, sleep, calories, etc.)
   - Historical data import capability

2. **HealthKit Integration**
   - Apple HealthKit framework access
   - Write data to Apple Health database
   - Options: PyObjC bindings or native Swift

3. **Perplexity Integration**
   - Format data for Perplexity analysis
   - Potentially trigger analysis via API
   - Generate markdown reports

4. **GitHub Automation**
   - Auto-commit health reports to Workbench repo
   - Structured markdown output for _life/health folder

5. **Scheduling**
   - cron job or launchd for automated daily syncs
   - Manual trigger option for on-demand syncs

## Development Approach

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

## Tech Stack

- **Language**: Python
- **APIs**: Fitbit Web API, Apple HealthKit
- **Libraries**: requests, PyObjC (or Swift for HealthKit)
- **Scheduling**: launchd (macOS)
- **Version Control**: Git/GitHub

## Benefits

- Complete data pipeline control
- Eliminates subscription costs
- Customized to exact workflow needs
- Open source potential (help others in same situation)
- Portfolio/demonstration piece
- Aligns with "workbench, not warehouse" philosophy

## Status

**Pinned as project idea** - 2026-01-13

## Related

- See: [[2026-01-13-perplexity-healthkit-integration.md]] for context
