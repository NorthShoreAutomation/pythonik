from enum import Enum


class CustomActionCreateSchemaType(str, Enum):
    OPEN = "OPEN"
    POST = "POST"
    PUBLISH = "PUBLISH"

    def __str__(self) -> str:
        return str(self.value)
