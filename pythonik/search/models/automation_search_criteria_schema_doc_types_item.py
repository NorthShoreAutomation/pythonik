from enum import Enum


class AutomationSearchCriteriaSchemaDocTypesItem(str, Enum):
    ASSETS = "assets"
    COLLECTIONS = "collections"
    SAVED_SEARCHES = "saved_searches"
    SAVED_SEARCH_GROUPS = "saved_search_groups"
    SEGMENTS = "segments"

    def __str__(self) -> str:
        return str(self.value)
