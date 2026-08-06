from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardWidget")


@_attrs_define
class DashboardWidget:
    """
    Attributes:
        expanded (bool | None | Unset):
        id (None | str | Unset):
        visible (bool | None | Unset):
    """

    expanded: bool | None | Unset = UNSET
    id: None | str | Unset = UNSET
    visible: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expanded: bool | None | Unset
        if isinstance(self.expanded, Unset):
            expanded = UNSET
        else:
            expanded = self.expanded

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        visible: bool | None | Unset
        if isinstance(self.visible, Unset):
            visible = UNSET
        else:
            visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expanded is not UNSET:
            field_dict["expanded"] = expanded
        if id is not UNSET:
            field_dict["id"] = id
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expanded(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        expanded = _parse_expanded(d.pop("expanded", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible = _parse_visible(d.pop("visible", UNSET))

        dashboard_widget = cls(
            expanded=expanded,
            id=id,
            visible=visible,
        )

        dashboard_widget.additional_properties = d
        return dashboard_widget

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
