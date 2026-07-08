from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedding_by_status_schema_status_type_1 import (
        EmbeddingByStatusSchemaStatusType1,
    )
    from ..models.embedding_by_status_schema_type_type_1 import (
        EmbeddingByStatusSchemaTypeType1,
    )


T = TypeVar("T", bound="EmbeddingByStatusSchema")


@_attrs_define
class EmbeddingByStatusSchema:
    """
    Attributes:
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        embedding_vector (list[float] | None | Unset):
        id (None | Unset | UUID):
        person_id (None | Unset | UUID):
        status (EmbeddingByStatusSchemaStatusType1 | None | Unset):
        system_domain_id (None | Unset | UUID):
        type_ (EmbeddingByStatusSchemaTypeType1 | None | Unset):
    """

    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    embedding_vector: list[float] | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    person_id: None | Unset | UUID = UNSET
    status: EmbeddingByStatusSchemaStatusType1 | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    type_: EmbeddingByStatusSchemaTypeType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedding_by_status_schema_status_type_1 import (
            EmbeddingByStatusSchemaStatusType1,
        )
        from ..models.embedding_by_status_schema_type_type_1 import (
            EmbeddingByStatusSchemaTypeType1,
        )

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

        embedding_vector: list[float] | None | Unset
        if isinstance(self.embedding_vector, Unset):
            embedding_vector = UNSET
        elif isinstance(self.embedding_vector, list):
            embedding_vector = self.embedding_vector

        else:
            embedding_vector = self.embedding_vector

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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
        elif isinstance(self.status, EmbeddingByStatusSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

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
        elif isinstance(self.type_, EmbeddingByStatusSchemaTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

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
        from ..models.embedding_by_status_schema_status_type_1 import (
            EmbeddingByStatusSchemaStatusType1,
        )
        from ..models.embedding_by_status_schema_type_type_1 import (
            EmbeddingByStatusSchemaTypeType1,
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

        def _parse_status(
            data: object,
        ) -> EmbeddingByStatusSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = EmbeddingByStatusSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddingByStatusSchemaStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        def _parse_type_(
            data: object,
        ) -> EmbeddingByStatusSchemaTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = EmbeddingByStatusSchemaTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddingByStatusSchemaTypeType1 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

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
