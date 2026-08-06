from enum import Enum


class UpdateACLActionType(str, Enum):
    UPDATE_ACL = "UPDATE_ACL"

    def __str__(self) -> str:
        return str(self.value)
