from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from pythonik.models.base import FileType, PaginatedResponse


class UploadUrlResponse(BaseModel):
    delete_url: str = ""
    download_url: str = ""
    key: str = ""
    number: int = None
    url: str = ""


class S3MultipartUploadResponse(BaseModel):
    objects: List[UploadUrlResponse]


class FileStatus(str, Enum):
    OPEN = "OPEN"
    GROWING = "GROWING"
    AWAITED = "AWAITED"
    CLOSED = "CLOSED"
    FAILED = "FAILED"
    ARCHIVED = "ARCHIVED"
    MISSING = "MISSING"
    REDISCOVERED = "REDISCOVERED"
    DELETED = "DELETED"


class File(BaseModel):
    asset_id: Optional[str] = ""
    checksum: Optional[str] = ""
    date_created: Optional[str] = ""
    date_modified: Optional[str] = ""
    directory_path: Optional[str] = None
    file_date_created: Optional[str] = ""
    file_date_modified: Optional[str] = ""
    file_set_id: Optional[str] = ""
    file_set_status: Optional[str] = ""
    format_id: Optional[str] = ""
    format_status: Optional[str] = ""
    id: Optional[str] = ""
    multipart_upload_url: Optional[str] = ""
    name: Optional[str] = ""
    original_name: Optional[str] = ""
    parent_id: Optional[str] = ""
    size: Optional[int] = ""
    status: Optional[FileStatus] = ""
    storage_id: Optional[str] = ""
    storage_method: Optional[str] = ""
    type: Optional[FileType] = ""
    upload_credentials: Optional[Dict[str, Any]] = {}
    upload_filename: Optional[str] = ""
    upload_method: Optional[str] = ""
    upload_url: Optional[str] = ""
    url: Optional[str] = ""
    user_id: Optional[str] = ""
    version_id: Optional[str] = ""
    system_domain_id: Optional[str] = ""


class FileSetsFilesResponse(BaseModel):
    per_page: int = 1000
    objects: List[File] = []


class FileCreate(File):
    file_set_id: str
    format_id: str
    storage_id: str
    name: str
    original_name: str
    size: int
    type: str
    directory_path: str = ""
    status: str


class FileSet(BaseModel):
    id: Optional[str] = ""
    asset_id: Optional[str] = ""
    archive_file_set_id: Optional[str] = ""
    format_id: Optional[str] = ""
    name: Optional[str] = ""
    original_storage_id: Optional[str] = ""
    storage_id: Optional[str] = ""
    version_id: Optional[str] = ""
    base_dir: str = ""
    component_ids: list = []
    date_created: Optional[str] = ""
    date_deleted: Optional[str] = ""
    date_modified: Optional[str] = ""
    deleted_by_user: Optional[str] = ""
    file_count: Optional[int] = 0
    status: Optional[str] = ""
    is_archive: Optional[bool] = False


class FileSetCreate(FileSet):
    format_id: str
    name: str
    storage_id: str
    base_dir: str = ""
    component_ids: list = []


class Files(PaginatedResponse):
    objects: Optional[List[File]] = []


class FileSets(PaginatedResponse):
    objects: Optional[List[FileSet]] = []
