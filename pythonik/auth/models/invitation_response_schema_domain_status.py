from enum import Enum


class InvitationResponseSchemaDomainStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DEACTIVATED = "DEACTIVATED"
    FROZEN = "FROZEN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
