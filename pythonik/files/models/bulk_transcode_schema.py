from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_transcode_schema_object_type import BulkTranscodeSchemaObjectType
from ..models.bulk_transcode_schema_preferred_storage_method import (
    BulkTranscodeSchemaPreferredStorageMethod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkTranscodeSchema")


@_attrs_define
class BulkTranscodeSchema:
    """
    Attributes:
        object_ids (list[UUID]):
        object_type (BulkTranscodeSchemaObjectType):
        format_name (str | Unset):  Default: 'ORIGINAL'.
        prefer_any_cloud (bool | Unset):
        preferred_storage_id (UUID | Unset):
        preferred_storage_method (BulkTranscodeSchemaPreferredStorageMethod | Unset):
        priority (int | Unset):
    """

    object_ids: list[UUID]
    object_type: BulkTranscodeSchemaObjectType
    format_name: str | Unset = "ORIGINAL"
    prefer_any_cloud: bool | Unset = UNSET
    preferred_storage_id: UUID | Unset = UNSET
    preferred_storage_method: BulkTranscodeSchemaPreferredStorageMethod | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

        format_name = self.format_name

        prefer_any_cloud = self.prefer_any_cloud

        preferred_storage_id: str | Unset = UNSET
        if not isinstance(self.preferred_storage_id, Unset):
            preferred_storage_id = str(self.preferred_storage_id)

        preferred_storage_method: str | Unset = UNSET
        if not isinstance(self.preferred_storage_method, Unset):
            preferred_storage_method = self.preferred_storage_method.value

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids": object_ids,
                "object_type": object_type,
            }
        )
        if format_name is not UNSET:
            field_dict["format_name"] = format_name
        if prefer_any_cloud is not UNSET:
            field_dict["prefer_any_cloud"] = prefer_any_cloud
        if preferred_storage_id is not UNSET:
            field_dict["preferred_storage_id"] = preferred_storage_id
        if preferred_storage_method is not UNSET:
            field_dict["preferred_storage_method"] = preferred_storage_method
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        object_type = BulkTranscodeSchemaObjectType(d.pop("object_type"))

        format_name = d.pop("format_name", UNSET)

        prefer_any_cloud = d.pop("prefer_any_cloud", UNSET)

        _preferred_storage_id = d.pop("preferred_storage_id", UNSET)
        preferred_storage_id: UUID | Unset
        if isinstance(_preferred_storage_id, Unset):
            preferred_storage_id = UNSET
        else:
            preferred_storage_id = UUID(_preferred_storage_id)

        _preferred_storage_method = d.pop("preferred_storage_method", UNSET)
        preferred_storage_method: BulkTranscodeSchemaPreferredStorageMethod | Unset
        if isinstance(_preferred_storage_method, Unset):
            preferred_storage_method = UNSET
        else:
            preferred_storage_method = BulkTranscodeSchemaPreferredStorageMethod(
                _preferred_storage_method
            )

        priority = d.pop("priority", UNSET)

        bulk_transcode_schema = cls(
            object_ids=object_ids,
            object_type=object_type,
            format_name=format_name,
            prefer_any_cloud=prefer_any_cloud,
            preferred_storage_id=preferred_storage_id,
            preferred_storage_method=preferred_storage_method,
            priority=priority,
        )

        bulk_transcode_schema.additional_properties = d
        return bulk_transcode_schema

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
