from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embedding_base_schema_type import EmbeddingBaseSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingBaseSchema")


@_attrs_define
class EmbeddingBaseSchema:
    """
    Attributes:
        date_created (datetime.datetime | None | Unset):
        embedding_vector (list[float] | None | Unset):
        type_ (EmbeddingBaseSchemaType | None | Unset):
    """

    date_created: datetime.datetime | None | Unset = UNSET
    embedding_vector: list[float] | None | Unset = UNSET
    type_: EmbeddingBaseSchemaType | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, EmbeddingBaseSchemaType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if embedding_vector is not UNSET:
            field_dict["embedding_vector"] = embedding_vector
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        def _parse_type_(data: object) -> EmbeddingBaseSchemaType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = EmbeddingBaseSchemaType(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddingBaseSchemaType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        embedding_base_schema = cls(
            date_created=date_created,
            embedding_vector=embedding_vector,
            type_=type_,
        )

        embedding_base_schema.additional_properties = d
        return embedding_base_schema

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
