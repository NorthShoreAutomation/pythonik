from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkAssetIdsWithFiles")


@_attrs_define
class BulkAssetIdsWithFiles:
    """
    Attributes:
        asset_ids (list[UUID] | Unset):
    """

    asset_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids: list[str] | Unset = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = []
            for asset_ids_item_data in self.asset_ids:
                asset_ids_item = str(asset_ids_item_data)
                asset_ids.append(asset_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_ids is not UNSET:
            field_dict["asset_ids"] = asset_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _asset_ids = d.pop("asset_ids", UNSET)
        asset_ids: list[UUID] | Unset = UNSET
        if _asset_ids is not UNSET:
            asset_ids = []
            for asset_ids_item_data in _asset_ids:
                asset_ids_item = UUID(asset_ids_item_data)

                asset_ids.append(asset_ids_item)

        bulk_asset_ids_with_files = cls(
            asset_ids=asset_ids,
        )

        bulk_asset_ids_with_files.additional_properties = d
        return bulk_asset_ids_with_files

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
