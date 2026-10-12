from enum import Enum


class NaturalSearchResponseMatchQuality(str, Enum):
    APPROXIMATE = "approximate"
    EXACT = "exact"
    FILTERS_ONLY = "filters_only"
    RELATED = "related"

    def __str__(self) -> str:
        return str(self.value)
