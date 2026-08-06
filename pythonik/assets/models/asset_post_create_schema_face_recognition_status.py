from enum import Enum


class AssetPostCreateSchemaFaceRecognitionStatus(str, Enum):
    DONE = "DONE"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NA = "N/A"
    REQUESTED = "REQUESTED"

    def __str__(self) -> str:
        return str(self.value)
