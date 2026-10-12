from enum import Enum


class MatchAssessmentBasis(str, Enum):
    JUDGE = "judge"
    RERANKER = "reranker"
    RETRIEVAL = "retrieval"

    def __str__(self) -> str:
        return str(self.value)
