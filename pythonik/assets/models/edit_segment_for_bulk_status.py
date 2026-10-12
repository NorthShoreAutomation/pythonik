from enum import Enum


class EditSegmentForBulkStatus(str, Enum):
    ACTIVE = "ACTIVE"
    AWAITED = "AWAITED"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
