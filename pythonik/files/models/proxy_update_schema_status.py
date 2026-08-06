from enum import Enum


class ProxyUpdateSchemaStatus(str, Enum):
    ARCHIVED = "ARCHIVED"
    AWAITED = "AWAITED"
    CLOSED = "CLOSED"
    DELETED = "DELETED"
    FAILED = "FAILED"
    GROWING = "GROWING"
    MISSING = "MISSING"
    OPEN = "OPEN"
    REDISCOVERED = "REDISCOVERED"

    def __str__(self) -> str:
        return str(self.value)
