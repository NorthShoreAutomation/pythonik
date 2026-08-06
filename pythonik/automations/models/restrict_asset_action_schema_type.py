from enum import Enum


class RestrictAssetActionSchemaType(str, Enum):
    RESTRICT_ASSET = "RESTRICT_ASSET"

    def __str__(self) -> str:
        return str(self.value)
