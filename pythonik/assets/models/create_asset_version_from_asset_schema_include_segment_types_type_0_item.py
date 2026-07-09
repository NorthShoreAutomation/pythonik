from enum import Enum


class CreateAssetVersionFromAssetSchemaIncludeSegmentTypesType0Item(str, Enum):
    COMMENT = "COMMENT"
    GENERIC = "GENERIC"
    MARKER = "MARKER"
    PERSON = "PERSON"
    QC = "QC"
    SCENE = "SCENE"
    TAG = "TAG"
    TRANSCRIPTION = "TRANSCRIPTION"

    def __str__(self) -> str:
        return str(self.value)
