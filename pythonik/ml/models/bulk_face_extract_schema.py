from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        face_image_analysis_profile_id (None | Unset | UUID):
        face_video_analysis_profile_id (None | Unset | UUID):
        force (bool | None | Unset):  Default: False.
        include_assets (bool | None | Unset):
        include_collections (bool | None | Unset):
    """

    object_ids: list[UUID]
    object_type: BulkFaceExtractSchemaObjectType
    face_image_analysis_profile_id: None | Unset | UUID = UNSET
    face_video_analysis_profile_id: None | Unset | UUID = UNSET
    force: bool | None | Unset = False
    include_assets: bool | None | Unset = UNSET
    include_collections: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

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

        force: bool | None | Unset
        if isinstance(self.force, Unset):
            force = UNSET
        else:
            force = self.force

        include_assets: bool | None | Unset
        if isinstance(self.include_assets, Unset):
            include_assets = UNSET
        else:
            include_assets = self.include_assets

        include_collections: bool | None | Unset
        if isinstance(self.include_collections, Unset):
            include_collections = UNSET
        else:
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

        def _parse_force(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force = _parse_force(d.pop("force", UNSET))

        def _parse_include_assets(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_assets = _parse_include_assets(d.pop("include_assets", UNSET))

        def _parse_include_collections(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_collections = _parse_include_collections(
            d.pop("include_collections", UNSET)
        )

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
