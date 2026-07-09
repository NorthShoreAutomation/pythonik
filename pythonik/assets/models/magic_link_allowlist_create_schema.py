from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.magic_link_allowlist_create_schema_entry_type import (
    MagicLinkAllowlistCreateSchemaEntryType,
)

T = TypeVar("T", bound="MagicLinkAllowlistCreateSchema")


@_attrs_define
class MagicLinkAllowlistCreateSchema:
    """
    Attributes:
        entry_type (MagicLinkAllowlistCreateSchemaEntryType):
        value (str):
    """

    entry_type: MagicLinkAllowlistCreateSchemaEntryType
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_type = self.entry_type.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry_type": entry_type,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry_type = MagicLinkAllowlistCreateSchemaEntryType(d.pop("entry_type"))

        value = d.pop("value")

        magic_link_allowlist_create_schema = cls(
            entry_type=entry_type,
            value=value,
        )

        magic_link_allowlist_create_schema.additional_properties = d
        return magic_link_allowlist_create_schema

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
