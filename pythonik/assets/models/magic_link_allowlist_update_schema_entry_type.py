from enum import Enum


class MagicLinkAllowlistUpdateSchemaEntryType(str, Enum):
    DOMAIN = "domain"
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
