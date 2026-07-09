from enum import Enum


class PlaylistItemSchemaObjectType(str, Enum):
    ASSETS = "assets"
    SEQUENCES = "sequences"

    def __str__(self) -> str:
        return str(self.value)
