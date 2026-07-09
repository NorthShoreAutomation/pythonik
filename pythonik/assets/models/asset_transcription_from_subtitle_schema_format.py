from enum import Enum


class AssetTranscriptionFromSubtitleSchemaFormat(str, Enum):
    SRT = "SRT"
    VTT = "VTT"
    WEBVTT = "WEBVTT"

    def __str__(self) -> str:
        return str(self.value)
