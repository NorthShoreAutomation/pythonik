from enum import Enum


class MetadataUpdateTriggerParametersEventType(str, Enum):
    ASSETS = "ASSETS"
    COLLECTIONS = "COLLECTIONS"

    def __str__(self) -> str:
        return str(self.value)
