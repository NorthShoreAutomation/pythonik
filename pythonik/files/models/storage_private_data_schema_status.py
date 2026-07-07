from enum import Enum


class StoragePrivateDataSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    FAILING = "FAILING"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
