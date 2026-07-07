from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
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
        confirmed_face_match_threshold (float | Unset):
        detection_threshold (float | Unset):
        is_system (bool | Unset):
        unconfirmed_face_match_threshold (float | Unset):
    """

    directory_path: str
    storage_id: UUID
    confirmed_face_match_threshold: float | Unset = UNSET
    detection_threshold: float | Unset = UNSET
    is_system: bool | Unset = UNSET
    unconfirmed_face_match_threshold: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directory_path = self.directory_path

        storage_id = str(self.storage_id)

        confirmed_face_match_threshold = self.confirmed_face_match_threshold

        detection_threshold = self.detection_threshold

        is_system = self.is_system

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

        confirmed_face_match_threshold = d.pop("confirmed_face_match_threshold", UNSET)

        detection_threshold = d.pop("detection_threshold", UNSET)

        is_system = d.pop("is_system", UNSET)

        unconfirmed_face_match_threshold = d.pop(
            "unconfirmed_face_match_threshold", UNSET
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
