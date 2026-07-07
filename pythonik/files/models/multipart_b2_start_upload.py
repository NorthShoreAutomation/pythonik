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
        authorization_token (str | Unset):
        error (str | Unset):
        error_code (str | Unset):
        status (str | Unset):
        upload_file_id (None | str | Unset):
        upload_url (str | Unset):
    """

    authorization_token: str | Unset = UNSET
    error: str | Unset = UNSET
    error_code: str | Unset = UNSET
    status: str | Unset = UNSET
    upload_file_id: None | str | Unset = UNSET
    upload_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorization_token = self.authorization_token

        error = self.error

        error_code = self.error_code

        status = self.status

        upload_file_id: None | str | Unset
        if isinstance(self.upload_file_id, Unset):
            upload_file_id = UNSET
        else:
            upload_file_id = self.upload_file_id

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
        authorization_token = d.pop("authorization_token", UNSET)

        error = d.pop("error", UNSET)

        error_code = d.pop("error_code", UNSET)

        status = d.pop("status", UNSET)

        def _parse_upload_file_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_file_id = _parse_upload_file_id(d.pop("upload_file_id", UNSET))

        upload_url = d.pop("upload_url", UNSET)

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
