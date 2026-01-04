# System-Workbench Reorganization Implementation Guide

## Overview
This guide provides the exact commands and steps to reorganize your system-workbench folder from the current scattered structure into a clean, functional architecture.

## Implementation Strategy

### Phase 1: Create New Directory Structure
### Phase 2: Move Files to New Locations
### Phase 3: Merge Duplicate/Similar Content
### Phase 4: Deploy New README
### Phase 5: Clean Up Empty Directories

---

## Phase 1: Create New Directory Structure

Create these directories within `_life/system-workbench/`:

```bash
mkdir -p ai-tools
mkdir -p tech-environment
mkdir -p display-optimization
mkdir -p productivity-systems
mkdir -p planning-workbenches
mkdir -p writing-workflows
mkdir -p chat-management
mkdir -p content-curation
mkdir -p health-optimization
mkdir -p system-meta
mkdir -p archive
```

---

## Phase 2: File Movement Plan

### AI Tools (18 files → `/ai-tools/`)

```bash
# Root level moves
git mv "02-model-comparison.md" "ai-tools/model-comparison.md"
git mv "10-ai-literacy.md" "ai-tools/ai-literacy.md"
git mv "2026 AI Stack Architecture.md" "ai-tools/2026-ai-stack-architecture.md"
git mv "ai_tool_stack_reference.md" "ai-tools/ai-tool-stack-reference.md"
git mv "ai_tool_stack_summary_2025-12-31.md" "ai-tools/ai-tool-stack-summary-2025-12.md"
git mv "chatgpt_custom_instructions.md" "ai-tools/chatgpt-custom-instructions.md"
git mv "gemini_custom_instructions.md" "ai-tools/gemini-custom-instructions.md"
git mv "perplexity-configuration.md" "ai-tools/perplexity-configuration.md"
git mv "notebooklm-integration.md" "ai-tools/notebooklm-integration.md"
git mv "\"Petting the AI\" and Parasocial Risk.md" "ai-tools/petting-ai-parasocial-risk.md"

# From 02_Technology_Tools subdirectory
git mv "02_Technology_Tools/AI_disclaimer_feedback.md" "ai-tools/ai-disclaimer-feedback.md"
git mv "02_Technology_Tools/AI_tool_comparison_2025.md" "ai-tools/ai-tool-comparison-2025.md"
git mv "02_Technology_Tools/ChatGPT-5_tricks_video.md" "ai-tools/chatgpt-5-tricks-video.md"
git mv "02_Technology_Tools/ChatGPT_archive_and_memory.md" "ai-tools/chatgpt-archive-memory.md"
git mv "02_Technology_Tools/ChatGPT_downgrade_pain_points.md" "ai-tools/chatgpt-downgrade-pain-points.md"
git mv "02_Technology_Tools/Chatbot_comparison_2025.md" "ai-tools/chatbot-comparison-2025.md"
git mv "02_Technology_Tools/Non-US_chatbot_comparison.md" "ai-tools/non-us-chatbot-comparison.md"
git mv "02_Technology_Tools/M365_Copilot_vs_ChatGPT.md" "ai-tools/m365-copilot-vs-chatgpt.md"
```

### Tech Environment (22 files → `/tech-environment/`)

