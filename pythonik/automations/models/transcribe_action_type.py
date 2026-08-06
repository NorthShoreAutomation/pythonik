from enum import Enum


class TranscribeActionType(str, Enum):
    TRANSCRIBE = "TRANSCRIBE"

    def __str__(self) -> str:
        return str(self.value)
