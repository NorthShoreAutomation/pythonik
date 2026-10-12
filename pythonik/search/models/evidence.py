from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.evidence_kind import EvidenceKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Evidence")


@_attrs_define
class Evidence:
    """One reason a hit is in the list, from one source.

    A hit carries a list of these. `field` is the backend's own name for where
    this came from (`transcription_text.analyzed`); `location` is the same
    thing in the words a person reads (`transcript`). `text` carries the
    highlight markers `[[mark]]` / `[[/mark]]` around the matched terms.

    An empty list means nothing matched textually — the filters alone selected
    the hit. `match.quality` says so as a value you can branch on.

        Attributes:
            field (None | str | Unset):
            kind (EvidenceKind | None | Unset):
            location (None | str | Unset):
            source (None | str | Unset): Which backend gave this account, as its internal key.
            source_label (None | str | Unset): That backend's display name ("iconik", "TwelveLabs").
            text (None | str | Unset):
    """

    field: None | str | Unset = UNSET
    kind: EvidenceKind | None | Unset = UNSET
    location: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    source_label: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, EvidenceKind):
            kind = self.kind.value
        else:
            kind = self.kind

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        source_label: None | str | Unset
        if isinstance(self.source_label, Unset):
            source_label = UNSET
        else:
            source_label = self.source_label

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if kind is not UNSET:
            field_dict["kind"] = kind
        if location is not UNSET:
            field_dict["location"] = location
        if source is not UNSET:
            field_dict["source"] = source
        if source_label is not UNSET:
            field_dict["source_label"] = source_label
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))

        def _parse_kind(data: object) -> EvidenceKind | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_1 = EvidenceKind(data)

                return kind_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvidenceKind | None | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_source_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_label = _parse_source_label(d.pop("source_label", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        evidence = cls(
            field=field,
            kind=kind,
            location=location,
            source=source,
            source_label=source_label,
            text=text,
        )

        evidence.additional_properties = d
        return evidence

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
