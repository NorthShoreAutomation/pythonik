from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_face_extract_schema_object_type import (
    BulkFaceExtractSchemaObjectType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkFaceExtractSchema")


@_attrs_define
class BulkFaceExtractSchema:
    """
    Attributes:
        object_ids (list[UUID]):
        object_type (BulkFaceExtractSchemaObjectType):
        face_image_analysis_profile_id (UUID | Unset):
        face_video_analysis_profile_id (UUID | Unset):
        force (bool | Unset):  Default: False.
        include_assets (bool | Unset):
        include_collections (bool | Unset):
    """

    object_ids: list[UUID]
    object_type: BulkFaceExtractSchemaObjectType
    face_image_analysis_profile_id: UUID | Unset = UNSET
    face_video_analysis_profile_id: UUID | Unset = UNSET
    force: bool | Unset = False
    include_assets: bool | Unset = UNSET
    include_collections: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

        face_image_analysis_profile_id: str | Unset = UNSET
        if not isinstance(self.face_image_analysis_profile_id, Unset):
            face_image_analysis_profile_id = str(self.face_image_analysis_profile_id)

        face_video_analysis_profile_id: str | Unset = UNSET
        if not isinstance(self.face_video_analysis_profile_id, Unset):
            face_video_analysis_profile_id = str(self.face_video_analysis_profile_id)

        force = self.force

        include_assets = self.include_assets

        include_collections = self.include_collections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids": object_ids,
                "object_type": object_type,
            }
        )
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
        if include_assets is not UNSET:
            field_dict["include_assets"] = include_assets
        if include_collections is not UNSET:
            field_dict["include_collections"] = include_collections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        object_type = BulkFaceExtractSchemaObjectType(d.pop("object_type"))

        _face_image_analysis_profile_id = d.pop("face_image_analysis_profile_id", UNSET)
        face_image_analysis_profile_id: UUID | Unset
        if isinstance(_face_image_analysis_profile_id, Unset):
            face_image_analysis_profile_id = UNSET
        else:
            face_image_analysis_profile_id = UUID(_face_image_analysis_profile_id)

        _face_video_analysis_profile_id = d.pop("face_video_analysis_profile_id", UNSET)
        face_video_analysis_profile_id: UUID | Unset
        if isinstance(_face_video_analysis_profile_id, Unset):
            face_video_analysis_profile_id = UNSET
        else:
            face_video_analysis_profile_id = UUID(_face_video_analysis_profile_id)

        force = d.pop("force", UNSET)

        include_assets = d.pop("include_assets", UNSET)

        include_collections = d.pop("include_collections", UNSET)

        bulk_face_extract_schema = cls(
            object_ids=object_ids,
            object_type=object_type,
            face_image_analysis_profile_id=face_image_analysis_profile_id,
            face_video_analysis_profile_id=face_video_analysis_profile_id,
            force=force,
            include_assets=include_assets,
            include_collections=include_collections,
        )

        bulk_face_extract_schema.additional_properties = d
        return bulk_face_extract_schema

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
