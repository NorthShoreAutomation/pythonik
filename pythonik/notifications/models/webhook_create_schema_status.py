from enum import Enum


class WebhookCreateSchemaStatus(str, Enum):
    DELETED = "DELETED"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    FAILING = "FAILING"

    def __str__(self) -> str:
        return str(self.value)
