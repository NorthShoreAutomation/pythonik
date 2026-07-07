from enum import Enum


class SubtitleAddedTriggerType(str, Enum):
    SUBTITLE_ADDED = "SUBTITLE_ADDED"

    def __str__(self) -> str:
        return str(self.value)
