from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultipartUploadProxyCleanupSchema")


@_attrs_define
class MultipartUploadProxyCleanupSchema:
    """
    Attributes:
        abort_upload (bool | Unset):
        upload_id (str | Unset):
    """

    abort_upload: bool | Unset = UNSET
    upload_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abort_upload = self.abort_upload

        upload_id = self.upload_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abort_upload is not UNSET:
            field_dict["abort_upload"] = abort_upload
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abort_upload = d.pop("abort_upload", UNSET)

        upload_id = d.pop("upload_id", UNSET)

        multipart_upload_proxy_cleanup_schema = cls(
            abort_upload=abort_upload,
            upload_id=upload_id,
        )

        multipart_upload_proxy_cleanup_schema.additional_properties = d
        return multipart_upload_proxy_cleanup_schema

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
