from enum import Enum


class RemoveAssetRestrictionActionSchemaType(str, Enum):
    REMOVE_ASSET_RESTRICTION = "REMOVE_ASSET_RESTRICTION"

    def __str__(self) -> str:
        return str(self.value)
