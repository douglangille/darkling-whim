#!/bin/bash
# System-Workbench Reorganization Script
# Run this from the _life/system-workbench/ directory

set -e  # Exit on error

echo "=== System-Workbench Reorganization ==="
echo "This script will reorganize 78 files into 11 functional categories."
echo ""
read -p "Press Enter to continue or Ctrl+C to cancel..."

# Phase 1: Create new directory structure
echo "\n[Phase 1] Creating directory structure..."
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
echo "✓ Directories created"

# Phase 2: Move files
echo "\n[Phase 2] Moving files to new locations..."

# AI Tools (18 files)
echo "Moving AI tools files..."
git mv "02-model-comparison.md" "ai-tools/model-comparison.md" 2>/dev/null || true
git mv "10-ai-literacy.md" "ai-tools/ai-literacy.md" 2>/dev/null || true
git mv "2026 AI Stack Architecture.md" "ai-tools/2026-ai-stack-architecture.md" 2>/dev/null || true
git mv "ai_tool_stack_reference.md" "ai-tools/ai-tool-stack-reference.md" 2>/dev/null || true
git mv "ai_tool_stack_summary_2025-12-31.md" "ai-tools/ai-tool-stack-summary-2025-12.md" 2>/dev/null || true
git mv "chatgpt_custom_instructions.md" "ai-tools/chatgpt-custom-instructions.md" 2>/dev/null || true
git mv "gemini_custom_instructions.md" "ai-tools/gemini-custom-instructions.md" 2>/dev/null || true
git mv "perplexity-configuration.md" "ai-tools/perplexity-configuration.md" 2>/dev/null || true
git mv "notebooklm-integration.md" "ai-tools/notebooklm-integration.md" 2>/dev/null || true
git mv '"Petting the AI" and Parasocial Risk.md' "ai-tools/petting-ai-parasocial-risk.md" 2>/dev/null || true
git mv "02_Technology_Tools/AI_disclaimer_feedback.md" "ai-tools/ai-disclaimer-feedback.md" 2>/dev/null || true
git mv "02_Technology_Tools/AI_tool_comparison_2025.md" "ai-tools/ai-tool-comparison-2025.md" 2>/dev/null || true
git mv "02_Technology_Tools/ChatGPT-5_tricks_video.md" "ai-tools/chatgpt-5-tricks-video.md" 2>/dev/null || true
git mv "02_Technology_Tools/ChatGPT_archive_and_memory.md" "ai-tools/chatgpt-archive-memory.md" 2>/dev/null || true
git mv "02_Technology_Tools/ChatGPT_downgrade_pain_points.md" "ai-tools/chatgpt-downgrade-pain-points.md" 2>/dev/null || true
git mv "02_Technology_Tools/Chatbot_comparison_2025.md" "ai-tools/chatbot-comparison-2025.md" 2>/dev/null || true
git mv "02_Technology_Tools/Non-US_chatbot_comparison.md" "ai-tools/non-us-chatbot-comparison.md" 2>/dev/null || true
git mv "02_Technology_Tools/M365_Copilot_vs_ChatGPT.md" "ai-tools/m365-copilot-vs-chatgpt.md" 2>/dev/null || true

