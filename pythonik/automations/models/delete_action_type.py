from enum import Enum


class DeleteActionType(str, Enum):
    DELETE_ASSET = "DELETE_ASSET"

    def __str__(self) -> str:
        return str(self.value)
