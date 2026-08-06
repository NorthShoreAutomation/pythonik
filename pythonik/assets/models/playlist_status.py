from enum import Enum


class PlaylistStatus(str, Enum):
    HIDDEN = "HIDDEN"

    def __str__(self) -> str:
        return str(self.value)
