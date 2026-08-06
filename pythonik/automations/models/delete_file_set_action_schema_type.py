from enum import Enum


class DeleteFileSetActionSchemaType(str, Enum):
    DELETE_FILE_SET = "DELETE_FILE_SET"

    def __str__(self) -> str:
        return str(self.value)
