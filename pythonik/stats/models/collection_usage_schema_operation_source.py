from enum import Enum


class CollectionUsageSchemaOperationSource(str, Enum):
    COLLECTION = "COLLECTION"
    NOTIFICATION = "NOTIFICATION"
    SEARCH = "SEARCH"

    def __str__(self) -> str:
        return str(self.value)
