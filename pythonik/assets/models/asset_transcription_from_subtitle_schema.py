from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_transcription_from_subtitle_schema_format import (
    AssetTranscriptionFromSubtitleSchemaFormat,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetTranscriptionFromSubtitleSchema")


@_attrs_define
class AssetTranscriptionFromSubtitleSchema:
    """
    Attributes:
        content (str | Unset):
        delete_old_transcriptions (bool | Unset):
        format_ (AssetTranscriptionFromSubtitleSchemaFormat | Unset):
        language (str | Unset):
        source_subtitle_id (UUID | Unset): Set to source subtitle_id or do not set and use the content fields instead
    """

    content: str | Unset = UNSET
    delete_old_transcriptions: bool | Unset = UNSET
    format_: AssetTranscriptionFromSubtitleSchemaFormat | Unset = UNSET
    language: str | Unset = UNSET
    source_subtitle_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        delete_old_transcriptions = self.delete_old_transcriptions

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        language = self.language

        source_subtitle_id: str | Unset = UNSET
        if not isinstance(self.source_subtitle_id, Unset):
            source_subtitle_id = str(self.source_subtitle_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if delete_old_transcriptions is not UNSET:
            field_dict["delete_old_transcriptions"] = delete_old_transcriptions
        if format_ is not UNSET:
            field_dict["format"] = format_
        if language is not UNSET:
            field_dict["language"] = language
        if source_subtitle_id is not UNSET:
            field_dict["source_subtitle_id"] = source_subtitle_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        delete_old_transcriptions = d.pop("delete_old_transcriptions", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: AssetTranscriptionFromSubtitleSchemaFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = AssetTranscriptionFromSubtitleSchemaFormat(_format_)

        language = d.pop("language", UNSET)

        _source_subtitle_id = d.pop("source_subtitle_id", UNSET)
        source_subtitle_id: UUID | Unset
        if isinstance(_source_subtitle_id, Unset):
            source_subtitle_id = UNSET
        else:
            source_subtitle_id = UUID(_source_subtitle_id)

        asset_transcription_from_subtitle_schema = cls(
            content=content,
            delete_old_transcriptions=delete_old_transcriptions,
            format_=format_,
            language=language,
            source_subtitle_id=source_subtitle_id,
        )

        asset_transcription_from_subtitle_schema.additional_properties = d
        return asset_transcription_from_subtitle_schema

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
