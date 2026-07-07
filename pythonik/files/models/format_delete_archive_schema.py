from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormatDeleteArchiveSchema")


@_attrs_define
class FormatDeleteArchiveSchema:
    """
    Attributes:
        file_set_id (UUID | Unset):
    """

    file_set_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_set_id: str | Unset = UNSET
        if not isinstance(self.file_set_id, Unset):
            file_set_id = str(self.file_set_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_set_id is not UNSET:
            field_dict["file_set_id"] = file_set_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _file_set_id = d.pop("file_set_id", UNSET)
        file_set_id: UUID | Unset
        if isinstance(_file_set_id, Unset):
            file_set_id = UNSET
        else:
            file_set_id = UUID(_file_set_id)

        format_delete_archive_schema = cls(
            file_set_id=file_set_id,
        )

        format_delete_archive_schema.additional_properties = d
        return format_delete_archive_schema

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
