from enum import Enum


class MetadataUpdateActionSchemaType(str, Enum):
    METADATA_UPDATE = "METADATA_UPDATE"

    def __str__(self) -> str:
        return str(self.value)
