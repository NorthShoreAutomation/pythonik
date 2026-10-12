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

from ..models.public_lexical_predicate_output_operator import (
    PublicLexicalPredicateOutputOperator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicLexicalPredicateOutput")


@_attrs_define
class PublicLexicalPredicateOutput:
    """A lexical clause as the API states it: without ``tier``.

    ``tier`` is compilation mechanics; the API exposes its outcome as
    :class:`FilterRole` instead (the two can disagree, e.g. a gate-lifted round
    runs ``require`` words that only rank). A replay reconstructs the tier from
    the role.

        Attributes:
            any_of (list[str] | None | Unset):
            fuzziness (None | str | Unset):
            kind (Literal['lexical'] | Unset):  Default: 'lexical'.
            operator (None | PublicLexicalPredicateOutputOperator | Unset):
            sub_field (None | str | Unset):
            terms (None | str | Unset):  Default: ''.
    """

    any_of: list[str] | None | Unset = UNSET
    fuzziness: None | str | Unset = UNSET
    kind: Literal["lexical"] | Unset = "lexical"
    operator: None | PublicLexicalPredicateOutputOperator | Unset = UNSET
    sub_field: None | str | Unset = UNSET
    terms: None | str | Unset = ""
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
        elif isinstance(self.operator, PublicLexicalPredicateOutputOperator):
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
        ) -> None | PublicLexicalPredicateOutputOperator | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operator_type_1 = PublicLexicalPredicateOutputOperator(data)

                return operator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicLexicalPredicateOutputOperator | Unset, data)

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

        public_lexical_predicate_output = cls(
            any_of=any_of,
            fuzziness=fuzziness,
            kind=kind,
            operator=operator,
            sub_field=sub_field,
            terms=terms,
        )

        public_lexical_predicate_output.additional_properties = d
        return public_lexical_predicate_output

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
