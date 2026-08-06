from enum import Enum


class PlaylistBaseSchemaStatus(str, Enum):
    HIDDEN = "HIDDEN"

    def __str__(self) -> str:
        return str(self.value)
