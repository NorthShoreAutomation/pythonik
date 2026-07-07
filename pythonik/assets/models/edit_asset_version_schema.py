from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_asset_version_schema_analyze_status import (
    EditAssetVersionSchemaAnalyzeStatus,
)
from ..models.edit_asset_version_schema_archive_status import (
    EditAssetVersionSchemaArchiveStatus,
)
from ..models.edit_asset_version_schema_face_recognition_status import (
    EditAssetVersionSchemaFaceRecognitionStatus,
)
from ..models.edit_asset_version_schema_status import EditAssetVersionSchemaStatus
from ..models.edit_asset_version_schema_transcribe_status import (
    EditAssetVersionSchemaTranscribeStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="EditAssetVersionSchema")


@_attrs_define
class EditAssetVersionSchema:
    """
    Attributes:
        id (UUID):
        analyze_status (EditAssetVersionSchemaAnalyzeStatus | Unset):
        archive_status (EditAssetVersionSchemaArchiveStatus | Unset):
        created_by_user (UUID | Unset):
        created_by_user_info (User | Unset):
        date_created (datetime.datetime | Unset):
        face_recognition_status (EditAssetVersionSchemaFaceRecognitionStatus | Unset):
        has_unconfirmed_persons (bool | Unset):
        is_online (bool | Unset):
        person_ids (list[UUID] | Unset):
        status (EditAssetVersionSchemaStatus | Unset):
        transcribe_status (EditAssetVersionSchemaTranscribeStatus | Unset):
        transcribed_languages (list[str] | Unset):
        version_number (int | Unset):
    """

    id: UUID
    analyze_status: EditAssetVersionSchemaAnalyzeStatus | Unset = UNSET
    archive_status: EditAssetVersionSchemaArchiveStatus | Unset = UNSET
    created_by_user: UUID | Unset = UNSET
    created_by_user_info: User | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    face_recognition_status: EditAssetVersionSchemaFaceRecognitionStatus | Unset = UNSET
    has_unconfirmed_persons: bool | Unset = UNSET
    is_online: bool | Unset = UNSET
    person_ids: list[UUID] | Unset = UNSET
    status: EditAssetVersionSchemaStatus | Unset = UNSET
    transcribe_status: EditAssetVersionSchemaTranscribeStatus | Unset = UNSET
    transcribed_languages: list[str] | Unset = UNSET
    version_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        analyze_status: str | Unset = UNSET
        if not isinstance(self.analyze_status, Unset):
            analyze_status = self.analyze_status.value

        archive_status: str | Unset = UNSET
        if not isinstance(self.archive_status, Unset):
            archive_status = self.archive_status.value

        created_by_user: str | Unset = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = str(self.created_by_user)

        created_by_user_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by_user_info, Unset):
            created_by_user_info = self.created_by_user_info.to_dict()

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        face_recognition_status: str | Unset = UNSET
        if not isinstance(self.face_recognition_status, Unset):
            face_recognition_status = self.face_recognition_status.value

        has_unconfirmed_persons = self.has_unconfirmed_persons

        is_online = self.is_online

        person_ids: list[str] | Unset = UNSET
        if not isinstance(self.person_ids, Unset):
            person_ids = []
            for person_ids_item_data in self.person_ids:
                person_ids_item = str(person_ids_item_data)
                person_ids.append(person_ids_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        transcribe_status: str | Unset = UNSET
        if not isinstance(self.transcribe_status, Unset):
            transcribe_status = self.transcribe_status.value

        transcribed_languages: list[str] | Unset = UNSET
        if not isinstance(self.transcribed_languages, Unset):
            transcribed_languages = self.transcribed_languages

        version_number = self.version_number

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
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if created_by_user_info is not UNSET:
            field_dict["created_by_user_info"] = created_by_user_info
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if face_recognition_status is not UNSET:
            field_dict["face_recognition_status"] = face_recognition_status
        if has_unconfirmed_persons is not UNSET:
            field_dict["has_unconfirmed_persons"] = has_unconfirmed_persons
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if person_ids is not UNSET:
            field_dict["person_ids"] = person_ids
        if status is not UNSET:
            field_dict["status"] = status
        if transcribe_status is not UNSET:
            field_dict["transcribe_status"] = transcribe_status
        if transcribed_languages is not UNSET:
            field_dict["transcribed_languages"] = transcribed_languages
        if version_number is not UNSET:
            field_dict["version_number"] = version_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        _analyze_status = d.pop("analyze_status", UNSET)
        analyze_status: EditAssetVersionSchemaAnalyzeStatus | Unset
        if isinstance(_analyze_status, Unset):
            analyze_status = UNSET
        else:
            analyze_status = EditAssetVersionSchemaAnalyzeStatus(_analyze_status)

        _archive_status = d.pop("archive_status", UNSET)
        archive_status: EditAssetVersionSchemaArchiveStatus | Unset
        if isinstance(_archive_status, Unset):
            archive_status = UNSET
        else:
            archive_status = EditAssetVersionSchemaArchiveStatus(_archive_status)

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

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _face_recognition_status = d.pop("face_recognition_status", UNSET)
        face_recognition_status: EditAssetVersionSchemaFaceRecognitionStatus | Unset
        if isinstance(_face_recognition_status, Unset):
            face_recognition_status = UNSET
        else:
            face_recognition_status = EditAssetVersionSchemaFaceRecognitionStatus(
                _face_recognition_status
            )

        has_unconfirmed_persons = d.pop("has_unconfirmed_persons", UNSET)

        is_online = d.pop("is_online", UNSET)

        _person_ids = d.pop("person_ids", UNSET)
        person_ids: list[UUID] | Unset = UNSET
        if _person_ids is not UNSET:
            person_ids = []
            for person_ids_item_data in _person_ids:
                person_ids_item = UUID(person_ids_item_data)

                person_ids.append(person_ids_item)

        _status = d.pop("status", UNSET)
        status: EditAssetVersionSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EditAssetVersionSchemaStatus(_status)

        _transcribe_status = d.pop("transcribe_status", UNSET)
        transcribe_status: EditAssetVersionSchemaTranscribeStatus | Unset
        if isinstance(_transcribe_status, Unset):
            transcribe_status = UNSET
        else:
            transcribe_status = EditAssetVersionSchemaTranscribeStatus(
                _transcribe_status
            )

        transcribed_languages = cast(list[str], d.pop("transcribed_languages", UNSET))

        version_number = d.pop("version_number", UNSET)

        edit_asset_version_schema = cls(
            id=id,
            analyze_status=analyze_status,
            archive_status=archive_status,
            created_by_user=created_by_user,
            created_by_user_info=created_by_user_info,
            date_created=date_created,
            face_recognition_status=face_recognition_status,
            has_unconfirmed_persons=has_unconfirmed_persons,
            is_online=is_online,
            person_ids=person_ids,
            status=status,
            transcribe_status=transcribe_status,
            transcribed_languages=transcribed_languages,
            version_number=version_number,
        )

        edit_asset_version_schema.additional_properties = d
        return edit_asset_version_schema

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
