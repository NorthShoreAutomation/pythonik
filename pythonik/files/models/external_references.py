from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalReferences")


@_attrs_define
class ExternalReferences:
    """
    Attributes:
        uri (str):
        action (str | Unset):
        display_name (str | Unset):
        icon (str | Unset):
    """

    uri: str
    action: str | Unset = UNSET
    display_name: str | Unset = UNSET
    icon: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        action = self.action

        display_name = self.display_name

        icon = self.icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri")

        action = d.pop("action", UNSET)

        display_name = d.pop("display_name", UNSET)

        icon = d.pop("icon", UNSET)

        external_references = cls(
            uri=uri,
            action=action,
            display_name=display_name,
            icon=icon,
        )

        external_references.additional_properties = d
        return external_references

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
