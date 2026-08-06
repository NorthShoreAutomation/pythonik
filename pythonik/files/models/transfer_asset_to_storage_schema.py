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
        all_versions (bool | None | Unset): If true, all versions of the asset will be transferred
        destination_directory_path (None | str | Unset):
        formats (list[str] | None | Unset): List of format names to transfer. If not specified, all formats will be
            transferred.
        version_ids (list[UUID] | None | Unset): List of version IDs to transfer. If not specified, the latest version
            will be transferred.
    """

    all_versions: bool | None | Unset = UNSET
    destination_directory_path: None | str | Unset = UNSET
    formats: list[str] | None | Unset = UNSET
    version_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_versions: bool | None | Unset
        if isinstance(self.all_versions, Unset):
            all_versions = UNSET
        else:
            all_versions = self.all_versions

        destination_directory_path: None | str | Unset
        if isinstance(self.destination_directory_path, Unset):
            destination_directory_path = UNSET
        else:
            destination_directory_path = self.destination_directory_path

        formats: list[str] | None | Unset
        if isinstance(self.formats, Unset):
            formats = UNSET
        elif isinstance(self.formats, list):
            formats = self.formats

        else:
            formats = self.formats

        version_ids: list[str] | None | Unset
        if isinstance(self.version_ids, Unset):
            version_ids = UNSET
        elif isinstance(self.version_ids, list):
            version_ids = []
            for version_ids_type_0_item_data in self.version_ids:
                version_ids_type_0_item = str(version_ids_type_0_item_data)
                version_ids.append(version_ids_type_0_item)

        else:
            version_ids = self.version_ids

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

        def _parse_all_versions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_versions = _parse_all_versions(d.pop("all_versions", UNSET))

        def _parse_destination_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_directory_path = _parse_destination_directory_path(
            d.pop("destination_directory_path", UNSET)
        )

        def _parse_formats(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                formats_type_0 = cast(list[str], data)

                return formats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        formats = _parse_formats(d.pop("formats", UNSET))

        def _parse_version_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                version_ids_type_0 = []
                _version_ids_type_0 = data
                for version_ids_type_0_item_data in _version_ids_type_0:
                    version_ids_type_0_item = UUID(version_ids_type_0_item_data)

                    version_ids_type_0.append(version_ids_type_0_item)

                return version_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        version_ids = _parse_version_ids(d.pop("version_ids", UNSET))

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
