from enum import Enum


class TranscodeActionSchemaType(str, Enum):
    TRANSCODE = "TRANSCODE"

    def __str__(self) -> str:
        return str(self.value)
