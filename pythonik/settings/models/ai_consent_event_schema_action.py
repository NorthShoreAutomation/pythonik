from enum import Enum


class AIConsentEventSchemaAction(str, Enum):
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    LEGACY_IMPORTED = "LEGACY_IMPORTED"
    NOTICE_ELAPSED = "NOTICE_ELAPSED"
    REVOKED = "REVOKED"
    REVOKED_BY_MASTER_SWITCH = "REVOKED_BY_MASTER_SWITCH"

    def __str__(self) -> str:
        return str(self.value)
