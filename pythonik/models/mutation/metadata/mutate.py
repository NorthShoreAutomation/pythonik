from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, RootModel


class FieldValue(BaseModel):
    value: Any


class FieldValues(BaseModel):
    field_values: Optional[List[FieldValue]]


class MetadataValues(RootModel):
    root: Dict[str, FieldValues]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class UpdateMetadata(BaseModel):
    metadata_values: Optional[MetadataValues] = {}


class UpdateMetadataResponse(BaseModel):
    date_created: Optional[str] = ""
    date_modified: Optional[str] = ""
    metadata_values: Optional[Dict[str, Any]] = {}
    object_id: Optional[str] = ""
    object_type: Optional[str] = ""
    version_id: Optional[str] = ""
