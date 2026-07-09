from enum import Enum


class ProxyFileSchemaStatus(str, Enum):
    CLOSED = "CLOSED"
    FAILED = "FAILED"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
