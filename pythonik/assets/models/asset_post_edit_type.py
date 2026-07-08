from enum import Enum


class AssetPostEditType(str, Enum):
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
