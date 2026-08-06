from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkAssetIdsWithFiles")


@_attrs_define
class BulkAssetIdsWithFiles:
    """
    Attributes:
        asset_ids (list[UUID] | None | Unset):
    """

    asset_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids: list[str] | None | Unset
        if isinstance(self.asset_ids, Unset):
            asset_ids = UNSET
        elif isinstance(self.asset_ids, list):
            asset_ids = []
            for asset_ids_type_0_item_data in self.asset_ids:
                asset_ids_type_0_item = str(asset_ids_type_0_item_data)
                asset_ids.append(asset_ids_type_0_item)

        else:
            asset_ids = self.asset_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_ids is not UNSET:
            field_dict["asset_ids"] = asset_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_asset_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_ids_type_0 = []
                _asset_ids_type_0 = data
                for asset_ids_type_0_item_data in _asset_ids_type_0:
                    asset_ids_type_0_item = UUID(asset_ids_type_0_item_data)

                    asset_ids_type_0.append(asset_ids_type_0_item)

                return asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        asset_ids = _parse_asset_ids(d.pop("asset_ids", UNSET))

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
