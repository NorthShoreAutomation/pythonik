from enum import Enum


class AddToCollectionActionSchemaType(str, Enum):
    ADD_TO_COLLECTION = "ADD_TO_COLLECTION"

    def __str__(self) -> str:
        return str(self.value)
