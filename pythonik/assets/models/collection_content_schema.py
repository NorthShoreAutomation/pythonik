from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionContentSchema")


@_attrs_define
class CollectionContentSchema:
    """
    Attributes:
        object_id (UUID):
        object_type (str):
        collection_id (UUID | Unset):
        date_created (datetime.datetime | Unset):
    """

    object_id: UUID
    object_type: str
    collection_id: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = str(self.object_id)

        object_type = self.object_type

        collection_id: str | Unset = UNSET
        if not isinstance(self.collection_id, Unset):
            collection_id = str(self.collection_id)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_id": object_id,
                "object_type": object_type,
            }
        )
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if date_created is not UNSET:
            field_dict["date_created"] = date_created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = UUID(d.pop("object_id"))

        object_type = d.pop("object_type")

        _collection_id = d.pop("collection_id", UNSET)
        collection_id: UUID | Unset
        if isinstance(_collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = UUID(_collection_id)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        collection_content_schema = cls(
            object_id=object_id,
            object_type=object_type,
            collection_id=collection_id,
            date_created=date_created,
        )

        collection_content_schema.additional_properties = d
        return collection_content_schema

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
