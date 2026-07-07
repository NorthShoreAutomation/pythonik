from enum import Enum


class TransferActionSchemaType(str, Enum):
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
