from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_schema import ApprovalSchema
    from ..models.asset_elastic_schema_analyze_status_type_1 import (
        AssetElasticSchemaAnalyzeStatusType1,
    )
    from ..models.asset_elastic_schema_archive_status_type_1 import (
        AssetElasticSchemaArchiveStatusType1,
    )
    from ..models.asset_elastic_schema_face_recognition_status_type_1 import (
        AssetElasticSchemaFaceRecognitionStatusType1,
    )
    from ..models.asset_elastic_schema_files_type_0_item import (
        AssetElasticSchemaFilesType0Item,
    )
    from ..models.asset_elastic_schema_formats_type_0_item import (
        AssetElasticSchemaFormatsType0Item,
    )
    from ..models.asset_elastic_schema_keyframes_type_0_item import (
        AssetElasticSchemaKeyframesType0Item,
    )
    from ..models.asset_elastic_schema_metadata_type_0 import (
        AssetElasticSchemaMetadataType0,
    )
    from ..models.asset_elastic_schema_proxies_type_0_item import (
        AssetElasticSchemaProxiesType0Item,
    )
    from ..models.asset_elastic_schema_status_type_1 import (
        AssetElasticSchemaStatusType1,
    )
    from ..models.asset_elastic_schema_type_type_1 import AssetElasticSchemaTypeType1
    from ..models.asset_version import AssetVersion
    from ..models.relation_elastic import RelationElastic
    from ..models.user import User


T = TypeVar("T", bound="AssetElasticSchema")


