from dataclasses import dataclass, field
from typing import Any


@dataclass
class SimulationResult:
    scenario: str = ""
    baseline: str = ""
    counterfactual_change: str = ""
    immediate_impacts: list[str] = field(default_factory=list)
    mid_term_impacts: list[str] = field(default_factory=list)
    long_term_impacts: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    confidence: str = "Medium"
    executive_summary: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SimulationResult":
        def as_list(value: Any) -> list[str]:
            if isinstance(value, list):
                return [str(item).strip() for item in value if str(item).strip()]
            if isinstance(value, str) and value.strip():
                return [value.strip()]
            return []

        confidence = str(data.get("confidence", "Medium")).strip().title()
        if confidence not in {"Low", "Medium", "High"}:
            confidence = "Medium"

        return cls(
            scenario=str(data.get("scenario", "")).strip(),
            baseline=str(data.get("baseline", "")).strip(),
            counterfactual_change=str(data.get("counterfactual_change", "")).strip(),
            immediate_impacts=as_list(data.get("immediate_impacts", [])),
            mid_term_impacts=as_list(data.get("mid_term_impacts", [])),
            long_term_impacts=as_list(data.get("long_term_impacts", [])),
            assumptions=as_list(data.get("assumptions", [])),
            confidence=confidence,
            executive_summary=str(data.get("executive_summary", "")).strip(),
        )