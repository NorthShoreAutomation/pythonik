from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisProfileGoogleVideoIntelligenceSettingsSchema")


@_attrs_define
class AnalysisProfileGoogleVideoIntelligenceSettingsSchema:
    """
    Attributes:
        frame_confidence_threshold (float | None | Unset):
        is_system (bool | None | Unset):
        video_confidence_threshold (float | None | Unset):
    """

    frame_confidence_threshold: float | None | Unset = UNSET
    is_system: bool | None | Unset = UNSET
    video_confidence_threshold: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frame_confidence_threshold: float | None | Unset
        if isinstance(self.frame_confidence_threshold, Unset):
            frame_confidence_threshold = UNSET
        else:
            frame_confidence_threshold = self.frame_confidence_threshold

        is_system: bool | None | Unset
        if isinstance(self.is_system, Unset):
            is_system = UNSET
        else:
            is_system = self.is_system

        video_confidence_threshold: float | None | Unset
        if isinstance(self.video_confidence_threshold, Unset):
            video_confidence_threshold = UNSET
        else:
            video_confidence_threshold = self.video_confidence_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if frame_confidence_threshold is not UNSET:
            field_dict["frame_confidence_threshold"] = frame_confidence_threshold
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if video_confidence_threshold is not UNSET:
            field_dict["video_confidence_threshold"] = video_confidence_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_frame_confidence_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        frame_confidence_threshold = _parse_frame_confidence_threshold(
            d.pop("frame_confidence_threshold", UNSET)
        )

        def _parse_is_system(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_system = _parse_is_system(d.pop("is_system", UNSET))

        def _parse_video_confidence_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_confidence_threshold = _parse_video_confidence_threshold(
            d.pop("video_confidence_threshold", UNSET)
        )

        analysis_profile_google_video_intelligence_settings_schema = cls(
            frame_confidence_threshold=frame_confidence_threshold,
            is_system=is_system,
            video_confidence_threshold=video_confidence_threshold,
        )

        analysis_profile_google_video_intelligence_settings_schema.additional_properties = d
        return analysis_profile_google_video_intelligence_settings_schema

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
