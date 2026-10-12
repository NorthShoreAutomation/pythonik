from enum import Enum


class CreateAssetVersionFromVersionSchemaIncludeSegmentTypesType0Item(str, Enum):
    COMMENT = "COMMENT"
    GENERIC = "GENERIC"
    MARKER = "MARKER"
    PERSON = "PERSON"
    QC = "QC"
    SCENE = "SCENE"
    SEMANTIC_TRANSCRIPTION = "SEMANTIC_TRANSCRIPTION"
    SHOT = "SHOT"
    TAG = "TAG"
    TRANSCRIPTION = "TRANSCRIPTION"

    def __str__(self) -> str:
        return str(self.value)
