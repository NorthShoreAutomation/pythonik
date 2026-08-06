from enum import Enum


class AssetOnlineTriggerSchemaType(str, Enum):
    ASSET_ONLINE = "ASSET_ONLINE"

    def __str__(self) -> str:
        return str(self.value)
