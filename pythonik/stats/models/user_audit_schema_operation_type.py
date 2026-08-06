from enum import Enum


class UserAuditSchemaOperationType(str, Enum):
    DELETE = "DELETE"
    GET = "GET"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"
    POST = "POST"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
