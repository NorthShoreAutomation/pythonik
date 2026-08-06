from enum import Enum


class EditAssetVersionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    DELETING = "DELETING"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"

    def __str__(self) -> str:
        return str(self.value)
