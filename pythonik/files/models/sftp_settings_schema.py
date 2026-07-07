from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SftpSettingsSchema")


@_attrs_define
class SftpSettingsSchema:
    """
    Attributes:
        address (str):
        password (str):
        user (str):
        delete (bool | Unset):
        is_system (bool | Unset):
        read (bool | Unset):
        scan (bool | Unset):
        write (bool | Unset):
    """

    address: str
    password: str
    user: str
    delete: bool | Unset = UNSET
    is_system: bool | Unset = UNSET
    read: bool | Unset = UNSET
    scan: bool | Unset = UNSET
    write: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        password = self.password

        user = self.user

        delete = self.delete

        is_system = self.is_system

        read = self.read

        scan = self.scan

        write = self.write

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "password": password,
                "user": user,
            }
        )
        if delete is not UNSET:
            field_dict["delete"] = delete
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if read is not UNSET:
            field_dict["read"] = read
        if scan is not UNSET:
            field_dict["scan"] = scan
        if write is not UNSET:
            field_dict["write"] = write

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        password = d.pop("password")

        user = d.pop("user")

        delete = d.pop("delete", UNSET)

        is_system = d.pop("is_system", UNSET)

        read = d.pop("read", UNSET)

        scan = d.pop("scan", UNSET)

        write = d.pop("write", UNSET)

        sftp_settings_schema = cls(
            address=address,
            password=password,
            user=user,
            delete=delete,
            is_system=is_system,
            read=read,
            scan=scan,
            write=write,
        )

        sftp_settings_schema.additional_properties = d
        return sftp_settings_schema

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
