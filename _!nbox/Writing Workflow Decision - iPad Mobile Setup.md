# Writing Workflow Decision: iPad Mobile Setup

*Decision Date: 2026-01-03*

## Question

How to enable productive creative writing on iPad for Workbench repository without compromising reliability?

## Context

**Current Workflow**
- Perplexity (AI assistance)
- GitHub web interface (version control)
- VSCode (editing)
- Works but not optimized for extended writing

**Previous Setup**
- Obsidian with GitHub plugin
- Worked well on desktop
- Uncertain about current iPad viability

**Requirements**
- Reliable Git sync with Workbench repo
- Good writing UX on iPad
- No fragile/complicated workarounds
- Free or minimal cost
- Cross-device consistency (iPad, MacBook, Windows)

## Options Evaluated

### Option 1: Obsidian Mobile + Git Plugin

**Pros**
- Superior writing experience
- Previous familiarity with Obsidian
- Good markdown editor

**Cons**
- Git plugin doesn't work natively on iOS
- Requires iSH (Linux shell emulator)
- Manual terminal commands before/after each session
- Frequent hanging and sync failures
- Fragile, unreliable setup
- Multiple user reports of issues (2023-2025)

**Status**: ❌ Rejected - Too fragile for reliable use

**Research Citations**
- Reddit discussions on iOS Git sync problems
- Forum posts requiring iSH workarounds
- GitHub issues reporting mobile sync failures

### Option 2: Working Copy + Writing App

**Solution**: Working Copy (Git client) + iA Writer or Editorial

**Pros**
- Working Copy is gold-standard iOS Git client
- Highly reliable, well-reviewed
- Integrates with iOS document providers
- iA Writer has excellent writing UX
- Proven workflow for Jekyll/GitHub Pages

**Cons**
- Working Copy costs $19.99 for push capability
- Requires managing two apps
- Additional workflow complexity

**Status**: ❌ Rejected - Preference for free solution

**Research Citations**
- Working Copy documentation
- Users successfully managing Jekyll blogs via this workflow
- iA Writer GitHub integration examples

### Option 3: Optimize VSCode (Browser-Based)

**Solution**: Configure VSCode.dev with writerly markdown settings

**Pros**
- Free - no additional apps
- Works in Safari on iPad (vscode.dev)
- Native Git integration
- Settings sync via GitHub account
- Consistent across all devices
- No fragile mobile workarounds
- Maintains existing workflow

**Cons**
- Not a dedicated writing app
- Requires configuration
- Some extensions may not work in browser version

**Status**: ✅ **SELECTED** - Best balance of reliability and cost

**Implementation**: See "VSCode Writing Environment Setup.md"

## Decision Rationale

### Why VSCode Won

1. **Reliability**: Browser-based, no mobile Git complications
2. **Cost**: Completely free
3. **Simplicity**: Single tool across all devices
4. **Integration**: Already part of existing workflow
5. **Configurability**: Can transform into good writing environment

### Why Not Obsidian Mobile

The dealbreaker was fragility. Multiple sources confirmed:
- iOS Git plugin requires iSH shell emulator
- Manual terminal commands each session
- Frequent sync failures and hanging
- "Non-starter" for reliable workflow

Even though Obsidian has superior writing UX, unreliable Git sync makes it unusable for this use case.

### Why Not Working Copy

While this would work reliably, the combination of:
- $19.99 cost
- Two-app workflow (Git client + editor)
- Existing functional browser-based option

Made it less attractive than optimizing existing free tools.

## Configuration Approach

### Settings Organization

**User Settings** (universal markdown preferences)
- Font stack: New York/Cambria/Georgia serif
- 18pt font, 28pt line height
- 80-column width
- Zen Mode support
- All distractions disabled
- Syncs across all devices

**Workspace Settings** (Workbench-specific)
- GitDoc disabled
- Image paste configuration
- Typewriter scroll enabled
- Stored in repo `.vscode/settings.json`

### Why This Split

- **User**: Writing preferences should work everywhere
- **Workspace**: Repo-specific behaviors stay with project
- **Sync**: User settings follow you; workspace stays in Git

## Results

### Before
- 16pt sans-serif font
- 72-column narrow width looked cramped
- Line numbers, minimap, suggestions enabled
- Standard code editor appearance
- Functional but not writerly

### After  
- 18pt serif font (elegant, readable)
- 80-column width (optimal prose readability)
- Clean, distraction-free interface
- Zen Mode for focused writing
- Typewriter scrolling (cursor stays centered)
- Book-like reading/writing experience

### Testing

✅ Verified on iPad (vscode.dev in Safari)
✅ Verified on MacBook (desktop VSCode)
✅ Settings sync working
✅ Font stack renders correctly on both platforms
✅ Markdown preview matches editor styling

## iPad-Specific Considerations

### What Works
- vscode.dev in Safari browser
- Full Git integration (commit, push, pull)
- User Settings sync
- Markdown preview
- Zen Mode
- Basic keyboard shortcuts

### What May Not Work
- Typewriter Scroll Mode extension (browser limitation)
- Some advanced extensions

### Workarounds
- Zen Mode alone provides good focused environment
- Core writing features work reliably
- Desktop VSCode has full extension support

## Lessons Learned

1. **Mobile Git is complicated**: Native iOS Git support is limited
2. **Fragility matters**: Unreliable tools worse than imperfect reliable ones
3. **Configuration over tools**: Sometimes optimizing existing tools beats adding new ones
4. **Free can be good**: VSCode.dev surprisingly capable for writing
5. **Research saves pain**: Discovering Obsidian Git issues before implementing saved time

## Future Considerations

### If VSCode Proves Insufficient

Fallback option: Working Copy + iA Writer
- Known reliable workflow
- Worth the $19.99 if writing productivity significantly impaired
- Can implement later without losing current setup

### Potential Improvements

- Custom CSS for markdown preview (more advanced styling)
- Additional VSCode extensions for writing (grammar, word count)
- Keyboard shortcuts optimization for iPad

### Not Recommended

- ❌ Obsidian mobile with Git plugin (too fragile)
- ❌ GitHub web editor alone (poor writing UX)
- ❌ Complex multi-tool workflows (unnecessary complexity)

## Related Documentation

- `VSCode Writing Environment Setup.md` - Configuration details
- `Workbench/.vscode/settings.json` - Workspace settings
- User Settings JSON - Universal markdown configuration

## External Resources

### Research Sources

- Obsidian Git plugin GitHub repo (mobile limitations documented)
- Reddit r/ObsidianMD discussions (2023-2025)
- Obsidian forum posts on iOS Git sync
- Working Copy documentation and user guides
- VSCode markdown documentation
- Jekyll + Obsidian workflow examples

### Key Insights

- 2025-2026: Obsidian Git still doesn't support iOS natively
- Working Copy remains the standard iOS Git solution
- VSCode.dev browser capabilities improved significantly
- Settings Sync makes VSCode viable across devices

## Timeline

- **2025-12-31**: Previously used Obsidian with GitHub plugin
- **2026-01-03**: Evaluated current iPad options
- **2026-01-03**: Tested Obsidian mobile viability (rejected)
- **2026-01-03**: Configured VSCode writing environment
- **2026-01-03**: Tested on iPad and MacBook (successful)
- **2026-01-03**: Decision finalized - VSCode solution

## Status

**Decision**: FINAL ✅  
**Implementation**: COMPLETE ✅  
**Testing**: SUCCESSFUL ✅  
**Rollback Plan**: Working Copy option available if needed

---

*This document captures the decision-making process for future reference and to avoid re-evaluating the same options unnecessarily.*