from enum import Enum


class PriceSchemaCurrency(str, Enum):
    EUR = "EUR"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
