from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
        force (bool | None | Unset):  Default: False.
        force_type (AnalyzeActionParametersForceType | None | Unset):
    """

    force: bool | None | Unset = False
    force_type: AnalyzeActionParametersForceType | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        force: bool | None | Unset
        if isinstance(self.force, Unset):
            force = UNSET
        else:
            force = self.force

        force_type: None | str | Unset
        if isinstance(self.force_type, Unset):
            force_type = UNSET
        elif isinstance(self.force_type, AnalyzeActionParametersForceType):
            force_type = self.force_type.value
        else:
            force_type = self.force_type

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

        def _parse_force(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force = _parse_force(d.pop("force", UNSET))

        def _parse_force_type(
            data: object,
        ) -> AnalyzeActionParametersForceType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                force_type_type_1 = AnalyzeActionParametersForceType(data)

                return force_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyzeActionParametersForceType | None | Unset, data)

        force_type = _parse_force_type(d.pop("force_type", UNSET))

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
