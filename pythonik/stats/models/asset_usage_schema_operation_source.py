from enum import Enum


class AssetUsageSchemaOperationSource(str, Enum):
    COLLECTION = "COLLECTION"
    DISCOVERY = "DISCOVERY"
    EXTERNAL_SHARE = "EXTERNAL_SHARE"
    NOTIFICATION = "NOTIFICATION"
    SEARCH = "SEARCH"
    SHARE = "SHARE"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
