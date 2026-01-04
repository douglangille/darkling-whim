# Obsidian Vault Management

## Philosophy

**Workbench, not warehouse**
- Practical toolbench
- Not a digital hoarding platform
- Not an everything-bucket

## Use Case

AI Writing Studio as sandbox to test Obsidian's value for story development and novel completion.

## Vault Structure

### 98 Scripts
- Templater automations
- Scripting only

### 99 Templates
- Prompt library
- Boilerplate content
- Insert-only style

### Core Philosophy

- **Lean templates**: No YAML frontmatter
- File naming convention carries organizational weight
- Flat file system for templates with descriptive filenames

## Sync Strategy (Apple Ecosystem, Zero Cost)

### Primary: iCloud Drive

**Setup**:
1. Create vault folder in iCloud Drive
2. Open Obsidian
3. Point to iCloud folder
4. Enable on all devices

**Caveats**:
- Requires internet for sync
- Occasional sync conflicts (rare)

### Backup Layer 1: Time Machine

- Baseline backup
- Automatic
- Catastrophic restore option

### Backup Layer 2: rsync Snapshots (Optional)

**Timestamped snapshots**:
- Manual or automated (Automator app or launchd script)
- Local backup
- Version history

### Backup Layer 3: Obsidian Git Plugin (Optional)

- Internal version history
- Granular rollback
- Lightweight

## Recovery Workflow

### Minor Fixes
- Obsidian plugins (version history, file recovery)

### Major Restore
- rsync snapshots

### Catastrophic Restore
- Time Machine

## Template System

### Core Templates Plugin

- Points to 99 Templates folder
- Insert prompts on demand
- No QuickAdd complexity

### QuickAdd

**Status**: Disabled
- Too complex for current needs
- Brought up text entry, not file picker

### Earlier Workflow (Discarded)

- Transcluded links for prompts
- Not needed with Core Templates approach

## Deferral Decision

**Until AI Writing Studio course complete**:
- No vault structure changes
- No plugin tinkering
- No expansion into broader workflows

## Open Loops

- Lean versions of earlier character, setting, and scene templates (without YAML)
- Consider regenerating entire 10-prompt library in lean style for 99 Templates
- Drag-and-drop Automator app version of snapshot backup script
- Bible file structure optimized for GPT-5 ingestion
- Boilerplate Reference Vault note template

## Discardables

- QuickAdd configuration attempt
- Transcluded links for prompts (earlier workflow)
- Plugin overthinking
- Third-party sync tools (Dropbox, Syncthing, etc.) — cost and ecosystem mismatch
- Expansion into broader workflows (on hold until course complete)
