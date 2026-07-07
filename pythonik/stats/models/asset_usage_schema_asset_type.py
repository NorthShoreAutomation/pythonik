from enum import Enum


class AssetUsageSchemaAssetType(str, Enum):
    ASSET = "ASSET"
    NLE_PROJECT = "NLE_PROJECT"
    PLACEHOLDER = "PLACEHOLDER"
    SEQUENCE = "SEQUENCE"

    def __str__(self) -> str:
        return str(self.value)
