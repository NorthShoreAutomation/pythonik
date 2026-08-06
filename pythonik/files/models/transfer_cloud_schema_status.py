from enum import Enum


class TransferCloudSchemaStatus(str, Enum):
    D = "D"
    E = "E"
    Q = "Q"
    U = "U"

    def __str__(self) -> str:
        return str(self.value)
