from enum import Enum


class DrawingPrimitiveType(str, Enum):
    ARROW = "ARROW"
    ELLIPSE = "ELLIPSE"
    LINE = "LINE"
    PENCIL = "PENCIL"
    RECTANGLE = "RECTANGLE"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
