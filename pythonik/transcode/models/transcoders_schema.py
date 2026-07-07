from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcoders_schema_settings import TranscodersSchemaSettings


T = TypeVar("T", bound="TranscodersSchema")


@_attrs_define
class TranscodersSchema:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        settings (TranscodersSchemaSettings | Unset):
        type_ (str | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    settings: TranscodersSchemaSettings | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if settings is not UNSET:
            field_dict["settings"] = settings
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcoders_schema_settings import TranscodersSchemaSettings

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: TranscodersSchemaSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = TranscodersSchemaSettings.from_dict(_settings)

        type_ = d.pop("type", UNSET)

        transcoders_schema = cls(
            id=id,
            name=name,
            settings=settings,
            type_=type_,
        )

        transcoders_schema.additional_properties = d
        return transcoders_schema

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
