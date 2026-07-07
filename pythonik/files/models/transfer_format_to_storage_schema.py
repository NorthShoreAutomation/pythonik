from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferFormatToStorageSchema")


@_attrs_define
class TransferFormatToStorageSchema:
    """
    Attributes:
        destination_directory_path (str | Unset):
        destination_filename (str | Unset):
    """

    destination_directory_path: str | Unset = UNSET
    destination_filename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_directory_path = self.destination_directory_path

        destination_filename = self.destination_filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if destination_filename is not UNSET:
            field_dict["destination_filename"] = destination_filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_directory_path = d.pop("destination_directory_path", UNSET)

        destination_filename = d.pop("destination_filename", UNSET)

        transfer_format_to_storage_schema = cls(
            destination_directory_path=destination_directory_path,
            destination_filename=destination_filename,
        )

        transfer_format_to_storage_schema.additional_properties = d
        return transfer_format_to_storage_schema

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
