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

from ..models.tier import Tier
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicSemanticPredicateInput")


@_attrs_define
class PublicSemanticPredicateInput:
    """A semantic clause as the API states it: without ``tier`` (always ``SCORING``).

    Attributes:
        text (str):
        kind (Literal['semantic'] | Unset):  Default: 'semantic'.
        tier (None | Tier | Unset):
    """

    text: str
    kind: Literal["semantic"] | Unset = "semantic"
    tier: None | Tier | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        kind: Literal["semantic"] | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        elif isinstance(self.tier, Tier):
            tier = self.tier.value
        else:
            tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        def _parse_kind(data: object) -> Literal["semantic"] | Unset:
            if isinstance(data, Unset):
                return data
            kind_type_0 = cast(Literal["semantic"], data)
            if kind_type_0 != "semantic":
                raise ValueError(
                    f"kind_type_0 must match const 'semantic', got '{kind_type_0}'"
                )
            return kind_type_0

        kind = _parse_kind(d.pop("kind", UNSET))

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

        public_semantic_predicate_input = cls(
            text=text,
            kind=kind,
            tier=tier,
        )

        public_semantic_predicate_input.additional_properties = d
        return public_semantic_predicate_input

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
