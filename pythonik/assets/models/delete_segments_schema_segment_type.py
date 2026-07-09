from enum import Enum


class DeleteSegmentsSchemaSegmentType(str, Enum):
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
