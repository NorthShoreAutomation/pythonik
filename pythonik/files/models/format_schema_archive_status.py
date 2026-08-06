from enum import Enum


class FormatSchemaArchiveStatus(str, Enum):
    ARCHIVED = "ARCHIVED"
    ARCHIVING = "ARCHIVING"
    FAILED_TO_ARCHIVE = "FAILED_TO_ARCHIVE"
    NOT_ARCHIVED = "NOT_ARCHIVED"

    def __str__(self) -> str:
        return str(self.value)
