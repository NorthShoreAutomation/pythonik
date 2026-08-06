from enum import Enum


class ComponentSchemaType(str, Enum):
    AUDIO = "AUDIO"
    EXIF = "EXIF"
    GENERAL = "GENERAL"
    IMAGE = "IMAGE"
    IPTC = "IPTC"
    MANIFEST = "MANIFEST"
    NON_MEDIA = "NON_MEDIA"
    OTHER = "OTHER"
    TEXT = "TEXT"
    VIDEO = "VIDEO"
    XMP = "XMP"

    def __str__(self) -> str:
        return str(self.value)
