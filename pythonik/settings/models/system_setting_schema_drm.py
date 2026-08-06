from enum import Enum


class SystemSettingSchemaDrm(str, Enum):
    NONE = "none"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
