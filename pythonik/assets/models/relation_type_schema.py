from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationTypeSchema")


@_attrs_define
class RelationTypeSchema:
    """
    Attributes:
        destination_label (str):
        name (str):
        source_label (str):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (None | str | Unset):
        is_directional (bool | Unset):
        is_system (bool | Unset):
    """

    destination_label: str
    name: str
    source_label: str
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: None | str | Unset = UNSET
    is_directional: bool | Unset = UNSET
    is_system: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_label = self.destination_label

        name = self.name

        source_label = self.source_label

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_directional = self.is_directional

        is_system = self.is_system

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination_label": destination_label,
                "name": name,
                "source_label": source_label,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if is_directional is not UNSET:
            field_dict["is_directional"] = is_directional
        if is_system is not UNSET:
            field_dict["is_system"] = is_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_label = d.pop("destination_label")

        name = d.pop("name")

        source_label = d.pop("source_label")

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_directional = d.pop("is_directional", UNSET)

        is_system = d.pop("is_system", UNSET)

        relation_type_schema = cls(
            destination_label=destination_label,
            name=name,
            source_label=source_label,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            is_directional=is_directional,
            is_system=is_system,
        )

        relation_type_schema.additional_properties = d
        return relation_type_schema

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
