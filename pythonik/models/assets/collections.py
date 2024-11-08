from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, field_serializer, Field

from pythonik.models.base import Status, PaginatedResponse
from pythonik.models.files.keyframe import Keyframe


class CustomOrderStatus(str, Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ENABLING = "ENABLING"


class Collection(BaseModel):
    category: str | None = ""
    created_by_user: str = ""
    custom_keyframe: str | None = ""
    custom_order_status: CustomOrderStatus = ""
    custom_poster: str | None = ""
    date_created: datetime | None = Field(default_factory=datetime.now)
    date_deleted: datetime | None = Field(default_factory=datetime.now)
    date_modified: datetime | None = Field(default_factory=datetime.now)
    # date_created: str | None = ""
    # date_deleted: str | None = ""
    # date_modified: str | None = ""
    deleted_by_user: str | None = ""
    external_id: str | None = ""
    favoured: bool = False
    id: str = ""
    in_collections: List[str] = []
    is_root: bool = False
    keyframe_asset_ids: List[str] = []
    keyframes: List[Keyframe] = []
    metadata: dict = {}
    object_type: str = ""
    parent_id: str | None = ""
    parents: List[str] = []
    permissions: List[str] = []
    position: int = -0
    status: Status = ""
    storage_id: str | None = ""
    title: str

    @field_serializer("date_created", "date_deleted", "date_modified")
    @classmethod
    def date_to_string(cls, dt: datetime) -> str:
        if dt:
            return dt.isoformat()
        return None


class CollectionContentInfo(BaseModel):
    assets_count: int
    collections_count: int


class CollectionContents(PaginatedResponse):
    pass
