from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultipartB2StartUpload")


@_attrs_define
class MultipartB2StartUpload:
    """
    Attributes:
        authorization_token (None | str | Unset):
        error (None | str | Unset):
        error_code (None | str | Unset):
        status (None | str | Unset):
        upload_file_id (None | str | Unset):
        upload_url (None | str | Unset):
    """

    authorization_token: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    error_code: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    upload_file_id: None | str | Unset = UNSET
    upload_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorization_token: None | str | Unset
        if isinstance(self.authorization_token, Unset):
            authorization_token = UNSET
        else:
            authorization_token = self.authorization_token

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        upload_file_id: None | str | Unset
        if isinstance(self.upload_file_id, Unset):
            upload_file_id = UNSET
        else:
            upload_file_id = self.upload_file_id

        upload_url: None | str | Unset
        if isinstance(self.upload_url, Unset):
            upload_url = UNSET
        else:
            upload_url = self.upload_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_token is not UNSET:
            field_dict["authorization_token"] = authorization_token
        if error is not UNSET:
            field_dict["error"] = error
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if status is not UNSET:
            field_dict["status"] = status
        if upload_file_id is not UNSET:
            field_dict["upload_file_id"] = upload_file_id
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_authorization_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorization_token = _parse_authorization_token(
            d.pop("authorization_token", UNSET)
        )

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("error_code", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_upload_file_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_file_id = _parse_upload_file_id(d.pop("upload_file_id", UNSET))

        def _parse_upload_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_url = _parse_upload_url(d.pop("upload_url", UNSET))

        multipart_b2_start_upload = cls(
            authorization_token=authorization_token,
            error=error,
            error_code=error_code,
            status=status,
            upload_file_id=upload_file_id,
            upload_url=upload_url,
        )

        multipart_b2_start_upload.additional_properties = d
        return multipart_b2_start_upload

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
