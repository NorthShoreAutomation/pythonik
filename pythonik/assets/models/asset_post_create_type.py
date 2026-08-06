from enum import Enum


class AssetPostCreateType(str, Enum):
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
