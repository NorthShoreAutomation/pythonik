from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.magic_link_allowlist_update_schema_entry_type import (
    MagicLinkAllowlistUpdateSchemaEntryType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MagicLinkAllowlistUpdateSchema")


@_attrs_define
class MagicLinkAllowlistUpdateSchema:
    """
    Attributes:
        entry_type (MagicLinkAllowlistUpdateSchemaEntryType | Unset):
        value (str | Unset):
    """

    entry_type: MagicLinkAllowlistUpdateSchemaEntryType | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_type: str | Unset = UNSET
        if not isinstance(self.entry_type, Unset):
            entry_type = self.entry_type.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_type is not UNSET:
            field_dict["entry_type"] = entry_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _entry_type = d.pop("entry_type", UNSET)
        entry_type: MagicLinkAllowlistUpdateSchemaEntryType | Unset
        if isinstance(_entry_type, Unset):
            entry_type = UNSET
        else:
            entry_type = MagicLinkAllowlistUpdateSchemaEntryType(_entry_type)

        value = d.pop("value", UNSET)

        magic_link_allowlist_update_schema = cls(
            entry_type=entry_type,
            value=value,
        )

        magic_link_allowlist_update_schema.additional_properties = d
        return magic_link_allowlist_update_schema

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
