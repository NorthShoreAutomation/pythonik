from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embedding_by_face_schema_type import EmbeddingByFaceSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingByFaceSchema")


@_attrs_define
class EmbeddingByFaceSchema:
    """
    Attributes:
        date_created (datetime.datetime | Unset):
        embedding_vector (list[float] | Unset):
        face_id (UUID | Unset):
        id (UUID | Unset):
        system_domain_id (UUID | Unset):
        type_ (EmbeddingByFaceSchemaType | Unset):
    """

    date_created: datetime.datetime | Unset = UNSET
    embedding_vector: list[float] | Unset = UNSET
    face_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    type_: EmbeddingByFaceSchemaType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        embedding_vector: list[float] | Unset = UNSET
        if not isinstance(self.embedding_vector, Unset):
            embedding_vector = self.embedding_vector

        face_id: str | Unset = UNSET
        if not isinstance(self.face_id, Unset):
            face_id = str(self.face_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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
        if embedding_vector is not UNSET:
            field_dict["embedding_vector"] = embedding_vector
        if face_id is not UNSET:
            field_dict["face_id"] = face_id
        if id is not UNSET:
            field_dict["id"] = id
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

        embedding_vector = cast(list[float], d.pop("embedding_vector", UNSET))

        _face_id = d.pop("face_id", UNSET)
        face_id: UUID | Unset
        if isinstance(_face_id, Unset):
            face_id = UNSET
        else:
            face_id = UUID(_face_id)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _type_ = d.pop("type", UNSET)
        type_: EmbeddingByFaceSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EmbeddingByFaceSchemaType(_type_)

        embedding_by_face_schema = cls(
            date_created=date_created,
            embedding_vector=embedding_vector,
            face_id=face_id,
            id=id,
            system_domain_id=system_domain_id,
            type_=type_,
        )

        embedding_by_face_schema.additional_properties = d
        return embedding_by_face_schema

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
