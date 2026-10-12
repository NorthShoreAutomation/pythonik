from enum import Enum


class KeywordPredicateOp(str, Enum):
    ALL = "all"
    ANY_OF = "any_of"
    EQ = "eq"
    EXISTS = "exists"
    IN = "in"
    RANGE = "range"

    def __str__(self) -> str:
        return str(self.value)
