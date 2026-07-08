from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.face_by_person_schema_status_type_1 import (
        FaceByPersonSchemaStatusType1,
    )


T = TypeVar("T", bound="FaceByPersonSchema")


@_attrs_define
class FaceByPersonSchema:
    """
    Attributes:
        augmented_embedding_ids (list[UUID] | None | Unset):
        created_by_user (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        directory_path (None | str | Unset):
        embedding_id (None | Unset | UUID):
        filename (None | str | Unset):
        id (None | Unset | UUID):
        image_url (None | str | Unset):
        person_id (None | Unset | UUID):
        status (FaceByPersonSchemaStatusType1 | None | Unset):
        storage_id (None | Unset | UUID):
        system_domain_id (None | Unset | UUID):
    """

    augmented_embedding_ids: list[UUID] | None | Unset = UNSET
    created_by_user: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    directory_path: None | str | Unset = UNSET
    embedding_id: None | Unset | UUID = UNSET
    filename: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    image_url: None | str | Unset = UNSET
    person_id: None | Unset | UUID = UNSET
    status: FaceByPersonSchemaStatusType1 | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.face_by_person_schema_status_type_1 import (
            FaceByPersonSchemaStatusType1,
        )

        augmented_embedding_ids: list[str] | None | Unset
        if isinstance(self.augmented_embedding_ids, Unset):
            augmented_embedding_ids = UNSET
        elif isinstance(self.augmented_embedding_ids, list):
            augmented_embedding_ids = []
            for (
                augmented_embedding_ids_type_0_item_data
            ) in self.augmented_embedding_ids:
                augmented_embedding_ids_type_0_item = str(
                    augmented_embedding_ids_type_0_item_data
                )
                augmented_embedding_ids.append(augmented_embedding_ids_type_0_item)

        else:
            augmented_embedding_ids = self.augmented_embedding_ids

        created_by_user: None | str | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        elif isinstance(self.created_by_user, UUID):
            created_by_user = str(self.created_by_user)
        else:
            created_by_user = self.created_by_user

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

        directory_path: None | str | Unset
        if isinstance(self.directory_path, Unset):
            directory_path = UNSET
        else:
            directory_path = self.directory_path

        embedding_id: None | str | Unset
        if isinstance(self.embedding_id, Unset):
            embedding_id = UNSET
        elif isinstance(self.embedding_id, UUID):
            embedding_id = str(self.embedding_id)
        else:
            embedding_id = self.embedding_id

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        person_id: None | str | Unset
        if isinstance(self.person_id, Unset):
            person_id = UNSET
        elif isinstance(self.person_id, UUID):
            person_id = str(self.person_id)
        else:
            person_id = self.person_id

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, FaceByPersonSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if augmented_embedding_ids is not UNSET:
            field_dict["augmented_embedding_ids"] = augmented_embedding_ids
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if directory_path is not UNSET:
            field_dict["directory_path"] = directory_path
        if embedding_id is not UNSET:
            field_dict["embedding_id"] = embedding_id
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if person_id is not UNSET:
            field_dict["person_id"] = person_id
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.face_by_person_schema_status_type_1 import (
            FaceByPersonSchemaStatusType1,
        )

        d = dict(src_dict)

        def _parse_augmented_embedding_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                augmented_embedding_ids_type_0 = []
                _augmented_embedding_ids_type_0 = data
                for (
                    augmented_embedding_ids_type_0_item_data
                ) in _augmented_embedding_ids_type_0:
                    augmented_embedding_ids_type_0_item = UUID(
                        augmented_embedding_ids_type_0_item_data
                    )

                    augmented_embedding_ids_type_0.append(
                        augmented_embedding_ids_type_0_item
                    )

                return augmented_embedding_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        augmented_embedding_ids = _parse_augmented_embedding_ids(
            d.pop("augmented_embedding_ids", UNSET)
        )

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

        def _parse_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directory_path = _parse_directory_path(d.pop("directory_path", UNSET))

        def _parse_embedding_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                embedding_id_type_0 = UUID(data)

                return embedding_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        embedding_id = _parse_embedding_id(d.pop("embedding_id", UNSET))

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

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

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("image_url", UNSET))

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

        def _parse_status(data: object) -> FaceByPersonSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = FaceByPersonSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FaceByPersonSchemaStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_id_type_0 = UUID(data)

                return storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_id = _parse_storage_id(d.pop("storage_id", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        face_by_person_schema = cls(
            augmented_embedding_ids=augmented_embedding_ids,
            created_by_user=created_by_user,
            date_created=date_created,
            date_modified=date_modified,
            directory_path=directory_path,
            embedding_id=embedding_id,
            filename=filename,
            id=id,
            image_url=image_url,
            person_id=person_id,
            status=status,
            storage_id=storage_id,
            system_domain_id=system_domain_id,
        )

        face_by_person_schema.additional_properties = d
        return face_by_person_schema

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
