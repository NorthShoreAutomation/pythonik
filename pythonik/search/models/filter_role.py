from enum import Enum


class FilterRole(str, Enum):
    FILTER = "filter"
    SCORING = "scoring"

    def __str__(self) -> str:
        return str(self.value)
