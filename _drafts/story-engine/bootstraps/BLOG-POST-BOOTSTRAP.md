# BLOG POST Bootstrap

**Purpose**: Plan, draft, and polish non-fiction blog posts from idea to publication.

---

## When to Use This Bootstrap

- Writing non-fiction blog posts
- Technical articles
- Essays and opinion pieces
- How-to guides and tutorials
- Commentary and analysis
- Weekly/regular blog content

---

## Blog Post Workflow

### Phase 1: IDEATION
**Goal**: Develop topic into focused post concept

**Tasks**:

**Step 1: Capture the Seed**
- What sparked this post idea?
- Why write this now?
- What's the core message?
- Who's the audience?

**Step 2: Define the Post**
- **Topic**: What is this post about?
- **Angle**: What's your specific take?
- **Purpose**: What do you want readers to gain?
  - Learn something new
  - Change perspective
  - Take action
  - Understand concept
  - Solve problem
- **Audience**: Who needs to read this?
- **Scope**: How deep/long?

**Step 3: Core Argument/Message**
- What's the main point in one sentence?
- What do you want readers to remember?
- What's the "so what?"

**Step 4: Validate**
- Do you have enough to say?
- Is this interesting/valuable?
- Does it fit your blog's purpose?
- Can you deliver on the promise?

**Deliverables**:
- `concept.md` (post idea and core message)

**Status Check**: ✅ Complete when concept is clear

---

### Phase 2: RESEARCH & PLANNING
**Goal**: Gather material and structure post

**Tasks**:

**Step 5: Research/Gather**
- What do you already know?
- What do you need to research?
- What examples/stories support points?
- What data/sources to cite?
- What personal experience applies?

**Step 6: Outline Structure**
Choose structure based on post type:

**Argument/Opinion Post**:
1. Hook/opening
2. State position
3. Support with 3-5 points
4. Address counterarguments
5. Conclusion/call to action

**How-To/Tutorial**:
1. Hook/problem statement
2. Overview of solution
3. Step-by-step instructions
4. Common mistakes/troubleshooting
5. Conclusion/next steps

**Analysis/Commentary**:
1. Hook/context
2. Explain the situation/topic
3. Analyze implications
4. Offer insights
5. Conclusion/what it means

**Personal Essay**:
1. Hook/scene/anecdote
2. Develop narrative
3. Reflection/insight
4. Universal application
5. Conclusion/resonance

**Listicle/Collection**:
1. Hook/promise
2. Item 1 (with explanation)
3. Item 2 (with explanation)
4. [Continue...]
5. Conclusion/synthesis

**Step 7: Detailed Outline**
- Break structure into sections
- Each section = 1-3 paragraphs
- Note key points for each section
- Identify transitions
- Plan opening hook
- Plan closing statement

