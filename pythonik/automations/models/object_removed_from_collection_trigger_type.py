from enum import Enum


class ObjectRemovedFromCollectionTriggerType(str, Enum):
    OBJECT_REMOVED_FROM_COLLECTION = "OBJECT_REMOVED_FROM_COLLECTION"

    def __str__(self) -> str:
        return str(self.value)
