# pythonik/models/metadata/fields.py
from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, HttpUrl


class IconikFieldType(str, Enum):
    """Iconik metadata field types as confirmed by API error messages.
    These are the exact values accepted by the Iconik API.
    """

    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"  # For Yes/No fields
    STRING = "string"  # General short text
    STRING_EXACT = "string_exact"  # Case-sensitive string matching
    TEXT = "text"  # Longer text (potentially multi-line in UI)
    DATE = "date"
    DATETIME = "datetime"  # For Date Time fields
    TAG_CLOUD = "tag_cloud"  # For free-form tag collections
    URL = "url"
    DROPDOWN = "drop_down"  # For fields with predefined options
    EMAIL = "email"


class FieldOption(BaseModel):
    """Represents an option for a metadata field (e.g., for dropdowns)."""

    label: Optional[str] = None
    value: Optional[str] = None


class _FieldConfigurable(BaseModel):
    """Base model for common configurable attributes of metadata fields."""

    label: Optional[str] = None
    field_type: Optional[IconikFieldType] = None
    description: Optional[str] = None
    options: Optional[List[FieldOption]] = None
    required: Optional[bool] = None
    auto_set: Optional[bool] = None
    hide_if_not_set: Optional[bool] = None
    is_block_field: Optional[bool] = None
    is_warning_field: Optional[bool] = None
    multi: Optional[bool] = None
    read_only: Optional[bool] = None
    representative: Optional[bool] = None
    sortable: Optional[bool] = None
    use_as_facet: Optional[bool] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    external_id: Optional[str] = None
    source_url: Optional[HttpUrl] = None


class FieldCreate(_FieldConfigurable):
    """Data Transfer Object for creating a new metadata field."""

    name: str
    label: str
    field_type: IconikFieldType


class FieldUpdate(_FieldConfigurable):
    """
    Data Transfer Object for updating an existing metadata field.
    All fields are optional to support partial updates.
    'name' is specified in the URL path for updates, not in the body.
    """

    pass


class Field(_FieldConfigurable):
    """Represents a metadata field as returned by the API."""

    id: str
    name: str
    label: str
    field_type: IconikFieldType

    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    mapped_field_name: Optional[str] = None


class FieldResponse(BaseModel):
    auto_set: Optional[bool] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    field_type: Optional[IconikFieldType] = None
    hide_if_not_set: Optional[bool] = None
    is_block_field: Optional[bool] = None
    is_warning_field: Optional[bool] = None
    label: Optional[str] = None
    mapped_field_name: Optional[str] = None
    max_value: Optional[float] = None
    min_value: Optional[float] = None
    multi: Optional[bool] = None
    name: Optional[str] = None
    options: Optional[List[FieldOption]] = None
    read_only: Optional[bool] = None
    representative: Optional[bool] = None
    required: Optional[bool] = None
    sortable: Optional[bool] = None
    source_url: Optional[HttpUrl] = None
    use_as_facet: Optional[bool] = None

    class Config:
        use_enum_values = True


class FieldListResponse(BaseModel):
    """Response model for a paginated list of metadata fields.

    This follows the standard pagination format used by the Iconik API.
    """

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: List[FieldResponse] = []
    page: Optional[int] = None
    pages: Optional[int] = None
    per_page: Optional[int] = None
    prev_url: Optional[str] = None
    total: Optional[int] = None

    class Config:
        use_enum_values = True
