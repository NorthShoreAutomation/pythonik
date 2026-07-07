from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractFacesParameters")


@_attrs_define
class ExtractFacesParameters:
    """
    Attributes:
        face_image_analysis_profile_id (None | Unset | UUID):
        face_video_analysis_profile_id (None | Unset | UUID):
        force (bool | Unset):  Default: False.
    """

    face_image_analysis_profile_id: None | Unset | UUID = UNSET
    face_video_analysis_profile_id: None | Unset | UUID = UNSET
    force: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        face_image_analysis_profile_id: None | str | Unset
        if isinstance(self.face_image_analysis_profile_id, Unset):
            face_image_analysis_profile_id = UNSET
        elif isinstance(self.face_image_analysis_profile_id, UUID):
            face_image_analysis_profile_id = str(self.face_image_analysis_profile_id)
        else:
            face_image_analysis_profile_id = self.face_image_analysis_profile_id

        face_video_analysis_profile_id: None | str | Unset
        if isinstance(self.face_video_analysis_profile_id, Unset):
            face_video_analysis_profile_id = UNSET
        elif isinstance(self.face_video_analysis_profile_id, UUID):
            face_video_analysis_profile_id = str(self.face_video_analysis_profile_id)
        else:
            face_video_analysis_profile_id = self.face_video_analysis_profile_id

        force = self.force

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if face_image_analysis_profile_id is not UNSET:
            field_dict["face_image_analysis_profile_id"] = (
                face_image_analysis_profile_id
            )
        if face_video_analysis_profile_id is not UNSET:
            field_dict["face_video_analysis_profile_id"] = (
                face_video_analysis_profile_id
            )
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_face_image_analysis_profile_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                face_image_analysis_profile_id_type_0 = UUID(data)

                return face_image_analysis_profile_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        face_image_analysis_profile_id = _parse_face_image_analysis_profile_id(
            d.pop("face_image_analysis_profile_id", UNSET)
        )

        def _parse_face_video_analysis_profile_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                face_video_analysis_profile_id_type_0 = UUID(data)

                return face_video_analysis_profile_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        face_video_analysis_profile_id = _parse_face_video_analysis_profile_id(
            d.pop("face_video_analysis_profile_id", UNSET)
        )

        force = d.pop("force", UNSET)

        extract_faces_parameters = cls(
            face_image_analysis_profile_id=face_image_analysis_profile_id,
            face_video_analysis_profile_id=face_video_analysis_profile_id,
            force=force,
        )

        extract_faces_parameters.additional_properties = d
        return extract_faces_parameters

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
