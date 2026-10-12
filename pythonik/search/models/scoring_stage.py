from enum import Enum


class ScoringStage(str, Enum):
    FUSION = "fusion"
    RERANK = "rerank"

    def __str__(self) -> str:
        return str(self.value)
