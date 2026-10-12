from enum import Enum


class EvidenceKind(str, Enum):
    CLAUSE = "clause"
    RATIONALE = "rationale"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
