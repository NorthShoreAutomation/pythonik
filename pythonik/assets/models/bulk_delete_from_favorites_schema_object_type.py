from enum import Enum


class BulkDeleteFromFavoritesSchemaObjectType(str, Enum):
    ASSETS = "assets"
    COLLECTIONS = "collections"

    def __str__(self) -> str:
        return str(self.value)
