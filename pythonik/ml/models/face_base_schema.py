from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.face_base_schema_status import FaceBaseSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FaceBaseSchema")


@_attrs_define
class FaceBaseSchema:
    """
    Attributes:
        augmented_embedding_ids (list[UUID] | Unset):
        created_by_user (UUID | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        directory_path (str | Unset):
        embedding_id (UUID | Unset):
        filename (str | Unset):
        image_url (str | Unset):
        status (FaceBaseSchemaStatus | Unset):
        storage_id (UUID | Unset):
    """

    augmented_embedding_ids: list[UUID] | Unset = UNSET
    created_by_user: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    directory_path: str | Unset = UNSET
    embedding_id: UUID | Unset = UNSET
    filename: str | Unset = UNSET
    image_url: str | Unset = UNSET
    status: FaceBaseSchemaStatus | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        augmented_embedding_ids: list[str] | Unset = UNSET
        if not isinstance(self.augmented_embedding_ids, Unset):
            augmented_embedding_ids = []
            for augmented_embedding_ids_item_data in self.augmented_embedding_ids:
                augmented_embedding_ids_item = str(augmented_embedding_ids_item_data)
                augmented_embedding_ids.append(augmented_embedding_ids_item)

        created_by_user: str | Unset = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = str(self.created_by_user)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        directory_path = self.directory_path

        embedding_id: str | Unset = UNSET
        if not isinstance(self.embedding_id, Unset):
            embedding_id = str(self.embedding_id)

        filename = self.filename

        image_url = self.image_url

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

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
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _augmented_embedding_ids = d.pop("augmented_embedding_ids", UNSET)
        augmented_embedding_ids: list[UUID] | Unset = UNSET
        if _augmented_embedding_ids is not UNSET:
            augmented_embedding_ids = []
            for augmented_embedding_ids_item_data in _augmented_embedding_ids:
                augmented_embedding_ids_item = UUID(augmented_embedding_ids_item_data)

                augmented_embedding_ids.append(augmented_embedding_ids_item)

        _created_by_user = d.pop("created_by_user", UNSET)
        created_by_user: UUID | Unset
        if isinstance(_created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = UUID(_created_by_user)

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

        directory_path = d.pop("directory_path", UNSET)

        _embedding_id = d.pop("embedding_id", UNSET)
        embedding_id: UUID | Unset
        if isinstance(_embedding_id, Unset):
            embedding_id = UNSET
        else:
            embedding_id = UUID(_embedding_id)

        filename = d.pop("filename", UNSET)

        image_url = d.pop("image_url", UNSET)

        _status = d.pop("status", UNSET)
        status: FaceBaseSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FaceBaseSchemaStatus(_status)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        face_base_schema = cls(
            augmented_embedding_ids=augmented_embedding_ids,
            created_by_user=created_by_user,
            date_created=date_created,
            date_modified=date_modified,
            directory_path=directory_path,
            embedding_id=embedding_id,
            filename=filename,
            image_url=image_url,
            status=status,
            storage_id=storage_id,
        )

        face_base_schema.additional_properties = d
        return face_base_schema

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
