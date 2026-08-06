from enum import Enum


class KeyframeSchemaType(str, Enum):
    KEYFRAME = "KEYFRAME"
    KEYFRAME_MAP = "KEYFRAME_MAP"
    POSTER = "POSTER"

    def __str__(self) -> str:
        return str(self.value)
