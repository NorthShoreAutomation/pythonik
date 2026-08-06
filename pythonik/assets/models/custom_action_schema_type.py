from enum import Enum


class CustomActionSchemaType(str, Enum):
    OPEN = "OPEN"
    POST = "POST"
    PUBLISH = "PUBLISH"

    def __str__(self) -> str:
        return str(self.value)
