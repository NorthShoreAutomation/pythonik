from enum import Enum


class FileCreateSchemaTemplateEngine(str, Enum):
    JINJA2 = "JINJA2"
    SIMPLE = "SIMPLE"

    def __str__(self) -> str:
        return str(self.value)
