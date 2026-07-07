from enum import Enum


class ExtractFacesActionSchemaType(str, Enum):
    EXTRACT_FACES = "EXTRACT_FACES"

    def __str__(self) -> str:
        return str(self.value)
