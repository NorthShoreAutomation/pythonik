from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_asset_version_analyze_status import EditAssetVersionAnalyzeStatus
from ..models.edit_asset_version_archive_status import EditAssetVersionArchiveStatus
from ..models.edit_asset_version_face_recognition_status import (
    EditAssetVersionFaceRecognitionStatus,
)
from ..models.edit_asset_version_status import EditAssetVersionStatus
from ..models.edit_asset_version_transcribe_status import (
    EditAssetVersionTranscribeStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="EditAssetVersion")


@_attrs_define
class EditAssetVersion:
    """
    Attributes:
        id (UUID):
        analyze_status (EditAssetVersionAnalyzeStatus | None | Unset):
        archive_status (EditAssetVersionArchiveStatus | None | Unset):
        created_by_user (None | Unset | UUID):
        created_by_user_info (None | Unset | User):
        date_created (datetime.datetime | None | Unset):
        face_recognition_status (EditAssetVersionFaceRecognitionStatus | None | Unset):
        has_unconfirmed_persons (bool | None | Unset):
        is_online (bool | None | Unset):
        person_ids (list[UUID] | None | Unset):
        status (EditAssetVersionStatus | None | Unset):
        transcribe_status (EditAssetVersionTranscribeStatus | None | Unset):
        transcribed_languages (list[str] | None | Unset):
        version_number (int | None | Unset):
    """

    id: UUID
    analyze_status: EditAssetVersionAnalyzeStatus | None | Unset = UNSET
    archive_status: EditAssetVersionArchiveStatus | None | Unset = UNSET
    created_by_user: None | Unset | UUID = UNSET
    created_by_user_info: None | Unset | User = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    face_recognition_status: EditAssetVersionFaceRecognitionStatus | None | Unset = (
        UNSET
    )
    has_unconfirmed_persons: bool | None | Unset = UNSET
    is_online: bool | None | Unset = UNSET
    person_ids: list[UUID] | None | Unset = UNSET
    status: EditAssetVersionStatus | None | Unset = UNSET
    transcribe_status: EditAssetVersionTranscribeStatus | None | Unset = UNSET
    transcribed_languages: list[str] | None | Unset = UNSET
    version_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User

        id = str(self.id)

        analyze_status: None | str | Unset
        if isinstance(self.analyze_status, Unset):
            analyze_status = UNSET
        elif isinstance(self.analyze_status, EditAssetVersionAnalyzeStatus):
            analyze_status = self.analyze_status.value
        else:
            analyze_status = self.analyze_status

        archive_status: None | str | Unset
        if isinstance(self.archive_status, Unset):
            archive_status = UNSET
        elif isinstance(self.archive_status, EditAssetVersionArchiveStatus):
            archive_status = self.archive_status.value
        else:
            archive_status = self.archive_status

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

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        face_recognition_status: None | str | Unset
        if isinstance(self.face_recognition_status, Unset):
            face_recognition_status = UNSET
        elif isinstance(
            self.face_recognition_status, EditAssetVersionFaceRecognitionStatus
        ):
            face_recognition_status = self.face_recognition_status.value
        else:
            face_recognition_status = self.face_recognition_status

        has_unconfirmed_persons: bool | None | Unset
        if isinstance(self.has_unconfirmed_persons, Unset):
            has_unconfirmed_persons = UNSET
        else:
            has_unconfirmed_persons = self.has_unconfirmed_persons

        is_online: bool | None | Unset
        if isinstance(self.is_online, Unset):
            is_online = UNSET
        else:
            is_online = self.is_online

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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, EditAssetVersionStatus):
            status = self.status.value
        else:
            status = self.status

        transcribe_status: None | str | Unset
        if isinstance(self.transcribe_status, Unset):
            transcribe_status = UNSET
        elif isinstance(self.transcribe_status, EditAssetVersionTranscribeStatus):
            transcribe_status = self.transcribe_status.value
        else:
            transcribe_status = self.transcribe_status

        transcribed_languages: list[str] | None | Unset
        if isinstance(self.transcribed_languages, Unset):
            transcribed_languages = UNSET
        elif isinstance(self.transcribed_languages, list):
            transcribed_languages = self.transcribed_languages

        else:
            transcribed_languages = self.transcribed_languages

        version_number: int | None | Unset
        if isinstance(self.version_number, Unset):
            version_number = UNSET
        else:
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

        def _parse_analyze_status(
            data: object,
        ) -> EditAssetVersionAnalyzeStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                analyze_status_type_1 = EditAssetVersionAnalyzeStatus(data)

                return analyze_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditAssetVersionAnalyzeStatus | None | Unset, data)

        analyze_status = _parse_analyze_status(d.pop("analyze_status", UNSET))

        def _parse_archive_status(
            data: object,
        ) -> EditAssetVersionArchiveStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archive_status_type_1 = EditAssetVersionArchiveStatus(data)

                return archive_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditAssetVersionArchiveStatus | None | Unset, data)

        archive_status = _parse_archive_status(d.pop("archive_status", UNSET))

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

        def _parse_face_recognition_status(
            data: object,
        ) -> EditAssetVersionFaceRecognitionStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                face_recognition_status_type_1 = EditAssetVersionFaceRecognitionStatus(
                    data
                )

                return face_recognition_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditAssetVersionFaceRecognitionStatus | None | Unset, data)

        face_recognition_status = _parse_face_recognition_status(
            d.pop("face_recognition_status", UNSET)
        )

        def _parse_has_unconfirmed_persons(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_unconfirmed_persons = _parse_has_unconfirmed_persons(
            d.pop("has_unconfirmed_persons", UNSET)
        )

        def _parse_is_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_online = _parse_is_online(d.pop("is_online", UNSET))

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

        def _parse_status(data: object) -> EditAssetVersionStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = EditAssetVersionStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditAssetVersionStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_transcribe_status(
            data: object,
        ) -> EditAssetVersionTranscribeStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transcribe_status_type_1 = EditAssetVersionTranscribeStatus(data)

                return transcribe_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditAssetVersionTranscribeStatus | None | Unset, data)

        transcribe_status = _parse_transcribe_status(d.pop("transcribe_status", UNSET))

        def _parse_transcribed_languages(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transcribed_languages_type_0 = cast(list[str], data)

                return transcribed_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        transcribed_languages = _parse_transcribed_languages(
            d.pop("transcribed_languages", UNSET)
        )

        def _parse_version_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version_number = _parse_version_number(d.pop("version_number", UNSET))

        edit_asset_version = cls(
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

        edit_asset_version.additional_properties = d
        return edit_asset_version

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
