from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReindexGroupSchema")


@_attrs_define
class ReindexGroupSchema:
    """
    Attributes:
        sync_to_another_dc (bool | Unset):
    """

    sync_to_another_dc: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_to_another_dc = self.sync_to_another_dc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sync_to_another_dc is not UNSET:
            field_dict["sync_to_another_dc"] = sync_to_another_dc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_to_another_dc = d.pop("sync_to_another_dc", UNSET)

        reindex_group_schema = cls(
            sync_to_another_dc=sync_to_another_dc,
        )

        reindex_group_schema.additional_properties = d
        return reindex_group_schema

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
