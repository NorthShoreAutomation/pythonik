from __future__ import annotations

from typing import Any, List, Optional, Dict

from pydantic import BaseModel, Field

from pythonik.models.base import PaginatedResponse
from pythonik.models.files.file import File
from pythonik.models.files.format import Format
from pythonik.models.files.keyframe import Keyframe
from pythonik.models.files.proxy import Proxy


class Highlight(BaseModel):
    """Represents highlighted search results."""

    title: Optional[List[str]] = []
    # Add other highlight fields as needed


# class FormatMetadata(BaseModel):
#     """Metadata specific to a format."""

#     format: Optional[str] = None
#     # Add other format metadata fields as needed


# class Format(BaseModel):
#     """Represents a file format."""

#     archive_status: Optional[str] = None
#     date_created: Optional[str] = None
#     date_deleted: Optional[str] = None
#     date_modified: Optional[str] = None
#     deleted_by_user: Optional[str] = None
#     id: Optional[str] = None
#     is_online: Optional[bool] = None
#     metadata: Optional[List[FormatMetadata]] = None
#     name: Optional[str] = None
#     size: Optional[int] = None
#     status: Optional[str] = None
#     storage_methods: Optional[List[str]] = None
#     user_id: Optional[str] = None


class Version(BaseModel):
    """Represents a version of an asset."""

    analyze_status: Optional[str] = None
    archive_status: Optional[str] = None
    created_by_user: Optional[str] = None
    date_created: Optional[str] = None
    face_recognition_status: Optional[str] = None
    has_unconfirmed_persons: Optional[bool] = None
    id: Optional[str] = None
    is_online: Optional[bool] = None
    person_ids: Optional[List[str]] = []
    status: Optional[str] = None
    transcribe_status: Optional[str] = None
    transcribed_languages: Optional[List[str]] = []


class Object(BaseModel):
    """Represents an object in the search response."""

    # Base fields from original model
    date_created: Optional[str] = None
    date_modified: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = {}
    object_type: Optional[str] = None
    title: Optional[str] = None
    files: Optional[List[File]] = []
    proxies: Optional[List[Proxy]] = []
    keyframes: Optional[List[Keyframe]] = []

    # Additional fields from example response
    highlight: Optional[Highlight] = Field(None, alias="_highlight")
    sort: Optional[List[Any]] = Field(None, alias="_sort")
    analyze_status: Optional[str] = None
    ancestor_collections: Optional[List[str]] = []
    archive_status: Optional[str] = None
    category: Optional[str] = None
    created_by_share: Optional[str] = None
    created_by_share_user: Optional[str] = None
    created_by_user: Optional[str] = None
    created_by_user_info: Optional[Any] = None
    custom_keyframe: Optional[str] = None
    custom_poster: Optional[str] = None
    date_deleted: Optional[str] = None
    date_imported: Optional[str] = None
    date_viewed: Optional[str] = None
    deleted_by_user: Optional[str] = None
    external_id: Optional[str] = None
    external_link: Optional[str] = None
    face_recognition_status: Optional[str] = None
    file_names: Optional[List[str]] = []
    format: Optional[str] = None
    formats: Optional[List[Format]] = []
    has_unconfirmed_persons: Optional[bool] = None
    in_collections: Optional[List[str]] = []
    is_blocked: Optional[bool] = None
    is_online: Optional[bool] = None
    last_archive_restore_date: Optional[str] = None
    media_type: Optional[str] = None
    original_asset_id: Optional[str] = None
    original_segment_id: Optional[str] = None
    original_version_id: Optional[str] = None
    permissions: Optional[List[str]] = []
    person_ids: Optional[List[str]] = []
    position: Optional[int] = None
    site_name: Optional[str] = None
    status: Optional[str] = None
    system_domain_id: Optional[str] = None
    system_name: Optional[str] = None
    time_end_milliseconds: Optional[int] = None
    time_start_milliseconds: Optional[int] = None
    transcribe_status: Optional[str] = None
    transcribed_languages: Optional[List[str]] = []
    type: Optional[str] = None
    updated_by_user: Optional[str] = None
    versions: Optional[List[Version]] = []
    versions_number: Optional[int] = None
    warning: Optional[str] = None


class SearchResponse(PaginatedResponse):
    """Represents the complete search response."""

    facets: Optional[Dict[str, Any]] = {}
    objects: Optional[List[Object]] = []
