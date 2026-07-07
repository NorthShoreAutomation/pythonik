from enum import Enum


class EmbeddingByFaceSchemaType(str, Enum):
    AUGMENTED = "AUGMENTED"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
