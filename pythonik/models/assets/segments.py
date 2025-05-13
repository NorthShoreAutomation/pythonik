from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel
from pythonik.models.base import UserInfo


class Point(BaseModel):
    x: Optional[int] = None
    y: Optional[int] = None


class Primitive(BaseModel):
    color: Optional[str] = ""
    points: List[Point] = []
    text: Optional[str] = ""
    type: Optional[str] = ""


class Drawing(BaseModel):
    primitives: List[Primitive] = []


class Word(BaseModel):
    end_ms: Optional[int] = None
    score: Optional[int] = None
    start_ms: Optional[int] = None
    value: Optional[str] = ""


class Transcription(BaseModel):
    speaker: Optional[int] = None
    words: List[Word] = []


class SegmentBody(BaseModel):
    drawing: Optional[Drawing] = None
    external_id: Optional[str] = ""
    keyframe_id: Optional[str] = ""
    metadata: Optional[Dict[str, Any]] = None
    metadata_view_id: Optional[str] = ""
    parent_id: Optional[str] = ""
    path: Optional[str] = ""
    segment_checked: Optional[bool] = None
    segment_color: Optional[str] = ""
    segment_text: Optional[str] = ""
    segment_track: Optional[str] = ""
    segment_type: Optional[str] = ""
    share_user_email: Optional[str] = ""
    status: Optional[str] = ""
    time_end_milliseconds: Optional[int] = None
    time_start_milliseconds: Optional[int] = None
    top_level: Optional[bool] = None
    transcription: Optional[Transcription] = None
    transcription_id: Optional[str] = ""
    user_id: Optional[str] = ""
    user_info: Optional[UserInfo] = None
    version_id: Optional[str] = ""


class SegmentResponse(SegmentBody):
    id: Optional[str] = ""


class BulkDeleteSegmentsBody(BaseModel):
    """Request body for bulk deleting segments."""
    segment_ids: Optional[List[str]] = None
    segment_type: Optional[str] = None
    version_id: Optional[str] = None
