from enum import Enum


class AIMetadataFillingActionSchemaType(str, Enum):
    AI_METADATA_FILLING = "AI_METADATA_FILLING"

    def __str__(self) -> str:
        return str(self.value)
