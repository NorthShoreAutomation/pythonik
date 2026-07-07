from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_create_schema_status import ProjectCreateSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectCreateSchema")


@_attrs_define
class ProjectCreateSchema:
    """
    Attributes:
        name (str):
        collection_id (UUID | Unset): ID of a collection that will become a project collection
        collection_parent_id (UUID | Unset): ID of a collection that the project should be a child of
        created_by_user (UUID | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        id (UUID | Unset):
        status (ProjectCreateSchemaStatus | Unset):
        storage_id (None | Unset | UUID):
        system_domain_id (UUID | Unset):
    """

    name: str
    collection_id: UUID | Unset = UNSET
    collection_parent_id: UUID | Unset = UNSET
    created_by_user: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    status: ProjectCreateSchemaStatus | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        collection_id: str | Unset = UNSET
        if not isinstance(self.collection_id, Unset):
            collection_id = str(self.collection_id)

        collection_parent_id: str | Unset = UNSET
        if not isinstance(self.collection_parent_id, Unset):
            collection_parent_id = str(self.collection_parent_id)

        created_by_user: str | Unset = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = str(self.created_by_user)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if collection_parent_id is not UNSET:
            field_dict["collection_parent_id"] = collection_parent_id
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _collection_id = d.pop("collection_id", UNSET)
        collection_id: UUID | Unset
        if isinstance(_collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = UUID(_collection_id)

        _collection_parent_id = d.pop("collection_parent_id", UNSET)
        collection_parent_id: UUID | Unset
        if isinstance(_collection_parent_id, Unset):
            collection_parent_id = UNSET
        else:
            collection_parent_id = UUID(_collection_parent_id)

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

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _status = d.pop("status", UNSET)
        status: ProjectCreateSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectCreateSchemaStatus(_status)

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

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        project_create_schema = cls(
            name=name,
            collection_id=collection_id,
            collection_parent_id=collection_parent_id,
            created_by_user=created_by_user,
            date_created=date_created,
            date_modified=date_modified,
            id=id,
            status=status,
            storage_id=storage_id,
            system_domain_id=system_domain_id,
        )

        project_create_schema.additional_properties = d
        return project_create_schema

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
