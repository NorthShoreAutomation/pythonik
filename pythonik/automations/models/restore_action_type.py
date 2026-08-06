from enum import Enum


class RestoreActionType(str, Enum):
    RESTORE = "RESTORE"

    def __str__(self) -> str:
        return str(self.value)
