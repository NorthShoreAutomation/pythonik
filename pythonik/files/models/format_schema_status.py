from enum import Enum


class FormatSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
