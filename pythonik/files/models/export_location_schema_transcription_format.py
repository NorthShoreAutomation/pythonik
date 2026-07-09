from enum import Enum


class ExportLocationSchemaTranscriptionFormat(str, Enum):
    SRT = "SRT"
    WEBVTT = "WEBVTT"

    def __str__(self) -> str:
        return str(self.value)
