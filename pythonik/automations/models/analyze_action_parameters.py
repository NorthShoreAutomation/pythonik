from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analyze_action_parameters_force_type import (
    AnalyzeActionParametersForceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyzeActionParameters")


@_attrs_define
class AnalyzeActionParameters:
    """
    Attributes:
        force (bool | Unset):  Default: False.
        force_type (AnalyzeActionParametersForceType | Unset):  Default: AnalyzeActionParametersForceType.OVERWRITE.
    """

    force: bool | Unset = False
    force_type: AnalyzeActionParametersForceType | Unset = (
        AnalyzeActionParametersForceType.OVERWRITE
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        force = self.force

        force_type: str | Unset = UNSET
        if not isinstance(self.force_type, Unset):
            force_type = self.force_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force is not UNSET:
            field_dict["force"] = force
        if force_type is not UNSET:
            field_dict["force_type"] = force_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        force = d.pop("force", UNSET)

        _force_type = d.pop("force_type", UNSET)
        force_type: AnalyzeActionParametersForceType | Unset
        if isinstance(_force_type, Unset):
            force_type = UNSET
        else:
            force_type = AnalyzeActionParametersForceType(_force_type)

        analyze_action_parameters = cls(
            force=force,
            force_type=force_type,
        )

        analyze_action_parameters.additional_properties = d
        return analyze_action_parameters

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
