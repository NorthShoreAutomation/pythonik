from enum import Enum


class AIConsentSchemaStatus(str, Enum):
    DECLINED = "DECLINED"
    GRANTED = "GRANTED"
    REVOKED = "REVOKED"

    def __str__(self) -> str:
        return str(self.value)
