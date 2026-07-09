from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.segment_elastic_schema_segment_type import SegmentElasticSchemaSegmentType
from ..models.segment_elastic_schema_status import SegmentElasticSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drawing_schema import DrawingSchema
    from ..models.face_bounding_box_schema import FaceBoundingBoxSchema
    from ..models.segment_elastic_schema_metadata_type_0 import (
        SegmentElasticSchemaMetadataType0,
    )
    from ..models.transcription_type import TranscriptionType
    from ..models.user import User


T = TypeVar("T", bound="SegmentElasticSchema")


@_attrs_define
class SegmentElasticSchema:
    """
    Attributes:
        segment_type (SegmentElasticSchemaSegmentType):
        asset_id (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        drawing (DrawingSchema | None | Unset):
        external_id (None | str | Unset):
        face_bounding_boxes (list[FaceBoundingBoxSchema] | None | Unset):
        has_drawing (bool | None | Unset):
        id (None | Unset | UUID):
        is_internal (bool | None | Unset): If set to true, the segment is only visible to internal iconik users
        keyframe_id (None | Unset | UUID):
        metadata (None | SegmentElasticSchemaMetadataType0 | Unset):
        metadata_view_id (None | Unset | UUID):
        parent_id (None | Unset | UUID):
        path (None | str | Unset):
        person_id (None | Unset | UUID):
        project_id (None | Unset | UUID): ID of a project if the segment is created from a project
        segment_checked (bool | None | Unset):
        segment_color (None | str | Unset):
        segment_text (None | str | Unset):
        segment_track (None | str | Unset):
        share_id (None | Unset | UUID): ID of a share if the segment is created from a share
        share_user_email (None | str | Unset):
        status (None | SegmentElasticSchemaStatus | Unset):
        subclip_id (None | Unset | UUID):
        time_end_milliseconds (int | None | Unset):
        time_start_milliseconds (int | None | Unset):
        top_level (bool | None | Unset):
        transcription (None | TranscriptionType | Unset):
        transcription_id (None | Unset | UUID):
        user_first_name (None | str | Unset):
        user_id (None | Unset | UUID):
        user_info (None | Unset | User):
        user_last_name (None | str | Unset):
        user_photo (None | str | Unset):
        version_id (None | Unset | UUID):
    """

    segment_type: SegmentElasticSchemaSegmentType
    asset_id: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    drawing: DrawingSchema | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    face_bounding_boxes: list[FaceBoundingBoxSchema] | None | Unset = UNSET
    has_drawing: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_internal: bool | None | Unset = UNSET
    keyframe_id: None | Unset | UUID = UNSET
    metadata: None | SegmentElasticSchemaMetadataType0 | Unset = UNSET
    metadata_view_id: None | Unset | UUID = UNSET
    parent_id: None | Unset | UUID = UNSET
    path: None | str | Unset = UNSET
    person_id: None | Unset | UUID = UNSET
    project_id: None | Unset | UUID = UNSET
    segment_checked: bool | None | Unset = UNSET
    segment_color: None | str | Unset = UNSET
    segment_text: None | str | Unset = UNSET
    segment_track: None | str | Unset = UNSET
    share_id: None | Unset | UUID = UNSET
    share_user_email: None | str | Unset = UNSET
    status: None | SegmentElasticSchemaStatus | Unset = UNSET
    subclip_id: None | Unset | UUID = UNSET
    time_end_milliseconds: int | None | Unset = UNSET
    time_start_milliseconds: int | None | Unset = UNSET
    top_level: bool | None | Unset = UNSET
    transcription: None | TranscriptionType | Unset = UNSET
    transcription_id: None | Unset | UUID = UNSET
    user_first_name: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    user_info: None | Unset | User = UNSET
    user_last_name: None | str | Unset = UNSET
    user_photo: None | str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.drawing_schema import DrawingSchema
        from ..models.segment_elastic_schema_metadata_type_0 import (
            SegmentElasticSchemaMetadataType0,
        )
        from ..models.transcription_type import TranscriptionType
        from ..models.user import User

        segment_type = self.segment_type.value

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        drawing: dict[str, Any] | None | Unset
        if isinstance(self.drawing, Unset):
            drawing = UNSET
        elif isinstance(self.drawing, DrawingSchema):
            drawing = self.drawing.to_dict()
        else:
            drawing = self.drawing

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        face_bounding_boxes: list[dict[str, Any]] | None | Unset
        if isinstance(self.face_bounding_boxes, Unset):
            face_bounding_boxes = UNSET
        elif isinstance(self.face_bounding_boxes, list):
            face_bounding_boxes = []
            for face_bounding_boxes_type_0_item_data in self.face_bounding_boxes:
                face_bounding_boxes_type_0_item = (
                    face_bounding_boxes_type_0_item_data.to_dict()
                )
                face_bounding_boxes.append(face_bounding_boxes_type_0_item)

        else:
            face_bounding_boxes = self.face_bounding_boxes

        has_drawing: bool | None | Unset
        if isinstance(self.has_drawing, Unset):
            has_drawing = UNSET
        else:
            has_drawing = self.has_drawing

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_internal: bool | None | Unset
        if isinstance(self.is_internal, Unset):
            is_internal = UNSET
        else:
            is_internal = self.is_internal

        keyframe_id: None | str | Unset
        if isinstance(self.keyframe_id, Unset):
            keyframe_id = UNSET
        elif isinstance(self.keyframe_id, UUID):
            keyframe_id = str(self.keyframe_id)
        else:
            keyframe_id = self.keyframe_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SegmentElasticSchemaMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        elif isinstance(self.metadata_view_id, UUID):
            metadata_view_id = str(self.metadata_view_id)
        else:
            metadata_view_id = self.metadata_view_id

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        person_id: None | str | Unset
        if isinstance(self.person_id, Unset):
            person_id = UNSET
        elif isinstance(self.person_id, UUID):
            person_id = str(self.person_id)
        else:
            person_id = self.person_id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        segment_checked: bool | None | Unset
        if isinstance(self.segment_checked, Unset):
            segment_checked = UNSET
        else:
            segment_checked = self.segment_checked

        segment_color: None | str | Unset
        if isinstance(self.segment_color, Unset):
            segment_color = UNSET
        else:
            segment_color = self.segment_color

        segment_text: None | str | Unset
        if isinstance(self.segment_text, Unset):
            segment_text = UNSET
        else:
            segment_text = self.segment_text

        segment_track: None | str | Unset
        if isinstance(self.segment_track, Unset):
            segment_track = UNSET
        else:
            segment_track = self.segment_track

        share_id: None | str | Unset
        if isinstance(self.share_id, Unset):
            share_id = UNSET
        elif isinstance(self.share_id, UUID):
            share_id = str(self.share_id)
        else:
            share_id = self.share_id

        share_user_email: None | str | Unset
        if isinstance(self.share_user_email, Unset):
            share_user_email = UNSET
        else:
            share_user_email = self.share_user_email

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SegmentElasticSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        subclip_id: None | str | Unset
        if isinstance(self.subclip_id, Unset):
            subclip_id = UNSET
        elif isinstance(self.subclip_id, UUID):
            subclip_id = str(self.subclip_id)
        else:
            subclip_id = self.subclip_id

        time_end_milliseconds: int | None | Unset
        if isinstance(self.time_end_milliseconds, Unset):
            time_end_milliseconds = UNSET
        else:
            time_end_milliseconds = self.time_end_milliseconds

        time_start_milliseconds: int | None | Unset
        if isinstance(self.time_start_milliseconds, Unset):
            time_start_milliseconds = UNSET
        else:
            time_start_milliseconds = self.time_start_milliseconds

        top_level: bool | None | Unset
        if isinstance(self.top_level, Unset):
            top_level = UNSET
        else:
            top_level = self.top_level

        transcription: dict[str, Any] | None | Unset
        if isinstance(self.transcription, Unset):
            transcription = UNSET
        elif isinstance(self.transcription, TranscriptionType):
            transcription = self.transcription.to_dict()
        else:
            transcription = self.transcription

        transcription_id: None | str | Unset
        if isinstance(self.transcription_id, Unset):
            transcription_id = UNSET
        elif isinstance(self.transcription_id, UUID):
            transcription_id = str(self.transcription_id)
        else:
            transcription_id = self.transcription_id

        user_first_name: None | str | Unset
        if isinstance(self.user_first_name, Unset):
            user_first_name = UNSET
        else:
            user_first_name = self.user_first_name

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        user_info: dict[str, Any] | None | Unset
        if isinstance(self.user_info, Unset):
            user_info = UNSET
        elif isinstance(self.user_info, User):
            user_info = self.user_info.to_dict()
        else:
            user_info = self.user_info

        user_last_name: None | str | Unset
        if isinstance(self.user_last_name, Unset):
            user_last_name = UNSET
        else:
            user_last_name = self.user_last_name

        user_photo: None | str | Unset
        if isinstance(self.user_photo, Unset):
            user_photo = UNSET
        else:
            user_photo = self.user_photo

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segment_type": segment_type,
            }
        )
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if drawing is not UNSET:
            field_dict["drawing"] = drawing
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if face_bounding_boxes is not UNSET:
            field_dict["face_bounding_boxes"] = face_bounding_boxes
        if has_drawing is not UNSET:
            field_dict["has_drawing"] = has_drawing
        if id is not UNSET:
            field_dict["id"] = id
        if is_internal is not UNSET:
            field_dict["is_internal"] = is_internal
        if keyframe_id is not UNSET:
            field_dict["keyframe_id"] = keyframe_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if metadata_view_id is not UNSET:
            field_dict["metadata_view_id"] = metadata_view_id
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if path is not UNSET:
            field_dict["path"] = path
        if person_id is not UNSET:
            field_dict["person_id"] = person_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if segment_checked is not UNSET:
            field_dict["segment_checked"] = segment_checked
        if segment_color is not UNSET:
            field_dict["segment_color"] = segment_color
        if segment_text is not UNSET:
            field_dict["segment_text"] = segment_text
        if segment_track is not UNSET:
            field_dict["segment_track"] = segment_track
        if share_id is not UNSET:
            field_dict["share_id"] = share_id
        if share_user_email is not UNSET:
            field_dict["share_user_email"] = share_user_email
        if status is not UNSET:
            field_dict["status"] = status
        if subclip_id is not UNSET:
            field_dict["subclip_id"] = subclip_id
        if time_end_milliseconds is not UNSET:
            field_dict["time_end_milliseconds"] = time_end_milliseconds
        if time_start_milliseconds is not UNSET:
            field_dict["time_start_milliseconds"] = time_start_milliseconds
        if top_level is not UNSET:
            field_dict["top_level"] = top_level
        if transcription is not UNSET:
            field_dict["transcription"] = transcription
        if transcription_id is not UNSET:
            field_dict["transcription_id"] = transcription_id
        if user_first_name is not UNSET:
            field_dict["user_first_name"] = user_first_name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_info is not UNSET:
            field_dict["user_info"] = user_info
        if user_last_name is not UNSET:
            field_dict["user_last_name"] = user_last_name
        if user_photo is not UNSET:
            field_dict["user_photo"] = user_photo
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drawing_schema import DrawingSchema
        from ..models.face_bounding_box_schema import FaceBoundingBoxSchema
        from ..models.segment_elastic_schema_metadata_type_0 import (
            SegmentElasticSchemaMetadataType0,
        )
        from ..models.transcription_type import TranscriptionType
        from ..models.user import User

        d = dict(src_dict)
        segment_type = SegmentElasticSchemaSegmentType(d.pop("segment_type"))

        def _parse_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_id_type_0 = UUID(data)

                return asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_drawing(data: object) -> DrawingSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                drawing_type_1 = DrawingSchema.from_dict(data)

                return drawing_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DrawingSchema | None | Unset, data)

        drawing = _parse_drawing(d.pop("drawing", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_face_bounding_boxes(
            data: object,
        ) -> list[FaceBoundingBoxSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                face_bounding_boxes_type_0 = []
                _face_bounding_boxes_type_0 = data
                for face_bounding_boxes_type_0_item_data in _face_bounding_boxes_type_0:
                    face_bounding_boxes_type_0_item = FaceBoundingBoxSchema.from_dict(
                        face_bounding_boxes_type_0_item_data
                    )

                    face_bounding_boxes_type_0.append(face_bounding_boxes_type_0_item)

                return face_bounding_boxes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FaceBoundingBoxSchema] | None | Unset, data)

        face_bounding_boxes = _parse_face_bounding_boxes(
            d.pop("face_bounding_boxes", UNSET)
        )

        def _parse_has_drawing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_drawing = _parse_has_drawing(d.pop("has_drawing", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_is_internal(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_internal = _parse_is_internal(d.pop("is_internal", UNSET))

        def _parse_keyframe_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                keyframe_id_type_0 = UUID(data)

                return keyframe_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        keyframe_id = _parse_keyframe_id(d.pop("keyframe_id", UNSET))

        def _parse_metadata(
            data: object,
        ) -> None | SegmentElasticSchemaMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SegmentElasticSchemaMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentElasticSchemaMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_metadata_view_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_view_id_type_0 = UUID(data)

                return metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        metadata_view_id = _parse_metadata_view_id(d.pop("metadata_view_id", UNSET))

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_person_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                person_id_type_0 = UUID(data)

                return person_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        person_id = _parse_person_id(d.pop("person_id", UNSET))

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_segment_checked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        segment_checked = _parse_segment_checked(d.pop("segment_checked", UNSET))

        def _parse_segment_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment_color = _parse_segment_color(d.pop("segment_color", UNSET))

        def _parse_segment_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment_text = _parse_segment_text(d.pop("segment_text", UNSET))

        def _parse_segment_track(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment_track = _parse_segment_track(d.pop("segment_track", UNSET))

        def _parse_share_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_id_type_0 = UUID(data)

                return share_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        share_id = _parse_share_id(d.pop("share_id", UNSET))

        def _parse_share_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        share_user_email = _parse_share_user_email(d.pop("share_user_email", UNSET))

        def _parse_status(data: object) -> None | SegmentElasticSchemaStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = SegmentElasticSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentElasticSchemaStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_subclip_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subclip_id_type_0 = UUID(data)

                return subclip_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subclip_id = _parse_subclip_id(d.pop("subclip_id", UNSET))

        def _parse_time_end_milliseconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_end_milliseconds = _parse_time_end_milliseconds(
            d.pop("time_end_milliseconds", UNSET)
        )

        def _parse_time_start_milliseconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_start_milliseconds = _parse_time_start_milliseconds(
            d.pop("time_start_milliseconds", UNSET)
        )

        def _parse_top_level(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        top_level = _parse_top_level(d.pop("top_level", UNSET))

        def _parse_transcription(data: object) -> None | TranscriptionType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcription_type_1 = TranscriptionType.from_dict(data)

                return transcription_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TranscriptionType | Unset, data)

        transcription = _parse_transcription(d.pop("transcription", UNSET))

        def _parse_transcription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transcription_id_type_0 = UUID(data)

                return transcription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        transcription_id = _parse_transcription_id(d.pop("transcription_id", UNSET))

        def _parse_user_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_first_name = _parse_user_first_name(d.pop("user_first_name", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_user_info(data: object) -> None | Unset | User:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_info_type_1 = User.from_dict(data)

                return user_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | User, data)

        user_info = _parse_user_info(d.pop("user_info", UNSET))

        def _parse_user_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_last_name = _parse_user_last_name(d.pop("user_last_name", UNSET))

        def _parse_user_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_photo = _parse_user_photo(d.pop("user_photo", UNSET))

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        segment_elastic_schema = cls(
            segment_type=segment_type,
            asset_id=asset_id,
            date_created=date_created,
            date_modified=date_modified,
            drawing=drawing,
            external_id=external_id,
            face_bounding_boxes=face_bounding_boxes,
            has_drawing=has_drawing,
            id=id,
            is_internal=is_internal,
            keyframe_id=keyframe_id,
            metadata=metadata,
            metadata_view_id=metadata_view_id,
            parent_id=parent_id,
            path=path,
            person_id=person_id,
            project_id=project_id,
            segment_checked=segment_checked,
            segment_color=segment_color,
            segment_text=segment_text,
            segment_track=segment_track,
            share_id=share_id,
            share_user_email=share_user_email,
            status=status,
            subclip_id=subclip_id,
            time_end_milliseconds=time_end_milliseconds,
            time_start_milliseconds=time_start_milliseconds,
            top_level=top_level,
            transcription=transcription,
            transcription_id=transcription_id,
            user_first_name=user_first_name,
            user_id=user_id,
            user_info=user_info,
            user_last_name=user_last_name,
            user_photo=user_photo,
            version_id=version_id,
        )

        segment_elastic_schema.additional_properties = d
        return segment_elastic_schema

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
