from enum import Enum


class WebhookInternalSchemaStatus(str, Enum):
    DELETED = "DELETED"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    FAILING = "FAILING"

    def __str__(self) -> str:
        return str(self.value)
