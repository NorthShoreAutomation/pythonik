from enum import Enum


class PlaylistSchemaStatus(str, Enum):
    HIDDEN = "HIDDEN"

    def __str__(self) -> str:
        return str(self.value)
