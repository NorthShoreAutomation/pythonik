from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStoragesVerificationsPermissionsResponse200")


@_attrs_define
class PostStoragesVerificationsPermissionsResponse200:
    """
    Example:
        {'cors': True, 'delete_access': True, 'read_access': True, 'write_access': False, 'write_access_error': 'ERROR:
            no access'}

    Attributes:
        cors (bool | Unset):
        cors_error (str | Unset):
        delete_access (bool | Unset):
        delete_access_error (str | Unset):
        error_message (str | Unset):
        read_access (bool | Unset):
        read_access_error (str | Unset):
        write_access (bool | Unset):
        write_access_error (str | Unset):
    """

    cors: bool | Unset = UNSET
    cors_error: str | Unset = UNSET
    delete_access: bool | Unset = UNSET
    delete_access_error: str | Unset = UNSET
    error_message: str | Unset = UNSET
    read_access: bool | Unset = UNSET
    read_access_error: str | Unset = UNSET
    write_access: bool | Unset = UNSET
    write_access_error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cors = self.cors

        cors_error = self.cors_error

        delete_access = self.delete_access

        delete_access_error = self.delete_access_error

        error_message = self.error_message

        read_access = self.read_access

        read_access_error = self.read_access_error

        write_access = self.write_access

        write_access_error = self.write_access_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cors is not UNSET:
            field_dict["cors"] = cors
        if cors_error is not UNSET:
            field_dict["cors_error"] = cors_error
        if delete_access is not UNSET:
            field_dict["delete_access"] = delete_access
        if delete_access_error is not UNSET:
            field_dict["delete_access_error"] = delete_access_error
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if read_access is not UNSET:
            field_dict["read_access"] = read_access
        if read_access_error is not UNSET:
            field_dict["read_access_error"] = read_access_error
        if write_access is not UNSET:
            field_dict["write_access"] = write_access
        if write_access_error is not UNSET:
            field_dict["write_access_error"] = write_access_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cors = d.pop("cors", UNSET)

        cors_error = d.pop("cors_error", UNSET)

        delete_access = d.pop("delete_access", UNSET)

        delete_access_error = d.pop("delete_access_error", UNSET)

        error_message = d.pop("error_message", UNSET)

        read_access = d.pop("read_access", UNSET)

        read_access_error = d.pop("read_access_error", UNSET)

        write_access = d.pop("write_access", UNSET)

        write_access_error = d.pop("write_access_error", UNSET)

        post_storages_verifications_permissions_response_200 = cls(
            cors=cors,
            cors_error=cors_error,
            delete_access=delete_access,
            delete_access_error=delete_access_error,
            error_message=error_message,
            read_access=read_access,
            read_access_error=read_access_error,
            write_access=write_access,
            write_access_error=write_access_error,
        )

        post_storages_verifications_permissions_response_200.additional_properties = d
        return post_storages_verifications_permissions_response_200

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
