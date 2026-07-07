from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomSettingsSchema")


@_attrs_define
class CustomSettingsSchema:
    """
    Attributes:
        custom (str | Unset):
        delete (bool | Unset):
        is_system (bool | Unset):
        read (bool | Unset):
        write (bool | Unset):
    """

    custom: str | Unset = UNSET
    delete: bool | Unset = UNSET
    is_system: bool | Unset = UNSET
    read: bool | Unset = UNSET
    write: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom = self.custom

        delete = self.delete

        is_system = self.is_system

        read = self.read

        write = self.write

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom is not UNSET:
            field_dict["custom"] = custom
        if delete is not UNSET:
            field_dict["delete"] = delete
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if read is not UNSET:
            field_dict["read"] = read
        if write is not UNSET:
            field_dict["write"] = write

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom = d.pop("custom", UNSET)

        delete = d.pop("delete", UNSET)

        is_system = d.pop("is_system", UNSET)

        read = d.pop("read", UNSET)

        write = d.pop("write", UNSET)

        custom_settings_schema = cls(
            custom=custom,
            delete=delete,
            is_system=is_system,
            read=read,
            write=write,
        )

        custom_settings_schema.additional_properties = d
        return custom_settings_schema

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
