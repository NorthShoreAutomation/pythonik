from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.magic_link_allowlist_update_schema_entry_type_type_1 import (
        MagicLinkAllowlistUpdateSchemaEntryTypeType1,
    )


T = TypeVar("T", bound="MagicLinkAllowlistUpdateSchema")


@_attrs_define
class MagicLinkAllowlistUpdateSchema:
    """
    Attributes:
        entry_type (MagicLinkAllowlistUpdateSchemaEntryTypeType1 | None | Unset):
        value (None | str | Unset):
    """

    entry_type: MagicLinkAllowlistUpdateSchemaEntryTypeType1 | None | Unset = UNSET
    value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.magic_link_allowlist_update_schema_entry_type_type_1 import (
            MagicLinkAllowlistUpdateSchemaEntryTypeType1,
        )

        entry_type: dict[str, Any] | None | Unset
        if isinstance(self.entry_type, Unset):
            entry_type = UNSET
        elif isinstance(self.entry_type, MagicLinkAllowlistUpdateSchemaEntryTypeType1):
            entry_type = self.entry_type.to_dict()
        else:
            entry_type = self.entry_type

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
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
        from ..models.magic_link_allowlist_update_schema_entry_type_type_1 import (
            MagicLinkAllowlistUpdateSchemaEntryTypeType1,
        )

        d = dict(src_dict)

        def _parse_entry_type(
            data: object,
        ) -> MagicLinkAllowlistUpdateSchemaEntryTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entry_type_type_1 = (
                    MagicLinkAllowlistUpdateSchemaEntryTypeType1.from_dict(data)
                )

                return entry_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MagicLinkAllowlistUpdateSchemaEntryTypeType1 | None | Unset, data
            )

        entry_type = _parse_entry_type(d.pop("entry_type", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

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
