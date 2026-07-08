from enum import Enum


class AnalysisTranscriptionSettingsSchemaServiceType(str, Enum):
    AMAZON_REKOGNITION = "AMAZON_REKOGNITION"
    GOOGLE_VIDEO_INTELLIGENCE = "GOOGLE_VIDEO_INTELLIGENCE"
    GOOGLE_VISION = "GOOGLE_VISION"
    ICONIK = "ICONIK"
    ICONIK_FACE_RECOGNITION = "ICONIK_FACE_RECOGNITION"
    REV_AI = "REV_AI"

    def __str__(self) -> str:
        return str(self.value)
