from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiPartUploadURLSchema")


@_attrs_define
class MultiPartUploadURLSchema:
    """
    Attributes:
        delete_url (str | Unset):
        download_url (str | Unset):
        key (str | Unset):
        number (int | Unset):
        url (str | Unset):
    """

    delete_url: str | Unset = UNSET
    download_url: str | Unset = UNSET
    key: str | Unset = UNSET
    number: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_url = self.delete_url

        download_url = self.download_url

        key = self.key

        number = self.number

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_url is not UNSET:
            field_dict["delete_url"] = delete_url
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if key is not UNSET:
            field_dict["key"] = key
        if number is not UNSET:
            field_dict["number"] = number
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_url = d.pop("delete_url", UNSET)

        download_url = d.pop("download_url", UNSET)

        key = d.pop("key", UNSET)

        number = d.pop("number", UNSET)

        url = d.pop("url", UNSET)

        multi_part_upload_url_schema = cls(
            delete_url=delete_url,
            download_url=download_url,
            key=key,
            number=number,
            url=url,
        )

        multi_part_upload_url_schema.additional_properties = d
        return multi_part_upload_url_schema

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
