from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageContentInfoSchema")


@_attrs_define
class StorageContentInfoSchema:
    """
    Attributes:
        assets_count (int | None | Unset):
        file_count (int | None | Unset):
        storage_id (None | Unset | UUID):
        total_duration_milliseconds (int | None | Unset):
        total_size (int | None | Unset):
    """

    assets_count: int | None | Unset = UNSET
    file_count: int | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    total_duration_milliseconds: int | None | Unset = UNSET
    total_size: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets_count: int | None | Unset
        if isinstance(self.assets_count, Unset):
            assets_count = UNSET
        else:
            assets_count = self.assets_count

        file_count: int | None | Unset
        if isinstance(self.file_count, Unset):
            file_count = UNSET
        else:
            file_count = self.file_count

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        total_duration_milliseconds: int | None | Unset
        if isinstance(self.total_duration_milliseconds, Unset):
            total_duration_milliseconds = UNSET
        else:
            total_duration_milliseconds = self.total_duration_milliseconds

        total_size: int | None | Unset
        if isinstance(self.total_size, Unset):
            total_size = UNSET
        else:
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

        def _parse_assets_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assets_count = _parse_assets_count(d.pop("assets_count", UNSET))

        def _parse_file_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_count = _parse_file_count(d.pop("file_count", UNSET))

        def _parse_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_id_type_0 = UUID(data)

                return storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_id = _parse_storage_id(d.pop("storage_id", UNSET))

        def _parse_total_duration_milliseconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_duration_milliseconds = _parse_total_duration_milliseconds(
            d.pop("total_duration_milliseconds", UNSET)
        )

        def _parse_total_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_size = _parse_total_size(d.pop("total_size", UNSET))

        storage_content_info_schema = cls(
            assets_count=assets_count,
            file_count=file_count,
            storage_id=storage_id,
            total_duration_milliseconds=total_duration_milliseconds,
            total_size=total_size,
        )

        storage_content_info_schema.additional_properties = d
        return storage_content_info_schema

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
