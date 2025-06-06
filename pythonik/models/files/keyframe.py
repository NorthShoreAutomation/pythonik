from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from pythonik.models.base import PaginatedResponse


class GCSKeyframeUploadResponse(BaseModel):
    upload_id: Optional[str] = ""
    location: Optional[str] = ""


class Resolution(BaseModel):
    height: Optional[int] = None
    width: Optional[int] = None

    # For Pydantic v2
    @classmethod
    def model_validate(cls, obj, *args, **kwargs):
        if isinstance(obj, dict):
            return super().model_validate(obj, *args, **kwargs)
        return obj


class TimeBase(BaseModel):
    denominator: Optional[int] = None
    numerator: Optional[int] = None


class TimeCode(BaseModel):
    frames_number: Optional[int] = None
    is_drop_frame: Optional[bool] = None
    time_base: Optional[TimeBase] = {}

    # For Pydantic v2
    @classmethod
    def model_validate(cls, obj, *args, **kwargs):
        if isinstance(obj, dict):
            return super().model_validate(obj, *args, **kwargs)
        return obj


class Keyframe(BaseModel):
    asset_id: Optional[str] = ""
    collection_id: Optional[str] = ""
    filename: Optional[str] = ""
    format: Optional[str] = ""
    id: Optional[str] = ""
    is_custom_keyframe: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = ""
    resolution: Optional[Union[Resolution, Dict[str, Any]]] = {}
    rotation: Optional[int] = None
    size: Optional[int] = None
    status: Optional[str] = ""
    storage_id: Optional[str] = ""
    storage_method: Optional[str] = ""
    time_code: Optional[Union[Resolution, Dict[str, Any]]] = {}
    type: Optional[str] = ""
    upload_credentials: Optional[Dict[str, Any]] = {}
    upload_method: Optional[str] = ""
    upload_url: Optional[str] = ""
    url: Optional[str] = ""
    version_id: Optional[str] = ""


class Keyframes(PaginatedResponse):
    objects: Optional[List[Keyframe]] = []
