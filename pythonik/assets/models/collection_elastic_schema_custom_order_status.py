from enum import Enum


class CollectionElasticSchemaCustomOrderStatus(str, Enum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    ENABLING = "ENABLING"

    def __str__(self) -> str:
        return str(self.value)
