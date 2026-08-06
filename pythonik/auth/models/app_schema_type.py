from enum import Enum


class AppSchemaType(str, Enum):
    OAUTH = "OAUTH"
    PAT = "PAT"

    def __str__(self) -> str:
        return str(self.value)
