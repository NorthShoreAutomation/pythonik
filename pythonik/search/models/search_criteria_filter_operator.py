from enum import Enum


class SearchCriteriaFilterOperator(str, Enum):
    AND = "AND"
    NOT = "NOT"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
