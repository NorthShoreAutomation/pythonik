from enum import Enum


class CollectionSchemaCustomOrderStatus(str, Enum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    ENABLING = "ENABLING"

    def __str__(self) -> str:
        return str(self.value)
