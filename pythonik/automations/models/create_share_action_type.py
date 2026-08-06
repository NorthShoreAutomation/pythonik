from enum import Enum


class CreateShareActionType(str, Enum):
    CREATE_SHARE = "CREATE_SHARE"

    def __str__(self) -> str:
        return str(self.value)
