from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, RootModel


class FieldValue(BaseModel):
    value: Any


class FieldValues(BaseModel):
    field_values: Optional[List[FieldValue]] = []


class MetadataValues(RootModel):
    root: Dict[str, FieldValues]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class ViewOption(BaseModel):
    """Option for a view field."""

    label: str
    value: str


class ViewField(BaseModel):
    """Field configuration for a view."""

    name: str
    label: Optional[str] = None
    auto_set: Optional[bool] = False
    date_created: Optional[str] = None
    date_modified: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    field_type: Optional[str] = None
    hide_if_not_set: Optional[bool] = False
    is_block_field: Optional[bool] = False
    is_warning_field: Optional[bool] = False
    mapped_field_name: Optional[str] = None
    max_value: Optional[int] = None
    min_value: Optional[int] = None
    multi: Optional[bool] = False
    options: Optional[List[ViewOption]] = None
    read_only: Optional[bool] = False
    representative: Optional[bool] = False
    required: Optional[bool] = False
    sortable: Optional[bool] = False
    source_url: Optional[str] = None
    use_as_facet: Optional[bool] = False


class CreateViewRequest(BaseModel):
    """Request model for creating a view."""

    name: str
    description: Optional[str] = None
    view_fields: List[ViewField]


class UpdateViewRequest(BaseModel):
    """Request model for updating a view."""

    name: Optional[str] = None
    description: Optional[str] = None
    view_fields: Optional[List[ViewField]] = None


class View(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    date_created: str
    date_modified: str
    view_fields: List[ViewField]


class ViewMetadata(BaseModel):
    date_created: Optional[str] = ""
    date_modified: Optional[str] = ""
    metadata_values: Optional[MetadataValues] = MetadataValues({})
    object_id: Optional[str] = ""
    object_type: Optional[str] = ""
    version_id: Optional[str] = ""
