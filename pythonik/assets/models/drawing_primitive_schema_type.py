from enum import Enum


class DrawingPrimitiveSchemaType(str, Enum):
    ARROW = "ARROW"
    ELLIPSE = "ELLIPSE"
    LINE = "LINE"
    PENCIL = "PENCIL"
    RECTANGLE = "RECTANGLE"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