# Tech Environment (22 files)
echo "Moving tech environment files..."
git mv "07-digital-environment.md" "tech-environment/digital-environment.md" 2>/dev/null || true
git mv "11-obsidian-vault.md" "tech-environment/obsidian-vault.md" 2>/dev/null || true
git mv "13-cross-platform.md" "tech-environment/cross-platform-strategy.md" 2>/dev/null || true
git mv "device-quick-reference.md" "tech-environment/device-quick-reference.md" 2>/dev/null || true
git mv "tech-ecosystem-overview.md" "tech-environment/tech-ecosystem-overview.md" 2>/dev/null || true
git mv "greyscale for idevices" "tech-environment/greyscale-idevices.md" 2>/dev/null || true
git mv "02_Technology_Tools/App_setup_for_iPad.md" "tech-environment/ipad-app-setup.md" 2>/dev/null || true
git mv "02_Technology_Tools/Apple_Notes_workflow_issues.md" "tech-environment/apple-notes-workflow-issues.md" 2>/dev/null || true
git mv "02_Technology_Tools/Delete_apps_from_iPad.md" "tech-environment/delete-apps-ipad.md" 2>/dev/null || true
git mv "02_Technology_Tools/Ecosystem_audit_simulation.md" "tech-environment/ecosystem-audit-simulation.md" 2>/dev/null || true
git mv "02_Technology_Tools/iOS_26_settings_guide.md" "tech-environment/ios-26-settings-guide.md" 2>/dev/null || true
git mv "02_Technology_Tools/iPadOS_dark_mode_issues.md" "tech-environment/ipados-dark-mode-issues.md" 2>/dev/null || true
git mv "02_Technology_Tools/iPhone_ad_blocking_options.md" "tech-environment/iphone-ad-blocking.md" 2>/dev/null || true
git mv "02_Technology_Tools/iPhone_layout_analysis.md" "tech-environment/iphone-layout-analysis.md" 2>/dev/null || true
git mv "02_Technology_Tools/macOS_Microsoft_apps_vs_PWA.md" "tech-environment/macos-microsoft-apps-vs-pwa.md" 2>/dev/null || true
git mv "02_Technology_Tools/Office_Online_default_workaround.md" "tech-environment/office-online-workaround.md" 2>/dev/null || true
git mv "02_Technology_Tools/Obsidian_GitHub_Pages_integration.md" "tech-environment/obsidian-github-pages.md" 2>/dev/null || true
git mv "02_Technology_Tools/Obsidian_MVP_course.md" "tech-environment/obsidian-mvp-course.md" 2>/dev/null || true
git mv "02_Technology_Tools/Apple_vs_Google_Maps.md" "tech-environment/apple-vs-google-maps.md" 2>/dev/null || true
git mv "02_Technology_Tools/Best_music_ecosystem_comparison.md" "tech-environment/music-ecosystem-comparison.md" 2>/dev/null || true
git mv "02_Technology_Tools/Weather_app_comparison.md" "tech-environment/weather-app-comparison.md" 2>/dev/null || true
git mv "02_Technology_Tools/Focused_Inbox_vs_Rule.md" "tech-environment/focused-inbox-vs-rule.md" 2>/dev/null || true

# Display Optimization (7 files)
echo "Moving display optimization files..."
git mv "adhd_display_optimization_guide.md" "display-optimization/adhd-display-guide.md" 2>/dev/null || true
git mv "dark_light_mode_quick_reference.md" "display-optimization/dark-light-quick-reference.md" 2>/dev/null || true
git mv "dark_light_mode_research_summary.md" "display-optimization/dark-light-research.md" 2>/dev/null || true
git mv "scientific_evidence_dark_light_mode.md" "display-optimization/scientific-evidence.md" 2>/dev/null || true
git mv "setup_checklist_dark_light_mode.md" "display-optimization/setup-checklist.md" 2>/dev/null || true
git mv "02_Technology_Tools/Brightness_and_battery_life.md" "display-optimization/brightness-battery.md" 2>/dev/null || true
git mv "02_Technology_Tools/Tap_to_wake_decision.md" "display-optimization/tap-to-wake-decision.md" 2>/dev/null || true

# Productivity Systems (4 files)
echo "Moving productivity systems files..."
git mv "08-productivity-frameworks.md" "productivity-systems/productivity-frameworks.md" 2>/dev/null || true
git mv "12-reminders-system.md" "productivity-systems/reminders-system.md" 2>/dev/null || true
git mv "03_Productivity_Planning/Task_management_cadence.md" "productivity-systems/task-management-cadence.md" 2>/dev/null || true
git mv "03_Productivity_Planning/Week_13_Q1_rule.md" "productivity-systems/week-13-q1-rule.md" 2>/dev/null || true

# Planning Workbenches (3 files)
echo "Moving planning workbenches files..."
git mv "03_Productivity_Planning/Counselling_Workbench.md" "planning-workbenches/counselling-workbench.md" 2>/dev/null || true
git mv "03_Productivity_Planning/Innovation_Bench.md" "planning-workbenches/innovation-bench.md" 2>/dev/null || true
git mv "03_Productivity_Planning/Planning_Workbench.md" "planning-workbenches/planning-workbench.md" 2>/dev/null || true