**Step 8: Title Options**
- Brainstorm 5-10 potential titles
- Test for:
  - Clarity (what's this about?)
  - Intrigue (want to read?)
  - SEO (searchable terms?)
  - Accuracy (delivers on promise?)
- Select working title

**Deliverables**:
- `research-notes.md` (sources, examples, data)
- `outline.md` (detailed structure)
- `titles.md` (title options)

**Status Check**: ✅ Complete when outline is approved

---

### Phase 3: DRAFTING
**Goal**: Write complete first draft

**Tasks**:

**Step 9: Draft Sections**
- Write section by section following outline
- Don't self-edit yet
- Keep momentum
- Mark unclear areas with [NOTE]
- Let voice flow naturally

**Step 10: Opening Hook**
Strong openings:
- Surprising statistic
- Provocative question
- Relevant anecdote
- Bold statement
- Paint a scene
- State the problem

**Step 11: Body Development**
- Each section makes one main point
- Support points with:
  - Examples
  - Data/research
  - Stories
  - Analogies
  - Personal experience
- Use clear transitions
- Vary paragraph length

**Step 12: Conclusion**
Strong closings:
- Summarize key points
- Call to action
- Future implications
- Circle back to opening
- Leave with resonant thought

**Step 13: Complete Draft**
- Read through full draft
- Fill in [NOTE] sections
- Ensure flow
- Check against outline (did you deliver?)

**Deliverables**:
- `draft.md` (complete first draft)

**Status Check**: ✅ Complete when full draft exists

---

### Phase 4: REVISION
**Goal**: Polish and strengthen post

**Tasks**:

**Step 14: Structural Revision**
- Does opening hook readers?
- Do sections flow logically?
- Is argument/message clear?
- Are examples effective?
- Does conclusion satisfy?
- Any sections to cut/move/expand?

**Step 15: Clarity Pass**
- Remove jargon (or explain it)
- Simplify complex sentences
- Define terms
- Add context where needed
- Ensure accessibility for audience

**Step 16: Voice & Style**
- Consistent tone throughout?
- Active voice where possible
- Vary sentence structure
- Remove unnecessary words
- Strengthen weak verbs
- Check for clichés

**Step 17: Evidence & Support**
- Are claims backed up?
- Are sources cited?
- Are examples relevant?
- Is data accurate?
- Add links where appropriate

**Step 18: Technical Polish**
- Grammar and punctuation
- Spelling
- Formatting (headers, lists, emphasis)
- Link checking
- Image attribution (if applicable)

**Deliverables**:
- `revised-draft.md` (polished version)
- `revision-notes.md` (what changed and why)

**Status Check**: ✅ Complete when post is polished

---

### Phase 5: FINALIZATION
**Goal**: Prepare for publication

**Tasks**:

**Step 19: Final Read**
- Read aloud or text-to-speech
- Catch awkward phrasing
- Verify flow
- Check for repetition

**Step 20: Metadata**
- Finalize title
- Write meta description (150-160 chars)
- Select categories/tags
- Choose publication date
- Add author info

**Step 21: SEO Check**
- Keywords naturally included?
- Headers use hierarchy (H2, H3)?
- Internal/external links present?
- Images have alt text?
- Meta description compelling?

**Step 22: Format for Platform**
- Add Jekyll/blog frontmatter
- Format code blocks (if technical)
- Add images/graphics
- Insert links
- Preview rendering

**Step 23: Final Checklist**
- [ ] Title is compelling
- [ ] Opening hooks reader
- [ ] Main points clear
- [ ] Examples support arguments
- [ ] Sources cited
- [ ] Links work
- [ ] Grammar/spelling clean
- [ ] Formatting correct
- [ ] Meta description written
- [ ] Tags/categories assigned
- [ ] Images added (if applicable)
- [ ] Ready to publish

**Deliverables**:
- Published post in `_posts/[date]-[slug].md`
- Archive of drafts in `_drafts/[post-name]/`

**Status Check**: ✅ Complete when published

---

## File Structure

```
[post-name]/
├── README.md
├── concept.md
├── research-notes.md
├── outline.md
├── titles.md
├── draft.md
├── revised-draft.md
└── revision-notes.md
```

After publication:
```
_posts/2025-12-23-post-slug.md  # Published
_drafts/post-name/              # Archive preserved
```

---

## Example Sessions

### Starting New Post

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/BLOG-POST-BOOTSTRAP.md

# New Blog Post: The Value of Writing Publicly

Project folder: _drafts/writing-publicly/

Topic: Why writers should blog despite AI content flood
Audience: Early-career writers, hobbyists
Purpose: Encourage authentic public writing

Begin concept development and outlining.
```

### Continuing Draft

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/BLOG-POST-BOOTSTRAP.md

# Drafting: The Value of Writing Publicly

Project folder: _drafts/writing-publicly/

Load artifacts:
- outline.md
- research-notes.md

Draft sections 3-5, following outline.
```

### Revision Session

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/BLOG-POST-BOOTSTRAP.md

# Revising: The Value of Writing Publicly

Project folder: _drafts/writing-publicly/

Load: draft.md

Revise for:
- Stronger opening hook
- Clearer examples in section 2
- Better conclusion
```

---

## Post Type Templates

### Argument/Opinion Post Outline

```markdown
# [Post Title]

## Opening (1-2 paragraphs)
- Hook: [Attention-grabbing opener]
- Context: [Why this matters now]
- Thesis: [Your main argument]

## Background (2-3 paragraphs)
- Explain the situation/issue
- Provide necessary context
- Set up your argument

## Point 1 (2-3 paragraphs)
- Make first supporting point
- Provide evidence/example
- Explain significance

## Point 2 (2-3 paragraphs)
- Make second supporting point
- Provide evidence/example
- Explain significance

## Point 3 (2-3 paragraphs)
- Make third supporting point
- Provide evidence/example
- Explain significance

## Counterarguments (1-2 paragraphs)
- Address opposing views
- Explain why your argument holds

## Conclusion (1-2 paragraphs)
- Summarize main points
- Restate thesis in new light
- Call to action or final thought
```

### How-To/Tutorial Outline

```markdown
# How to [Accomplish Goal]

## Introduction (1-2 paragraphs)
- State the problem
- Promise the solution
- Set expectations (time, difficulty, prerequisites)

## Overview (1 paragraph)
- What you'll learn
- High-level process

## Prerequisites (list)
- What you need before starting
- Tools, knowledge, materials

## Step 1: [First Step]
- Explain what to do
- Why this step matters
- Common mistakes to avoid

## Step 2: [Second Step]
- Explain what to do
- Why this step matters
- Common mistakes to avoid

[Continue for all steps]

## Troubleshooting
- Common problems and solutions

## Conclusion
- Recap what was accomplished
- Next steps or extensions
- Where to go for more
```

### Personal Essay Outline

```markdown
# [Post Title]

## Opening Scene (2-3 paragraphs)
- Set the scene
- Hook with anecdote or moment
- Establish stakes

## Development (multiple paragraphs)
- Tell the story
- Show progression/change
- Include sensory details
- Build to realization

## Reflection (2-3 paragraphs)
- What this experience taught
- Insight gained
- How it changed perspective

## Universal Application (1-2 paragraphs)
- Connect to broader truth
- What readers can take away
- Resonant closing thought
```

---

## Frontmatter Template

```yaml
---
layout: post
title: "[Post Title]"
date: YYYY-MM-DD HH:MM:SS
categories: [Category1, Category2]
tags: [tag1, tag2, tag3]
author: Douglas Langille
excerpt: "[Meta description / excerpt for preview]"
readtime: true
comments: true
---
```

---

## Title Formulas

**How-To**: "How to [Accomplish Goal]"  
**List**: "[Number] Ways to [Benefit]"  
**Question**: "Why [Surprising Thing]?"  
**Statement**: "[Bold Claim] and Why It Matters"  
**Story**: "What [Experience] Taught Me About [Lesson]"  
**Controversy**: "Why [Common Belief] Is Wrong"  
**Guide**: "The Complete Guide to [Topic]"  

**Test**: Would you click this if you saw it?

---

## Working Principles

- **One main point**: Every post has a core message
- **Hook early**: First paragraph determines if they read on
- **Show, don't tell**: Use examples and stories
- **Be specific**: Concrete beats abstract
- **Respect reader time**: Get to the point
- **End strong**: Last impression matters
- **Edit ruthlessly**: Cut what doesn't serve the message

---

## Commit Message Standards

- "Start blog post: [Title]"
- "Draft outline for [Title]"
- "Complete first draft: [Title]"
- "Revise [Title]: strengthen opening"
- "Finalize [Title] for publication"
- "Publish: [Title]"

---

## Quick vs. Deep Posts

### Quick Post (1-2 hours)
- Short (500-800 words)
- Single point or observation
- Minimal research
- Fast draft → light edit → publish
- Good for regular cadence

### Deep Post (4-8 hours)
- Long (1,500-3,000 words)
- Complex argument or tutorial
- Research required
- Multiple drafts
- Thorough revision
- Good for cornerstone content

**Both are valuable**. Match effort to purpose.

---

**Bootstrap Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
