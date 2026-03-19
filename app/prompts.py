def build_master_counterfactual_prompt(user_input: str) -> str:
    return f"""
You are a premium strategic counterfactual analysis engine.

Analyze this hypothetical scenario:

USER INPUT:
{user_input}

Return STRICT JSON ONLY.
Do not include markdown.
Do not include code fences.
Do not include commentary before or after JSON.

Use exactly this schema:
{{
  "scenario": "short clear scenario title",
  "baseline": "3 to 5 lines max. Clear description of the real-world baseline.",
  "counterfactual_change": "2 to 3 lines max. State the exact hypothetical change.",
  "immediate_impacts": [
    "exactly 3 concise impact statements"
  ],
  "mid_term_impacts": [
    "exactly 3 concise impact statements"
  ],
  "long_term_impacts": [
    "exactly 3 concise impact statements"
  ],
  "assumptions": [
    "exactly 3 concise assumptions"
  ],
  "confidence": "Low or Medium or High",
  "executive_summary": "4 to 6 lines max. Crisp, premium, strategic summary."
}}

Hard rules:
- Be specific, not vague.
- Do not say information is missing unless the user input is truly empty.
- Do not invent placeholder text like 'core input absent' or 'counterfactual change missing'.
- Keep all impacts directly tied to the hypothetical scenario.
- Each impact must be one sentence only.
- No philosophical filler.
- No academic essay style.
- No repeated wording.
- Confidence must be exactly one word: Low, Medium, or High.
- Output valid JSON only.
""".strip()