from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_lexical_predicate_input_operator import (
    PublicLexicalPredicateInputOperator,
)
from ..models.tier import Tier
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicLexicalPredicateInput")


@_attrs_define
class PublicLexicalPredicateInput:
    """A lexical clause as the API states it: without ``tier``.

    ``tier`` is compilation mechanics; the API exposes its outcome as
    :class:`FilterRole` instead (the two can disagree, e.g. a gate-lifted round
    runs ``require`` words that only rank). A replay reconstructs the tier from
    the role.

        Attributes:
            any_of (list[str] | None | Unset):
            fuzziness (None | str | Unset):
            kind (Literal['lexical'] | Unset):  Default: 'lexical'.
            operator (None | PublicLexicalPredicateInputOperator | Unset):
            sub_field (None | str | Unset):
            terms (None | str | Unset):  Default: ''.
            tier (None | Tier | Unset):
    """

    any_of: list[str] | None | Unset = UNSET
    fuzziness: None | str | Unset = UNSET
    kind: Literal["lexical"] | Unset = "lexical"
    operator: None | PublicLexicalPredicateInputOperator | Unset = UNSET
    sub_field: None | str | Unset = UNSET
    terms: None | str | Unset = ""
    tier: None | Tier | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        any_of: list[str] | None | Unset
        if isinstance(self.any_of, Unset):
            any_of = UNSET
        elif isinstance(self.any_of, list):
            any_of = self.any_of

        else:
            any_of = self.any_of

        fuzziness: None | str | Unset
        if isinstance(self.fuzziness, Unset):
            fuzziness = UNSET
        else:
            fuzziness = self.fuzziness

        kind: Literal["lexical"] | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        operator: None | str | Unset
        if isinstance(self.operator, Unset):
            operator = UNSET
        elif isinstance(self.operator, PublicLexicalPredicateInputOperator):
            operator = self.operator.value
        else:
            operator = self.operator

        sub_field: None | str | Unset
        if isinstance(self.sub_field, Unset):
            sub_field = UNSET
        else:
            sub_field = self.sub_field

        terms: None | str | Unset
        if isinstance(self.terms, Unset):
            terms = UNSET
        else:
            terms = self.terms

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        elif isinstance(self.tier, Tier):
            tier = self.tier.value
        else:
            tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if any_of is not UNSET:
            field_dict["any_of"] = any_of
        if fuzziness is not UNSET:
            field_dict["fuzziness"] = fuzziness
        if kind is not UNSET:
            field_dict["kind"] = kind
        if operator is not UNSET:
            field_dict["operator"] = operator
        if sub_field is not UNSET:
            field_dict["sub_field"] = sub_field
        if terms is not UNSET:
            field_dict["terms"] = terms
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_any_of(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                any_of_type_0 = cast(list[str], data)

                return any_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        any_of = _parse_any_of(d.pop("any_of", UNSET))

        def _parse_fuzziness(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fuzziness = _parse_fuzziness(d.pop("fuzziness", UNSET))

        def _parse_kind(data: object) -> Literal["lexical"] | Unset:
            if isinstance(data, Unset):
                return data
            kind_type_0 = cast(Literal["lexical"], data)
            if kind_type_0 != "lexical":
                raise ValueError(
                    f"kind_type_0 must match const 'lexical', got '{kind_type_0}'"
                )
            return kind_type_0

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_operator(
            data: object,
        ) -> None | PublicLexicalPredicateInputOperator | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operator_type_1 = PublicLexicalPredicateInputOperator(data)

                return operator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicLexicalPredicateInputOperator | Unset, data)

        operator = _parse_operator(d.pop("operator", UNSET))

        def _parse_sub_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_field = _parse_sub_field(d.pop("sub_field", UNSET))

        def _parse_terms(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terms = _parse_terms(d.pop("terms", UNSET))

        def _parse_tier(data: object) -> None | Tier | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tier_type_1 = Tier(data)

                return tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Tier | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        public_lexical_predicate_input = cls(
            any_of=any_of,
            fuzziness=fuzziness,
            kind=kind,
            operator=operator,
            sub_field=sub_field,
            terms=terms,
            tier=tier,
        )

        public_lexical_predicate_input.additional_properties = d
        return public_lexical_predicate_input

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
