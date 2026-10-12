from enum import Enum


class PortalBaseSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"

    def __str__(self) -> str:
        return str(self.value)
