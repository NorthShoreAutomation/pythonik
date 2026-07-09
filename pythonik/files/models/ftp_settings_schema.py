from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FtpSettingsSchema")


@_attrs_define
class FtpSettingsSchema:
    """
    Attributes:
        address (str):
        password (str):
        user (str):
        delete (bool | None | Unset):
        is_system (bool | None | Unset):
        read (bool | None | Unset):
        scan (bool | None | Unset):
        write (bool | None | Unset):
    """

    address: str
    password: str
    user: str
    delete: bool | None | Unset = UNSET
    is_system: bool | None | Unset = UNSET
    read: bool | None | Unset = UNSET
    scan: bool | None | Unset = UNSET
    write: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        password = self.password

        user = self.user

        delete: bool | None | Unset
        if isinstance(self.delete, Unset):
            delete = UNSET
        else:
            delete = self.delete

        is_system: bool | None | Unset
        if isinstance(self.is_system, Unset):
            is_system = UNSET
        else:
            is_system = self.is_system

        read: bool | None | Unset
        if isinstance(self.read, Unset):
            read = UNSET
        else:
            read = self.read

        scan: bool | None | Unset
        if isinstance(self.scan, Unset):
            scan = UNSET
        else:
            scan = self.scan

        write: bool | None | Unset
        if isinstance(self.write, Unset):
            write = UNSET
        else:
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

        def _parse_delete(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete = _parse_delete(d.pop("delete", UNSET))

        def _parse_is_system(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_system = _parse_is_system(d.pop("is_system", UNSET))

        def _parse_read(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read = _parse_read(d.pop("read", UNSET))

        def _parse_scan(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        scan = _parse_scan(d.pop("scan", UNSET))

        def _parse_write(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        write = _parse_write(d.pop("write", UNSET))

        ftp_settings_schema = cls(
            address=address,
            password=password,
            user=user,
            delete=delete,
            is_system=is_system,
            read=read,
            scan=scan,
            write=write,
        )

        ftp_settings_schema.additional_properties = d
        return ftp_settings_schema

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
