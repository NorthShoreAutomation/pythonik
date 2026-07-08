from enum import Enum


class AssetPostEditSchemaPublicationStatus(str, Enum):
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    PUBLISHED = "PUBLISHED"
    PUBLISHED_WITH_WARNING = "PUBLISHED_WITH_WARNING"
    RUNNING = "RUNNING"
    SCHEDULED = "SCHEDULED"

    def __str__(self) -> str:
        return str(self.value)
