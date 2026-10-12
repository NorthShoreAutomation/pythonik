from enum import Enum


class AIConsentSchemaOrigin(str, Enum):
    ADMIN_ACCEPTED = "ADMIN_ACCEPTED"
    LEGACY_BETA_AGREEMENT = "LEGACY_BETA_AGREEMENT"
    LEGACY_UI_CONSENT = "LEGACY_UI_CONSENT"
    NOTICE_ELAPSED = "NOTICE_ELAPSED"

    def __str__(self) -> str:
        return str(self.value)
