from enum import Enum


class ShareCreateSchemaDrm(str, Enum):
    NONE = "none"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
