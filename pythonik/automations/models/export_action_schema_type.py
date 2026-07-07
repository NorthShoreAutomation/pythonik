from enum import Enum


class ExportActionSchemaType(str, Enum):
    EXPORT = "EXPORT"

    def __str__(self) -> str:
        return str(self.value)
