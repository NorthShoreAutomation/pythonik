from enum import Enum


class DashboardSchemaViewType(str, Enum):
    CARD = "card"
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
