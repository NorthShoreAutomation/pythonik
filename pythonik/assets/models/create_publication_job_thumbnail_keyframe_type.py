from enum import Enum


class CreatePublicationJobThumbnailKeyframeType(str, Enum):
    KEYFRAME = "KEYFRAME"

    def __str__(self) -> str:
        return str(self.value)
