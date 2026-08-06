from enum import Enum


class GroupWithRolesElasticSchemaGroupType(str, Enum):
    ROLE_GROUP = "ROLE_GROUP"
    TEAM = "TEAM"

    def __str__(self) -> str:
        return str(self.value)
