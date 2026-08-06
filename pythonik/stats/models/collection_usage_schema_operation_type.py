from enum import Enum


class CollectionUsageSchemaOperationType(str, Enum):
    CREATE = "CREATE"
    DELETE = "DELETE"
    RENAME = "RENAME"
    VIEW = "VIEW"

    def __str__(self) -> str:
        return str(self.value)
