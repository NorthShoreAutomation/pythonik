from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationElasticSchema")


@_attrs_define
class RelationElasticSchema:
    """
    Attributes:
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        related_from_asset_id (UUID | Unset):
        related_to_asset_id (UUID | Unset):
        relation_type (str | Unset):
    """

    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    related_from_asset_id: UUID | Unset = UNSET
    related_to_asset_id: UUID | Unset = UNSET
    relation_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        related_from_asset_id: str | Unset = UNSET
        if not isinstance(self.related_from_asset_id, Unset):
            related_from_asset_id = str(self.related_from_asset_id)

        related_to_asset_id: str | Unset = UNSET
        if not isinstance(self.related_to_asset_id, Unset):
            related_to_asset_id = str(self.related_to_asset_id)

        relation_type = self.relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if related_from_asset_id is not UNSET:
            field_dict["related_from_asset_id"] = related_from_asset_id
        if related_to_asset_id is not UNSET:
            field_dict["related_to_asset_id"] = related_to_asset_id
        if relation_type is not UNSET:
            field_dict["relation_type"] = relation_type

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

        description = d.pop("description", UNSET)

        _related_from_asset_id = d.pop("related_from_asset_id", UNSET)
        related_from_asset_id: UUID | Unset
        if isinstance(_related_from_asset_id, Unset):
            related_from_asset_id = UNSET
        else:
            related_from_asset_id = UUID(_related_from_asset_id)

        _related_to_asset_id = d.pop("related_to_asset_id", UNSET)
        related_to_asset_id: UUID | Unset
        if isinstance(_related_to_asset_id, Unset):
            related_to_asset_id = UNSET
        else:
            related_to_asset_id = UUID(_related_to_asset_id)

        relation_type = d.pop("relation_type", UNSET)

        relation_elastic_schema = cls(
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            related_from_asset_id=related_from_asset_id,
            related_to_asset_id=related_to_asset_id,
            relation_type=relation_type,
        )

        relation_elastic_schema.additional_properties = d
        return relation_elastic_schema

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
