from enum import Enum


class BulkFilesetArchiveSchemaObjectType(str, Enum):
    ASSETS = "assets"
    COLLECTIONS = "collections"
    PLAYLISTS = "playlists"
    SAVED_SEARCHES = "saved_searches"

    def __str__(self) -> str:
        return str(self.value)
