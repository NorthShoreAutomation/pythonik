from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataFillingSchema")


@_attrs_define
class MetadataFillingSchema:
    """
    Attributes:
        field_names (list[str]):
        view_id (UUID):
        auto_accept (bool | None | Unset):  Default: False.
        overwrite (bool | None | Unset):  Default: True.
    """

    field_names: list[str]
    view_id: UUID
    auto_accept: bool | None | Unset = False
    overwrite: bool | None | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_names = self.field_names

        view_id = str(self.view_id)

        auto_accept: bool | None | Unset
        if isinstance(self.auto_accept, Unset):
            auto_accept = UNSET
        else:
            auto_accept = self.auto_accept

        overwrite: bool | None | Unset
        if isinstance(self.overwrite, Unset):
            overwrite = UNSET
        else:
            overwrite = self.overwrite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_names": field_names,
                "view_id": view_id,
            }
        )
        if auto_accept is not UNSET:
            field_dict["auto_accept"] = auto_accept
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_names = cast(list[str], d.pop("field_names"))

        view_id = UUID(d.pop("view_id"))

        def _parse_auto_accept(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_accept = _parse_auto_accept(d.pop("auto_accept", UNSET))

        def _parse_overwrite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overwrite = _parse_overwrite(d.pop("overwrite", UNSET))

        metadata_filling_schema = cls(
            field_names=field_names,
            view_id=view_id,
            auto_accept=auto_accept,
            overwrite=overwrite,
        )

        metadata_filling_schema.additional_properties = d
        return metadata_filling_schema

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
