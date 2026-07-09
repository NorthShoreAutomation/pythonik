from enum import Enum


class CreatePublicationJobActionSchemaType(str, Enum):
    CREATE_PUBLICATION_JOB = "CREATE_PUBLICATION_JOB"

    def __str__(self) -> str:
        return str(self.value)
