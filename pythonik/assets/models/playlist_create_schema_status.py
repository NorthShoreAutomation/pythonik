from enum import Enum


class PlaylistCreateSchemaStatus(str, Enum):
    HIDDEN = "HIDDEN"

    def __str__(self) -> str:
        return str(self.value)
