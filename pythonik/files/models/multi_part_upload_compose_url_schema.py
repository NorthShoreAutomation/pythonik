from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiPartUploadComposeURLSchema")


@_attrs_define
class MultiPartUploadComposeURLSchema:
    """
    Attributes:
        compose_url (None | str | Unset):
        delete_url (None | str | Unset):
        key (None | str | Unset):
        url (None | str | Unset):
    """

    compose_url: None | str | Unset = UNSET
    delete_url: None | str | Unset = UNSET
    key: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compose_url: None | str | Unset
        if isinstance(self.compose_url, Unset):
            compose_url = UNSET
        else:
            compose_url = self.compose_url

        delete_url: None | str | Unset
        if isinstance(self.delete_url, Unset):
            delete_url = UNSET
        else:
            delete_url = self.delete_url

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compose_url is not UNSET:
            field_dict["compose_url"] = compose_url
        if delete_url is not UNSET:
            field_dict["delete_url"] = delete_url
        if key is not UNSET:
            field_dict["key"] = key
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_compose_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compose_url = _parse_compose_url(d.pop("compose_url", UNSET))

        def _parse_delete_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delete_url = _parse_delete_url(d.pop("delete_url", UNSET))

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        multi_part_upload_compose_url_schema = cls(
            compose_url=compose_url,
            delete_url=delete_url,
            key=key,
            url=url,
        )

        multi_part_upload_compose_url_schema.additional_properties = d
        return multi_part_upload_compose_url_schema

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
