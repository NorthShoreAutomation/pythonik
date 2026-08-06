from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcription_element_type_schema import (
        TranscriptionElementTypeSchema,
    )


T = TypeVar("T", bound="TranscriptionTypeSchema")


@_attrs_define
class TranscriptionTypeSchema:
    """
    Attributes:
        words (list[TranscriptionElementTypeSchema]):
        speaker (int | None | Unset):
    """

    words: list[TranscriptionElementTypeSchema]
    speaker: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        words = []
        for words_item_data in self.words:
            words_item = words_item_data.to_dict()
            words.append(words_item)

        speaker: int | None | Unset
        if isinstance(self.speaker, Unset):
            speaker = UNSET
        else:
            speaker = self.speaker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "words": words,
            }
        )
        if speaker is not UNSET:
            field_dict["speaker"] = speaker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcription_element_type_schema import (
            TranscriptionElementTypeSchema,
        )

        d = dict(src_dict)
        words = []
        _words = d.pop("words")
        for words_item_data in _words:
            words_item = TranscriptionElementTypeSchema.from_dict(words_item_data)

            words.append(words_item)

        def _parse_speaker(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        speaker = _parse_speaker(d.pop("speaker", UNSET))

        transcription_type_schema = cls(
            words=words,
            speaker=speaker,
        )

        transcription_type_schema.additional_properties = d
        return transcription_type_schema

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
