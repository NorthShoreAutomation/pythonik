from enum import Enum


class RequestOriginalActionType(str, Enum):
    REQUEST_ORIGINAL = "REQUEST_ORIGINAL"

    def __str__(self) -> str:
        return str(self.value)
