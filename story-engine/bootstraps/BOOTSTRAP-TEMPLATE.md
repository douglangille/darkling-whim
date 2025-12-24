# [WORKFLOW-NAME] Bootstrap

**Purpose**: [One sentence describing what this bootstrap accomplishes]

**Use this for**:
- [Use case 1]
- [Use case 2]
- [Use case 3]

---

## When to Use This Bootstrap

[2-3 sentences describing the specific situations where this bootstrap is the right choice]

---

## [Workflow Name] Workflow

### Phase 1: [PHASE NAME]
**Goal**: [What this phase accomplishes in one sentence]

**Tasks**:
1. **[Task category 1]**:
   - [Specific task]
   - [Specific task]
   - [Specific task]

2. **[Task category 2]**:
   - [Specific task]
   - [Specific task]

**Deliverables**:
- `[filename.md]` ([description])
- `[filename.md]` ([description])

**Status Check**: ✅ Complete when [completion criteria]

---

### Phase 2: [PHASE NAME]
**Goal**: [What this phase accomplishes in one sentence]

**Tasks**:
1. **[Task category 1]**:
   - [Specific task]
   - [Specific task]

2. **[Task category 2]**:
   - [Specific task]
   - [Specific task]

**Deliverables**:
- `[filename.md]` ([description])

**Status Check**: ✅ Complete when [completion criteria]

---

[Repeat phase structure for all phases]

---

## File Structure

Project folder: `_drafts/[project-name]/`

```
[project-name]/
├── README.md
├── [phase-artifact-1].md
├── [phase-artifact-2].md
├── [phase-artifact-3].md
└── [subfolder]/ (if needed)
    ├── [file].md
    └── [file].md
```

---

## Example Sessions

### Starting New [Project Type]

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/[WORKFLOW-NAME]-BOOTSTRAP.md

# New [Project Type]: [Example Title]

[Specific setup details]

Begin [first phase name].
```

### Continuing Existing [Project Type]

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/[WORKFLOW-NAME]-BOOTSTRAP.md

# [Project Type]: [Example Title]

Load artifacts: _drafts/[project-name]/
Report current phase and resume.
```

---

## [Optional: Template Sections]

If your workflow uses specific templates, include them here.

### [Template Name] Template

In `[filename.md]`:

```markdown
# [Template Title]

**[Field Name]**: [Description]

---

## [Section Name]

[Template content]

---

## [Section Name]

[Template content]
```

---

## Working Principles

- **[Principle 1]**: [Brief description]
- **[Principle 2]**: [Brief description]
- **[Principle 3]**: [Brief description]
- **[Principle 4]**: [Brief description]

---

## Common Patterns

[If applicable, describe common patterns or approaches within this workflow]

### Pattern 1: [Name]
[Description of when and how to use this pattern]

### Pattern 2: [Name]
[Description of when and how to use this pattern]

---

## Commit Message Standards

- "Initialize [project type]: [Title]"
- "Complete Phase 1 ([phase name]) for [Title]"
- "Complete Phase 2 ([phase name]) for [Title]"
- "[Specific action] for [Title]: [details]"

---

## Tips for Success

1. **[Tip 1]**: [Practical advice]
2. **[Tip 2]**: [Practical advice]
3. **[Tip 3]**: [Practical advice]

---

## What Can Go Wrong

**Problem**: [Common issue]
**Solution**: [How to address it]

**Problem**: [Common issue]
**Solution**: [How to address it]

---

## Related Bootstraps

**Precedes**: [Bootstrap that commonly comes before this one]

**Follows**: [Bootstrap that commonly comes after this one]

**Alternatives**: [Similar bootstraps and when to use each]

---

**Bootstrap Version**: 1.0  
**Created**: [Date]  
**Last Updated**: [Date]  
**Author**: Doug Langille  
**Repository**: github.com/douglangille/Workbench

---

## Template Usage Notes

**To create a new bootstrap using this template**:

1. Copy this file to `[WORKFLOW-NAME]-BOOTSTRAP.md`
2. Replace all bracketed placeholders with actual content
3. Remove this "Template Usage Notes" section
4. Adjust phase count (2-7 phases typical)
5. Include at least 2 example sessions
6. Add any workflow-specific sections needed
7. Update metadata at bottom

**Required sections**:
- Purpose statement
- "When to Use This Bootstrap" section
- At least 2 phases with Tasks/Deliverables/Status Check
- File Structure section
- At least 2 Example Sessions
- Working Principles
- Commit Message Standards
- Related Bootstraps
- Metadata (version, dates, author)

**Optional but recommended**:
- Template sections (if workflow uses specific document templates)
- Common Patterns
- Tips for Success
- What Can Go Wrong
- Multiple example sessions for different scenarios

**Style guidelines**:
- Use active voice
- Keep instructions clear and actionable
- One task per bullet point
- Status checks should be unambiguous
- Example sessions should be copy-paste ready
- File structure should show actual filenames

**Testing your bootstrap**:
1. Try using it for a real project
2. Note where you get stuck or confused
3. Revise those sections for clarity
4. Have someone else try to follow it
5. Iterate until smooth
