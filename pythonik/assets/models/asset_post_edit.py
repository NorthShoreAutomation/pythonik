from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_post_edit_analyze_status import AssetPostEditAnalyzeStatus
from ..models.asset_post_edit_archive_status import AssetPostEditArchiveStatus
from ..models.asset_post_edit_face_recognition_status import (
    AssetPostEditFaceRecognitionStatus,
)
from ..models.asset_post_edit_publication_status import AssetPostEditPublicationStatus
from ..models.asset_post_edit_status import AssetPostEditStatus
from ..models.asset_post_edit_type import AssetPostEditType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="AssetPostEdit")


@_attrs_define
class AssetPostEdit:
    """
    Attributes:
        id (UUID):
        analyze_status (AssetPostEditAnalyzeStatus | Unset):
        archive_status (AssetPostEditArchiveStatus | Unset):
        category (None | str | Unset):
        clip_aspect_ratio (None | str | Unset):
        clip_duration (float | None | Unset):
        clip_id (int | None | Unset):
        clip_mime_type (None | str | Unset):
        created_by_user (UUID | Unset):
        created_by_user_info (User | Unset):
        custom_keyframe (None | Unset | UUID):
        custom_poster (None | Unset | UUID):
        date_created (datetime.datetime | Unset):
        date_deleted (datetime.datetime | Unset):
        date_imported (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        date_published_at (datetime.datetime | Unset):
        date_viewed (datetime.datetime | Unset):
        deleted_by_user (UUID | Unset):
        deleted_by_user_info (User | Unset):
        destination_icon (None | str | Unset):
        destination_name (None | str | Unset):
        destination_picture (None | str | Unset):
        destination_type (None | str | Unset):
        external_id (None | str | Unset):
        external_link (None | str | Unset):
        face_recognition_status (AssetPostEditFaceRecognitionStatus | Unset):
        favoured (bool | Unset):
        has_unconfirmed_persons (bool | Unset):
        is_blocked (bool | Unset):
        is_online (bool | Unset):
        last_archive_restore_date (datetime.datetime | Unset):
        likes (int | None | Unset):  Default: 0.
        limit_download_to_groups (list[UUID] | None | Unset):
        original_asset_id (UUID | Unset):
        original_segment_id (UUID | Unset):
        original_version_id (UUID | Unset):
        person_ids (list[UUID] | None | Unset):
        publication_status (AssetPostEditPublicationStatus | Unset):  Default: AssetPostEditPublicationStatus.PUBLISHED.
        site_name (None | str | Unset):
        status (AssetPostEditStatus | Unset):
        time_end_milliseconds (int | Unset):
        time_start_milliseconds (int | Unset):
        title (str | Unset):
        type_ (AssetPostEditType | Unset):
        updated_by_user (UUID | Unset):
        updated_by_user_info (User | Unset):
        views (int | None | Unset):  Default: 0.
        warning (None | str | Unset):
    """

    id: UUID
    analyze_status: AssetPostEditAnalyzeStatus | Unset = UNSET
    archive_status: AssetPostEditArchiveStatus | Unset = UNSET
    category: None | str | Unset = UNSET
    clip_aspect_ratio: None | str | Unset = UNSET
    clip_duration: float | None | Unset = UNSET
    clip_id: int | None | Unset = UNSET
    clip_mime_type: None | str | Unset = UNSET
    created_by_user: UUID | Unset = UNSET
    created_by_user_info: User | Unset = UNSET
    custom_keyframe: None | Unset | UUID = UNSET
    custom_poster: None | Unset | UUID = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_deleted: datetime.datetime | Unset = UNSET
    date_imported: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    date_published_at: datetime.datetime | Unset = UNSET
    date_viewed: datetime.datetime | Unset = UNSET
    deleted_by_user: UUID | Unset = UNSET
    deleted_by_user_info: User | Unset = UNSET
    destination_icon: None | str | Unset = UNSET
    destination_name: None | str | Unset = UNSET
    destination_picture: None | str | Unset = UNSET
    destination_type: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    external_link: None | str | Unset = UNSET
    face_recognition_status: AssetPostEditFaceRecognitionStatus | Unset = UNSET
    favoured: bool | Unset = UNSET
    has_unconfirmed_persons: bool | Unset = UNSET
    is_blocked: bool | Unset = UNSET
    is_online: bool | Unset = UNSET
    last_archive_restore_date: datetime.datetime | Unset = UNSET
    likes: int | None | Unset = 0
    limit_download_to_groups: list[UUID] | None | Unset = UNSET
    original_asset_id: UUID | Unset = UNSET
    original_segment_id: UUID | Unset = UNSET
    original_version_id: UUID | Unset = UNSET
    person_ids: list[UUID] | None | Unset = UNSET
    publication_status: AssetPostEditPublicationStatus | Unset = (
        AssetPostEditPublicationStatus.PUBLISHED
    )
    site_name: None | str | Unset = UNSET
    status: AssetPostEditStatus | Unset = UNSET
    time_end_milliseconds: int | Unset = UNSET
    time_start_milliseconds: int | Unset = UNSET
    title: str | Unset = UNSET
    type_: AssetPostEditType | Unset = UNSET
    updated_by_user: UUID | Unset = UNSET
    updated_by_user_info: User | Unset = UNSET
    views: int | None | Unset = 0
    warning: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        analyze_status: str | Unset = UNSET
        if not isinstance(self.analyze_status, Unset):
            analyze_status = self.analyze_status.value

        archive_status: str | Unset = UNSET
        if not isinstance(self.archive_status, Unset):
            archive_status = self.archive_status.value

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        clip_aspect_ratio: None | str | Unset
        if isinstance(self.clip_aspect_ratio, Unset):
            clip_aspect_ratio = UNSET
        else:
            clip_aspect_ratio = self.clip_aspect_ratio

        clip_duration: float | None | Unset
        if isinstance(self.clip_duration, Unset):
            clip_duration = UNSET
        else:
            clip_duration = self.clip_duration

        clip_id: int | None | Unset
        if isinstance(self.clip_id, Unset):
            clip_id = UNSET
        else:
            clip_id = self.clip_id

        clip_mime_type: None | str | Unset
        if isinstance(self.clip_mime_type, Unset):
            clip_mime_type = UNSET
        else:
            clip_mime_type = self.clip_mime_type

        created_by_user: str | Unset = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = str(self.created_by_user)

        created_by_user_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by_user_info, Unset):
            created_by_user_info = self.created_by_user_info.to_dict()

        custom_keyframe: None | str | Unset
        if isinstance(self.custom_keyframe, Unset):
            custom_keyframe = UNSET
        elif isinstance(self.custom_keyframe, UUID):
            custom_keyframe = str(self.custom_keyframe)
        else:
            custom_keyframe = self.custom_keyframe

        custom_poster: None | str | Unset
        if isinstance(self.custom_poster, Unset):
            custom_poster = UNSET
        elif isinstance(self.custom_poster, UUID):
            custom_poster = str(self.custom_poster)
        else:
            custom_poster = self.custom_poster

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_deleted: str | Unset = UNSET
        if not isinstance(self.date_deleted, Unset):
            date_deleted = self.date_deleted.isoformat()

        date_imported: str | Unset = UNSET
        if not isinstance(self.date_imported, Unset):
            date_imported = self.date_imported.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        date_published_at: str | Unset = UNSET
        if not isinstance(self.date_published_at, Unset):
            date_published_at = self.date_published_at.isoformat()

        date_viewed: str | Unset = UNSET
        if not isinstance(self.date_viewed, Unset):
            date_viewed = self.date_viewed.isoformat()

        deleted_by_user: str | Unset = UNSET
        if not isinstance(self.deleted_by_user, Unset):
            deleted_by_user = str(self.deleted_by_user)

        deleted_by_user_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_by_user_info, Unset):
            deleted_by_user_info = self.deleted_by_user_info.to_dict()

        destination_icon: None | str | Unset
        if isinstance(self.destination_icon, Unset):
            destination_icon = UNSET
        else:
            destination_icon = self.destination_icon

        destination_name: None | str | Unset
        if isinstance(self.destination_name, Unset):
            destination_name = UNSET
        else:
            destination_name = self.destination_name

        destination_picture: None | str | Unset
        if isinstance(self.destination_picture, Unset):
            destination_picture = UNSET
        else:
            destination_picture = self.destination_picture

        destination_type: None | str | Unset
        if isinstance(self.destination_type, Unset):
            destination_type = UNSET
        else:
            destination_type = self.destination_type

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_link: None | str | Unset
        if isinstance(self.external_link, Unset):
            external_link = UNSET
        else:
            external_link = self.external_link

        face_recognition_status: str | Unset = UNSET
        if not isinstance(self.face_recognition_status, Unset):
            face_recognition_status = self.face_recognition_status.value

        favoured = self.favoured

        has_unconfirmed_persons = self.has_unconfirmed_persons

        is_blocked = self.is_blocked

        is_online = self.is_online

        last_archive_restore_date: str | Unset = UNSET
        if not isinstance(self.last_archive_restore_date, Unset):
            last_archive_restore_date = self.last_archive_restore_date.isoformat()

        likes: int | None | Unset
        if isinstance(self.likes, Unset):
            likes = UNSET
        else:
            likes = self.likes

        limit_download_to_groups: list[str] | None | Unset
        if isinstance(self.limit_download_to_groups, Unset):
            limit_download_to_groups = UNSET
        elif isinstance(self.limit_download_to_groups, list):
            limit_download_to_groups = []
            for (
                limit_download_to_groups_type_0_item_data
            ) in self.limit_download_to_groups:
                limit_download_to_groups_type_0_item = str(
                    limit_download_to_groups_type_0_item_data
                )
                limit_download_to_groups.append(limit_download_to_groups_type_0_item)

        else:
            limit_download_to_groups = self.limit_download_to_groups

        original_asset_id: str | Unset = UNSET
        if not isinstance(self.original_asset_id, Unset):
            original_asset_id = str(self.original_asset_id)

        original_segment_id: str | Unset = UNSET
        if not isinstance(self.original_segment_id, Unset):
            original_segment_id = str(self.original_segment_id)

        original_version_id: str | Unset = UNSET
        if not isinstance(self.original_version_id, Unset):
            original_version_id = str(self.original_version_id)

        person_ids: list[str] | None | Unset
        if isinstance(self.person_ids, Unset):
            person_ids = UNSET
        elif isinstance(self.person_ids, list):
            person_ids = []
            for person_ids_type_0_item_data in self.person_ids:
                person_ids_type_0_item = str(person_ids_type_0_item_data)
                person_ids.append(person_ids_type_0_item)

        else:
            person_ids = self.person_ids

        publication_status: str | Unset = UNSET
        if not isinstance(self.publication_status, Unset):
            publication_status = self.publication_status.value

        site_name: None | str | Unset
        if isinstance(self.site_name, Unset):
            site_name = UNSET
        else:
            site_name = self.site_name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        time_end_milliseconds = self.time_end_milliseconds

        time_start_milliseconds = self.time_start_milliseconds

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_by_user: str | Unset = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = str(self.updated_by_user)

        updated_by_user_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_by_user_info, Unset):
            updated_by_user_info = self.updated_by_user_info.to_dict()

        views: int | None | Unset
        if isinstance(self.views, Unset):
            views = UNSET
        else:
            views = self.views

        warning: None | str | Unset
        if isinstance(self.warning, Unset):
            warning = UNSET
        else:
            warning = self.warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if analyze_status is not UNSET:
            field_dict["analyze_status"] = analyze_status
        if archive_status is not UNSET:
            field_dict["archive_status"] = archive_status
        if category is not UNSET:
            field_dict["category"] = category
        if clip_aspect_ratio is not UNSET:
            field_dict["clip_aspect_ratio"] = clip_aspect_ratio
        if clip_duration is not UNSET:
            field_dict["clip_duration"] = clip_duration
        if clip_id is not UNSET:
            field_dict["clip_id"] = clip_id
        if clip_mime_type is not UNSET:
            field_dict["clip_mime_type"] = clip_mime_type
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if created_by_user_info is not UNSET:
            field_dict["created_by_user_info"] = created_by_user_info
        if custom_keyframe is not UNSET:
            field_dict["custom_keyframe"] = custom_keyframe
        if custom_poster is not UNSET:
            field_dict["custom_poster"] = custom_poster
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_deleted is not UNSET:
            field_dict["date_deleted"] = date_deleted
        if date_imported is not UNSET:
            field_dict["date_imported"] = date_imported
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if date_published_at is not UNSET:
            field_dict["date_published_at"] = date_published_at
        if date_viewed is not UNSET:
            field_dict["date_viewed"] = date_viewed
        if deleted_by_user is not UNSET:
            field_dict["deleted_by_user"] = deleted_by_user
        if deleted_by_user_info is not UNSET:
            field_dict["deleted_by_user_info"] = deleted_by_user_info
        if destination_icon is not UNSET:
            field_dict["destination_icon"] = destination_icon
        if destination_name is not UNSET:
            field_dict["destination_name"] = destination_name
        if destination_picture is not UNSET:
            field_dict["destination_picture"] = destination_picture
        if destination_type is not UNSET:
            field_dict["destination_type"] = destination_type
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_link is not UNSET:
            field_dict["external_link"] = external_link
        if face_recognition_status is not UNSET:
            field_dict["face_recognition_status"] = face_recognition_status
        if favoured is not UNSET:
            field_dict["favoured"] = favoured
        if has_unconfirmed_persons is not UNSET:
            field_dict["has_unconfirmed_persons"] = has_unconfirmed_persons
        if is_blocked is not UNSET:
            field_dict["is_blocked"] = is_blocked
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if last_archive_restore_date is not UNSET:
            field_dict["last_archive_restore_date"] = last_archive_restore_date
        if likes is not UNSET:
            field_dict["likes"] = likes
        if limit_download_to_groups is not UNSET:
            field_dict["limit_download_to_groups"] = limit_download_to_groups
        if original_asset_id is not UNSET:
            field_dict["original_asset_id"] = original_asset_id
        if original_segment_id is not UNSET:
            field_dict["original_segment_id"] = original_segment_id
        if original_version_id is not UNSET:
            field_dict["original_version_id"] = original_version_id
        if person_ids is not UNSET:
            field_dict["person_ids"] = person_ids
        if publication_status is not UNSET:
            field_dict["publication_status"] = publication_status
        if site_name is not UNSET:
            field_dict["site_name"] = site_name
        if status is not UNSET:
            field_dict["status"] = status
        if time_end_milliseconds is not UNSET:
            field_dict["time_end_milliseconds"] = time_end_milliseconds
        if time_start_milliseconds is not UNSET:
            field_dict["time_start_milliseconds"] = time_start_milliseconds
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_by_user is not UNSET:
            field_dict["updated_by_user"] = updated_by_user
        if updated_by_user_info is not UNSET:
            field_dict["updated_by_user_info"] = updated_by_user_info
        if views is not UNSET:
            field_dict["views"] = views
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        _analyze_status = d.pop("analyze_status", UNSET)
        analyze_status: AssetPostEditAnalyzeStatus | Unset
        if isinstance(_analyze_status, Unset):
            analyze_status = UNSET
        else:
            analyze_status = AssetPostEditAnalyzeStatus(_analyze_status)

        _archive_status = d.pop("archive_status", UNSET)
        archive_status: AssetPostEditArchiveStatus | Unset
        if isinstance(_archive_status, Unset):
            archive_status = UNSET
        else:
            archive_status = AssetPostEditArchiveStatus(_archive_status)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_clip_aspect_ratio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        clip_aspect_ratio = _parse_clip_aspect_ratio(d.pop("clip_aspect_ratio", UNSET))

        def _parse_clip_duration(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        clip_duration = _parse_clip_duration(d.pop("clip_duration", UNSET))

        def _parse_clip_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        clip_id = _parse_clip_id(d.pop("clip_id", UNSET))

        def _parse_clip_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        clip_mime_type = _parse_clip_mime_type(d.pop("clip_mime_type", UNSET))

        _created_by_user = d.pop("created_by_user", UNSET)
        created_by_user: UUID | Unset
        if isinstance(_created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = UUID(_created_by_user)

        _created_by_user_info = d.pop("created_by_user_info", UNSET)
        created_by_user_info: User | Unset
        if isinstance(_created_by_user_info, Unset):
            created_by_user_info = UNSET
        else:
            created_by_user_info = User.from_dict(_created_by_user_info)

        def _parse_custom_keyframe(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                custom_keyframe_type_0 = UUID(data)

                return custom_keyframe_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        custom_keyframe = _parse_custom_keyframe(d.pop("custom_keyframe", UNSET))

        def _parse_custom_poster(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                custom_poster_type_0 = UUID(data)

                return custom_poster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        custom_poster = _parse_custom_poster(d.pop("custom_poster", UNSET))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_deleted = d.pop("date_deleted", UNSET)
        date_deleted: datetime.datetime | Unset
        if isinstance(_date_deleted, Unset):
            date_deleted = UNSET
        else:
            date_deleted = datetime.datetime.fromisoformat(_date_deleted)

        _date_imported = d.pop("date_imported", UNSET)
        date_imported: datetime.datetime | Unset
        if isinstance(_date_imported, Unset):
            date_imported = UNSET
        else:
            date_imported = datetime.datetime.fromisoformat(_date_imported)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        _date_published_at = d.pop("date_published_at", UNSET)
        date_published_at: datetime.datetime | Unset
        if isinstance(_date_published_at, Unset):
            date_published_at = UNSET
        else:
            date_published_at = datetime.datetime.fromisoformat(_date_published_at)

        _date_viewed = d.pop("date_viewed", UNSET)
        date_viewed: datetime.datetime | Unset
        if isinstance(_date_viewed, Unset):
            date_viewed = UNSET
        else:
            date_viewed = datetime.datetime.fromisoformat(_date_viewed)

        _deleted_by_user = d.pop("deleted_by_user", UNSET)
        deleted_by_user: UUID | Unset
        if isinstance(_deleted_by_user, Unset):
            deleted_by_user = UNSET
        else:
            deleted_by_user = UUID(_deleted_by_user)

        _deleted_by_user_info = d.pop("deleted_by_user_info", UNSET)
        deleted_by_user_info: User | Unset
        if isinstance(_deleted_by_user_info, Unset):
            deleted_by_user_info = UNSET
        else:
            deleted_by_user_info = User.from_dict(_deleted_by_user_info)

        def _parse_destination_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_icon = _parse_destination_icon(d.pop("destination_icon", UNSET))

        def _parse_destination_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_name = _parse_destination_name(d.pop("destination_name", UNSET))

        def _parse_destination_picture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_picture = _parse_destination_picture(
            d.pop("destination_picture", UNSET)
        )

        def _parse_destination_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_type = _parse_destination_type(d.pop("destination_type", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_link = _parse_external_link(d.pop("external_link", UNSET))

        _face_recognition_status = d.pop("face_recognition_status", UNSET)
        face_recognition_status: AssetPostEditFaceRecognitionStatus | Unset
        if isinstance(_face_recognition_status, Unset):
            face_recognition_status = UNSET
        else:
            face_recognition_status = AssetPostEditFaceRecognitionStatus(
                _face_recognition_status
            )

        favoured = d.pop("favoured", UNSET)

        has_unconfirmed_persons = d.pop("has_unconfirmed_persons", UNSET)

        is_blocked = d.pop("is_blocked", UNSET)

        is_online = d.pop("is_online", UNSET)

        _last_archive_restore_date = d.pop("last_archive_restore_date", UNSET)
        last_archive_restore_date: datetime.datetime | Unset
        if isinstance(_last_archive_restore_date, Unset):
            last_archive_restore_date = UNSET
        else:
            last_archive_restore_date = datetime.datetime.fromisoformat(
                _last_archive_restore_date
            )

        def _parse_likes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        likes = _parse_likes(d.pop("likes", UNSET))

        def _parse_limit_download_to_groups(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                limit_download_to_groups_type_0 = []
                _limit_download_to_groups_type_0 = data
                for (
                    limit_download_to_groups_type_0_item_data
                ) in _limit_download_to_groups_type_0:
                    limit_download_to_groups_type_0_item = UUID(
                        limit_download_to_groups_type_0_item_data
                    )

                    limit_download_to_groups_type_0.append(
                        limit_download_to_groups_type_0_item
                    )

                return limit_download_to_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        limit_download_to_groups = _parse_limit_download_to_groups(
            d.pop("limit_download_to_groups", UNSET)
        )

        _original_asset_id = d.pop("original_asset_id", UNSET)
        original_asset_id: UUID | Unset
        if isinstance(_original_asset_id, Unset):
            original_asset_id = UNSET
        else:
            original_asset_id = UUID(_original_asset_id)

        _original_segment_id = d.pop("original_segment_id", UNSET)
        original_segment_id: UUID | Unset
        if isinstance(_original_segment_id, Unset):
            original_segment_id = UNSET
        else:
            original_segment_id = UUID(_original_segment_id)

        _original_version_id = d.pop("original_version_id", UNSET)
        original_version_id: UUID | Unset
        if isinstance(_original_version_id, Unset):
            original_version_id = UNSET
        else:
            original_version_id = UUID(_original_version_id)

        def _parse_person_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                person_ids_type_0 = []
                _person_ids_type_0 = data
                for person_ids_type_0_item_data in _person_ids_type_0:
                    person_ids_type_0_item = UUID(person_ids_type_0_item_data)

                    person_ids_type_0.append(person_ids_type_0_item)

                return person_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        person_ids = _parse_person_ids(d.pop("person_ids", UNSET))

        _publication_status = d.pop("publication_status", UNSET)
        publication_status: AssetPostEditPublicationStatus | Unset
        if isinstance(_publication_status, Unset):
            publication_status = UNSET
        else:
            publication_status = AssetPostEditPublicationStatus(_publication_status)

        def _parse_site_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_name = _parse_site_name(d.pop("site_name", UNSET))

        _status = d.pop("status", UNSET)
        status: AssetPostEditStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AssetPostEditStatus(_status)

        time_end_milliseconds = d.pop("time_end_milliseconds", UNSET)

        time_start_milliseconds = d.pop("time_start_milliseconds", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AssetPostEditType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AssetPostEditType(_type_)

        _updated_by_user = d.pop("updated_by_user", UNSET)
        updated_by_user: UUID | Unset
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UUID(_updated_by_user)

        _updated_by_user_info = d.pop("updated_by_user_info", UNSET)
        updated_by_user_info: User | Unset
        if isinstance(_updated_by_user_info, Unset):
            updated_by_user_info = UNSET
        else:
            updated_by_user_info = User.from_dict(_updated_by_user_info)

        def _parse_views(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        views = _parse_views(d.pop("views", UNSET))

        def _parse_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        warning = _parse_warning(d.pop("warning", UNSET))

        asset_post_edit = cls(
            id=id,
            analyze_status=analyze_status,
            archive_status=archive_status,
            category=category,
            clip_aspect_ratio=clip_aspect_ratio,
            clip_duration=clip_duration,
            clip_id=clip_id,
            clip_mime_type=clip_mime_type,
            created_by_user=created_by_user,
            created_by_user_info=created_by_user_info,
            custom_keyframe=custom_keyframe,
            custom_poster=custom_poster,
            date_created=date_created,
            date_deleted=date_deleted,
            date_imported=date_imported,
            date_modified=date_modified,
            date_published_at=date_published_at,
            date_viewed=date_viewed,
            deleted_by_user=deleted_by_user,
            deleted_by_user_info=deleted_by_user_info,
            destination_icon=destination_icon,
            destination_name=destination_name,
            destination_picture=destination_picture,
            destination_type=destination_type,
            external_id=external_id,
            external_link=external_link,
            face_recognition_status=face_recognition_status,
            favoured=favoured,
            has_unconfirmed_persons=has_unconfirmed_persons,
            is_blocked=is_blocked,
            is_online=is_online,
            last_archive_restore_date=last_archive_restore_date,
            likes=likes,
            limit_download_to_groups=limit_download_to_groups,
            original_asset_id=original_asset_id,
            original_segment_id=original_segment_id,
            original_version_id=original_version_id,
            person_ids=person_ids,
            publication_status=publication_status,
            site_name=site_name,
            status=status,
            time_end_milliseconds=time_end_milliseconds,
            time_start_milliseconds=time_start_milliseconds,
            title=title,
            type_=type_,
            updated_by_user=updated_by_user,
            updated_by_user_info=updated_by_user_info,
            views=views,
            warning=warning,
        )

        asset_post_edit.additional_properties = d
        return asset_post_edit

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
