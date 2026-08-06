from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationElastic")


@_attrs_define
class RelationElastic:
    """
    Attributes:
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        description (None | str | Unset):
        related_from_asset_id (None | Unset | UUID):
        related_to_asset_id (None | Unset | UUID):
        relation_type (None | str | Unset):
    """

    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    related_from_asset_id: None | Unset | UUID = UNSET
    related_to_asset_id: None | Unset | UUID = UNSET
    relation_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        related_from_asset_id: None | str | Unset
        if isinstance(self.related_from_asset_id, Unset):
            related_from_asset_id = UNSET
        elif isinstance(self.related_from_asset_id, UUID):
            related_from_asset_id = str(self.related_from_asset_id)
        else:
            related_from_asset_id = self.related_from_asset_id

        related_to_asset_id: None | str | Unset
        if isinstance(self.related_to_asset_id, Unset):
            related_to_asset_id = UNSET
        elif isinstance(self.related_to_asset_id, UUID):
            related_to_asset_id = str(self.related_to_asset_id)
        else:
            related_to_asset_id = self.related_to_asset_id

        relation_type: None | str | Unset
        if isinstance(self.relation_type, Unset):
            relation_type = UNSET
        else:
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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_related_from_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_from_asset_id_type_0 = UUID(data)

                return related_from_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        related_from_asset_id = _parse_related_from_asset_id(
            d.pop("related_from_asset_id", UNSET)
        )

        def _parse_related_to_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_to_asset_id_type_0 = UUID(data)

                return related_to_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        related_to_asset_id = _parse_related_to_asset_id(
            d.pop("related_to_asset_id", UNSET)
        )

        def _parse_relation_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation_type = _parse_relation_type(d.pop("relation_type", UNSET))

        relation_elastic = cls(
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            related_from_asset_id=related_from_asset_id,
            related_to_asset_id=related_to_asset_id,
            relation_type=relation_type,
        )

        relation_elastic.additional_properties = d
        return relation_elastic

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
