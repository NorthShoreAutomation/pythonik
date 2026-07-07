from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.segment_segment_type import SegmentSegmentType
from ..models.segment_status import SegmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drawing import Drawing
    from ..models.face_bounding_box import FaceBoundingBox
    from ..models.segment_metadata import SegmentMetadata
    from ..models.transcription_type import TranscriptionType
    from ..models.user import User


T = TypeVar("T", bound="Segment")


@_attrs_define
class Segment:
    """
    Attributes:
        segment_type (SegmentSegmentType):
        asset_id (UUID | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        drawing (Drawing | None | Unset):
        external_id (None | str | Unset):
        face_bounding_boxes (list[FaceBoundingBox] | None | Unset):
        has_drawing (Any | Unset):
        id (UUID | Unset):
        is_internal (bool | None | Unset): If set to true, the segment is only visible to internal iconik users
        keyframe_id (None | Unset | UUID):
        metadata (SegmentMetadata | Unset):
        metadata_view_id (None | Unset | UUID):
        parent_id (UUID | Unset):
        path (str | Unset):
        person_id (None | Unset | UUID):
        project_id (None | Unset | UUID): ID of a project if the segment is created from a project
        segment_checked (bool | Unset):
        segment_color (str | Unset):
        segment_text (None | str | Unset):
        segment_track (None | str | Unset):
        share_id (None | Unset | UUID): ID of a share if the segment is created from a share
        share_user_email (None | str | Unset):
        status (SegmentStatus | Unset):
        subclip_id (UUID | Unset):
        time_end_milliseconds (int | None | Unset):
        time_start_milliseconds (int | None | Unset):
        top_level (bool | Unset):
        transcription (TranscriptionType | Unset):
        transcription_id (None | Unset | UUID):
        user_first_name (str | Unset):
        user_id (UUID | Unset):
        user_info (User | Unset):
        user_last_name (str | Unset):
        user_photo (str | Unset):
        version_id (UUID | Unset):
    """

    segment_type: SegmentSegmentType
    asset_id: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    drawing: Drawing | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    face_bounding_boxes: list[FaceBoundingBox] | None | Unset = UNSET
    has_drawing: Any | Unset = UNSET
    id: UUID | Unset = UNSET
    is_internal: bool | None | Unset = UNSET
    keyframe_id: None | Unset | UUID = UNSET
    metadata: SegmentMetadata | Unset = UNSET
    metadata_view_id: None | Unset | UUID = UNSET
    parent_id: UUID | Unset = UNSET
    path: str | Unset = UNSET
    person_id: None | Unset | UUID = UNSET
    project_id: None | Unset | UUID = UNSET
    segment_checked: bool | Unset = UNSET
    segment_color: str | Unset = UNSET
    segment_text: None | str | Unset = UNSET
    segment_track: None | str | Unset = UNSET
    share_id: None | Unset | UUID = UNSET
    share_user_email: None | str | Unset = UNSET
    status: SegmentStatus | Unset = UNSET
    subclip_id: UUID | Unset = UNSET
    time_end_milliseconds: int | None | Unset = UNSET
    time_start_milliseconds: int | None | Unset = UNSET
    top_level: bool | Unset = UNSET
    transcription: TranscriptionType | Unset = UNSET
    transcription_id: None | Unset | UUID = UNSET
    user_first_name: str | Unset = UNSET
    user_id: UUID | Unset = UNSET
    user_info: User | Unset = UNSET
    user_last_name: str | Unset = UNSET
    user_photo: str | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.drawing import Drawing

        segment_type = self.segment_type.value

        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        drawing: dict[str, Any] | None | Unset
        if isinstance(self.drawing, Unset):
            drawing = UNSET
        elif isinstance(self.drawing, Drawing):
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

        has_drawing = self.has_drawing

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        elif isinstance(self.metadata_view_id, UUID):
            metadata_view_id = str(self.metadata_view_id)
        else:
            metadata_view_id = self.metadata_view_id

        parent_id: str | Unset = UNSET
        if not isinstance(self.parent_id, Unset):
            parent_id = str(self.parent_id)

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

        segment_checked = self.segment_checked

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        subclip_id: str | Unset = UNSET
        if not isinstance(self.subclip_id, Unset):
            subclip_id = str(self.subclip_id)

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

        top_level = self.top_level

        transcription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transcription, Unset):
            transcription = self.transcription.to_dict()

        transcription_id: None | str | Unset
        if isinstance(self.transcription_id, Unset):
            transcription_id = UNSET
        elif isinstance(self.transcription_id, UUID):
            transcription_id = str(self.transcription_id)
        else:
            transcription_id = self.transcription_id

        user_first_name = self.user_first_name

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        user_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict()

        user_last_name = self.user_last_name

        user_photo = self.user_photo

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

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
        from ..models.drawing import Drawing
        from ..models.face_bounding_box import FaceBoundingBox
        from ..models.segment_metadata import SegmentMetadata
        from ..models.transcription_type import TranscriptionType
        from ..models.user import User

        d = dict(src_dict)
        segment_type = SegmentSegmentType(d.pop("segment_type"))

        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        def _parse_drawing(data: object) -> Drawing | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                drawing_type_1 = Drawing.from_dict(data)

                return drawing_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Drawing | None | Unset, data)

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
        ) -> list[FaceBoundingBox] | None | Unset:
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
                    face_bounding_boxes_type_0_item = FaceBoundingBox.from_dict(
                        face_bounding_boxes_type_0_item_data
                    )

                    face_bounding_boxes_type_0.append(face_bounding_boxes_type_0_item)

                return face_bounding_boxes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FaceBoundingBox] | None | Unset, data)

        face_bounding_boxes = _parse_face_bounding_boxes(
            d.pop("face_bounding_boxes", UNSET)
        )

        has_drawing = d.pop("has_drawing", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

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

        _metadata = d.pop("metadata", UNSET)
        metadata: SegmentMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SegmentMetadata.from_dict(_metadata)

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

        _parent_id = d.pop("parent_id", UNSET)
        parent_id: UUID | Unset
        if isinstance(_parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = UUID(_parent_id)

        path = d.pop("path", UNSET)

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

        segment_checked = d.pop("segment_checked", UNSET)

        segment_color = d.pop("segment_color", UNSET)

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

        _status = d.pop("status", UNSET)
        status: SegmentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SegmentStatus(_status)

        _subclip_id = d.pop("subclip_id", UNSET)
        subclip_id: UUID | Unset
        if isinstance(_subclip_id, Unset):
            subclip_id = UNSET
        else:
            subclip_id = UUID(_subclip_id)

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

        top_level = d.pop("top_level", UNSET)

        _transcription = d.pop("transcription", UNSET)
        transcription: TranscriptionType | Unset
        if isinstance(_transcription, Unset):
            transcription = UNSET
        else:
            transcription = TranscriptionType.from_dict(_transcription)

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

        user_first_name = d.pop("user_first_name", UNSET)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        _user_info = d.pop("user_info", UNSET)
        user_info: User | Unset
        if isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = User.from_dict(_user_info)

        user_last_name = d.pop("user_last_name", UNSET)

        user_photo = d.pop("user_photo", UNSET)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        segment = cls(
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

        segment.additional_properties = d
        return segment

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
