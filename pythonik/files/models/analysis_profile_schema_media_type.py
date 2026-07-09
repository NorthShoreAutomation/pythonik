from enum import Enum


class AnalysisProfileSchemaMediaType(str, Enum):
    FACE_IMAGE = "face_image"
    FACE_VIDEO = "face_video"
    IMAGE = "image"
    TRANSCRIPTION = "transcription"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
