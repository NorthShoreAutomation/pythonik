from __future__ import annotations

from typing import Any, List, Optional, Dict

from pydantic import BaseModel

from pythonik.models.base import PaginatedResponse
from pythonik.models.files.file import File
from pythonik.models.files.format import Format
from pythonik.models.files.keyframe import Keyframe
from pythonik.models.files.proxy import Proxy


class Object(BaseModel):
    date_created: Optional[str] = ""
    date_modified: Optional[str] = ""
    description: Optional[str] = ""
    id: Optional[str] = ""
    metadata: Optional[Dict[str, Any]] = {}
    object_type: Optional[str] = ""
    title: Optional[str] = ""
    files: Optional[List[File]] = []
    proxies: Optional[List[Proxy]] = []
    keyframes: Optional[List[Keyframe]] = []
    formats: Optional[List[Format]] = []
    in_collections: Optional[List[str]] = []
    permissions: Optional[List[str]] = []
    external_id: Optional[str] = None
    external_link: Optional[str] = None


class SearchResponse(PaginatedResponse):
    facets: Optional[Dict[str, Any]] = {}
    objects: Optional[List[Object]] = []
