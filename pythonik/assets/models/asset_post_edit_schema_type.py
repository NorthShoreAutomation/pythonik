from enum import Enum


class AssetPostEditSchemaType(str, Enum):
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
