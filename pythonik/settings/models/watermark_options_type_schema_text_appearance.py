from enum import Enum


class WatermarkOptionsTypeSchemaTextAppearance(str, Enum):
    BOTTOM = "bottom"
    CENTER = "center"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
