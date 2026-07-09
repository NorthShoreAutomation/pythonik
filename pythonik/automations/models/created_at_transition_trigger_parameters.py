from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreatedAtTransitionTriggerParameters")


@_attrs_define
class CreatedAtTransitionTriggerParameters:
    """
    Attributes:
        days_since_created (int): Indicates a number of days passed since an objects was created.
    """

    days_since_created: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days_since_created = self.days_since_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days_since_created": days_since_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days_since_created = d.pop("days_since_created")

        created_at_transition_trigger_parameters = cls(
            days_since_created=days_since_created,
        )

        created_at_transition_trigger_parameters.additional_properties = d
        return created_at_transition_trigger_parameters

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
