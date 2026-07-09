from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        conditions (list[Condition] | None | Unset):
        filters (list[Condition] | None | Unset):
        path (None | str | Unset):
        terms (list[Term] | None | Unset):
    """

    operator: str
    conditions: list[Condition] | None | Unset = UNSET
    filters: list[Condition] | None | Unset = UNSET
    path: None | str | Unset = UNSET
    terms: list[Term] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator

        conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        terms: list[dict[str, Any]] | None | Unset
        if isinstance(self.terms, Unset):
            terms = UNSET
        elif isinstance(self.terms, list):
            terms = []
            for terms_type_0_item_data in self.terms:
                terms_type_0_item = terms_type_0_item_data.to_dict()
                terms.append(terms_type_0_item)

        else:
            terms = self.terms

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

        def _parse_conditions(data: object) -> list[Condition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:
                    conditions_type_0_item = Condition.from_dict(
                        conditions_type_0_item_data
                    )

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Condition] | None | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        def _parse_filters(data: object) -> list[Condition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = Condition.from_dict(filters_type_0_item_data)

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Condition] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_terms(data: object) -> list[Term] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                terms_type_0 = []
                _terms_type_0 = data
                for terms_type_0_item_data in _terms_type_0:
                    terms_type_0_item = Term.from_dict(terms_type_0_item_data)

                    terms_type_0.append(terms_type_0_item)

                return terms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Term] | None | Unset, data)

        terms = _parse_terms(d.pop("terms", UNSET))

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
