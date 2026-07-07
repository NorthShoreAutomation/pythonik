from enum import Enum


class SystemDomainBasicSchemaType(str, Enum):
    CUSTOMER = "CUSTOMER"
    INTERNAL = "INTERNAL"
    PARTNER = "PARTNER"
    TRIAL = "TRIAL"

    def __str__(self) -> str:
        return str(self.value)
