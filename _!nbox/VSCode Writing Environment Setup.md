# VSCode Writing Environment Setup

*Created: 2026-01-03*

## Overview

Optimized VSCode configuration for distraction-free markdown writing across iPad, MacBook, and Windows devices. This setup transforms VSCode into a writerly environment without requiring paid apps or fragile mobile Git solutions.

## Key Features

- **18pt serif font** with ligatures (New York/Cambria/Georgia)
- **80-column width** for optimal prose readability
- **Zen Mode** support with centered layout
- **Typewriter scrolling** keeps cursor centered
- **All distractions disabled** (line numbers, minimap, suggestions, highlights)
- **Cross-device sync** via GitHub account

## User Settings (Syncs Across All Devices)

Add to User Settings JSON (`Cmd+Shift+P` → "Preferences: Open User Settings (JSON)"):

```json
"[markdown]": {
  "editor.cursorStyle": "line",
  "editor.fontFamily": "'New York', Cambria, Georgia, serif",
  "editor.fontLigatures": true,
  "editor.fontSize": 18,
  "editor.inlayHints.enabled": "off",
  "editor.lineHeight": 28,
  "editor.lineNumbers": "off",
  "editor.minimap.enabled": false,
  "editor.occurrencesHighlight": "off",
  "editor.quickSuggestions": {
    "other": false,
    "comments": false,
    "strings": false
  },
  "editor.rulers": [],
  "editor.selectionHighlight": false,
  "editor.suggest.showWords": false,
  "editor.wordBasedSuggestions": "off",
  "editor.wordWrap": "bounded",
  "editor.wordWrapColumn": 80,
  "editor.wrappingIndent": "none",
  "files.trimTrailingWhitespace": false,
  "zenMode.centerLayout": true,
  "editor.cursorSurroundingLines": 0,
  "editor.tabSize": 4
},
"markdown.preview.fontFamily": "'New York', Cambria, Georgia, serif",
"markdown.preview.fontSize": 18,
"markdown.preview.lineHeight": 1.6
```

## Workspace Settings (Workbench Repo Only)

Add to `.vscode/settings.json` in Workbench repository:

```json
{
  "gitdoc.enabled": false,
  "markdown.copyFiles.destination": {
    "**/*": "/assets/images/${fileName}"
  },
  "markdown.copyFiles.name": "${datetime}-pasted-image",
  "typewriterScrollMode.enable": true
}
```

## Required Extension

**Typewriter Scroll Mode** by andyhuzhill
- Install from VSCode marketplace
- Toggle: `Ctrl+Shift+T`
- Keeps cursor vertically centered while typing
- Note: May not work in vscode.dev browser version

## Font Stack Behavior

- **iPad/MacBook**: New York (Apple's serif system font)
- **Windows**: Cambria (Microsoft's screen-optimized serif)
- **Fallback**: Georgia (universal)

All three fonts are high-quality, readable serifs designed for screens.

## Usage Tips

### Zen Mode
- **Enter**: `Cmd+K Z`
- **Exit**: Press `Esc` twice
- Hides all UI for distraction-free writing
- Text centers automatically with your settings

### Optimal Column Width
- 80 columns = ~66-75 characters per line
- Optimal for prose readability
- Reduces eye travel fatigue
- Can adjust to 85-90 if feels too narrow

### Adjusting Font Size
- Current: 18pt font, 28pt line height
- Increase both proportionally if needed
- Example: 20pt font → 30pt line height

## Why This Works

**No Paid Apps**: Uses free VSCode across all platforms
**No Fragile Sync**: Avoids problematic Obsidian Git plugin on iPad
**Consistent**: Settings sync via GitHub/Microsoft account
**Native**: Works in vscode.dev browser on iPad
**Integrated**: Maintains existing GitHub workflow

## Alternative Solutions Considered

### Obsidian Mobile + Git (Rejected)
- Obsidian Git plugin doesn't work natively on iOS
- Requires iSH (Linux shell) with manual commands
- Fragile, unreliable sync
- Frequent hanging issues

### Working Copy + Writing App (Rejected)
- Working Copy: $19.99 for push capability
- Pairs with iA Writer or other apps
- Reliable but requires paid software
- Preference for free solution

### GitHub Web Interface (Insufficient)
- Free and functional
- Poor writing experience
- No offline work
- Clunky for extended sessions

## Configuration Levels Explained

**User Settings**
- Syncs across all devices with your account
- Best for universal writing preferences
- Font, size, spacing, distraction removal

**Workspace Settings**
- Stored in repo's `.vscode/settings.json`
- Only applies to this specific repository
- Best for project-specific behaviors
- Git settings, asset management

**Local Settings**
- Device-specific, doesn't sync
- Not useful for multi-device workflow

## Device Coverage

✓ **iPad**: vscode.dev in Safari browser
✓ **MacBook**: Desktop VSCode app
✓ **Work Windows**: Desktop VSCode or Edge browser

All settings sync automatically when signed into GitHub/Microsoft account.

## Troubleshooting

**Text looks too narrow**
- Increase `wordWrapColumn` to 85-90
- Or increase `fontSize` while keeping column width at 72-80

**Text looks too wide**
- Reduce `wordWrapColumn` to 72-75
- Wider lines cause eye fatigue

**Preview doesn't match editor font**
- Check `markdown.preview.fontFamily` in User Settings
- Should match editor font stack

**Settings not syncing**
- Verify signed into VSCode with GitHub/Microsoft account
- Check Settings Sync is enabled (gear icon → Settings Sync On)

**Typewriter mode not working**
- Extension may not work in vscode.dev browser version
- Works reliably in desktop VSCode
- Alternative: Use Zen Mode without typewriter scrolling

## References

- [VSCode Markdown Documentation](https://code.visualstudio.com/docs/languages/markdown)
- [Typewriter Scroll Mode Extension](https://marketplace.visualstudio.com/items?itemName=andyhuzhill.typewriterscrollmode)
- Configured: 2026-01-03
- Status: Active, tested on iPad and MacBook