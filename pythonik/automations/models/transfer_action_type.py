from enum import Enum


class TransferActionType(str, Enum):
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
