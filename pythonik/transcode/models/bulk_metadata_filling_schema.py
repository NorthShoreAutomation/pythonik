from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_metadata_filling_schema_object_type import (
    BulkMetadataFillingSchemaObjectType,
)

T = TypeVar("T", bound="BulkMetadataFillingSchema")


@_attrs_define
class BulkMetadataFillingSchema:
    """
    Attributes:
        field_names (list[str]):
        object_ids (list[UUID]):
        object_type (BulkMetadataFillingSchemaObjectType):
        view_id (UUID):
    """

    field_names: list[str]
    object_ids: list[UUID]
    object_type: BulkMetadataFillingSchemaObjectType
    view_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_names = self.field_names

        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

        view_id = str(self.view_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_names": field_names,
                "object_ids": object_ids,
                "object_type": object_type,
                "view_id": view_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_names = cast(list[str], d.pop("field_names"))

        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        object_type = BulkMetadataFillingSchemaObjectType(d.pop("object_type"))

        view_id = UUID(d.pop("view_id"))

        bulk_metadata_filling_schema = cls(
            field_names=field_names,
            object_ids=object_ids,
            object_type=object_type,
            view_id=view_id,
        )

        bulk_metadata_filling_schema.additional_properties = d
        return bulk_metadata_filling_schema

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
