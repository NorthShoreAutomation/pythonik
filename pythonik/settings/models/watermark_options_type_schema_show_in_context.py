from enum import Enum


class WatermarkOptionsTypeSchemaShowInContext(str, Enum):
    PROXIES = "proxies"
    SHARES = "shares"

    def __str__(self) -> str:
        return str(self.value)
