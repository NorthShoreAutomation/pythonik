from enum import Enum


class AppCreateSchemaType(str, Enum):
    OAUTH = "OAUTH"
    PAT = "PAT"

    def __str__(self) -> str:
        return str(self.value)
