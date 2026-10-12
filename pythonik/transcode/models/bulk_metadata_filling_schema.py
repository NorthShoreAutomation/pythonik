from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_metadata_filling_schema_object_type import (
    BulkMetadataFillingSchemaObjectType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkMetadataFillingSchema")


@_attrs_define
class BulkMetadataFillingSchema:
    """
    Attributes:
        object_ids (list[UUID]):
        object_type (BulkMetadataFillingSchemaObjectType):
        view_id (UUID):
        auto_accept (bool | None | Unset):  Default: False.
        field_names (list[str] | None | Unset):
        overwrite (bool | None | Unset):  Default: True.
    """

    object_ids: list[UUID]
    object_type: BulkMetadataFillingSchemaObjectType
    view_id: UUID
    auto_accept: bool | None | Unset = False
    field_names: list[str] | None | Unset = UNSET
    overwrite: bool | None | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

        view_id = str(self.view_id)

        auto_accept: bool | None | Unset
        if isinstance(self.auto_accept, Unset):
            auto_accept = UNSET
        else:
            auto_accept = self.auto_accept

        field_names: list[str] | None | Unset
        if isinstance(self.field_names, Unset):
            field_names = UNSET
        elif isinstance(self.field_names, list):
            field_names = self.field_names

        else:
            field_names = self.field_names

        overwrite: bool | None | Unset
        if isinstance(self.overwrite, Unset):
            overwrite = UNSET
        else:
            overwrite = self.overwrite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids": object_ids,
                "object_type": object_type,
                "view_id": view_id,
            }
        )
        if auto_accept is not UNSET:
            field_dict["auto_accept"] = auto_accept
        if field_names is not UNSET:
            field_dict["field_names"] = field_names
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        object_type = BulkMetadataFillingSchemaObjectType(d.pop("object_type"))

        view_id = UUID(d.pop("view_id"))

        def _parse_auto_accept(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_accept = _parse_auto_accept(d.pop("auto_accept", UNSET))

        def _parse_field_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_names_type_0 = cast(list[str], data)

                return field_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        field_names = _parse_field_names(d.pop("field_names", UNSET))

        def _parse_overwrite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overwrite = _parse_overwrite(d.pop("overwrite", UNSET))

        bulk_metadata_filling_schema = cls(
            object_ids=object_ids,
            object_type=object_type,
            view_id=view_id,
            auto_accept=auto_accept,
            field_names=field_names,
            overwrite=overwrite,
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
