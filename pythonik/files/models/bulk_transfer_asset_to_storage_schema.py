from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkTransferAssetToStorageSchema")


@_attrs_define
class BulkTransferAssetToStorageSchema:
    """
    Attributes:
        asset_ids (list[UUID]):
        all_versions (bool | Unset): If true, all versions of the asset will be transferred
        destination_directory_path (str | Unset):
        formats (list[str] | Unset): List of format names to transfer. If not specified, all formats will be
            transferred.
    """

    asset_ids: list[UUID]
    all_versions: bool | Unset = UNSET
    destination_directory_path: str | Unset = UNSET
    formats: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids = []
        for asset_ids_item_data in self.asset_ids:
            asset_ids_item = str(asset_ids_item_data)
            asset_ids.append(asset_ids_item)

        all_versions = self.all_versions

        destination_directory_path = self.destination_directory_path

        formats: list[str] | Unset = UNSET
        if not isinstance(self.formats, Unset):
            formats = self.formats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_ids": asset_ids,
            }
        )
        if all_versions is not UNSET:
            field_dict["all_versions"] = all_versions
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if formats is not UNSET:
            field_dict["formats"] = formats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_ids = []
        _asset_ids = d.pop("asset_ids")
        for asset_ids_item_data in _asset_ids:
            asset_ids_item = UUID(asset_ids_item_data)

            asset_ids.append(asset_ids_item)

        all_versions = d.pop("all_versions", UNSET)

        destination_directory_path = d.pop("destination_directory_path", UNSET)

        formats = cast(list[str], d.pop("formats", UNSET))

        bulk_transfer_asset_to_storage_schema = cls(
            asset_ids=asset_ids,
            all_versions=all_versions,
            destination_directory_path=destination_directory_path,
            formats=formats,
        )

        bulk_transfer_asset_to_storage_schema.additional_properties = d
        return bulk_transfer_asset_to_storage_schema

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
