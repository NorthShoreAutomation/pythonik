from enum import Enum


class SubtitleAddedTriggerSchemaType(str, Enum):
    SUBTITLE_ADDED = "SUBTITLE_ADDED"

    def __str__(self) -> str:
        return str(self.value)
