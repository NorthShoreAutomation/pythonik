from __future__ import annotations

from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel


class Response(BaseModel):
    # response: Type[requests.Response]
    response: Any
    data: Any
    # data: Optional[BaseModel] = None


class Status(str, Enum):
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
