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
        date_created (datetime.datetime | Unset):
        embedding_vector (list[float] | Unset):
        type_ (EmbeddingBaseSchemaType | Unset):
    """

    date_created: datetime.datetime | Unset = UNSET
    embedding_vector: list[float] | Unset = UNSET
    type_: EmbeddingBaseSchemaType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        embedding_vector: list[float] | Unset = UNSET
        if not isinstance(self.embedding_vector, Unset):
            embedding_vector = self.embedding_vector

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

        _type_ = d.pop("type", UNSET)
        type_: EmbeddingBaseSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EmbeddingBaseSchemaType(_type_)

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
