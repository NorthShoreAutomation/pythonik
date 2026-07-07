from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_history_widget import UsageHistoryWidget


T = TypeVar("T", bound="UsageHistorySchema")


@_attrs_define
class UsageHistorySchema:
    """
    Attributes:
        widgets (list[UsageHistoryWidget] | Unset):
    """

    widgets: list[UsageHistoryWidget] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        widgets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.widgets, Unset):
            widgets = []
            for widgets_item_data in self.widgets:
                widgets_item = widgets_item_data.to_dict()
                widgets.append(widgets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if widgets is not UNSET:
            field_dict["widgets"] = widgets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_history_widget import UsageHistoryWidget

        d = dict(src_dict)
        _widgets = d.pop("widgets", UNSET)
        widgets: list[UsageHistoryWidget] | Unset = UNSET
        if _widgets is not UNSET:
            widgets = []
            for widgets_item_data in _widgets:
                widgets_item = UsageHistoryWidget.from_dict(widgets_item_data)

                widgets.append(widgets_item)

        usage_history_schema = cls(
            widgets=widgets,
        )

        usage_history_schema.additional_properties = d
        return usage_history_schema

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
