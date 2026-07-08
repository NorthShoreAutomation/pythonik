from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_assets_latest_version_schema_object_type_type_1 import (
        GetAssetsLatestVersionSchemaObjectTypeType1,
    )


T = TypeVar("T", bound="GetAssetsLatestVersionSchema")


@_attrs_define
class GetAssetsLatestVersionSchema:
    """
    Attributes:
        object_ids (list[UUID]):
        include_in_progress (bool | None | Unset):  Default: False.
        object_type (GetAssetsLatestVersionSchemaObjectTypeType1 | None | Unset):
    """

    object_ids: list[UUID]
    include_in_progress: bool | None | Unset = False
    object_type: GetAssetsLatestVersionSchemaObjectTypeType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_assets_latest_version_schema_object_type_type_1 import (
            GetAssetsLatestVersionSchemaObjectTypeType1,
        )

        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        include_in_progress: bool | None | Unset
        if isinstance(self.include_in_progress, Unset):
            include_in_progress = UNSET
        else:
            include_in_progress = self.include_in_progress

        object_type: dict[str, Any] | None | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        elif isinstance(self.object_type, GetAssetsLatestVersionSchemaObjectTypeType1):
            object_type = self.object_type.to_dict()
        else:
            object_type = self.object_type

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
        from ..models.get_assets_latest_version_schema_object_type_type_1 import (
            GetAssetsLatestVersionSchemaObjectTypeType1,
        )

        d = dict(src_dict)
        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        def _parse_include_in_progress(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_in_progress = _parse_include_in_progress(
            d.pop("include_in_progress", UNSET)
        )

        def _parse_object_type(
            data: object,
        ) -> GetAssetsLatestVersionSchemaObjectTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_type_type_1 = (
                    GetAssetsLatestVersionSchemaObjectTypeType1.from_dict(data)
                )

                return object_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetAssetsLatestVersionSchemaObjectTypeType1 | None | Unset, data
            )

        object_type = _parse_object_type(d.pop("object_type", UNSET))

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
