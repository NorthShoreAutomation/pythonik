from enum import Enum


class SegmentBaseSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
