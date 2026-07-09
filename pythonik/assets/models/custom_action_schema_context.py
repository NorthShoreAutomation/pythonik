from enum import Enum


class CustomActionSchemaContext(str, Enum):
    ASSET = "ASSET"
    ASSET_SUBCLIP = "ASSET_SUBCLIP"
    BULK = "BULK"
    COLLECTION = "COLLECTION"
    NONE = "NONE"
    PLAYLIST = "PLAYLIST"
    SAVED_SEARCH = "SAVED_SEARCH"
    SHARED_ASSET = "SHARED_ASSET"
    SHARED_COLLECTION = "SHARED_COLLECTION"
    SHARED_PLAYLIST = "SHARED_PLAYLIST"

    def __str__(self) -> str:
        return str(self.value)
