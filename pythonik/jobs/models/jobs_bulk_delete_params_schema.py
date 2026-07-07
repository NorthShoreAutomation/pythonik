from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jobs_bulk_delete_params_schema_status_item import (
    JobsBulkDeleteParamsSchemaStatusItem,
)
from ..models.jobs_bulk_delete_params_schema_type_item import (
    JobsBulkDeleteParamsSchemaTypeItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsBulkDeleteParamsSchema")


@_attrs_define
class JobsBulkDeleteParamsSchema:
    """
    Attributes:
        field_exists (list[str] | Unset):
        field_missing (list[str] | Unset):
        created_by (list[UUID] | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        ids (list[UUID] | Unset):
        metadata_automation_id (str | Unset):
        object_id (UUID | Unset):
        parent_id (UUID | Unset):
        query (str | Unset):
        status (list[JobsBulkDeleteParamsSchemaStatusItem] | Unset):
        type_ (list[JobsBulkDeleteParamsSchemaTypeItem] | Unset):
    """

    field_exists: list[str] | Unset = UNSET
    field_missing: list[str] | Unset = UNSET
    created_by: list[UUID] | Unset = UNSET
    date_created: str | Unset = UNSET
    date_modified: str | Unset = UNSET
    ids: list[UUID] | Unset = UNSET
    metadata_automation_id: str | Unset = UNSET
    object_id: UUID | Unset = UNSET
    parent_id: UUID | Unset = UNSET
    query: str | Unset = UNSET
    status: list[JobsBulkDeleteParamsSchemaStatusItem] | Unset = UNSET
    type_: list[JobsBulkDeleteParamsSchemaTypeItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_exists: list[str] | Unset = UNSET
        if not isinstance(self.field_exists, Unset):
            field_exists = self.field_exists

        field_missing: list[str] | Unset = UNSET
        if not isinstance(self.field_missing, Unset):
            field_missing = self.field_missing

        created_by: list[str] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = []
            for created_by_item_data in self.created_by:
                created_by_item = str(created_by_item_data)
                created_by.append(created_by_item)

        date_created = self.date_created

        date_modified = self.date_modified

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = []
            for ids_item_data in self.ids:
                ids_item = str(ids_item_data)
                ids.append(ids_item)

        metadata_automation_id = self.metadata_automation_id

        object_id: str | Unset = UNSET
        if not isinstance(self.object_id, Unset):
            object_id = str(self.object_id)

        parent_id: str | Unset = UNSET
        if not isinstance(self.parent_id, Unset):
            parent_id = str(self.parent_id)

        query = self.query

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value
                status.append(status_item)

        type_: list[str] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = []
            for type_item_data in self.type_:
                type_item = type_item_data.value
                type_.append(type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_exists is not UNSET:
            field_dict["_exists_"] = field_exists
        if field_missing is not UNSET:
            field_dict["_missing_"] = field_missing
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if ids is not UNSET:
            field_dict["ids"] = ids
        if metadata_automation_id is not UNSET:
            field_dict["metadata.automation_id"] = metadata_automation_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if query is not UNSET:
            field_dict["query"] = query
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_exists = cast(list[str], d.pop("_exists_", UNSET))

        field_missing = cast(list[str], d.pop("_missing_", UNSET))

        _created_by = d.pop("created_by", UNSET)
        created_by: list[UUID] | Unset = UNSET
        if _created_by is not UNSET:
            created_by = []
            for created_by_item_data in _created_by:
                created_by_item = UUID(created_by_item_data)

                created_by.append(created_by_item)

        date_created = d.pop("date_created", UNSET)

        date_modified = d.pop("date_modified", UNSET)

        _ids = d.pop("ids", UNSET)
        ids: list[UUID] | Unset = UNSET
        if _ids is not UNSET:
            ids = []
            for ids_item_data in _ids:
                ids_item = UUID(ids_item_data)

                ids.append(ids_item)

        metadata_automation_id = d.pop("metadata.automation_id", UNSET)

        _object_id = d.pop("object_id", UNSET)
        object_id: UUID | Unset
        if isinstance(_object_id, Unset):
            object_id = UNSET
        else:
            object_id = UUID(_object_id)

        _parent_id = d.pop("parent_id", UNSET)
        parent_id: UUID | Unset
        if isinstance(_parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = UUID(_parent_id)

        query = d.pop("query", UNSET)

        _status = d.pop("status", UNSET)
        status: list[JobsBulkDeleteParamsSchemaStatusItem] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = JobsBulkDeleteParamsSchemaStatusItem(status_item_data)

                status.append(status_item)

        _type_ = d.pop("type", UNSET)
        type_: list[JobsBulkDeleteParamsSchemaTypeItem] | Unset = UNSET
        if _type_ is not UNSET:
            type_ = []
            for type_item_data in _type_:
                type_item = JobsBulkDeleteParamsSchemaTypeItem(type_item_data)

                type_.append(type_item)

        jobs_bulk_delete_params_schema = cls(
            field_exists=field_exists,
            field_missing=field_missing,
            created_by=created_by,
            date_created=date_created,
            date_modified=date_modified,
            ids=ids,
            metadata_automation_id=metadata_automation_id,
            object_id=object_id,
            parent_id=parent_id,
            query=query,
            status=status,
            type_=type_,
        )

        jobs_bulk_delete_params_schema.additional_properties = d
        return jobs_bulk_delete_params_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
