from enum import Enum


class ObjectAddedToCollectionTriggerSchemaType(str, Enum):
    OBJECT_ADDED_TO_COLLECTION = "OBJECT_ADDED_TO_COLLECTION"

    def __str__(self) -> str:
        return str(self.value)
