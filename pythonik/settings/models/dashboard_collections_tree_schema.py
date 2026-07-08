from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardCollectionsTreeSchema")


@_attrs_define
class DashboardCollectionsTreeSchema:
    """
    Attributes:
        visible (bool | None | Unset):
    """

    visible: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visible: bool | None | Unset
        if isinstance(self.visible, Unset):
            visible = UNSET
        else:
            visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible = _parse_visible(d.pop("visible", UNSET))

        dashboard_collections_tree_schema = cls(
            visible=visible,
        )

        dashboard_collections_tree_schema.additional_properties = d
        return dashboard_collections_tree_schema

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
