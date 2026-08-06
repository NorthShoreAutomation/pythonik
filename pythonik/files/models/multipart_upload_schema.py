from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultipartUploadSchema")


@_attrs_define
class MultipartUploadSchema:
    """
    Attributes:
        parts_range (list[str]):
        parts_group (int | None | Unset):
    """

    parts_range: list[str]
    parts_group: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parts_range = self.parts_range

        parts_group: int | None | Unset
        if isinstance(self.parts_group, Unset):
            parts_group = UNSET
        else:
            parts_group = self.parts_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parts_range": parts_range,
            }
        )
        if parts_group is not UNSET:
            field_dict["parts_group"] = parts_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parts_range = cast(list[str], d.pop("parts_range"))

        def _parse_parts_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parts_group = _parse_parts_group(d.pop("parts_group", UNSET))

        multipart_upload_schema = cls(
            parts_range=parts_range,
            parts_group=parts_group,
        )

        multipart_upload_schema.additional_properties = d
        return multipart_upload_schema

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
