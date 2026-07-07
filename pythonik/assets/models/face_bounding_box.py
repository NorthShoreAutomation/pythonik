from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.face_landmark import FaceLandmark


T = TypeVar("T", bound="FaceBoundingBox")


@_attrs_define
class FaceBoundingBox:
    """
    Attributes:
        person_version_face_id (UUID):
        bounding_box (list[float] | Unset):
        landmarks (list[FaceLandmark] | None | Unset):
        timestamp_ms (int | Unset):
    """

    person_version_face_id: UUID
    bounding_box: list[float] | Unset = UNSET
    landmarks: list[FaceLandmark] | None | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_version_face_id = str(self.person_version_face_id)

        bounding_box: list[float] | Unset = UNSET
        if not isinstance(self.bounding_box, Unset):
            bounding_box = self.bounding_box

        landmarks: list[dict[str, Any]] | None | Unset
        if isinstance(self.landmarks, Unset):
            landmarks = UNSET
        elif isinstance(self.landmarks, list):
            landmarks = []
            for landmarks_type_0_item_data in self.landmarks:
                landmarks_type_0_item = landmarks_type_0_item_data.to_dict()
                landmarks.append(landmarks_type_0_item)

        else:
            landmarks = self.landmarks

        timestamp_ms = self.timestamp_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "person_version_face_id": person_version_face_id,
            }
        )
        if bounding_box is not UNSET:
            field_dict["bounding_box"] = bounding_box
        if landmarks is not UNSET:
            field_dict["landmarks"] = landmarks
        if timestamp_ms is not UNSET:
            field_dict["timestamp_ms"] = timestamp_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.face_landmark import FaceLandmark

        d = dict(src_dict)
        person_version_face_id = UUID(d.pop("person_version_face_id"))

        bounding_box = cast(list[float], d.pop("bounding_box", UNSET))

        def _parse_landmarks(data: object) -> list[FaceLandmark] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                landmarks_type_0 = []
                _landmarks_type_0 = data
                for landmarks_type_0_item_data in _landmarks_type_0:
                    landmarks_type_0_item = FaceLandmark.from_dict(
                        landmarks_type_0_item_data
                    )

                    landmarks_type_0.append(landmarks_type_0_item)

                return landmarks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FaceLandmark] | None | Unset, data)

        landmarks = _parse_landmarks(d.pop("landmarks", UNSET))

        timestamp_ms = d.pop("timestamp_ms", UNSET)

        face_bounding_box = cls(
            person_version_face_id=person_version_face_id,
            bounding_box=bounding_box,
            landmarks=landmarks,
            timestamp_ms=timestamp_ms,
        )

        face_bounding_box.additional_properties = d
        return face_bounding_box

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
