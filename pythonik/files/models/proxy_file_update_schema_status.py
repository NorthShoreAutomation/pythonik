from enum import Enum


class ProxyFileUpdateSchemaStatus(str, Enum):
    CLOSED = "CLOSED"
    FAILED = "FAILED"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
