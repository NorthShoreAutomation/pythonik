from enum import Enum


class SegmentAttributeMatchSchemaOperator(str, Enum):
    EQ = "eq"
    GT = "gt"
    LT = "lt"

    def __str__(self) -> str:
        return str(self.value)
