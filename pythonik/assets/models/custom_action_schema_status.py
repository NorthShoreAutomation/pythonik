from enum import Enum


class CustomActionSchemaStatus(str, Enum):
    FAILING = "FAILING"
    HEALTHY = "HEALTHY"

    def __str__(self) -> str:
        return str(self.value)
