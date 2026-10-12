from enum import Enum


class ResultOrder(str, Enum):
    RECENT = "recent"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
