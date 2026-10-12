from enum import Enum


class VideoSourceMode(str, Enum):
    AS_IS = "as-is"

    def __str__(self) -> str:
        return str(self.value)
