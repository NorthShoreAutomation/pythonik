from enum import Enum


class CreatePublicationJobThumbnailKeyframeSchemaType(str, Enum):
    KEYFRAME = "KEYFRAME"

    def __str__(self) -> str:
        return str(self.value)
