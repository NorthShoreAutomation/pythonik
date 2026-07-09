from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jobs_bulk_params_schema_type_type_0_item import (
    JobsBulkParamsSchemaTypeType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsBulkParamsSchema")


@_attrs_define
class JobsBulkParamsSchema:
    """
    Attributes:
        field_exists (list[str] | None | Unset):
        field_missing (list[str] | None | Unset):
        created_by (list[UUID] | None | Unset):
        date_created (None | str | Unset):
        date_modified (None | str | Unset):
        ids (list[UUID] | None | Unset):
        metadata_automation_id (None | str | Unset):
        object_id (None | Unset | UUID):
        parent_id (None | Unset | UUID):
        query (None | str | Unset):
        type_ (list[JobsBulkParamsSchemaTypeType0Item] | None | Unset):
    """

    field_exists: list[str] | None | Unset = UNSET
    field_missing: list[str] | None | Unset = UNSET
    created_by: list[UUID] | None | Unset = UNSET
    date_created: None | str | Unset = UNSET
    date_modified: None | str | Unset = UNSET
    ids: list[UUID] | None | Unset = UNSET
    metadata_automation_id: None | str | Unset = UNSET
    object_id: None | Unset | UUID = UNSET
    parent_id: None | Unset | UUID = UNSET
    query: None | str | Unset = UNSET
    type_: list[JobsBulkParamsSchemaTypeType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_exists: list[str] | None | Unset
        if isinstance(self.field_exists, Unset):
            field_exists = UNSET
        elif isinstance(self.field_exists, list):
            field_exists = self.field_exists

        else:
            field_exists = self.field_exists

        field_missing: list[str] | None | Unset
        if isinstance(self.field_missing, Unset):
            field_missing = UNSET
        elif isinstance(self.field_missing, list):
            field_missing = self.field_missing

        else:
            field_missing = self.field_missing

        created_by: list[str] | None | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, list):
            created_by = []
            for created_by_type_0_item_data in self.created_by:
                created_by_type_0_item = str(created_by_type_0_item_data)
                created_by.append(created_by_type_0_item)

        else:
            created_by = self.created_by

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = self.date_modified

        ids: list[str] | None | Unset
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = []
            for ids_type_0_item_data in self.ids:
                ids_type_0_item = str(ids_type_0_item_data)
                ids.append(ids_type_0_item)

        else:
            ids = self.ids

        metadata_automation_id: None | str | Unset
        if isinstance(self.metadata_automation_id, Unset):
            metadata_automation_id = UNSET
        else:
            metadata_automation_id = self.metadata_automation_id

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        elif isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        type_: list[str] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, list):
            type_ = []
            for type_type_0_item_data in self.type_:
                type_type_0_item = type_type_0_item_data.value
                type_.append(type_type_0_item)

        else:
            type_ = self.type_

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
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_field_exists(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_exists_type_0 = cast(list[str], data)

                return field_exists_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        field_exists = _parse_field_exists(d.pop("_exists_", UNSET))

        def _parse_field_missing(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_missing_type_0 = cast(list[str], data)

                return field_missing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        field_missing = _parse_field_missing(d.pop("_missing_", UNSET))

        def _parse_created_by(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                created_by_type_0 = []
                _created_by_type_0 = data
                for created_by_type_0_item_data in _created_by_type_0:
                    created_by_type_0_item = UUID(created_by_type_0_item_data)

                    created_by_type_0.append(created_by_type_0_item)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_date_created(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = []
                _ids_type_0 = data
                for ids_type_0_item_data in _ids_type_0:
                    ids_type_0_item = UUID(ids_type_0_item_data)

                    ids_type_0.append(ids_type_0_item)

                return ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        ids = _parse_ids(d.pop("ids", UNSET))

        def _parse_metadata_automation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_automation_id = _parse_metadata_automation_id(
            d.pop("metadata.automation_id", UNSET)
        )

        def _parse_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_id_type_0 = UUID(data)

                return object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_type_(
            data: object,
        ) -> list[JobsBulkParamsSchemaTypeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                type_type_0 = []
                _type_type_0 = data
                for type_type_0_item_data in _type_type_0:
                    type_type_0_item = JobsBulkParamsSchemaTypeType0Item(
                        type_type_0_item_data
                    )

                    type_type_0.append(type_type_0_item)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobsBulkParamsSchemaTypeType0Item] | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        jobs_bulk_params_schema = cls(
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
            type_=type_,
        )

        jobs_bulk_params_schema.additional_properties = d
        return jobs_bulk_params_schema

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
