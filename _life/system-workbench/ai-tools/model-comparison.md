# Model Comparison & Usage

## GPT Model Variants

### GPT-5
- **Strengths**: Continuity, reasoning, tone/voice control
- **Use when**: Continuity-heavy work, logic precision, tone matters
- **Characteristics**: Slower, structured, continuity-aware
- **Orchestration**: Dynamic router, proactive behavior, reduced babysitting

### GPT-4o
- **Strengths**: Dialogue, cinematic style, quick inspiration
- **Use when**: Low-stakes ideas, UI tasks, speed matters
- **Characteristics**: Fast responses, cinematic detail, playful tone, shallow reasoning
- **Tell-tale signs**: Fast, vivid, lighter reasoning

### GPT-4o mini
- **Strengths**: Speed, variations, lightweight tasks
- **Use when**: Quick iterations, simple tasks

### GPT-4 turbo
- **Strengths**: Rigid structure, frameworks
- **Use when**: Need formal scaffolding
- **Note**: Rarely routed by system

## Router Behavior

- Defaults to GPT-5
- Opportunistically routes to 4o/mini for speed or multimodal
- Rarely routes to turbo
- **Decision**: Don't micromanage; trust router; force GPT-5 only when continuity/tone critical

## Claude 4.1 Opus vs GPT-5

### Claude Excels At
- Deep reasoning
- Complex bug fixes
- Code cleanliness
- Context memory

### GPT-5 Excels At
- Speed
- Multimodality
- UI/front-end tasks
- Cost efficiency

### Combined Strategy
- Some developers use both
- GPT-5 for planning/scaffolding
- Claude for execution/stability

## Creative Writing Stance

- ChatGPT = best all-around
- Claude = second-best for longform narrative
- R-rated boundaries fine
- NC-17 not needed
- GPT-5 can produce cinematic styles without switching models

## Voice Selection

### Onyx (GPT-4o voice)
- Best match for "Sharp Collaborator" tone
- Structured, candid, dry wit, subtext-capable
- Masculine-coded
- **Status**: Awaiting rollout

### Ember (Current)
- Acceptable fallback
- User confirmed OK until Onyx available

## Model Launch Timeline

- GPT-5 launched: August 7, 2025
- Rolling out across Plus tiers
- Variations in access depth by subscription
