from enum import Enum


class KeyframeCreateSchemaType(str, Enum):
    KEYFRAME = "KEYFRAME"
    KEYFRAME_MAP = "KEYFRAME_MAP"
    POSTER = "POSTER"

    def __str__(self) -> str:
        return str(self.value)
