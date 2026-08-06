from enum import Enum


class JobsDashboardWidgetType(str, Enum):
    JOBS_LIST = "JOBS_LIST"
    JOBS_STATS_LIST = "JOBS_STATS_LIST"

    def __str__(self) -> str:
        return str(self.value)
