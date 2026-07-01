from __future__ import annotations

from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel


class Response(BaseModel):
    # response: Type[requests.Response]
    response: Any
    data: Any
    # data: Optional[BaseModel] = None

class ObjectType(str, Enum):
    ASSETS = "assets"
    COLLECTIONS = "collections"

class Status(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    ACTIVE = "ACTIVE"
    HIDDEN = "HIDDEN"
    DELETED = "DELETED"


class ArchiveStatus(str, Enum):
    NOT_ARCHIVED = "NOT_ARCHIVED"
    ARCHIVING = "ARCHIVING"
    FAILED_TO_ARCHIVE = "FAILED_TO_ARCHIVE"
    ARCHIVED = "ARCHIVED"


class FileType(str, Enum):
    FILE = "FILE"
    DIRECTORY = "DIRECTORY"
    SYMLINK = "SYMLINK"


class StorageMethod(str, Enum):
    S3 = "S3"
    GCS = "GCS"


class HistoryOperationType(str, Enum):
    """Known asset history operation types.

    This enum is provided for convenience and discoverability. The Iconik API
    may add new operation types over time, so ``create_history_entity`` also
    accepts arbitrary strings rather than restricting callers to these values.
    """

    EXPORT = "EXPORT"
    TRANSCODE = "TRANSCODE"
    ANALYZE = "ANALYZE"
    ADD_FORMAT = "ADD_FORMAT"
    DELETE_FORMAT = "DELETE_FORMAT"
    RESTORE_FORMAT = "RESTORE_FORMAT"
    DELETE_FILESET = "DELETE_FILESET"
    DELETE_FILE = "DELETE_FILE"
    RESTORE_FILESET = "RESTORE_FILESET"
    MODIFY_FILESET = "MODIFY_FILESET"
    APPROVE = "APPROVE"
    REJECT = "REJECT"
    DOWNLOAD = "DOWNLOAD"
    METADATA = "METADATA"
    CUSTOM = "CUSTOM"
    TRANSCRIPTION = "TRANSCRIPTION"
    VERSION_CREATE = "VERSION_CREATE"
    VERSION_DELETE = "VERSION_DELETE"
    VERSION_UPDATE = "VERSION_UPDATE"
    VERSION_PROMOTE = "VERSION_PROMOTE"
    RESTORE = "RESTORE"
    RESTORE_FROM_GLACIER = "RESTORE_FROM_GLACIER"
    ARCHIVE = "ARCHIVE"
    RESTORE_ARCHIVE = "RESTORE_ARCHIVE"
    DELETE = "DELETE"
    TRANSFER = "TRANSFER"
    UNLINK_SUBCLIP = "UNLINK_SUBCLIP"
    FACE_RECOGNITION = "FACE_RECOGNITION"


class PaginatedResponse(BaseModel):
    first_url: Optional[str] = ""
    last_url: Optional[str] = ""
    next_url: Optional[str] = ""
    objects: Optional[Any] = None
    page: Optional[int] = None
    pages: Optional[int] = None
    per_page: Optional[int] = None
    prev_url: Optional[str] = ""
    scroll_id: Optional[str] = ""
    total: Optional[int] = None


class UserInfo(BaseModel):
    email: Optional[str] = ""
    first_name: Optional[str] = ""
    id: Optional[str] = ""
    last_name: Optional[str] = ""
    photo: Optional[str] = ""
    photo_big: Optional[str] = ""
    photo_small: Optional[str] = ""
