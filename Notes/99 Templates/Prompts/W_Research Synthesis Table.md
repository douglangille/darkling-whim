# Research Synthesis → Table

```xml
<context>
Topic/question: [topic]. Sources: [notes/excerpts].
</context>
<role>
You are an analyst turning messy notes into a table.
</role>
<task>
Create a comparison table + recommendation.
</task>
<constraints>
- Columns: Source, Key Claims, Evidence Strength, Bias Notes, Takeaway
- Max 6 rows
- Add 3 criteria for recommendation
</constraints>
<format>
Markdown table + 3-bullet recommendation.
</format>
<process>
Step 1: Normalize claims.
Step 2: Assign evidence strength.
Step 3: Draft recommendation.
</process>
<iteration>
Rubric: correctness, bias awareness, decisiveness, brevity. Revise once.
</iteration>