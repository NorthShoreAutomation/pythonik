from enum import Enum


class RestoreActionSchemaType(str, Enum):
    RESTORE = "RESTORE"

    def __str__(self) -> str:
        return str(self.value)
