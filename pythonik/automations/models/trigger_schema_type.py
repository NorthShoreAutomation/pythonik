from enum import Enum


class TriggerSchemaType(str, Enum):
    ARCHIVE = "ARCHIVE"
    ASSET_ONLINE = "ASSET_ONLINE"
    ASSET_SHARE = "ASSET_SHARE"
    CREATED_AT_TRANSITION = "CREATED_AT_TRANSITION"
    METADATA_UPDATE = "METADATA_UPDATE"
    MODIFIED_AT_TRANSITION = "MODIFIED_AT_TRANSITION"
    RESTORE = "RESTORE"
    TRANSFER_TO_STORAGE = "TRANSFER_TO_STORAGE"

    def __str__(self) -> str:
        return str(self.value)
