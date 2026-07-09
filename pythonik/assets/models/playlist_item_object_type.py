from enum import Enum


class PlaylistItemObjectType(str, Enum):
    ASSETS = "assets"
    SEQUENCES = "sequences"

    def __str__(self) -> str:
        return str(self.value)
