from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_predicate_op import KeywordPredicateOp
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_bound import RangeBound


T = TypeVar("T", bound="KeywordPredicate")


@_attrs_define
class KeywordPredicate:
    """Exact keyword / metadata constraint.

    Ops: ``eq`` (scalar), ``in`` (ANY of a list), ``all`` (EVERY value of a
    list must be present -- multivalued fields), ``range`` (bounds),
    ``exists`` (field presence; ``value`` is ignored and normalized to ``True``)
    and ``any_of`` (see below). ``negate`` inverts whichever op is set ("not
    archived", "not in July", "has no approval status"), composing with every op
    instead of doubling the op vocabulary.

    ``any_of`` is the *disjunctive* op: ``value`` is a list of branches (each a
    scalar / list / :class:`RangeBound`) on the **same field**, of which at least
    one must match -- the one way to state a mandatory "A or B" that plain
    clauses cannot, since those all AND together (two ranges on one field would
    contradict). Its canonical use is an OR of date windows ("created this month
    or three months ago"). Negated, De Morgan applies: "in none of the branches".
    Cross-field OR is explicitly out of scope: it would explode both pushdown and
    gate validation, and a disjunction across fields is better expressed as a
    ``try`` probe.

    The Understanding compiler's ``_keyword_predicate`` is the single place
    that builds these; each backend adapter folds only the ops it declares
    support for (``FieldCapability.supported_ops``), so a simple plugin never
    sees a shape it cannot express -- mandatory enforcement of the rest is the
    authority gate's job.

        Attributes:
            op (KeywordPredicateOp):
            value (bool | float | int | list[bool | float | int | list[bool | float | int | str] | RangeBound | str] |
                RangeBound | str):
            kind (Literal['keyword'] | Unset):  Default: 'keyword'.
            negate (bool | None | Unset):  Default: False.
    """

    op: KeywordPredicateOp
    value: (
        bool
        | float
        | int
        | list[bool | float | int | list[bool | float | int | str] | RangeBound | str]
        | RangeBound
        | str
    )
    kind: Literal["keyword"] | Unset = "keyword"
    negate: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.range_bound import RangeBound

        op = self.op.value

        value: (
            bool
            | dict[str, Any]
            | float
            | int
            | list[
                bool
                | dict[str, Any]
                | float
                | int
                | list[bool | float | int | str]
                | str
            ]
            | str
        )
        if isinstance(self.value, RangeBound):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = []
            for value_type_5_item_data in self.value:
                value_type_5_item: (
                    bool
                    | dict[str, Any]
                    | float
                    | int
                    | list[bool | float | int | str]
                    | str
                )
                if isinstance(value_type_5_item_data, RangeBound):
                    value_type_5_item = value_type_5_item_data.to_dict()
                elif isinstance(value_type_5_item_data, list):
                    value_type_5_item = []
                    for value_type_5_item_type_1_item_data in value_type_5_item_data:
                        value_type_5_item_type_1_item: bool | float | int | str
                        value_type_5_item_type_1_item = (
                            value_type_5_item_type_1_item_data
                        )
                        value_type_5_item.append(value_type_5_item_type_1_item)

                else:
                    value_type_5_item = value_type_5_item_data
                value.append(value_type_5_item)

        else:
            value = self.value

        kind: Literal["keyword"] | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        negate: bool | None | Unset
        if isinstance(self.negate, Unset):
            negate = UNSET
        else:
            negate = self.negate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "value": value,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if negate is not UNSET:
            field_dict["negate"] = negate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_bound import RangeBound

        d = dict(src_dict)
        op = KeywordPredicateOp(d.pop("op"))

        def _parse_value(
            data: object,
        ) -> (
            bool
            | float
            | int
            | list[
                bool | float | int | list[bool | float | int | str] | RangeBound | str
            ]
            | RangeBound
            | str
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_4 = RangeBound.from_dict(data)

                return value_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_5 = []
                _value_type_5 = data
                for value_type_5_item_data in _value_type_5:

                    def _parse_value_type_5_item(
                        data: object,
                    ) -> (
                        bool
                        | float
                        | int
                        | list[bool | float | int | str]
                        | RangeBound
                        | str
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            value_type_5_item_type_0 = RangeBound.from_dict(data)

                            return value_type_5_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, list):
                                raise TypeError()
                            value_type_5_item_type_1 = []
                            _value_type_5_item_type_1 = data
                            for (
                                value_type_5_item_type_1_item_data
                            ) in _value_type_5_item_type_1:

                                def _parse_value_type_5_item_type_1_item(
                                    data: object,
                                ) -> bool | float | int | str:
                                    return cast(bool | float | int | str, data)

                                value_type_5_item_type_1_item = (
                                    _parse_value_type_5_item_type_1_item(
                                        value_type_5_item_type_1_item_data
                                    )
                                )

                                value_type_5_item_type_1.append(
                                    value_type_5_item_type_1_item
                                )

                            return value_type_5_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            bool
                            | float
                            | int
                            | list[bool | float | int | str]
                            | RangeBound
                            | str,
                            data,
                        )

                    value_type_5_item = _parse_value_type_5_item(value_type_5_item_data)

                    value_type_5.append(value_type_5_item)

                return value_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool
                | float
                | int
                | list[
                    bool
                    | float
                    | int
                    | list[bool | float | int | str]
                    | RangeBound
                    | str
                ]
                | RangeBound
                | str,
                data,
            )

        value = _parse_value(d.pop("value"))

        def _parse_kind(data: object) -> Literal["keyword"] | Unset:
            if isinstance(data, Unset):
                return data
            kind_type_0 = cast(Literal["keyword"], data)
            if kind_type_0 != "keyword":
                raise ValueError(
                    f"kind_type_0 must match const 'keyword', got '{kind_type_0}'"
                )
            return kind_type_0

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_negate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        negate = _parse_negate(d.pop("negate", UNSET))

        keyword_predicate = cls(
            op=op,
            value=value,
            kind=kind,
            negate=negate,
        )

        keyword_predicate.additional_properties = d
        return keyword_predicate

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
