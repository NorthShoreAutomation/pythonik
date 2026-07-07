from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscriptionElementType")


@_attrs_define
class TranscriptionElementType:
    """
    Attributes:
        end_ms (int):
        start_ms (int):
        value (str):
        score (float | Unset):
    """

    end_ms: int
    start_ms: int
    value: str
    score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_ms = self.end_ms

        start_ms = self.start_ms

        value = self.value

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_ms": end_ms,
                "start_ms": start_ms,
                "value": value,
            }
        )
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_ms = d.pop("end_ms")

        start_ms = d.pop("start_ms")

        value = d.pop("value")

        score = d.pop("score", UNSET)

        transcription_element_type = cls(
            end_ms=end_ms,
            start_ms=start_ms,
            value=value,
            score=score,
        )

        transcription_element_type.additional_properties = d
        return transcription_element_type

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
