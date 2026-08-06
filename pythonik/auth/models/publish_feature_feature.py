from enum import Enum


class PublishFeatureFeature(str, Enum):
    WM_PUBLISH_PANEL = "WM_PUBLISH_PANEL"

    def __str__(self) -> str:
        return str(self.value)
