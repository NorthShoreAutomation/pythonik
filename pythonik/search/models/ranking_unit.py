from enum import Enum


class RankingUnit(str, Enum):
    ASSET = "asset"
    COLLECTION = "collection"
    POST = "post"
    SEGMENT = "segment"

    def __str__(self) -> str:
        return str(self.value)
