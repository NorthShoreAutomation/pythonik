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

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicSemanticPredicateOutput")


@_attrs_define
class PublicSemanticPredicateOutput:
    """A semantic clause as the API states it: without ``tier`` (always ``SCORING``).

    Attributes:
        text (str):
        kind (Literal['semantic'] | Unset):  Default: 'semantic'.
    """

    text: str
    kind: Literal["semantic"] | Unset = "semantic"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        kind: Literal["semantic"] | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind

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

        public_semantic_predicate_output = cls(
            text=text,
            kind=kind,
        )

        public_semantic_predicate_output.additional_properties = d
        return public_semantic_predicate_output

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
