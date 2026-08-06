from enum import Enum


class AnalyzeActionSchemaType(str, Enum):
    ANALYZE = "ANALYZE"

    def __str__(self) -> str:
        return str(self.value)
