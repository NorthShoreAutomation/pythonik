from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkShareDeleteSchema")


@_attrs_define
class BulkShareDeleteSchema:
    """
    Attributes:
        share_ids (list[UUID]):
    """

    share_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_ids = []
        for share_ids_item_data in self.share_ids:
            share_ids_item = str(share_ids_item_data)
            share_ids.append(share_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "share_ids": share_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        share_ids = []
        _share_ids = d.pop("share_ids")
        for share_ids_item_data in _share_ids:
            share_ids_item = UUID(share_ids_item_data)

            share_ids.append(share_ids_item)

        bulk_share_delete_schema = cls(
            share_ids=share_ids,
        )

        bulk_share_delete_schema.additional_properties = d
        return bulk_share_delete_schema

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
