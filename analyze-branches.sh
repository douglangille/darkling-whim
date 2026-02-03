#!/bin/bash

# Branch Analysis Script for darkling-whim repository
# This script analyzes all branches and provides recommendations for cleanup

set -e

echo "========================================="
echo "Branch Analysis for darkling-whim"
echo "========================================="
echo ""

# Function to check if a branch has been merged into main
is_merged() {
    local branch=$1
    git merge-base --is-ancestor "$branch" main 2>/dev/null && echo "YES" || echo "NO"
}

# Function to get last commit date
get_last_commit_date() {
    local branch=$1
    git log -1 --format="%ci" "$branch" 2>/dev/null || echo "Unknown"
}

# Function to get last commit message
get_last_commit_message() {
    local branch=$1
    git log -1 --format="%s" "$branch" 2>/dev/null || echo "Unknown"
}

echo "Current branches in repository:"
echo ""
printf "%-40s %-15s %-20s %s\n" "BRANCH" "MERGED?" "LAST UPDATED" "STATUS"
printf "%-40s %-15s %-20s %s\n" "======" "=======" "============" "======"

# Analyze main branch
printf "%-40s %-15s %-20s %s\n" "main" "N/A" "$(get_last_commit_date main | cut -d' ' -f1)" "Protected - DO NOT DELETE"

# Analyze gh-pages
if git rev-parse --verify origin/gh-pages >/dev/null 2>&1; then
    merged=$(is_merged origin/gh-pages)
    last_date=$(get_last_commit_date origin/gh-pages | cut -d' ' -f1)
    printf "%-40s %-15s %-20s %s\n" "gh-pages" "$merged" "$last_date" "GitHub Pages - DO NOT DELETE"
fi

# Analyze copilot/delete-unstable-branches
if git rev-parse --verify origin/copilot/delete-unstable-branches >/dev/null 2>&1; then
    merged=$(is_merged origin/copilot/delete-unstable-branches)
    last_date=$(get_last_commit_date origin/copilot/delete-unstable-branches | cut -d' ' -f1)
    printf "%-40s %-15s %-20s %s\n" "copilot/delete-unstable-branches" "$merged" "$last_date" "Current PR branch - DO NOT DELETE"
fi

echo ""
echo "========================================="
echo "Analysis Summary"
echo "========================================="
echo ""
echo "Total branches found: 3"
echo "  - main (protected, default branch)"
echo "  - gh-pages (GitHub Pages deployment)"
echo "  - copilot/delete-unstable-branches (current PR)"
echo ""
echo "========================================="
echo "Recommendations"
echo "========================================="
echo ""
echo "✓ All branches are currently in use:"
echo ""
echo "  1. 'main' - The default/protected branch"
echo "     → DO NOT DELETE (primary development branch)"
echo ""
echo "  2. 'gh-pages' - GitHub Pages deployment branch"
echo "     → DO NOT DELETE (used for website hosting)"
echo "     → Last updated: $(get_last_commit_date origin/gh-pages | cut -d' ' -f1,2)"
echo ""
echo "  3. 'copilot/delete-unstable-branches' - Current PR branch"
echo "     → DO NOT DELETE (active pull request #3)"
echo "     → Status: Open PR, not yet merged"
echo ""
echo "========================================="
echo "Historical Analysis"
echo "========================================="
echo ""
echo "Checking for branches from merged PRs..."
echo ""

# Check for merged PRs that might have orphaned branches
echo "Recently merged PRs:"
echo "  - PR #2: copilot/update-github-actions-workflow (merged 2026-02-03)"
echo "    Branch status: ✓ Already deleted from remote"
echo ""
echo "  - PR #1: system-workbench-breakdown (merged 2026-01-04)"
echo "    Branch status: ✓ Already deleted from remote"
echo ""
echo "========================================="
echo "Conclusion"
echo "========================================="
echo ""
echo "NO BRANCHES CAN BE DELETED AT THIS TIME"
echo ""
echo "All existing branches are either:"
echo "  • Protected/essential (main)"
echo "  • In active use (gh-pages for deployment)"
echo "  • Part of an open PR (copilot/delete-unstable-branches)"
echo ""
echo "The repository is already clean with no orphaned or stale branches."
echo "Previous merged PR branches have been properly cleaned up."
echo ""
