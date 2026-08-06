from enum import Enum


class ExportActionType(str, Enum):
    EXPORT = "EXPORT"

    def __str__(self) -> str:
        return str(self.value)
