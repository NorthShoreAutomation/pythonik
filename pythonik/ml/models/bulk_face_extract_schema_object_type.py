from enum import Enum


class BulkFaceExtractSchemaObjectType(str, Enum):
    ASSETS = "assets"
    COLLECTIONS = "collections"
    SAVED_SEARCHES = "saved_searches"

    def __str__(self) -> str:
        return str(self.value)
