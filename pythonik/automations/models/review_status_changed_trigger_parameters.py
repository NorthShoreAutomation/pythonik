from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.review_status_changed_trigger_parameters_statuses_item import (
    ReviewStatusChangedTriggerParametersStatusesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewStatusChangedTriggerParameters")


@_attrs_define
class ReviewStatusChangedTriggerParameters:
    """
    Attributes:
        statuses (list[ReviewStatusChangedTriggerParametersStatusesItem] | Unset):
    """

    statuses: list[ReviewStatusChangedTriggerParametersStatusesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statuses: list[str] | Unset = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.value
                statuses.append(statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _statuses = d.pop("statuses", UNSET)
        statuses: list[ReviewStatusChangedTriggerParametersStatusesItem] | Unset = UNSET
        if _statuses is not UNSET:
            statuses = []
            for statuses_item_data in _statuses:
                statuses_item = ReviewStatusChangedTriggerParametersStatusesItem(
                    statuses_item_data
                )

                statuses.append(statuses_item)

        review_status_changed_trigger_parameters = cls(
            statuses=statuses,
        )

        review_status_changed_trigger_parameters.additional_properties = d
        return review_status_changed_trigger_parameters

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
