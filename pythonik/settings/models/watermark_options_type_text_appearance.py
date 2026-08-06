from enum import Enum


class WatermarkOptionsTypeTextAppearance(str, Enum):
    BOTTOM = "bottom"
    CENTER = "center"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
