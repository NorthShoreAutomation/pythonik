from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BucketSchema")


@_attrs_define
class BucketSchema:
    """
    Attributes:
        doc_count (int | Unset):
        key (str | Unset):
    """

    doc_count: int | Unset = UNSET
    key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        doc_count = self.doc_count

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_count is not UNSET:
            field_dict["doc_count"] = doc_count
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        doc_count = d.pop("doc_count", UNSET)

        key = d.pop("key", UNSET)

        bucket_schema = cls(
            doc_count=doc_count,
            key=key,
        )

        bucket_schema.additional_properties = d
        return bucket_schema

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
