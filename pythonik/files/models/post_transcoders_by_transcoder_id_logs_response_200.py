from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTranscodersByTranscoderIdLogsResponse200")


@_attrs_define
class PostTranscodersByTranscoderIdLogsResponse200:
    """
    Attributes:
        path (None | str | Unset):
        upload_url (None | str | Unset):
    """

    path: None | str | Unset = UNSET
    upload_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        upload_url: None | str | Unset
        if isinstance(self.upload_url, Unset):
            upload_url = UNSET
        else:
            upload_url = self.upload_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_upload_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_url = _parse_upload_url(d.pop("upload_url", UNSET))

        post_transcoders_by_transcoder_id_logs_response_200 = cls(
            path=path,
            upload_url=upload_url,
        )

        post_transcoders_by_transcoder_id_logs_response_200.additional_properties = d
        return post_transcoders_by_transcoder_id_logs_response_200

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
