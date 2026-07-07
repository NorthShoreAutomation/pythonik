from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferAssetToStorageSchema")


@_attrs_define
class TransferAssetToStorageSchema:
    """
    Attributes:
        all_versions (bool | Unset): If true, all versions of the asset will be transferred
        destination_directory_path (str | Unset):
        formats (list[str] | Unset): List of format names to transfer. If not specified, all formats will be
            transferred.
        version_ids (list[UUID] | Unset): List of version IDs to transfer. If not specified, the latest version will be
            transferred.
    """

    all_versions: bool | Unset = UNSET
    destination_directory_path: str | Unset = UNSET
    formats: list[str] | Unset = UNSET
    version_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_versions = self.all_versions

        destination_directory_path = self.destination_directory_path

        formats: list[str] | Unset = UNSET
        if not isinstance(self.formats, Unset):
            formats = self.formats

        version_ids: list[str] | Unset = UNSET
        if not isinstance(self.version_ids, Unset):
            version_ids = []
            for version_ids_item_data in self.version_ids:
                version_ids_item = str(version_ids_item_data)
                version_ids.append(version_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_versions is not UNSET:
            field_dict["all_versions"] = all_versions
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if formats is not UNSET:
            field_dict["formats"] = formats
        if version_ids is not UNSET:
            field_dict["version_ids"] = version_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_versions = d.pop("all_versions", UNSET)

        destination_directory_path = d.pop("destination_directory_path", UNSET)

        formats = cast(list[str], d.pop("formats", UNSET))

        _version_ids = d.pop("version_ids", UNSET)
        version_ids: list[UUID] | Unset = UNSET
        if _version_ids is not UNSET:
            version_ids = []
            for version_ids_item_data in _version_ids:
                version_ids_item = UUID(version_ids_item_data)

                version_ids.append(version_ids_item)

        transfer_asset_to_storage_schema = cls(
            all_versions=all_versions,
            destination_directory_path=destination_directory_path,
            formats=formats,
            version_ids=version_ids,
        )

        transfer_asset_to_storage_schema.additional_properties = d
        return transfer_asset_to_storage_schema

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
