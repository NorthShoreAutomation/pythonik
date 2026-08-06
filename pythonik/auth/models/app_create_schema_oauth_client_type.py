from enum import Enum


class AppCreateSchemaOauthClientType(str, Enum):
    CONFIDENTIAL = "confidential"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
