from enum import Enum


class BulkAddToFavoritesSchemaObjectType(str, Enum):
    ASSETS = "assets"
    COLLECTIONS = "collections"

    def __str__(self) -> str:
        return str(self.value)
