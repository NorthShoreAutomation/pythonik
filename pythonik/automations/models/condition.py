from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.term import Term


T = TypeVar("T", bound="Condition")


@_attrs_define
class Condition:
    """
    Attributes:
        operator (str):
        conditions (list[Condition] | Unset):
        filters (list[Condition] | Unset):
        path (str | Unset):
        terms (list[Term] | Unset):
    """

    operator: str
    conditions: list[Condition] | Unset = UNSET
    filters: list[Condition] | Unset = UNSET
    path: str | Unset = UNSET
    terms: list[Term] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        path = self.path

        terms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = []
            for terms_item_data in self.terms:
                terms_item = terms_item_data.to_dict()
                terms.append(terms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if filters is not UNSET:
            field_dict["filters"] = filters
        if path is not UNSET:
            field_dict["path"] = path
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.term import Term

        d = dict(src_dict)
        operator = d.pop("operator")

        _conditions = d.pop("conditions", UNSET)
        conditions: list[Condition] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = Condition.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        _filters = d.pop("filters", UNSET)
        filters: list[Condition] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = Condition.from_dict(filters_item_data)

                filters.append(filters_item)

        path = d.pop("path", UNSET)

        _terms = d.pop("terms", UNSET)
        terms: list[Term] | Unset = UNSET
        if _terms is not UNSET:
            terms = []
            for terms_item_data in _terms:
                terms_item = Term.from_dict(terms_item_data)

                terms.append(terms_item)

        condition = cls(
            operator=operator,
            conditions=conditions,
            filters=filters,
            path=path,
            terms=terms,
        )

        condition.additional_properties = d
        return condition

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
