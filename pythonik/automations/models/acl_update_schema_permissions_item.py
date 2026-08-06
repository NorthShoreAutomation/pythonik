from enum import Enum


class ACLUpdateSchemaPermissionsItem(str, Enum):
    CHANGE_ACL = "change-acl"
    DELETE = "delete"
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