```bash
# Root level moves
git mv "07-digital-environment.md" "tech-environment/digital-environment.md"
git mv "11-obsidian-vault.md" "tech-environment/obsidian-vault.md"
git mv "13-cross-platform.md" "tech-environment/cross-platform-strategy.md"
git mv "device-quick-reference.md" "tech-environment/device-quick-reference.md"
git mv "tech-ecosystem-overview.md" "tech-environment/tech-ecosystem-overview.md"
git mv "greyscale for idevices" "tech-environment/greyscale-idevices.md"

# From 02_Technology_Tools
git mv "02_Technology_Tools/App_setup_for_iPad.md" "tech-environment/ipad-app-setup.md"
git mv "02_Technology_Tools/Apple_Notes_workflow_issues.md" "tech-environment/apple-notes-workflow-issues.md"
git mv "02_Technology_Tools/Delete_apps_from_iPad.md" "tech-environment/delete-apps-ipad.md"
git mv "02_Technology_Tools/Ecosystem_audit_simulation.md" "tech-environment/ecosystem-audit-simulation.md"
git mv "02_Technology_Tools/iOS_26_settings_guide.md" "tech-environment/ios-26-settings-guide.md"
git mv "02_Technology_Tools/iPadOS_dark_mode_issues.md" "tech-environment/ipados-dark-mode-issues.md"
git mv "02_Technology_Tools/iPhone_ad_blocking_options.md" "tech-environment/iphone-ad-blocking.md"
git mv "02_Technology_Tools/iPhone_layout_analysis.md" "tech-environment/iphone-layout-analysis.md"
git mv "02_Technology_Tools/macOS_Microsoft_apps_vs_PWA.md" "tech-environment/macos-microsoft-apps-vs-pwa.md"
git mv "02_Technology_Tools/Office_Online_default_workaround.md" "tech-environment/office-online-workaround.md"
git mv "02_Technology_Tools/Obsidian_GitHub_Pages_integration.md" "tech-environment/obsidian-github-pages.md"
git mv "02_Technology_Tools/Obsidian_MVP_course.md" "tech-environment/obsidian-mvp-course.md"
git mv "02_Technology_Tools/Apple_vs_Google_Maps.md" "tech-environment/apple-vs-google-maps.md"
git mv "02_Technology_Tools/Best_music_ecosystem_comparison.md" "tech-environment/music-ecosystem-comparison.md"
git mv "02_Technology_Tools/Weather_app_comparison.md" "tech-environment/weather-app-comparison.md"
git mv "02_Technology_Tools/Focused_Inbox_vs_Rule.md" "tech-environment/focused-inbox-vs-rule.md"
```

### Display Optimization (7 files → `/display-optimization/`)

```bash
git mv "adhd_display_optimization_guide.md" "display-optimization/adhd-display-guide.md"
git mv "dark_light_mode_quick_reference.md" "display-optimization/dark-light-quick-reference.md"
git mv "dark_light_mode_research_summary.md" "display-optimization/dark-light-research.md"
git mv "scientific_evidence_dark_light_mode.md" "display-optimization/scientific-evidence.md"
git mv "setup_checklist_dark_light_mode.md" "display-optimization/setup-checklist.md"
git mv "02_Technology_Tools/Brightness_and_battery_life.md" "display-optimization/brightness-battery.md"
git mv "02_Technology_Tools/Tap_to_wake_decision.md" "display-optimization/tap-to-wake-decision.md"
```

### Productivity Systems (4 files → `/productivity-systems/`)

```bash
git mv "08-productivity-frameworks.md" "productivity-systems/productivity-frameworks.md"
git mv "12-reminders-system.md" "productivity-systems/reminders-system.md"
git mv "03_Productivity_Planning/Task_management_cadence.md" "productivity-systems/task-management-cadence.md"
git mv "03_Productivity_Planning/Week_13_Q1_rule.md" "productivity-systems/week-13-q1-rule.md"
```

### Planning Workbenches (3 files → `/planning-workbenches/`)

```bash
git mv "03_Productivity_Planning/Counselling_Workbench.md" "planning-workbenches/counselling-workbench.md"
git mv "03_Productivity_Planning/Innovation_Bench.md" "planning-workbenches/innovation-bench.md"
git mv "03_Productivity_Planning/Planning_Workbench.md" "planning-workbenches/planning-workbench.md"
```

### Writing Workflows (4 files → `/writing-workflows/`)

```bash
git mv "03-creative-writing.md" "writing-workflows/creative-writing-system.md"
git mv "VSCode Writing Environment Setup.md" "writing-workflows/vscode-writing-setup.md"
git mv "Writing Workflow Decision - iPad Mobile Setup.md" "writing-workflows/ipad-mobile-writing.md"
git mv "02_Technology_Tools/Obsidian_AI_longform_writing.md" "writing-workflows/obsidian-longform-writing.md"
```

### Chat Management (5 files → `/chat-management/`)

```bash
git mv "01-chatmerge-system.md" "chat-management/chatmerge-system.md"
git mv "04-interaction-rules.md" "chat-management/interaction-rules.md"
git mv "Chat Hygiene and Triage Ritual.md" "chat-management/chat-hygiene-ritual.md"
git mv "conversation_sprawl_management.md" "chat-management/conversation-sprawl-management.md"
git mv "Perplexity → GitHub Keeper Workflow.md" "chat-management/perplexity-github-workflow.md"
```

