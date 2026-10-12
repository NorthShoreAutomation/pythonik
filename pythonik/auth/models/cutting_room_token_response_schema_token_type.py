from enum import Enum


class CuttingRoomTokenResponseSchemaTokenType(str, Enum):
    BEARER = "Bearer"

    def __str__(self) -> str:
        return str(self.value)
