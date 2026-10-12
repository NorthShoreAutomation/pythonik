from enum import Enum


class SourceState(str, Enum):
    ERROR = "error"
    OK = "ok"
    PARTIAL = "partial"
    TIMEOUT = "timeout"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
