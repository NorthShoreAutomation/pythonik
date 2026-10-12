from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_role import FilterRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword_predicate import KeywordPredicate
    from ..models.public_lexical_predicate_output import PublicLexicalPredicateOutput
    from ..models.public_semantic_predicate_output import PublicSemanticPredicateOutput
    from ..models.response_filter_output_value_labels_type_0 import (
        ResponseFilterOutputValueLabelsType0,
    )


T = TypeVar("T", bound="ResponseFilterOutput")


@_attrs_define
class ResponseFilterOutput:
    """One filter as the response states it, re-sendable as-is in
    ``SearchConstraint.filters``.

    Retrieval clauses (words, meaning) are reported here too, on the field they
    ran against, in the form the answering round actually ran (e.g. fuzzed).
    ``disposition`` is not serialized: ``applied`` vs ``relaxed`` already says
    it, and it is ignored inbound.

        Attributes:
            field (str):
            predicate (KeywordPredicate | PublicLexicalPredicateOutput | PublicSemanticPredicateOutput):
            facetable (bool | None | Unset):  Default: False.
            field_type (None | str | Unset):  Default: ''.
            label (None | str | Unset):
            pushed_down (bool | None | Unset):  Default: False.
            reason (None | str | Unset):
            role (FilterRole | None | Unset):
            value_labels (None | ResponseFilterOutputValueLabelsType0 | Unset):
            weight (float | None | Unset):  Default: 1.0.
    """

    field: str
    predicate: (
        KeywordPredicate | PublicLexicalPredicateOutput | PublicSemanticPredicateOutput
    )
    facetable: bool | None | Unset = False
    field_type: None | str | Unset = ""
    label: None | str | Unset = UNSET
    pushed_down: bool | None | Unset = False
    reason: None | str | Unset = UNSET
    role: FilterRole | None | Unset = UNSET
    value_labels: None | ResponseFilterOutputValueLabelsType0 | Unset = UNSET
    weight: float | None | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_predicate import KeywordPredicate
        from ..models.public_lexical_predicate_output import (
            PublicLexicalPredicateOutput,
        )
        from ..models.response_filter_output_value_labels_type_0 import (
            ResponseFilterOutputValueLabelsType0,
        )

        field = self.field

        predicate: dict[str, Any]
        if isinstance(self.predicate, KeywordPredicate):
            predicate = self.predicate.to_dict()
        elif isinstance(self.predicate, PublicLexicalPredicateOutput):
            predicate = self.predicate.to_dict()
        else:
            predicate = self.predicate.to_dict()

        facetable: bool | None | Unset
        if isinstance(self.facetable, Unset):
            facetable = UNSET
        else:
            facetable = self.facetable

        field_type: None | str | Unset
        if isinstance(self.field_type, Unset):
            field_type = UNSET
        else:
            field_type = self.field_type

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        pushed_down: bool | None | Unset
        if isinstance(self.pushed_down, Unset):
            pushed_down = UNSET
        else:
            pushed_down = self.pushed_down

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, FilterRole):
            role = self.role.value
        else:
            role = self.role

        value_labels: dict[str, Any] | None | Unset
        if isinstance(self.value_labels, Unset):
            value_labels = UNSET
        elif isinstance(self.value_labels, ResponseFilterOutputValueLabelsType0):
            value_labels = self.value_labels.to_dict()
        else:
            value_labels = self.value_labels

        weight: float | None | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "predicate": predicate,
            }
        )
        if facetable is not UNSET:
            field_dict["facetable"] = facetable
        if field_type is not UNSET:
            field_dict["field_type"] = field_type
        if label is not UNSET:
            field_dict["label"] = label
        if pushed_down is not UNSET:
            field_dict["pushed_down"] = pushed_down
        if reason is not UNSET:
            field_dict["reason"] = reason
        if role is not UNSET:
            field_dict["role"] = role
        if value_labels is not UNSET:
            field_dict["value_labels"] = value_labels
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.keyword_predicate import KeywordPredicate
        from ..models.public_lexical_predicate_output import (
            PublicLexicalPredicateOutput,
        )
        from ..models.public_semantic_predicate_output import (
            PublicSemanticPredicateOutput,
        )
        from ..models.response_filter_output_value_labels_type_0 import (
            ResponseFilterOutputValueLabelsType0,
        )

        d = dict(src_dict)
        field = d.pop("field")

        def _parse_predicate(
            data: object,
        ) -> (
            KeywordPredicate
            | PublicLexicalPredicateOutput
            | PublicSemanticPredicateOutput
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                predicate_type_0 = KeywordPredicate.from_dict(data)

                return predicate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                predicate_type_1 = PublicLexicalPredicateOutput.from_dict(data)

                return predicate_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            predicate_type_2 = PublicSemanticPredicateOutput.from_dict(data)

            return predicate_type_2

        predicate = _parse_predicate(d.pop("predicate"))

        def _parse_facetable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        facetable = _parse_facetable(d.pop("facetable", UNSET))

        def _parse_field_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_type = _parse_field_type(d.pop("field_type", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_pushed_down(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        pushed_down = _parse_pushed_down(d.pop("pushed_down", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_role(data: object) -> FilterRole | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = FilterRole(data)

                return role_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FilterRole | None | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_value_labels(
            data: object,
        ) -> None | ResponseFilterOutputValueLabelsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_labels_type_0 = ResponseFilterOutputValueLabelsType0.from_dict(
                    data
                )

                return value_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResponseFilterOutputValueLabelsType0 | Unset, data)

        value_labels = _parse_value_labels(d.pop("value_labels", UNSET))

        def _parse_weight(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weight = _parse_weight(d.pop("weight", UNSET))

        response_filter_output = cls(
            field=field,
            predicate=predicate,
            facetable=facetable,
            field_type=field_type,
            label=label,
            pushed_down=pushed_down,
            reason=reason,
            role=role,
            value_labels=value_labels,
            weight=weight,
        )

        response_filter_output.additional_properties = d
        return response_filter_output

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
