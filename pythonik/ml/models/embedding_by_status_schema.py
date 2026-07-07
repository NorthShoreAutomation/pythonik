from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embedding_by_status_schema_status import EmbeddingByStatusSchemaStatus
from ..models.embedding_by_status_schema_type import EmbeddingByStatusSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingByStatusSchema")


@_attrs_define
class EmbeddingByStatusSchema:
    """
    Attributes:
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        embedding_vector (list[float] | Unset):
        id (UUID | Unset):
        person_id (UUID | Unset):
        status (EmbeddingByStatusSchemaStatus | Unset):
        system_domain_id (UUID | Unset):
        type_ (EmbeddingByStatusSchemaType | Unset):
    """

    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    embedding_vector: list[float] | Unset = UNSET
    id: UUID | Unset = UNSET
    person_id: UUID | Unset = UNSET
    status: EmbeddingByStatusSchemaStatus | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    type_: EmbeddingByStatusSchemaType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        embedding_vector: list[float] | Unset = UNSET
        if not isinstance(self.embedding_vector, Unset):
            embedding_vector = self.embedding_vector

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        person_id: str | Unset = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if embedding_vector is not UNSET:
            field_dict["embedding_vector"] = embedding_vector
        if id is not UNSET:
            field_dict["id"] = id
        if person_id is not UNSET:
            field_dict["person_id"] = person_id
        if status is not UNSET:
            field_dict["status"] = status
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        embedding_vector = cast(list[float], d.pop("embedding_vector", UNSET))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _person_id = d.pop("person_id", UNSET)
        person_id: UUID | Unset
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _status = d.pop("status", UNSET)
        status: EmbeddingByStatusSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EmbeddingByStatusSchemaStatus(_status)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _type_ = d.pop("type", UNSET)
        type_: EmbeddingByStatusSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EmbeddingByStatusSchemaType(_type_)

        embedding_by_status_schema = cls(
            date_created=date_created,
            date_modified=date_modified,
            embedding_vector=embedding_vector,
            id=id,
            person_id=person_id,
            status=status,
            system_domain_id=system_domain_id,
            type_=type_,
        )

        embedding_by_status_schema.additional_properties = d
        return embedding_by_status_schema

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
