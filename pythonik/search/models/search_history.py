from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_history_criteria import SearchHistoryCriteria


T = TypeVar("T", bound="SearchHistory")


@_attrs_define
class SearchHistory:
    """
    Attributes:
        criteria (SearchHistoryCriteria):
        id (UUID):
        date_created (datetime.datetime | Unset):
    """

    criteria: SearchHistoryCriteria
    id: UUID
    date_created: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        criteria = self.criteria.to_dict()

        id = str(self.id)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "criteria": criteria,
                "id": id,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_history_criteria import SearchHistoryCriteria

        d = dict(src_dict)
        criteria = SearchHistoryCriteria.from_dict(d.pop("criteria"))

        id = UUID(d.pop("id"))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        search_history = cls(
            criteria=criteria,
            id=id,
            date_created=date_created,
        )

        search_history.additional_properties = d
        return search_history

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
