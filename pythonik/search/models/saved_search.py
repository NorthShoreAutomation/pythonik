from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_criteria_saved import SearchCriteriaSaved


T = TypeVar("T", bound="SavedSearch")


@_attrs_define
class SavedSearch:
    """
    Attributes:
        criteria (SearchCriteriaSaved):
        name (str):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        favoured (bool | Unset):
        group_id (None | Unset | UUID):
        id (UUID | Unset):
        permissions (list[str] | Unset):
    """

    criteria: SearchCriteriaSaved
    name: str
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    favoured: bool | Unset = UNSET
    group_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        criteria = self.criteria.to_dict()

        name = self.name

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        favoured = self.favoured

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "criteria": criteria,
                "name": name,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if favoured is not UNSET:
            field_dict["favoured"] = favoured
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_criteria_saved import SearchCriteriaSaved

        d = dict(src_dict)
        criteria = SearchCriteriaSaved.from_dict(d.pop("criteria"))

        name = d.pop("name")

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

        favoured = d.pop("favoured", UNSET)

        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)

                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        saved_search = cls(
            criteria=criteria,
            name=name,
            date_created=date_created,
            date_modified=date_modified,
            favoured=favoured,
            group_id=group_id,
            id=id,
            permissions=permissions,
        )

        saved_search.additional_properties = d
        return saved_search

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
