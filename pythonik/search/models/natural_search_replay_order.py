from enum import Enum


class NaturalSearchReplayOrder(str, Enum):
    RECENT = "recent"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
