from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_assets_latest_version_schema_object_type import (
    GetAssetsLatestVersionSchemaObjectType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAssetsLatestVersionSchema")


@_attrs_define
class GetAssetsLatestVersionSchema:
    """
    Attributes:
        object_ids (list[UUID]):
        include_in_progress (bool | Unset):  Default: False.
        object_type (GetAssetsLatestVersionSchemaObjectType | Unset):  Default:
            GetAssetsLatestVersionSchemaObjectType.ASSETS.
    """

    object_ids: list[UUID]
    include_in_progress: bool | Unset = False
    object_type: GetAssetsLatestVersionSchemaObjectType | Unset = (
        GetAssetsLatestVersionSchemaObjectType.ASSETS
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        include_in_progress = self.include_in_progress

        object_type: str | Unset = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids": object_ids,
            }
        )
        if include_in_progress is not UNSET:
            field_dict["include_in_progress"] = include_in_progress
        if object_type is not UNSET:
            field_dict["object_type"] = object_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        include_in_progress = d.pop("include_in_progress", UNSET)

        _object_type = d.pop("object_type", UNSET)
        object_type: GetAssetsLatestVersionSchemaObjectType | Unset
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = GetAssetsLatestVersionSchemaObjectType(_object_type)

        get_assets_latest_version_schema = cls(
            object_ids=object_ids,
            include_in_progress=include_in_progress,
            object_type=object_type,
        )

        get_assets_latest_version_schema.additional_properties = d
        return get_assets_latest_version_schema

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