@_attrs_define
class AssetElasticSchema:
    """
    Attributes:
        title (str):
        analyze_status (AssetElasticSchemaAnalyzeStatusType1 | None | Unset):
        ancestor_collections (list[str] | None | Unset): Unordered list of all ancestor collection ids
        approval (ApprovalSchema | None | Unset):
        archive_status (AssetElasticSchemaArchiveStatusType1 | None | Unset):
        category (None | str | Unset):
        comments_count (int | None | Unset):
        created_by_user (None | Unset | UUID):
        created_by_user_info (None | Unset | User):
        custom_keyframe (None | Unset | UUID):
        custom_poster (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_deleted (datetime.datetime | None | Unset):
        date_imported (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        date_viewed (datetime.datetime | None | Unset):
        deleted_by_user (None | Unset | UUID):
        deleted_by_user_info (None | Unset | User):
        duration_milliseconds (int | None | Unset):
        external_id (None | str | Unset):
        external_link (None | str | Unset):
        face_recognition_status (AssetElasticSchemaFaceRecognitionStatusType1 | None | Unset):
        favoured (bool | None | Unset):
        files (list[AssetElasticSchemaFilesType0Item] | None | Unset):
        formats (list[AssetElasticSchemaFormatsType0Item] | None | Unset):
        has_unconfirmed_persons (bool | None | Unset):
        id (None | Unset | UUID):
        in_collections (list[str] | None | Unset):
        is_blocked (bool | None | Unset):
        is_online (bool | None | Unset):
        keyframes (list[AssetElasticSchemaKeyframesType0Item] | None | Unset):
        last_archive_restore_date (datetime.datetime | None | Unset):
        limit_download_to_groups (list[UUID] | None | Unset):
        media_type (None | str | Unset):
        metadata (AssetElasticSchemaMetadataType0 | None | Unset):
        object_type (None | str | Unset):
        original_asset_id (None | Unset | UUID):
        original_segment_id (None | Unset | UUID):
        original_version_id (None | Unset | UUID):
        person_ids (list[UUID] | None | Unset):
        position (int | None | Unset):
        proxies (list[AssetElasticSchemaProxiesType0Item] | None | Unset):
        relations (list[RelationElastic] | None | Unset):
        site_name (None | str | Unset):
        status (AssetElasticSchemaStatusType1 | None | Unset):
        time_end_milliseconds (int | None | Unset):
        time_start_milliseconds (int | None | Unset):
        type_ (AssetElasticSchemaTypeType1 | None | Unset):
        updated_by_user (None | Unset | UUID):
        updated_by_user_info (None | Unset | User):
        versions (list[AssetVersion] | None | Unset):
        versions_number (int | None | Unset):
        warning (None | str | Unset):
    """

    title: str
    analyze_status: AssetElasticSchemaAnalyzeStatusType1 | None | Unset = UNSET
    ancestor_collections: list[str] | None | Unset = UNSET
    approval: ApprovalSchema | None | Unset = UNSET
    archive_status: AssetElasticSchemaArchiveStatusType1 | None | Unset = UNSET
    category: None | str | Unset = UNSET
    comments_count: int | None | Unset = UNSET
    created_by_user: None | Unset | UUID = UNSET
    created_by_user_info: None | Unset | User = UNSET
    custom_keyframe: None | Unset | UUID = UNSET
    custom_poster: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_deleted: datetime.datetime | None | Unset = UNSET
    date_imported: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    date_viewed: datetime.datetime | None | Unset = UNSET
    deleted_by_user: None | Unset | UUID = UNSET
    deleted_by_user_info: None | Unset | User = UNSET
    duration_milliseconds: int | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    external_link: None | str | Unset = UNSET
    face_recognition_status: (
        AssetElasticSchemaFaceRecognitionStatusType1 | None | Unset
    ) = UNSET
    favoured: bool | None | Unset = UNSET
    files: list[AssetElasticSchemaFilesType0Item] | None | Unset = UNSET
    formats: list[AssetElasticSchemaFormatsType0Item] | None | Unset = UNSET
    has_unconfirmed_persons: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    in_collections: list[str] | None | Unset = UNSET
    is_blocked: bool | None | Unset = UNSET
    is_online: bool | None | Unset = UNSET
    keyframes: list[AssetElasticSchemaKeyframesType0Item] | None | Unset = UNSET
    last_archive_restore_date: datetime.datetime | None | Unset = UNSET
    limit_download_to_groups: list[UUID] | None | Unset = UNSET
    media_type: None | str | Unset = UNSET
    metadata: AssetElasticSchemaMetadataType0 | None | Unset = UNSET
    object_type: None | str | Unset = UNSET
    original_asset_id: None | Unset | UUID = UNSET
    original_segment_id: None | Unset | UUID = UNSET
    original_version_id: None | Unset | UUID = UNSET
    person_ids: list[UUID] | None | Unset = UNSET
    position: int | None | Unset = UNSET
    proxies: list[AssetElasticSchemaProxiesType0Item] | None | Unset = UNSET
    relations: list[RelationElastic] | None | Unset = UNSET
    site_name: None | str | Unset = UNSET
    status: AssetElasticSchemaStatusType1 | None | Unset = UNSET
    time_end_milliseconds: int | None | Unset = UNSET
    time_start_milliseconds: int | None | Unset = UNSET
    type_: AssetElasticSchemaTypeType1 | None | Unset = UNSET
    updated_by_user: None | Unset | UUID = UNSET
    updated_by_user_info: None | Unset | User = UNSET
    versions: list[AssetVersion] | None | Unset = UNSET
    versions_number: int | None | Unset = UNSET
    warning: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_schema import ApprovalSchema
        from ..models.asset_elastic_schema_analyze_status_type_1 import (
            AssetElasticSchemaAnalyzeStatusType1,
        )
        from ..models.asset_elastic_schema_archive_status_type_1 import (
            AssetElasticSchemaArchiveStatusType1,
        )
        from ..models.asset_elastic_schema_face_recognition_status_type_1 import (
            AssetElasticSchemaFaceRecognitionStatusType1,
        )
        from ..models.asset_elastic_schema_metadata_type_0 import (
            AssetElasticSchemaMetadataType0,
        )
        from ..models.asset_elastic_schema_status_type_1 import (
            AssetElasticSchemaStatusType1,
        )
        from ..models.asset_elastic_schema_type_type_1 import (
            AssetElasticSchemaTypeType1,
        )
        from ..models.user import User

        title = self.title

        analyze_status: dict[str, Any] | None | Unset
        if isinstance(self.analyze_status, Unset):
            analyze_status = UNSET
        elif isinstance(self.analyze_status, AssetElasticSchemaAnalyzeStatusType1):
            analyze_status = self.analyze_status.to_dict()
        else:
            analyze_status = self.analyze_status

        ancestor_collections: list[str] | None | Unset
        if isinstance(self.ancestor_collections, Unset):
            ancestor_collections = UNSET
        elif isinstance(self.ancestor_collections, list):
            ancestor_collections = self.ancestor_collections

        else:
            ancestor_collections = self.ancestor_collections

        approval: dict[str, Any] | None | Unset
        if isinstance(self.approval, Unset):
            approval = UNSET
        elif isinstance(self.approval, ApprovalSchema):
            approval = self.approval.to_dict()
        else:
            approval = self.approval

        archive_status: dict[str, Any] | None | Unset
        if isinstance(self.archive_status, Unset):
            archive_status = UNSET
        elif isinstance(self.archive_status, AssetElasticSchemaArchiveStatusType1):
            archive_status = self.archive_status.to_dict()
        else:
            archive_status = self.archive_status

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        comments_count: int | None | Unset
        if isinstance(self.comments_count, Unset):
            comments_count = UNSET
        else:
            comments_count = self.comments_count

        created_by_user: None | str | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        elif isinstance(self.created_by_user, UUID):
            created_by_user = str(self.created_by_user)
        else:
            created_by_user = self.created_by_user

        created_by_user_info: dict[str, Any] | None | Unset
        if isinstance(self.created_by_user_info, Unset):
            created_by_user_info = UNSET
        elif isinstance(self.created_by_user_info, User):
            created_by_user_info = self.created_by_user_info.to_dict()
        else:
            created_by_user_info = self.created_by_user_info

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

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_deleted: None | str | Unset
        if isinstance(self.date_deleted, Unset):
            date_deleted = UNSET
        elif isinstance(self.date_deleted, datetime.datetime):
            date_deleted = self.date_deleted.isoformat()
        else:
            date_deleted = self.date_deleted

        date_imported: None | str | Unset
        if isinstance(self.date_imported, Unset):
            date_imported = UNSET
        elif isinstance(self.date_imported, datetime.datetime):
            date_imported = self.date_imported.isoformat()
        else:
            date_imported = self.date_imported

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        date_viewed: None | str | Unset
        if isinstance(self.date_viewed, Unset):
            date_viewed = UNSET
        elif isinstance(self.date_viewed, datetime.datetime):
            date_viewed = self.date_viewed.isoformat()
        else:
            date_viewed = self.date_viewed

        deleted_by_user: None | str | Unset
        if isinstance(self.deleted_by_user, Unset):
            deleted_by_user = UNSET
        elif isinstance(self.deleted_by_user, UUID):
            deleted_by_user = str(self.deleted_by_user)
        else:
            deleted_by_user = self.deleted_by_user

        deleted_by_user_info: dict[str, Any] | None | Unset
        if isinstance(self.deleted_by_user_info, Unset):
            deleted_by_user_info = UNSET
        elif isinstance(self.deleted_by_user_info, User):
            deleted_by_user_info = self.deleted_by_user_info.to_dict()
        else:
            deleted_by_user_info = self.deleted_by_user_info

        duration_milliseconds: int | None | Unset
        if isinstance(self.duration_milliseconds, Unset):
            duration_milliseconds = UNSET
        else:
            duration_milliseconds = self.duration_milliseconds

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

        face_recognition_status: dict[str, Any] | None | Unset
        if isinstance(self.face_recognition_status, Unset):
            face_recognition_status = UNSET
        elif isinstance(
            self.face_recognition_status, AssetElasticSchemaFaceRecognitionStatusType1
        ):
            face_recognition_status = self.face_recognition_status.to_dict()
        else:
            face_recognition_status = self.face_recognition_status

        favoured: bool | None | Unset
        if isinstance(self.favoured, Unset):
            favoured = UNSET
        else:
            favoured = self.favoured

        files: list[dict[str, Any]] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_dict()
                files.append(files_type_0_item)

        else:
            files = self.files

        formats: list[dict[str, Any]] | None | Unset
        if isinstance(self.formats, Unset):
            formats = UNSET
        elif isinstance(self.formats, list):
            formats = []
            for formats_type_0_item_data in self.formats:
                formats_type_0_item = formats_type_0_item_data.to_dict()
                formats.append(formats_type_0_item)

        else:
            formats = self.formats

        has_unconfirmed_persons: bool | None | Unset
        if isinstance(self.has_unconfirmed_persons, Unset):
            has_unconfirmed_persons = UNSET
        else:
            has_unconfirmed_persons = self.has_unconfirmed_persons

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        in_collections: list[str] | None | Unset
        if isinstance(self.in_collections, Unset):
            in_collections = UNSET
        elif isinstance(self.in_collections, list):
            in_collections = self.in_collections

        else:
            in_collections = self.in_collections

        is_blocked: bool | None | Unset
        if isinstance(self.is_blocked, Unset):
            is_blocked = UNSET
        else:
            is_blocked = self.is_blocked

        is_online: bool | None | Unset
        if isinstance(self.is_online, Unset):
            is_online = UNSET
        else:
            is_online = self.is_online

        keyframes: list[dict[str, Any]] | None | Unset
        if isinstance(self.keyframes, Unset):
            keyframes = UNSET
        elif isinstance(self.keyframes, list):
            keyframes = []
            for keyframes_type_0_item_data in self.keyframes:
                keyframes_type_0_item = keyframes_type_0_item_data.to_dict()
                keyframes.append(keyframes_type_0_item)

        else:
            keyframes = self.keyframes

        last_archive_restore_date: None | str | Unset
        if isinstance(self.last_archive_restore_date, Unset):
            last_archive_restore_date = UNSET
        elif isinstance(self.last_archive_restore_date, datetime.datetime):
            last_archive_restore_date = self.last_archive_restore_date.isoformat()
        else:
            last_archive_restore_date = self.last_archive_restore_date

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

        media_type: None | str | Unset
        if isinstance(self.media_type, Unset):
            media_type = UNSET
        else:
            media_type = self.media_type

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AssetElasticSchemaMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        original_asset_id: None | str | Unset
        if isinstance(self.original_asset_id, Unset):
            original_asset_id = UNSET
        elif isinstance(self.original_asset_id, UUID):
            original_asset_id = str(self.original_asset_id)
        else:
            original_asset_id = self.original_asset_id

        original_segment_id: None | str | Unset
        if isinstance(self.original_segment_id, Unset):
            original_segment_id = UNSET
        elif isinstance(self.original_segment_id, UUID):
            original_segment_id = str(self.original_segment_id)
        else:
            original_segment_id = self.original_segment_id

        original_version_id: None | str | Unset
        if isinstance(self.original_version_id, Unset):
            original_version_id = UNSET
        elif isinstance(self.original_version_id, UUID):
            original_version_id = str(self.original_version_id)
        else:
            original_version_id = self.original_version_id

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

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        proxies: list[dict[str, Any]] | None | Unset
        if isinstance(self.proxies, Unset):
            proxies = UNSET
        elif isinstance(self.proxies, list):
            proxies = []
            for proxies_type_0_item_data in self.proxies:
                proxies_type_0_item = proxies_type_0_item_data.to_dict()
                proxies.append(proxies_type_0_item)

        else:
            proxies = self.proxies

        relations: list[dict[str, Any]] | None | Unset
        if isinstance(self.relations, Unset):
            relations = UNSET
        elif isinstance(self.relations, list):
            relations = []
            for relations_type_0_item_data in self.relations:
                relations_type_0_item = relations_type_0_item_data.to_dict()
                relations.append(relations_type_0_item)

        else:
            relations = self.relations

        site_name: None | str | Unset
        if isinstance(self.site_name, Unset):
            site_name = UNSET
        else:
            site_name = self.site_name

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, AssetElasticSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

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

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, AssetElasticSchemaTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        updated_by_user: None | str | Unset
        if isinstance(self.updated_by_user, Unset):
            updated_by_user = UNSET
        elif isinstance(self.updated_by_user, UUID):
            updated_by_user = str(self.updated_by_user)
        else:
            updated_by_user = self.updated_by_user

        updated_by_user_info: dict[str, Any] | None | Unset
        if isinstance(self.updated_by_user_info, Unset):
            updated_by_user_info = UNSET
        elif isinstance(self.updated_by_user_info, User):
            updated_by_user_info = self.updated_by_user_info.to_dict()
        else:
            updated_by_user_info = self.updated_by_user_info

        versions: list[dict[str, Any]] | None | Unset
        if isinstance(self.versions, Unset):
            versions = UNSET
        elif isinstance(self.versions, list):
            versions = []
            for versions_type_0_item_data in self.versions:
                versions_type_0_item = versions_type_0_item_data.to_dict()
                versions.append(versions_type_0_item)

        else:
            versions = self.versions

        versions_number: int | None | Unset
        if isinstance(self.versions_number, Unset):
            versions_number = UNSET
        else:
            versions_number = self.versions_number

        warning: None | str | Unset
        if isinstance(self.warning, Unset):
            warning = UNSET
        else:
            warning = self.warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if analyze_status is not UNSET:
            field_dict["analyze_status"] = analyze_status
        if ancestor_collections is not UNSET:
            field_dict["ancestor_collections"] = ancestor_collections
        if approval is not UNSET:
            field_dict["approval"] = approval
        if archive_status is not UNSET:
            field_dict["archive_status"] = archive_status
        if category is not UNSET:
            field_dict["category"] = category
        if comments_count is not UNSET:
            field_dict["comments_count"] = comments_count
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
        if date_viewed is not UNSET:
            field_dict["date_viewed"] = date_viewed
        if deleted_by_user is not UNSET:
            field_dict["deleted_by_user"] = deleted_by_user
        if deleted_by_user_info is not UNSET:
            field_dict["deleted_by_user_info"] = deleted_by_user_info
        if duration_milliseconds is not UNSET:
            field_dict["duration_milliseconds"] = duration_milliseconds
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_link is not UNSET:
            field_dict["external_link"] = external_link
        if face_recognition_status is not UNSET:
            field_dict["face_recognition_status"] = face_recognition_status
        if favoured is not UNSET:
            field_dict["favoured"] = favoured
        if files is not UNSET:
            field_dict["files"] = files
        if formats is not UNSET:
            field_dict["formats"] = formats
        if has_unconfirmed_persons is not UNSET:
            field_dict["has_unconfirmed_persons"] = has_unconfirmed_persons
        if id is not UNSET:
            field_dict["id"] = id
        if in_collections is not UNSET:
            field_dict["in_collections"] = in_collections
        if is_blocked is not UNSET:
            field_dict["is_blocked"] = is_blocked
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if keyframes is not UNSET:
            field_dict["keyframes"] = keyframes
        if last_archive_restore_date is not UNSET:
            field_dict["last_archive_restore_date"] = last_archive_restore_date
        if limit_download_to_groups is not UNSET:
            field_dict["limit_download_to_groups"] = limit_download_to_groups
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if original_asset_id is not UNSET:
            field_dict["original_asset_id"] = original_asset_id
        if original_segment_id is not UNSET:
            field_dict["original_segment_id"] = original_segment_id
        if original_version_id is not UNSET:
            field_dict["original_version_id"] = original_version_id
        if person_ids is not UNSET:
            field_dict["person_ids"] = person_ids
        if position is not UNSET:
            field_dict["position"] = position
        if proxies is not UNSET:
            field_dict["proxies"] = proxies
        if relations is not UNSET:
            field_dict["relations"] = relations
        if site_name is not UNSET:
            field_dict["site_name"] = site_name
        if status is not UNSET:
            field_dict["status"] = status
        if time_end_milliseconds is not UNSET:
            field_dict["time_end_milliseconds"] = time_end_milliseconds
        if time_start_milliseconds is not UNSET:
            field_dict["time_start_milliseconds"] = time_start_milliseconds
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_by_user is not UNSET:
            field_dict["updated_by_user"] = updated_by_user
        if updated_by_user_info is not UNSET:
            field_dict["updated_by_user_info"] = updated_by_user_info
        if versions is not UNSET:
            field_dict["versions"] = versions
        if versions_number is not UNSET:
            field_dict["versions_number"] = versions_number
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_schema import ApprovalSchema
        from ..models.asset_elastic_schema_analyze_status_type_1 import (
            AssetElasticSchemaAnalyzeStatusType1,
        )
        from ..models.asset_elastic_schema_archive_status_type_1 import (
            AssetElasticSchemaArchiveStatusType1,
        )
        from ..models.asset_elastic_schema_face_recognition_status_type_1 import (
            AssetElasticSchemaFaceRecognitionStatusType1,
        )
        from ..models.asset_elastic_schema_files_type_0_item import (
            AssetElasticSchemaFilesType0Item,
        )
        from ..models.asset_elastic_schema_formats_type_0_item import (
            AssetElasticSchemaFormatsType0Item,
        )
        from ..models.asset_elastic_schema_keyframes_type_0_item import (
            AssetElasticSchemaKeyframesType0Item,
        )
        from ..models.asset_elastic_schema_metadata_type_0 import (
            AssetElasticSchemaMetadataType0,
        )
        from ..models.asset_elastic_schema_proxies_type_0_item import (
            AssetElasticSchemaProxiesType0Item,
        )
        from ..models.asset_elastic_schema_status_type_1 import (
            AssetElasticSchemaStatusType1,
        )
        from ..models.asset_elastic_schema_type_type_1 import (
            AssetElasticSchemaTypeType1,
        )
        from ..models.asset_version import AssetVersion
        from ..models.relation_elastic import RelationElastic
        from ..models.user import User

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_analyze_status(
            data: object,
        ) -> AssetElasticSchemaAnalyzeStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                analyze_status_type_1 = AssetElasticSchemaAnalyzeStatusType1.from_dict(
                    data
                )

                return analyze_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetElasticSchemaAnalyzeStatusType1 | None | Unset, data)

        analyze_status = _parse_analyze_status(d.pop("analyze_status", UNSET))

        def _parse_ancestor_collections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ancestor_collections_type_0 = cast(list[str], data)

                return ancestor_collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ancestor_collections = _parse_ancestor_collections(
            d.pop("ancestor_collections", UNSET)
        )

        def _parse_approval(data: object) -> ApprovalSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approval_type_1 = ApprovalSchema.from_dict(data)

                return approval_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalSchema | None | Unset, data)

        approval = _parse_approval(d.pop("approval", UNSET))

        def _parse_archive_status(
            data: object,
        ) -> AssetElasticSchemaArchiveStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                archive_status_type_1 = AssetElasticSchemaArchiveStatusType1.from_dict(
                    data
                )

                return archive_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetElasticSchemaArchiveStatusType1 | None | Unset, data)

        archive_status = _parse_archive_status(d.pop("archive_status", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_comments_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comments_count = _parse_comments_count(d.pop("comments_count", UNSET))

        def _parse_created_by_user(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_user_type_0 = UUID(data)

                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user", UNSET))

        def _parse_created_by_user_info(data: object) -> None | Unset | User:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_user_info_type_1 = User.from_dict(data)

                return created_by_user_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | User, data)

        created_by_user_info = _parse_created_by_user_info(
            d.pop("created_by_user_info", UNSET)
        )

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

        def _parse_date_deleted(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_deleted_type_0 = datetime.datetime.fromisoformat(data)

                return date_deleted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_deleted = _parse_date_deleted(d.pop("date_deleted", UNSET))

        def _parse_date_imported(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_imported_type_0 = datetime.datetime.fromisoformat(data)

                return date_imported_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_imported = _parse_date_imported(d.pop("date_imported", UNSET))

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

        def _parse_date_viewed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_viewed_type_0 = datetime.datetime.fromisoformat(data)

                return date_viewed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_viewed = _parse_date_viewed(d.pop("date_viewed", UNSET))

        def _parse_deleted_by_user(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_by_user_type_0 = UUID(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user", UNSET))

        def _parse_deleted_by_user_info(data: object) -> None | Unset | User:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_info_type_1 = User.from_dict(data)

                return deleted_by_user_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | User, data)

        deleted_by_user_info = _parse_deleted_by_user_info(
            d.pop("deleted_by_user_info", UNSET)
        )

        def _parse_duration_milliseconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_milliseconds = _parse_duration_milliseconds(
            d.pop("duration_milliseconds", UNSET)
        )

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

        def _parse_face_recognition_status(
            data: object,
        ) -> AssetElasticSchemaFaceRecognitionStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                face_recognition_status_type_1 = (
                    AssetElasticSchemaFaceRecognitionStatusType1.from_dict(data)
                )

                return face_recognition_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AssetElasticSchemaFaceRecognitionStatusType1 | None | Unset, data
            )

        face_recognition_status = _parse_face_recognition_status(
            d.pop("face_recognition_status", UNSET)
        )

        def _parse_favoured(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        favoured = _parse_favoured(d.pop("favoured", UNSET))

        def _parse_files(
            data: object,
        ) -> list[AssetElasticSchemaFilesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in _files_type_0:
                    files_type_0_item = AssetElasticSchemaFilesType0Item.from_dict(
                        files_type_0_item_data
                    )

                    files_type_0.append(files_type_0_item)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetElasticSchemaFilesType0Item] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))

        def _parse_formats(
            data: object,
        ) -> list[AssetElasticSchemaFormatsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                formats_type_0 = []
                _formats_type_0 = data
                for formats_type_0_item_data in _formats_type_0:
                    formats_type_0_item = AssetElasticSchemaFormatsType0Item.from_dict(
                        formats_type_0_item_data
                    )

                    formats_type_0.append(formats_type_0_item)

                return formats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetElasticSchemaFormatsType0Item] | None | Unset, data)

        formats = _parse_formats(d.pop("formats", UNSET))

        def _parse_has_unconfirmed_persons(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_unconfirmed_persons = _parse_has_unconfirmed_persons(
            d.pop("has_unconfirmed_persons", UNSET)
        )

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

        def _parse_in_collections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                in_collections_type_0 = cast(list[str], data)

                return in_collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        in_collections = _parse_in_collections(d.pop("in_collections", UNSET))

        def _parse_is_blocked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_blocked = _parse_is_blocked(d.pop("is_blocked", UNSET))

        def _parse_is_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_online = _parse_is_online(d.pop("is_online", UNSET))

        def _parse_keyframes(
            data: object,
        ) -> list[AssetElasticSchemaKeyframesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyframes_type_0 = []
                _keyframes_type_0 = data
                for keyframes_type_0_item_data in _keyframes_type_0:
                    keyframes_type_0_item = (
                        AssetElasticSchemaKeyframesType0Item.from_dict(
                            keyframes_type_0_item_data
                        )
                    )

                    keyframes_type_0.append(keyframes_type_0_item)

                return keyframes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetElasticSchemaKeyframesType0Item] | None | Unset, data)

        keyframes = _parse_keyframes(d.pop("keyframes", UNSET))

        def _parse_last_archive_restore_date(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_archive_restore_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_archive_restore_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_archive_restore_date = _parse_last_archive_restore_date(
            d.pop("last_archive_restore_date", UNSET)
        )

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

        def _parse_media_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_type = _parse_media_type(d.pop("media_type", UNSET))

        def _parse_metadata(
            data: object,
        ) -> AssetElasticSchemaMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AssetElasticSchemaMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetElasticSchemaMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_original_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_asset_id_type_0 = UUID(data)

                return original_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        original_asset_id = _parse_original_asset_id(d.pop("original_asset_id", UNSET))

        def _parse_original_segment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_segment_id_type_0 = UUID(data)

                return original_segment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        original_segment_id = _parse_original_segment_id(
            d.pop("original_segment_id", UNSET)
        )

        def _parse_original_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_version_id_type_0 = UUID(data)

                return original_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        original_version_id = _parse_original_version_id(
            d.pop("original_version_id", UNSET)
        )

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

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_proxies(
            data: object,
        ) -> list[AssetElasticSchemaProxiesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                proxies_type_0 = []
                _proxies_type_0 = data
                for proxies_type_0_item_data in _proxies_type_0:
                    proxies_type_0_item = AssetElasticSchemaProxiesType0Item.from_dict(
                        proxies_type_0_item_data
                    )

                    proxies_type_0.append(proxies_type_0_item)

                return proxies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetElasticSchemaProxiesType0Item] | None | Unset, data)

        proxies = _parse_proxies(d.pop("proxies", UNSET))

        def _parse_relations(data: object) -> list[RelationElastic] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                relations_type_0 = []
                _relations_type_0 = data
                for relations_type_0_item_data in _relations_type_0:
                    relations_type_0_item = RelationElastic.from_dict(
                        relations_type_0_item_data
                    )

                    relations_type_0.append(relations_type_0_item)

                return relations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RelationElastic] | None | Unset, data)

        relations = _parse_relations(d.pop("relations", UNSET))

        def _parse_site_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_name = _parse_site_name(d.pop("site_name", UNSET))

        def _parse_status(data: object) -> AssetElasticSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = AssetElasticSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetElasticSchemaStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        def _parse_type_(data: object) -> AssetElasticSchemaTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = AssetElasticSchemaTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetElasticSchemaTypeType1 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_updated_by_user(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_user_type_0 = UUID(data)

                return updated_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by_user = _parse_updated_by_user(d.pop("updated_by_user", UNSET))

        def _parse_updated_by_user_info(data: object) -> None | Unset | User:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_user_info_type_1 = User.from_dict(data)

                return updated_by_user_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | User, data)

        updated_by_user_info = _parse_updated_by_user_info(
            d.pop("updated_by_user_info", UNSET)
        )

        def _parse_versions(data: object) -> list[AssetVersion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                versions_type_0 = []
                _versions_type_0 = data
                for versions_type_0_item_data in _versions_type_0:
                    versions_type_0_item = AssetVersion.from_dict(
                        versions_type_0_item_data
                    )

                    versions_type_0.append(versions_type_0_item)

                return versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetVersion] | None | Unset, data)

        versions = _parse_versions(d.pop("versions", UNSET))

        def _parse_versions_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        versions_number = _parse_versions_number(d.pop("versions_number", UNSET))

        def _parse_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        warning = _parse_warning(d.pop("warning", UNSET))

        asset_elastic_schema = cls(
            title=title,
            analyze_status=analyze_status,
            ancestor_collections=ancestor_collections,
            approval=approval,
            archive_status=archive_status,
            category=category,
            comments_count=comments_count,
            created_by_user=created_by_user,
            created_by_user_info=created_by_user_info,
            custom_keyframe=custom_keyframe,
            custom_poster=custom_poster,
            date_created=date_created,
            date_deleted=date_deleted,
            date_imported=date_imported,
            date_modified=date_modified,
            date_viewed=date_viewed,
            deleted_by_user=deleted_by_user,
            deleted_by_user_info=deleted_by_user_info,
            duration_milliseconds=duration_milliseconds,
            external_id=external_id,
            external_link=external_link,
            face_recognition_status=face_recognition_status,
            favoured=favoured,
            files=files,
            formats=formats,
            has_unconfirmed_persons=has_unconfirmed_persons,
            id=id,
            in_collections=in_collections,
            is_blocked=is_blocked,
            is_online=is_online,
            keyframes=keyframes,
            last_archive_restore_date=last_archive_restore_date,
            limit_download_to_groups=limit_download_to_groups,
            media_type=media_type,
            metadata=metadata,
            object_type=object_type,
            original_asset_id=original_asset_id,
            original_segment_id=original_segment_id,
            original_version_id=original_version_id,
            person_ids=person_ids,
            position=position,
            proxies=proxies,
            relations=relations,
            site_name=site_name,
            status=status,
            time_end_milliseconds=time_end_milliseconds,
            time_start_milliseconds=time_start_milliseconds,
            type_=type_,
            updated_by_user=updated_by_user,
            updated_by_user_info=updated_by_user_info,
            versions=versions,
            versions_number=versions_number,
            warning=warning,
        )

        asset_elastic_schema.additional_properties = d
        return asset_elastic_schema

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
