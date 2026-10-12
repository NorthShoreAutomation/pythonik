from enum import Enum


class TranscriptionEngineInfoType(str, Enum):
    EXTERNAL = "EXTERNAL"
    INTERNAL = "INTERNAL"

    def __str__(self) -> str:
        return str(self.value)
