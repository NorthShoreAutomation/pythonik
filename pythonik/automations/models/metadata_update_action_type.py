from enum import Enum


class MetadataUpdateActionType(str, Enum):
    METADATA_UPDATE = "METADATA_UPDATE"

    def __str__(self) -> str:
        return str(self.value)
