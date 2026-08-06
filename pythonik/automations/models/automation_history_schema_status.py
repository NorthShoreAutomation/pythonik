from enum import Enum


class AutomationHistorySchemaStatus(str, Enum):
    FAILED = "FAILED"
    SUCCEED = "SUCCEED"

    def __str__(self) -> str:
        return str(self.value)
