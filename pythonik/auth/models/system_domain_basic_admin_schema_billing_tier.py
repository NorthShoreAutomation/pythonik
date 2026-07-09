from enum import Enum


class SystemDomainBasicAdminSchemaBillingTier(str, Enum):
    ENTERPRISE = "ENTERPRISE"
    ENTERPRISE_LEGACY_2025 = "ENTERPRISE_LEGACY_2025"
    PAYGO = "PAYGO"
    PRO = "PRO"
    PRO_LEGACY_2025 = "PRO_LEGACY_2025"

    def __str__(self) -> str:
        return str(self.value)
