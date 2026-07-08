from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiPartS3UrlPartSchema")


@_attrs_define
class MultiPartS3UrlPartSchema:
    """
    Attributes:
        checksum (None | str | Unset): base64-encoded md5 digest
        part_number (int | None | Unset):
        url (None | str | Unset):
    """

    checksum: None | str | Unset = UNSET
    part_number: int | None | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksum: None | str | Unset
        if isinstance(self.checksum, Unset):
            checksum = UNSET
        else:
            checksum = self.checksum

        part_number: int | None | Unset
        if isinstance(self.part_number, Unset):
            part_number = UNSET
        else:
            part_number = self.part_number

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checksum = _parse_checksum(d.pop("checksum", UNSET))

        def _parse_part_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        part_number = _parse_part_number(d.pop("part_number", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        multi_part_s3_url_part_schema = cls(
            checksum=checksum,
            part_number=part_number,
            url=url,
        )

        multi_part_s3_url_part_schema.additional_properties = d
        return multi_part_s3_url_part_schema

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
