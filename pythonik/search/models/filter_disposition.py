from enum import Enum


class FilterDisposition(str, Enum):
    MANDATORY = "mandatory"
    RELAXABLE = "relaxable"

    def __str__(self) -> str:
        return str(self.value)