# Writing Workflows (4 files)
echo "Moving writing workflows files..."
git mv "03-creative-writing.md" "writing-workflows/creative-writing-system.md" 2>/dev/null || true
git mv "VSCode Writing Environment Setup.md" "writing-workflows/vscode-writing-setup.md" 2>/dev/null || true
git mv "Writing Workflow Decision - iPad Mobile Setup.md" "writing-workflows/ipad-mobile-writing.md" 2>/dev/null || true
git mv "02_Technology_Tools/Obsidian_AI_longform_writing.md" "writing-workflows/obsidian-longform-writing.md" 2>/dev/null || true

# Chat Management (5 files)
echo "Moving chat management files..."
git mv "01-chatmerge-system.md" "chat-management/chatmerge-system.md" 2>/dev/null || true
git mv "04-interaction-rules.md" "chat-management/interaction-rules.md" 2>/dev/null || true
git mv "Chat Hygiene and Triage Ritual.md" "chat-management/chat-hygiene-ritual.md" 2>/dev/null || true
git mv "conversation_sprawl_management.md" "chat-management/conversation-sprawl-management.md" 2>/dev/null || true
git mv "Perplexity → GitHub Keeper Workflow.md" "chat-management/perplexity-github-workflow.md" 2>/dev/null || true

# Content Curation (1 file)
echo "Moving content curation files..."
git mv "06-rss-strategy.md" "content-curation/rss-strategy.md" 2>/dev/null || true

# Health Optimization (2 files)
echo "Moving health optimization files..."
git mv "05-health-data.md" "health-optimization/health-data.md" 2>/dev/null || true
git mv "09-diet-health.md" "health-optimization/diet-health.md" 2>/dev/null || true

# System Meta (6 files)
echo "Moving system meta files..."
git mv "14-experiments-tips.md" "system-meta/experiments-tips.md" 2>/dev/null || true
git mv "12_System_Meta/Article_analysis_options.md" "system-meta/article-analysis-options.md" 2>/dev/null || true
git mv "12_System_Meta/Backup_iCloud_Photos.md" "system-meta/backup-icloud-photos.md" 2>/dev/null || true
git mv "12_System_Meta/Google_privacy_impact.md" "system-meta/google-privacy-impact.md" 2>/dev/null || true
git mv "12_System_Meta/Memory_pruning_plan.md" "system-meta/memory-pruning-plan.md" 2>/dev/null || true
git mv "12_System_Meta/System_assumption_confirmation.md" "system-meta/system-assumptions.md" 2>/dev/null || true

# Archive (6 files)
echo "Moving archive files..."
git mv "ChatGPT-Weekly Planning with Reminders.md" "archive/chatgpt-weekly-planning.md" 2>/dev/null || true
git mv "Writing workflow options.md" "archive/writing-workflow-options.md" 2>/dev/null || true
git mv "notes dump.md" "archive/notes-dump.md" 2>/dev/null || true
git mv "12_System_Meta/File_review_complete.md" "archive/file-review-complete.md" 2>/dev/null || true
git mv "12_System_Meta/Narration_types_summary.md" "archive/narration-types-summary.md" 2>/dev/null || true
git mv "12_System_Meta/Wait_for_instructions.md" "archive/wait-for-instructions.md" 2>/dev/null || true

echo "✓ Files moved"

# Phase 3: Clean up empty directories
echo "\n[Phase 3] Cleaning up old structure..."
git rm -r "02_Technology_Tools/" 2>/dev/null || true
git rm -r "03_Productivity_Planning/" 2>/dev/null || true
git rm -r "12_System_Meta/" 2>/dev/null || true
echo "✓ Old directories removed"

# Phase 4: Archive old README
echo "\n[Phase 4] Archiving old README..."
git mv "README.md" "archive/old-readme.md" 2>/dev/null || true
echo "✓ Old README archived"

echo "\n=== Reorganization Complete ==="
echo "\nNext steps:"
echo "1. Review the changes with: git status"
echo "2. Check a few moved files to ensure they're correct"
echo "3. Commit with: git commit -m 'Reorganize system-workbench into functional categories'"
echo "4. Push with: git push origin main"
echo "5. Upload the new README.md to complete the reorganization"
echo "\nTo undo (before committing): git reset --hard HEAD"
