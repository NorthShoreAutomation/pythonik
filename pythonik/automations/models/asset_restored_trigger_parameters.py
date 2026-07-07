from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetRestoredTriggerParameters")


@_attrs_define
class AssetRestoredTriggerParameters:
    """
    Attributes:
        storage_id (UUID | Unset):
    """

    storage_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        asset_restored_trigger_parameters = cls(
            storage_id=storage_id,
        )

        asset_restored_trigger_parameters.additional_properties = d
        return asset_restored_trigger_parameters

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
