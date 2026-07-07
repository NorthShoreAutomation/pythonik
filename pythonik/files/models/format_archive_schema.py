from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormatArchiveSchema")


@_attrs_define
class FormatArchiveSchema:
    """
    Attributes:
        delete_original (bool | Unset):
        destination_directory_path (str | Unset):
        destination_file_set_name (str | Unset):
        destination_storage_id (UUID | Unset):
        destination_storage_method (str | Unset):
        format_id (UUID | Unset):
        original_file_set_id (UUID | Unset):
    """

    delete_original: bool | Unset = UNSET
    destination_directory_path: str | Unset = UNSET
    destination_file_set_name: str | Unset = UNSET
    destination_storage_id: UUID | Unset = UNSET
    destination_storage_method: str | Unset = UNSET
    format_id: UUID | Unset = UNSET
    original_file_set_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_original = self.delete_original

        destination_directory_path = self.destination_directory_path

        destination_file_set_name = self.destination_file_set_name

        destination_storage_id: str | Unset = UNSET
        if not isinstance(self.destination_storage_id, Unset):
            destination_storage_id = str(self.destination_storage_id)

        destination_storage_method = self.destination_storage_method

        format_id: str | Unset = UNSET
        if not isinstance(self.format_id, Unset):
            format_id = str(self.format_id)

        original_file_set_id: str | Unset = UNSET
        if not isinstance(self.original_file_set_id, Unset):
            original_file_set_id = str(self.original_file_set_id)

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
        delete_original = d.pop("delete_original", UNSET)

        destination_directory_path = d.pop("destination_directory_path", UNSET)

        destination_file_set_name = d.pop("destination_file_set_name", UNSET)

        _destination_storage_id = d.pop("destination_storage_id", UNSET)
        destination_storage_id: UUID | Unset
        if isinstance(_destination_storage_id, Unset):
            destination_storage_id = UNSET
        else:
            destination_storage_id = UUID(_destination_storage_id)

        destination_storage_method = d.pop("destination_storage_method", UNSET)

        _format_id = d.pop("format_id", UNSET)
        format_id: UUID | Unset
        if isinstance(_format_id, Unset):
            format_id = UNSET
        else:
            format_id = UUID(_format_id)

        _original_file_set_id = d.pop("original_file_set_id", UNSET)
        original_file_set_id: UUID | Unset
        if isinstance(_original_file_set_id, Unset):
            original_file_set_id = UNSET
        else:
            original_file_set_id = UUID(_original_file_set_id)

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
