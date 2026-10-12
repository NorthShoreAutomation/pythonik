from enum import Enum


class AIFeatureStateSchemaStatus(str, Enum):
    CONSENT_REQUIRED = "CONSENT_REQUIRED"
    CONSENT_STALE = "CONSENT_STALE"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    UNAVAILABLE = "UNAVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
