from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedding_by_face_schema_type_type_1 import (
        EmbeddingByFaceSchemaTypeType1,
    )


T = TypeVar("T", bound="EmbeddingByFaceSchema")


@_attrs_define
class EmbeddingByFaceSchema:
    """
    Attributes:
        date_created (datetime.datetime | None | Unset):
        embedding_vector (list[float] | None | Unset):
        face_id (None | Unset | UUID):
        id (None | Unset | UUID):
        system_domain_id (None | Unset | UUID):
        type_ (EmbeddingByFaceSchemaTypeType1 | None | Unset):
    """

    date_created: datetime.datetime | None | Unset = UNSET
    embedding_vector: list[float] | None | Unset = UNSET
    face_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    type_: EmbeddingByFaceSchemaTypeType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedding_by_face_schema_type_type_1 import (
            EmbeddingByFaceSchemaTypeType1,
        )

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        embedding_vector: list[float] | None | Unset
        if isinstance(self.embedding_vector, Unset):
            embedding_vector = UNSET
        elif isinstance(self.embedding_vector, list):
            embedding_vector = self.embedding_vector

        else:
            embedding_vector = self.embedding_vector

        face_id: None | str | Unset
        if isinstance(self.face_id, Unset):
            face_id = UNSET
        elif isinstance(self.face_id, UUID):
            face_id = str(self.face_id)
        else:
            face_id = self.face_id

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, EmbeddingByFaceSchemaTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

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
        from ..models.embedding_by_face_schema_type_type_1 import (
            EmbeddingByFaceSchemaTypeType1,
        )

        d = dict(src_dict)

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

        def _parse_embedding_vector(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                embedding_vector_type_0 = cast(list[float], data)

                return embedding_vector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        embedding_vector = _parse_embedding_vector(d.pop("embedding_vector", UNSET))

        def _parse_face_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                face_id_type_0 = UUID(data)

                return face_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        face_id = _parse_face_id(d.pop("face_id", UNSET))

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

        def _parse_type_(data: object) -> EmbeddingByFaceSchemaTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = EmbeddingByFaceSchemaTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddingByFaceSchemaTypeType1 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

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
