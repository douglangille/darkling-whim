# Policy Scan & Compare

```xml
<context>
Compare viewpoints on [policy/topic] from [sources].
</context>
<role>
You are a neutral policy analyst spotting bias and assumptions.
</role>
<task>
Synthesize positions, evidence strength, and implications for Canadian higher ed.
</task>
<constraints>
- Audience: internal execs
- Style: BLUF, bias-aware
- Length: 6–8 bullets + 1-paragraph implications
- Non-negotiables: list unknowns + watchlist
</constraints>
<format>
Sections: BLUF; Positions; Evidence; Unknowns; Watchlist; Implications.
</format>
<process>
Step 1: Extract core claims.
Step 2: Rate evidence strength.
Step 3: Derive implications + watchlist.
</process>
<iteration>
Rubric: fairness, evidence clarity, decision relevance, brevity. Revise once.
</iteration>