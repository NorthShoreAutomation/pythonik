from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
        cors (bool | None | Unset):
        cors_error (None | str | Unset):
        delete_access (bool | None | Unset):
        delete_access_error (None | str | Unset):
        error_message (None | str | Unset):
        read_access (bool | None | Unset):
        read_access_error (None | str | Unset):
        write_access (bool | None | Unset):
        write_access_error (None | str | Unset):
    """

    cors: bool | None | Unset = UNSET
    cors_error: None | str | Unset = UNSET
    delete_access: bool | None | Unset = UNSET
    delete_access_error: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    read_access: bool | None | Unset = UNSET
    read_access_error: None | str | Unset = UNSET
    write_access: bool | None | Unset = UNSET
    write_access_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cors: bool | None | Unset
        if isinstance(self.cors, Unset):
            cors = UNSET
        else:
            cors = self.cors

        cors_error: None | str | Unset
        if isinstance(self.cors_error, Unset):
            cors_error = UNSET
        else:
            cors_error = self.cors_error

        delete_access: bool | None | Unset
        if isinstance(self.delete_access, Unset):
            delete_access = UNSET
        else:
            delete_access = self.delete_access

        delete_access_error: None | str | Unset
        if isinstance(self.delete_access_error, Unset):
            delete_access_error = UNSET
        else:
            delete_access_error = self.delete_access_error

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        read_access: bool | None | Unset
        if isinstance(self.read_access, Unset):
            read_access = UNSET
        else:
            read_access = self.read_access

        read_access_error: None | str | Unset
        if isinstance(self.read_access_error, Unset):
            read_access_error = UNSET
        else:
            read_access_error = self.read_access_error

        write_access: bool | None | Unset
        if isinstance(self.write_access, Unset):
            write_access = UNSET
        else:
            write_access = self.write_access

        write_access_error: None | str | Unset
        if isinstance(self.write_access_error, Unset):
            write_access_error = UNSET
        else:
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

        def _parse_cors(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cors = _parse_cors(d.pop("cors", UNSET))

        def _parse_cors_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cors_error = _parse_cors_error(d.pop("cors_error", UNSET))

        def _parse_delete_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_access = _parse_delete_access(d.pop("delete_access", UNSET))

        def _parse_delete_access_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delete_access_error = _parse_delete_access_error(
            d.pop("delete_access_error", UNSET)
        )

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_read_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_access = _parse_read_access(d.pop("read_access", UNSET))

        def _parse_read_access_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        read_access_error = _parse_read_access_error(d.pop("read_access_error", UNSET))

        def _parse_write_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        write_access = _parse_write_access(d.pop("write_access", UNSET))

        def _parse_write_access_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        write_access_error = _parse_write_access_error(
            d.pop("write_access_error", UNSET)
        )

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
