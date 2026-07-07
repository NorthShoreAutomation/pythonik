from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HttpSettingsSchema")


@_attrs_define
class HttpSettingsSchema:
    """
    Attributes:
        address (str):
        auto (bool | Unset):
        delete (bool | Unset):
        is_system (bool | Unset):
        read (bool | Unset):
        scan (bool | Unset):
    """

    address: str
    auto: bool | Unset = UNSET
    delete: bool | Unset = UNSET
    is_system: bool | Unset = UNSET
    read: bool | Unset = UNSET
    scan: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        auto = self.auto

        delete = self.delete

        is_system = self.is_system

        read = self.read

        scan = self.scan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
            }
        )
        if auto is not UNSET:
            field_dict["auto"] = auto
        if delete is not UNSET:
            field_dict["delete"] = delete
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if read is not UNSET:
            field_dict["read"] = read
        if scan is not UNSET:
            field_dict["scan"] = scan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        auto = d.pop("auto", UNSET)

        delete = d.pop("delete", UNSET)

        is_system = d.pop("is_system", UNSET)

        read = d.pop("read", UNSET)

        scan = d.pop("scan", UNSET)

        http_settings_schema = cls(
            address=address,
            auto=auto,
            delete=delete,
            is_system=is_system,
            read=read,
            scan=scan,
        )

        http_settings_schema.additional_properties = d
        return http_settings_schema

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
