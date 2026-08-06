from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        archive_file_set_id (None | Unset | UUID):
        asset_id (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_deleted (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        deleted_by_user (None | Unset | UUID):
        file_count (int | None | Unset):
        id (None | Unset | UUID):
        is_archive (bool | None | Unset):
        original_storage_id (None | Unset | UUID):
        status (FileSetElasticSchemaStatus | None | Unset):
        storage_id (None | Unset | UUID):
        type_ (FileSetElasticSchemaType | None | Unset):
        version_id (None | Unset | UUID):
    """

    base_dir: str
    component_ids: list[UUID]
    format_id: UUID
    name: str
    archive_file_set_id: None | Unset | UUID = UNSET
    asset_id: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_deleted: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    deleted_by_user: None | Unset | UUID = UNSET
    file_count: int | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_archive: bool | None | Unset = UNSET
    original_storage_id: None | Unset | UUID = UNSET
    status: FileSetElasticSchemaStatus | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    type_: FileSetElasticSchemaType | None | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_dir = self.base_dir

        component_ids = []
        for component_ids_item_data in self.component_ids:
            component_ids_item = str(component_ids_item_data)
            component_ids.append(component_ids_item)

        format_id = str(self.format_id)

        name = self.name

        archive_file_set_id: None | str | Unset
        if isinstance(self.archive_file_set_id, Unset):
            archive_file_set_id = UNSET
        elif isinstance(self.archive_file_set_id, UUID):
            archive_file_set_id = str(self.archive_file_set_id)
        else:
            archive_file_set_id = self.archive_file_set_id

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

        date_deleted: None | str | Unset
        if isinstance(self.date_deleted, Unset):
            date_deleted = UNSET
        elif isinstance(self.date_deleted, datetime.datetime):
            date_deleted = self.date_deleted.isoformat()
        else:
            date_deleted = self.date_deleted

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        deleted_by_user: None | str | Unset
        if isinstance(self.deleted_by_user, Unset):
            deleted_by_user = UNSET
        elif isinstance(self.deleted_by_user, UUID):
            deleted_by_user = str(self.deleted_by_user)
        else:
            deleted_by_user = self.deleted_by_user

        file_count: int | None | Unset
        if isinstance(self.file_count, Unset):
            file_count = UNSET
        else:
            file_count = self.file_count

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_archive: bool | None | Unset
        if isinstance(self.is_archive, Unset):
            is_archive = UNSET
        else:
            is_archive = self.is_archive

        original_storage_id: None | str | Unset
        if isinstance(self.original_storage_id, Unset):
            original_storage_id = UNSET
        elif isinstance(self.original_storage_id, UUID):
            original_storage_id = str(self.original_storage_id)
        else:
            original_storage_id = self.original_storage_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, FileSetElasticSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, FileSetElasticSchemaType):
            type_ = self.type_.value
        else:
            type_ = self.type_

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

        def _parse_archive_file_set_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archive_file_set_id_type_0 = UUID(data)

                return archive_file_set_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        archive_file_set_id = _parse_archive_file_set_id(
            d.pop("archive_file_set_id", UNSET)
        )

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

        def _parse_file_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_count = _parse_file_count(d.pop("file_count", UNSET))

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

        def _parse_is_archive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_archive = _parse_is_archive(d.pop("is_archive", UNSET))

        def _parse_original_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_storage_id_type_0 = UUID(data)

                return original_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        original_storage_id = _parse_original_storage_id(
            d.pop("original_storage_id", UNSET)
        )

        def _parse_status(data: object) -> FileSetElasticSchemaStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = FileSetElasticSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileSetElasticSchemaStatus | None | Unset, data)

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

        def _parse_type_(data: object) -> FileSetElasticSchemaType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = FileSetElasticSchemaType(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileSetElasticSchemaType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

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
