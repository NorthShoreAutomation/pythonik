from enum import Enum


class PaginationRefusal(str, Enum):
    EXTERNAL_BACKEND = "external_backend"
    MULTIPLE_ROUNDS = "multiple_rounds"
    NO_RESULTS = "no_results"
    RERANK_APPLIED = "rerank_applied"
    SEGMENT_RESULT_UNIT = "segment_result_unit"
    UNEXPRESSIBLE_QUERY = "unexpressible_query"

    def __str__(self) -> str:
        return str(self.value)
