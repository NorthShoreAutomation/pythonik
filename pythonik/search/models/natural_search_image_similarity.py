from enum import Enum


class NaturalSearchImageSimilarity(str, Enum):
    SEMANTIC = "semantic"
    VISUAL = "visual"

    def __str__(self) -> str:
        return str(self.value)
