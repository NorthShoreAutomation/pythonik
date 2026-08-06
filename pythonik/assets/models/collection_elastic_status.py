from enum import Enum


class CollectionElasticStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    HIDDEN = "HIDDEN"

    def __str__(self) -> str:
        return str(self.value)
