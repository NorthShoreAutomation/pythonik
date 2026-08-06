from enum import Enum


class ArchiveActionSchemaType(str, Enum):
    ARCHIVE = "ARCHIVE"

    def __str__(self) -> str:
        return str(self.value)
