from enum import Enum


class EmbeddingByStatusSchemaStatus(str, Enum):
    NEW = "NEW"
    SYSTEM_CONFIRMED = "SYSTEM_CONFIRMED"
    UNCONFIRMED = "UNCONFIRMED"
    USER_CONFIRMED = "USER_CONFIRMED"

    def __str__(self) -> str:
        return str(self.value)
