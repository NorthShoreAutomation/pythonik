from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkArchiveAssetSchema")


@_attrs_define
class BulkArchiveAssetSchema:
    """
    Attributes:
        asset_ids (list[UUID]):
        all_versions (bool | Unset): If true, all versions of the asset will be transferred
        delete_only_from_source_folder (bool | Unset):  Default: False.
        delete_original (bool | Unset):  Default: False.
        destination_directory_path (str | Unset):
        destination_storage_id (None | Unset | UUID):
        formats (list[str] | Unset): List of format names to transfer. If not specified, all formats will be
            transferred.
        preferred_original_storage_id (None | Unset | UUID):
    """

    asset_ids: list[UUID]
    all_versions: bool | Unset = UNSET
    delete_only_from_source_folder: bool | Unset = False
    delete_original: bool | Unset = False
    destination_directory_path: str | Unset = UNSET
    destination_storage_id: None | Unset | UUID = UNSET
    formats: list[str] | Unset = UNSET
    preferred_original_storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids = []
        for asset_ids_item_data in self.asset_ids:
            asset_ids_item = str(asset_ids_item_data)
            asset_ids.append(asset_ids_item)

        all_versions = self.all_versions

        delete_only_from_source_folder = self.delete_only_from_source_folder

        delete_original = self.delete_original

        destination_directory_path = self.destination_directory_path

        destination_storage_id: None | str | Unset
        if isinstance(self.destination_storage_id, Unset):
            destination_storage_id = UNSET
        elif isinstance(self.destination_storage_id, UUID):
            destination_storage_id = str(self.destination_storage_id)
        else:
            destination_storage_id = self.destination_storage_id

        formats: list[str] | Unset = UNSET
        if not isinstance(self.formats, Unset):
            formats = self.formats

        preferred_original_storage_id: None | str | Unset
        if isinstance(self.preferred_original_storage_id, Unset):
            preferred_original_storage_id = UNSET
        elif isinstance(self.preferred_original_storage_id, UUID):
            preferred_original_storage_id = str(self.preferred_original_storage_id)
        else:
            preferred_original_storage_id = self.preferred_original_storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_ids": asset_ids,
            }
        )
        if all_versions is not UNSET:
            field_dict["all_versions"] = all_versions
        if delete_only_from_source_folder is not UNSET:
            field_dict["delete_only_from_source_folder"] = (
                delete_only_from_source_folder
            )
        if delete_original is not UNSET:
            field_dict["delete_original"] = delete_original
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if destination_storage_id is not UNSET:
            field_dict["destination_storage_id"] = destination_storage_id
        if formats is not UNSET:
            field_dict["formats"] = formats
        if preferred_original_storage_id is not UNSET:
            field_dict["preferred_original_storage_id"] = preferred_original_storage_id

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

        delete_only_from_source_folder = d.pop("delete_only_from_source_folder", UNSET)

        delete_original = d.pop("delete_original", UNSET)

        destination_directory_path = d.pop("destination_directory_path", UNSET)

        def _parse_destination_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                destination_storage_id_type_0 = UUID(data)

                return destination_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        destination_storage_id = _parse_destination_storage_id(
            d.pop("destination_storage_id", UNSET)
        )

        formats = cast(list[str], d.pop("formats", UNSET))

        def _parse_preferred_original_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_original_storage_id_type_0 = UUID(data)

                return preferred_original_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        preferred_original_storage_id = _parse_preferred_original_storage_id(
            d.pop("preferred_original_storage_id", UNSET)
        )

        bulk_archive_asset_schema = cls(
            asset_ids=asset_ids,
            all_versions=all_versions,
            delete_only_from_source_folder=delete_only_from_source_folder,
            delete_original=delete_original,
            destination_directory_path=destination_directory_path,
            destination_storage_id=destination_storage_id,
            formats=formats,
            preferred_original_storage_id=preferred_original_storage_id,
        )

        bulk_archive_asset_schema.additional_properties = d
        return bulk_archive_asset_schema

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
