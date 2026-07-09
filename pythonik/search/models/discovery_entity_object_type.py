from enum import Enum


class DiscoveryEntityObjectType(str, Enum):
    COLLECTION = "COLLECTION"
    SAVED_SEARCH = "SAVED_SEARCH"

    def __str__(self) -> str:
        return str(self.value)
