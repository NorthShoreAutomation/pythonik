from enum import Enum


class MatchAssessmentQuality(str, Enum):
    APPROXIMATE = "approximate"
    EXACT = "exact"
    FILTERS_ONLY = "filters_only"
    RELATED = "related"

    def __str__(self) -> str:
        return str(self.value)
