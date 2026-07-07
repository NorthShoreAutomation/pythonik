from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisProfileGoogleVisionSettingsSchema")


@_attrs_define
class AnalysisProfileGoogleVisionSettingsSchema:
    """
    Attributes:
        is_system (bool | Unset):
        min_confidence (float | Unset):
    """

    is_system: bool | Unset = UNSET
    min_confidence: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_system = self.is_system

        min_confidence = self.min_confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if min_confidence is not UNSET:
            field_dict["min_confidence"] = min_confidence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_system = d.pop("is_system", UNSET)

        min_confidence = d.pop("min_confidence", UNSET)

        analysis_profile_google_vision_settings_schema = cls(
            is_system=is_system,
            min_confidence=min_confidence,
        )

        analysis_profile_google_vision_settings_schema.additional_properties = d
        return analysis_profile_google_vision_settings_schema

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
