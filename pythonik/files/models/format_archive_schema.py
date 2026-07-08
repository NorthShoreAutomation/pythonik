from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormatArchiveSchema")


@_attrs_define
class FormatArchiveSchema:
    """
    Attributes:
        delete_original (bool | None | Unset):
        destination_directory_path (None | str | Unset):
        destination_file_set_name (None | str | Unset):
        destination_storage_id (None | Unset | UUID):
        destination_storage_method (None | str | Unset):
        format_id (None | Unset | UUID):
        original_file_set_id (None | Unset | UUID):
    """

    delete_original: bool | None | Unset = UNSET
    destination_directory_path: None | str | Unset = UNSET
    destination_file_set_name: None | str | Unset = UNSET
    destination_storage_id: None | Unset | UUID = UNSET
    destination_storage_method: None | str | Unset = UNSET
    format_id: None | Unset | UUID = UNSET
    original_file_set_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_original: bool | None | Unset
        if isinstance(self.delete_original, Unset):
            delete_original = UNSET
        else:
            delete_original = self.delete_original

        destination_directory_path: None | str | Unset
        if isinstance(self.destination_directory_path, Unset):
            destination_directory_path = UNSET
        else:
            destination_directory_path = self.destination_directory_path

        destination_file_set_name: None | str | Unset
        if isinstance(self.destination_file_set_name, Unset):
            destination_file_set_name = UNSET
        else:
            destination_file_set_name = self.destination_file_set_name

        destination_storage_id: None | str | Unset
        if isinstance(self.destination_storage_id, Unset):
            destination_storage_id = UNSET
        elif isinstance(self.destination_storage_id, UUID):
            destination_storage_id = str(self.destination_storage_id)
        else:
            destination_storage_id = self.destination_storage_id

        destination_storage_method: None | str | Unset
        if isinstance(self.destination_storage_method, Unset):
            destination_storage_method = UNSET
        else:
            destination_storage_method = self.destination_storage_method

        format_id: None | str | Unset
        if isinstance(self.format_id, Unset):
            format_id = UNSET
        elif isinstance(self.format_id, UUID):
            format_id = str(self.format_id)
        else:
            format_id = self.format_id

        original_file_set_id: None | str | Unset
        if isinstance(self.original_file_set_id, Unset):
            original_file_set_id = UNSET
        elif isinstance(self.original_file_set_id, UUID):
            original_file_set_id = str(self.original_file_set_id)
        else:
            original_file_set_id = self.original_file_set_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_original is not UNSET:
            field_dict["delete_original"] = delete_original
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if destination_file_set_name is not UNSET:
            field_dict["destination_file_set_name"] = destination_file_set_name
        if destination_storage_id is not UNSET:
            field_dict["destination_storage_id"] = destination_storage_id
        if destination_storage_method is not UNSET:
            field_dict["destination_storage_method"] = destination_storage_method
        if format_id is not UNSET:
            field_dict["format_id"] = format_id
        if original_file_set_id is not UNSET:
            field_dict["original_file_set_id"] = original_file_set_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_delete_original(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_original = _parse_delete_original(d.pop("delete_original", UNSET))

        def _parse_destination_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_directory_path = _parse_destination_directory_path(
            d.pop("destination_directory_path", UNSET)
        )

        def _parse_destination_file_set_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_file_set_name = _parse_destination_file_set_name(
            d.pop("destination_file_set_name", UNSET)
        )

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

        def _parse_destination_storage_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_storage_method = _parse_destination_storage_method(
            d.pop("destination_storage_method", UNSET)
        )

        def _parse_format_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_id_type_0 = UUID(data)

                return format_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        format_id = _parse_format_id(d.pop("format_id", UNSET))

        def _parse_original_file_set_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_file_set_id_type_0 = UUID(data)

                return original_file_set_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        original_file_set_id = _parse_original_file_set_id(
            d.pop("original_file_set_id", UNSET)
        )

        format_archive_schema = cls(
            delete_original=delete_original,
            destination_directory_path=destination_directory_path,
            destination_file_set_name=destination_file_set_name,
            destination_storage_id=destination_storage_id,
            destination_storage_method=destination_storage_method,
            format_id=format_id,
            original_file_set_id=original_file_set_id,
        )

        format_archive_schema.additional_properties = d
        return format_archive_schema

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
