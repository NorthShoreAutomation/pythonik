from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveAssetResourceSchema")


@_attrs_define
class MoveAssetResourceSchema:
    """
    Attributes:
        destination_asset_id (UUID):
        destination_version_id (UUID):
        source_version_id (UUID):
        exclude_format_ids (list[str] | None | Unset):
    """

    destination_asset_id: UUID
    destination_version_id: UUID
    source_version_id: UUID
    exclude_format_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_asset_id = str(self.destination_asset_id)

        destination_version_id = str(self.destination_version_id)

        source_version_id = str(self.source_version_id)

        exclude_format_ids: list[str] | None | Unset
        if isinstance(self.exclude_format_ids, Unset):
            exclude_format_ids = UNSET
        elif isinstance(self.exclude_format_ids, list):
            exclude_format_ids = self.exclude_format_ids

        else:
            exclude_format_ids = self.exclude_format_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination_asset_id": destination_asset_id,
                "destination_version_id": destination_version_id,
                "source_version_id": source_version_id,
            }
        )
        if exclude_format_ids is not UNSET:
            field_dict["exclude_format_ids"] = exclude_format_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_asset_id = UUID(d.pop("destination_asset_id"))

        destination_version_id = UUID(d.pop("destination_version_id"))

        source_version_id = UUID(d.pop("source_version_id"))

        def _parse_exclude_format_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_format_ids_type_0 = cast(list[str], data)

                return exclude_format_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_format_ids = _parse_exclude_format_ids(
            d.pop("exclude_format_ids", UNSET)
        )

        move_asset_resource_schema = cls(
            destination_asset_id=destination_asset_id,
            destination_version_id=destination_version_id,
            source_version_id=source_version_id,
            exclude_format_ids=exclude_format_ids,
        )

        move_asset_resource_schema.additional_properties = d
        return move_asset_resource_schema

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
