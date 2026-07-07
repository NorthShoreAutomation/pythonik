from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageContentInfo")


@_attrs_define
class StorageContentInfo:
    """
    Attributes:
        assets_count (int | Unset):
        file_count (int | Unset):
        storage_id (UUID | Unset):
        total_duration_milliseconds (int | Unset):
        total_size (int | Unset):
    """

    assets_count: int | Unset = UNSET
    file_count: int | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    total_duration_milliseconds: int | Unset = UNSET
    total_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets_count = self.assets_count

        file_count = self.file_count

        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

        total_duration_milliseconds = self.total_duration_milliseconds

        total_size = self.total_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets_count is not UNSET:
            field_dict["assets_count"] = assets_count
        if file_count is not UNSET:
            field_dict["file_count"] = file_count
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if total_duration_milliseconds is not UNSET:
            field_dict["total_duration_milliseconds"] = total_duration_milliseconds
        if total_size is not UNSET:
            field_dict["total_size"] = total_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assets_count = d.pop("assets_count", UNSET)

        file_count = d.pop("file_count", UNSET)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        total_duration_milliseconds = d.pop("total_duration_milliseconds", UNSET)

        total_size = d.pop("total_size", UNSET)

        storage_content_info = cls(
            assets_count=assets_count,
            file_count=file_count,
            storage_id=storage_id,
            total_duration_milliseconds=total_duration_milliseconds,
            total_size=total_size,
        )

        storage_content_info.additional_properties = d
        return storage_content_info

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
