from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisProfileIconikFaceRecognitionSettingsSchema")


@_attrs_define
class AnalysisProfileIconikFaceRecognitionSettingsSchema:
    """
    Attributes:
        directory_path (str):
        storage_id (UUID):
        confirmed_face_match_threshold (float | None | Unset):
        detection_threshold (float | None | Unset):
        is_system (bool | None | Unset):
        unconfirmed_face_match_threshold (float | None | Unset):
    """

    directory_path: str
    storage_id: UUID
    confirmed_face_match_threshold: float | None | Unset = UNSET
    detection_threshold: float | None | Unset = UNSET
    is_system: bool | None | Unset = UNSET
    unconfirmed_face_match_threshold: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directory_path = self.directory_path

        storage_id = str(self.storage_id)

        confirmed_face_match_threshold: float | None | Unset
        if isinstance(self.confirmed_face_match_threshold, Unset):
            confirmed_face_match_threshold = UNSET
        else:
            confirmed_face_match_threshold = self.confirmed_face_match_threshold

        detection_threshold: float | None | Unset
        if isinstance(self.detection_threshold, Unset):
            detection_threshold = UNSET
        else:
            detection_threshold = self.detection_threshold

        is_system: bool | None | Unset
        if isinstance(self.is_system, Unset):
            is_system = UNSET
        else:
            is_system = self.is_system

        unconfirmed_face_match_threshold: float | None | Unset
        if isinstance(self.unconfirmed_face_match_threshold, Unset):
            unconfirmed_face_match_threshold = UNSET
        else:
            unconfirmed_face_match_threshold = self.unconfirmed_face_match_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "directory_path": directory_path,
                "storage_id": storage_id,
            }
        )
        if confirmed_face_match_threshold is not UNSET:
            field_dict["confirmed_face_match_threshold"] = (
                confirmed_face_match_threshold
            )
        if detection_threshold is not UNSET:
            field_dict["detection_threshold"] = detection_threshold
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if unconfirmed_face_match_threshold is not UNSET:
            field_dict["unconfirmed_face_match_threshold"] = (
                unconfirmed_face_match_threshold
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directory_path = d.pop("directory_path")

        storage_id = UUID(d.pop("storage_id"))

        def _parse_confirmed_face_match_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        confirmed_face_match_threshold = _parse_confirmed_face_match_threshold(
            d.pop("confirmed_face_match_threshold", UNSET)
        )

        def _parse_detection_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        detection_threshold = _parse_detection_threshold(
            d.pop("detection_threshold", UNSET)
        )

        def _parse_is_system(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_system = _parse_is_system(d.pop("is_system", UNSET))

        def _parse_unconfirmed_face_match_threshold(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unconfirmed_face_match_threshold = _parse_unconfirmed_face_match_threshold(
            d.pop("unconfirmed_face_match_threshold", UNSET)
        )

        analysis_profile_iconik_face_recognition_settings_schema = cls(
            directory_path=directory_path,
            storage_id=storage_id,
            confirmed_face_match_threshold=confirmed_face_match_threshold,
            detection_threshold=detection_threshold,
            is_system=is_system,
            unconfirmed_face_match_threshold=unconfirmed_face_match_threshold,
        )

        analysis_profile_iconik_face_recognition_settings_schema.additional_properties = d
        return analysis_profile_iconik_face_recognition_settings_schema

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
