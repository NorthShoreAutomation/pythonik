from enum import Enum


class EditSegmentForBulkSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
