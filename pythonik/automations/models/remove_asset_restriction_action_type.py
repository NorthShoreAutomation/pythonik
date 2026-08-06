from enum import Enum


class RemoveAssetRestrictionActionType(str, Enum):
    REMOVE_ASSET_RESTRICTION = "REMOVE_ASSET_RESTRICTION"

    def __str__(self) -> str:
        return str(self.value)
