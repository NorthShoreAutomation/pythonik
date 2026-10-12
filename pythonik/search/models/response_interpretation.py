from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_filters import ResponseFilters


T = TypeVar("T", bound="ResponseInterpretation")


@_attrs_define
class ResponseInterpretation:
    """One way the query was read.

    Readings run best first until one finds something (``answered``); the
    others are "did you mean ...?" suggestions a client runs by replaying their
    ``filters`` as the request's ``replay``.

        Attributes:
            answered (bool | None | Unset):  Default: False.
            confidence (float | None | Unset):  Default: 1.0.
            filters (None | ResponseFilters | Unset):
            why (None | str | Unset):  Default: ''.
    """

    answered: bool | None | Unset = False
    confidence: float | None | Unset = 1.0
    filters: None | ResponseFilters | Unset = UNSET
    why: None | str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.response_filters import ResponseFilters

        answered: bool | None | Unset
        if isinstance(self.answered, Unset):
            answered = UNSET
        else:
            answered = self.answered

        confidence: float | None | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ResponseFilters):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        why: None | str | Unset
        if isinstance(self.why, Unset):
            why = UNSET
        else:
            why = self.why

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answered is not UNSET:
            field_dict["answered"] = answered
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if filters is not UNSET:
            field_dict["filters"] = filters
        if why is not UNSET:
            field_dict["why"] = why

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_filters import ResponseFilters

        d = dict(src_dict)

        def _parse_answered(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        answered = _parse_answered(d.pop("answered", UNSET))

        def _parse_confidence(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_filters(data: object) -> None | ResponseFilters | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_1 = ResponseFilters.from_dict(data)

                return filters_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResponseFilters | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_why(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        why = _parse_why(d.pop("why", UNSET))

        response_interpretation = cls(
            answered=answered,
            confidence=confidence,
            filters=filters,
            why=why,
        )

        response_interpretation.additional_properties = d
        return response_interpretation

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
