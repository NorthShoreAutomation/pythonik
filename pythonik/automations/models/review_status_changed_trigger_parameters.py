from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.review_status_changed_trigger_parameters_statuses_type_0_item import (
    ReviewStatusChangedTriggerParametersStatusesType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewStatusChangedTriggerParameters")


@_attrs_define
class ReviewStatusChangedTriggerParameters:
    """
    Attributes:
        statuses (list[ReviewStatusChangedTriggerParametersStatusesType0Item] | None | Unset):
    """

    statuses: (
        list[ReviewStatusChangedTriggerParametersStatusesType0Item] | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statuses: list[str] | None | Unset
        if isinstance(self.statuses, Unset):
            statuses = UNSET
        elif isinstance(self.statuses, list):
            statuses = []
            for statuses_type_0_item_data in self.statuses:
                statuses_type_0_item = statuses_type_0_item_data.value
                statuses.append(statuses_type_0_item)

        else:
            statuses = self.statuses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_statuses(
            data: object,
        ) -> list[ReviewStatusChangedTriggerParametersStatusesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                statuses_type_0 = []
                _statuses_type_0 = data
                for statuses_type_0_item_data in _statuses_type_0:
                    statuses_type_0_item = (
                        ReviewStatusChangedTriggerParametersStatusesType0Item(
                            statuses_type_0_item_data
                        )
                    )

                    statuses_type_0.append(statuses_type_0_item)

                return statuses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[ReviewStatusChangedTriggerParametersStatusesType0Item]
                | None
                | Unset,
                data,
            )

        statuses = _parse_statuses(d.pop("statuses", UNSET))

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
