from enum import Enum


class AssetSharedTriggerSchemaType(str, Enum):
    ASSET_SHARE = "ASSET_SHARE"

    def __str__(self) -> str:
        return str(self.value)
