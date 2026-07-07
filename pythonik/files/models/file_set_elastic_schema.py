from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_set_elastic_schema_status import FileSetElasticSchemaStatus
from ..models.file_set_elastic_schema_type import FileSetElasticSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSetElasticSchema")


@_attrs_define
class FileSetElasticSchema:
    """
    Attributes:
        base_dir (str):
        component_ids (list[UUID]):
        format_id (UUID):
        name (str):
        archive_file_set_id (UUID | Unset):
        asset_id (UUID | Unset):
        date_created (datetime.datetime | Unset):
        date_deleted (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        deleted_by_user (UUID | Unset):
        file_count (int | Unset):
        id (UUID | Unset):
        is_archive (bool | Unset):
        original_storage_id (UUID | Unset):
        status (FileSetElasticSchemaStatus | Unset):
        storage_id (UUID | Unset):
        type_ (FileSetElasticSchemaType | Unset):
        version_id (UUID | Unset):
    """

    base_dir: str
    component_ids: list[UUID]
    format_id: UUID
    name: str
    archive_file_set_id: UUID | Unset = UNSET
    asset_id: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_deleted: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    deleted_by_user: UUID | Unset = UNSET
    file_count: int | Unset = UNSET
    id: UUID | Unset = UNSET
    is_archive: bool | Unset = UNSET
    original_storage_id: UUID | Unset = UNSET
    status: FileSetElasticSchemaStatus | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    type_: FileSetElasticSchemaType | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_dir = self.base_dir

        component_ids = []
        for component_ids_item_data in self.component_ids:
            component_ids_item = str(component_ids_item_data)
            component_ids.append(component_ids_item)

        format_id = str(self.format_id)

        name = self.name

        archive_file_set_id: str | Unset = UNSET
        if not isinstance(self.archive_file_set_id, Unset):
            archive_file_set_id = str(self.archive_file_set_id)

        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_deleted: str | Unset = UNSET
        if not isinstance(self.date_deleted, Unset):
            date_deleted = self.date_deleted.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        deleted_by_user: str | Unset = UNSET
        if not isinstance(self.deleted_by_user, Unset):
            deleted_by_user = str(self.deleted_by_user)

        file_count = self.file_count

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_archive = self.is_archive

        original_storage_id: str | Unset = UNSET
        if not isinstance(self.original_storage_id, Unset):
            original_storage_id = str(self.original_storage_id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_dir": base_dir,
                "component_ids": component_ids,
                "format_id": format_id,
                "name": name,
            }
        )
        if archive_file_set_id is not UNSET:
            field_dict["archive_file_set_id"] = archive_file_set_id
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_deleted is not UNSET:
            field_dict["date_deleted"] = date_deleted
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if deleted_by_user is not UNSET:
            field_dict["deleted_by_user"] = deleted_by_user
        if file_count is not UNSET:
            field_dict["file_count"] = file_count
        if id is not UNSET:
            field_dict["id"] = id
        if is_archive is not UNSET:
            field_dict["is_archive"] = is_archive
        if original_storage_id is not UNSET:
            field_dict["original_storage_id"] = original_storage_id
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_dir = d.pop("base_dir")

        component_ids = []
        _component_ids = d.pop("component_ids")
        for component_ids_item_data in _component_ids:
            component_ids_item = UUID(component_ids_item_data)

            component_ids.append(component_ids_item)

        format_id = UUID(d.pop("format_id"))

        name = d.pop("name")

        _archive_file_set_id = d.pop("archive_file_set_id", UNSET)
        archive_file_set_id: UUID | Unset
        if isinstance(_archive_file_set_id, Unset):
            archive_file_set_id = UNSET
        else:
            archive_file_set_id = UUID(_archive_file_set_id)

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

        _date_deleted = d.pop("date_deleted", UNSET)
        date_deleted: datetime.datetime | Unset
        if isinstance(_date_deleted, Unset):
            date_deleted = UNSET
        else:
            date_deleted = datetime.datetime.fromisoformat(_date_deleted)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        _deleted_by_user = d.pop("deleted_by_user", UNSET)
        deleted_by_user: UUID | Unset
        if isinstance(_deleted_by_user, Unset):
            deleted_by_user = UNSET
        else:
            deleted_by_user = UUID(_deleted_by_user)

        file_count = d.pop("file_count", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_archive = d.pop("is_archive", UNSET)

        _original_storage_id = d.pop("original_storage_id", UNSET)
        original_storage_id: UUID | Unset
        if isinstance(_original_storage_id, Unset):
            original_storage_id = UNSET
        else:
            original_storage_id = UUID(_original_storage_id)

        _status = d.pop("status", UNSET)
        status: FileSetElasticSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FileSetElasticSchemaStatus(_status)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        _type_ = d.pop("type", UNSET)
        type_: FileSetElasticSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FileSetElasticSchemaType(_type_)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        file_set_elastic_schema = cls(
            base_dir=base_dir,
            component_ids=component_ids,
            format_id=format_id,
            name=name,
            archive_file_set_id=archive_file_set_id,
            asset_id=asset_id,
            date_created=date_created,
            date_deleted=date_deleted,
            date_modified=date_modified,
            deleted_by_user=deleted_by_user,
            file_count=file_count,
            id=id,
            is_archive=is_archive,
            original_storage_id=original_storage_id,
            status=status,
            storage_id=storage_id,
            type_=type_,
            version_id=version_id,
        )

        file_set_elastic_schema.additional_properties = d
        return file_set_elastic_schema

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
