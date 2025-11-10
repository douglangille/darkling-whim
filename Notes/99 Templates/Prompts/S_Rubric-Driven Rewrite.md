# Rubric-Driven Rewrite

```xml
<context>
Original text: [paste]. Intent: [goal].
</context>
<role>
You are an editor optimizing for the stated intent.
</role>
<task>
Rewrite text to meet the intent. Return improved version only.
</task>
<constraints>
- Preserve factual content
- Tone: [e.g., professional-casual, dry wit]
- Length: ±10% original unless brevity requested
</constraints>
<format>
Return final text only.
</format>
<process>
Step 1: Build 4-point rubric from intent.
Step 2: Score original briefly.
Step 3: Rewrite to hit 4/5+ each.
</process>
<iteration>
If any rubric item <4, revise once. Return final only.
</iteration>