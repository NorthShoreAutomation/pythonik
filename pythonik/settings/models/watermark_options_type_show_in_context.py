from enum import Enum


class WatermarkOptionsTypeShowInContext(str, Enum):
    PROXIES = "proxies"
    SHARES = "shares"

    def __str__(self) -> str:
        return str(self.value)