### Content Curation (1 file → `/content-curation/`)

```bash
git mv "06-rss-strategy.md" "content-curation/rss-strategy.md"
```

### Health Optimization (2 files → `/health-optimization/`)

```bash
git mv "05-health-data.md" "health-optimization/health-data.md"
git mv "09-diet-health.md" "health-optimization/diet-health.md"
```

### System Meta (6 files → `/system-meta/`)

```bash
git mv "14-experiments-tips.md" "system-meta/experiments-tips.md"
git mv "12_System_Meta/Article_analysis_options.md" "system-meta/article-analysis-options.md"
git mv "12_System_Meta/Backup_iCloud_Photos.md" "system-meta/backup-icloud-photos.md"
git mv "12_System_Meta/Google_privacy_impact.md" "system-meta/google-privacy-impact.md"
git mv "12_System_Meta/Memory_pruning_plan.md" "system-meta/memory-pruning-plan.md"
git mv "12_System_Meta/System_assumption_confirmation.md" "system-meta/system-assumptions.md"
```

### Archive (6 files → `/archive/`)

```bash
git mv "ChatGPT-Weekly Planning with Reminders.md" "archive/chatgpt-weekly-planning.md"
git mv "Writing workflow options.md" "archive/writing-workflow-options.md"
git mv "notes dump.md" "archive/notes-dump.md"
git mv "12_System_Meta/File_review_complete.md" "archive/file-review-complete.md"
git mv "12_System_Meta/Narration_types_summary.md" "archive/narration-types-summary.md"
git mv "12_System_Meta/Wait_for_instructions.md" "archive/wait-for-instructions.md"
```

---

## Phase 3: Merge Duplicate Content (Optional - Can be done later)

### Recommended Merges

**Dark/Light Mode Files** → Single comprehensive guide
- Merge: `dark_light_mode_quick_reference.md`, `dark_light_mode_research_summary.md`, `scientific_evidence_dark_light_mode.md`, `setup_checklist_dark_light_mode.md`
- Into: `display-optimization/dark-light-mode-guide.md`
- Keep separate: `adhd-display-guide.md` (specialized)

**AI Tool Comparisons** → Single comparison matrix
- Merge: `AI_tool_comparison_2025.md`, `Chatbot_comparison_2025.md`, `Non-US_chatbot_comparison.md`
- Into: `ai-tools/comprehensive-comparison-2025.md`

---

## Phase 4: Deploy New README

The new README.md will replace the current one and serve as the master navigation hub.

---

## Phase 5: Clean Up

Remove empty directories:
```bash
git rm -r "02_Technology_Tools/"
git rm -r "03_Productivity_Planning/"
git rm -r "12_System_Meta/"
```

---

## Commit Strategy

Recommended approach:

```bash
# Single comprehensive commit
git add -A
git commit -m "Reorganize system-workbench: consolidate into functional categories

- Flatten nested subdirectories into 11 functional categories
- Standardize file naming to kebab-case
- Move 78 files to new organized structure
- Archive 6 large historical reference documents
- Add comprehensive master README with navigation
- Preserve all git history through git mv operations"
```

---

## File Count Summary

- **Total files moved**: 78
- **New directories**: 11
- **Files archived**: 6 (large reference documents)
- **Files to potentially merge**: ~10 (optional, can be done later)

---

## Post-Implementation Checklist

- [ ] All files moved to new locations
- [ ] Old subdirectories removed
- [ ] New README deployed
- [ ] Test navigation and links
- [ ] Update any external references to old file paths
- [ ] Update Perplexity configuration if it references specific files
- [ ] Verify git history preserved for all moved files

---

## Rollback Plan

If needed, you can rollback using:
```bash
git reset --hard HEAD~1  # Undo last commit (before pushing)
```

Or use GitHub's web interface to revert the commit after pushing.

---

## Notes

- All `git mv` commands preserve file history
- Files are renamed to use kebab-case for consistency
- Large conversation logs moved to archive but kept for reference
- Subdirectory READMEs removed (provided minimal value)
- New structure aligns with mental models and usage patterns
- This is a "workbench, not warehouse" reorganization
