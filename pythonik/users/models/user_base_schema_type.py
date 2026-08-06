from enum import Enum


class UserBaseSchemaType(str, Enum):
    BROWSE_API_ONLY = "BROWSE_API_ONLY"
    BROWSE_ONLY = "BROWSE_ONLY"
    POWER = "POWER"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
