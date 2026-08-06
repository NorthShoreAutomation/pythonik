from enum import Enum


class RoleGroupSchemaGroupType(str, Enum):
    ROLE_GROUP = "ROLE_GROUP"
    TEAM = "TEAM"

    def __str__(self) -> str:
        return str(self.value)
