from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, field_serializer, Field

from pythonik.models.base import ArchiveStatus, Status, UserInfo


class BulkDeleteObjectType(str, Enum):
    ASSETS = "assets"
    COLLECTIONS = "collections"
    SAVE_SEARCHES = "saved_searches"


class AnalyzeStatus(str, Enum):
    N_A = "N/A"
    REQUESTED = "REQUESTED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    DONE = "DONE"


class AssetType(str, Enum):
    ASSET = "ASSET"
    SEQUENCE = "SEQUENCE"
    NLE_PROJECT = "NLE_PROJECT"
    PLACEHOLDER = "PLACEHOLDER"
    CUSTOM = "CUSTOM"
    LINK = "LINK"
    SUBCLIP = "SUBCLIP"


class CreatedByUserInfo(UserInfo):
    pass


class DeletedByUserInfo(UserInfo):
    pass


class UpdatedByUserInfo(UserInfo):
    pass


class Version(BaseModel):
    analyze_status: Optional[str] = ""
    archive_status: Optional[str] = ""
    created_by_user: Optional[str] = ""
    created_by_user_info: Optional[CreatedByUserInfo] = None
    date_created: Optional[str] = ""
    id: Optional[str] = ""
    is_online: Optional[bool] = None
    status: Optional[str] = ""
    transcribe_status: Optional[str] = ""


class Asset(BaseModel):
    analyze_status: Optional[AnalyzeStatus] = None
    archive_status: Optional[ArchiveStatus] = None
    category: Optional[str] = ""
    created_by_user: Optional[str] = ""
    created_by_user_info: Optional[CreatedByUserInfo] = None
    custom_keyframe: Optional[str] = ""
    custom_poster: Optional[str] = ""
    date_created: Optional[str] = ""
    date_deleted: Optional[str] = ""
    date_imported: Optional[str] = ""
    date_modified: Optional[str] = ""
    deleted_by_user: Optional[str] = ""
    deleted_by_user_info: Optional[DeletedByUserInfo] = None
    external_id: Optional[str] = ""
    external_link: Optional[str] = ""
    favoured: Optional[bool] = None
    id: Optional[str] = ""
    in_collections: Optional[List[str]] = []
    is_blocked: Optional[bool] = None
    is_online: Optional[bool] = None
    site_name: Optional[str] = ""
    status: Optional[Status] = Status.ACTIVE
    title: Optional[str] = ""
    type: Optional[AssetType] = AssetType.ASSET
    updated_by_user: Optional[str] = ""
    updated_by_user_info: Optional[UpdatedByUserInfo] = None
    versions: Optional[List[Version]] = []
    warning: Optional[str] = ""


class AssetCreate(BaseModel):
    title: str
    date_created: datetime = Field(default_factory=datetime.now)
    date_deleted: datetime = Field(default_factory=datetime.now)
    date_modified: datetime = Field(default_factory=datetime.now)
    type: Optional[AssetType] = None
    status: Optional[str] = None
    is_online: Optional[bool] = None
    is_blocked: Optional[bool] = None
    has_unconfirmed_persons: Optional[bool] = None
    analyze_status: Optional[AnalyzeStatus] = None
    archive_status: Optional[ArchiveStatus] = None
    category: Optional[str] = None
    custom_keyframe: Optional[str] = None
    custom_poster: Optional[str] = None
    external_id: Optional[str] = None
    external_link: Optional[str] = None
    favoured: Optional[bool] = None
    face_recognition_status: Optional[AnalyzeStatus] = None
    site_name: Optional[str] = None
    time_end_milliseconds: Optional[int] = None
    time_start_milliseconds: Optional[int] = None
    warning: Optional[str] = None

    @field_serializer("date_created", "date_deleted", "date_modified")
    @classmethod
    def date_to_string(cls, dt: datetime) -> str:
        return dt.isoformat()


class BulkDelete(BaseModel):
    object_ids: List[str]
    content_only: bool = True
    object_type: BulkDeleteObjectType
