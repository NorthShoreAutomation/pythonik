from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_state import SourceState

T = TypeVar("T", bound="ResponseSource")


@_attrs_define
class ResponseSource:
    """One backend queried for these results, and how it fared (the public
    half of :class:`SourceRoundState`, without the round).

        Attributes:
            display_name (str):
            ref (str):
            state (SourceState): Per-source execution outcome (a slow/down source must not fail us).
    """

    display_name: str
    ref: str
    state: SourceState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        ref = self.ref

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "ref": ref,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        ref = d.pop("ref")

        state = SourceState(d.pop("state"))

        response_source = cls(
            display_name=display_name,
            ref=ref,
            state=state,
        )

        response_source.additional_properties = d
        return response_source

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
