from enum import Enum


class AssetTransferredToStorageTriggerSchemaType(str, Enum):
    TRANSFER_TO_STORAGE = "TRANSFER_TO_STORAGE"

    def __str__(self) -> str:
        return str(self.value)
