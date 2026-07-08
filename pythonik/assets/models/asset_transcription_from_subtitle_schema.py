from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        content (None | str | Unset):
        delete_old_transcriptions (bool | None | Unset):
        format_ (AssetTranscriptionFromSubtitleSchemaFormat | None | Unset):
        language (None | str | Unset):
        source_subtitle_id (None | Unset | UUID): Set to source subtitle_id or do not set and use the content fields
            instead
    """

    content: None | str | Unset = UNSET
    delete_old_transcriptions: bool | None | Unset = UNSET
    format_: AssetTranscriptionFromSubtitleSchemaFormat | None | Unset = UNSET
    language: None | str | Unset = UNSET
    source_subtitle_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        delete_old_transcriptions: bool | None | Unset
        if isinstance(self.delete_old_transcriptions, Unset):
            delete_old_transcriptions = UNSET
        else:
            delete_old_transcriptions = self.delete_old_transcriptions

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        elif isinstance(self.format_, AssetTranscriptionFromSubtitleSchemaFormat):
            format_ = self.format_.value
        else:
            format_ = self.format_

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        source_subtitle_id: None | str | Unset
        if isinstance(self.source_subtitle_id, Unset):
            source_subtitle_id = UNSET
        elif isinstance(self.source_subtitle_id, UUID):
            source_subtitle_id = str(self.source_subtitle_id)
        else:
            source_subtitle_id = self.source_subtitle_id

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

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_delete_old_transcriptions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_old_transcriptions = _parse_delete_old_transcriptions(
            d.pop("delete_old_transcriptions", UNSET)
        )

        def _parse_format_(
            data: object,
        ) -> AssetTranscriptionFromSubtitleSchemaFormat | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_1 = AssetTranscriptionFromSubtitleSchemaFormat(data)

                return format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetTranscriptionFromSubtitleSchemaFormat | None | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_source_subtitle_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_subtitle_id_type_0 = UUID(data)

                return source_subtitle_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_subtitle_id = _parse_source_subtitle_id(
            d.pop("source_subtitle_id", UNSET)
        )

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
