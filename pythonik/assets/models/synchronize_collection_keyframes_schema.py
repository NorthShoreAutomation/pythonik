from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SynchronizeCollectionKeyframesSchema")


@_attrs_define
class SynchronizeCollectionKeyframesSchema:
    """
    Attributes:
        asset_ids (list[str] | None | Unset):
    """

    asset_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids: list[str] | None | Unset
        if isinstance(self.asset_ids, Unset):
            asset_ids = UNSET
        elif isinstance(self.asset_ids, list):
            asset_ids = self.asset_ids

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

        def _parse_asset_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_ids_type_0 = cast(list[str], data)

                return asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        asset_ids = _parse_asset_ids(d.pop("asset_ids", UNSET))

        synchronize_collection_keyframes_schema = cls(
            asset_ids=asset_ids,
        )

        synchronize_collection_keyframes_schema.additional_properties = d
        return synchronize_collection_keyframes_schema

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
