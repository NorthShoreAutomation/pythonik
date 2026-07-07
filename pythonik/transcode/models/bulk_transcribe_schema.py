from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_transcribe_schema_object_type import BulkTranscribeSchemaObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkTranscribeSchema")


@_attrs_define
class BulkTranscribeSchema:
    """
    Attributes:
        object_ids (list[UUID]):
        object_type (BulkTranscribeSchemaObjectType):
        engine (None | str | Unset):
        force (bool | Unset):  Default: False.
        language (None | str | Unset):
        profile_id (UUID | Unset):
        speakers (int | None | Unset):
        summary (bool | None | Unset):
        topics_extraction (bool | Unset):  Default: True.
        translate_languages (list[str] | None | Unset):
    """

    object_ids: list[UUID]
    object_type: BulkTranscribeSchemaObjectType
    engine: None | str | Unset = UNSET
    force: bool | Unset = False
    language: None | str | Unset = UNSET
    profile_id: UUID | Unset = UNSET
    speakers: int | None | Unset = UNSET
    summary: bool | None | Unset = UNSET
    topics_extraction: bool | Unset = True
    translate_languages: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

        engine: None | str | Unset
        if isinstance(self.engine, Unset):
            engine = UNSET
        else:
            engine = self.engine

        force = self.force

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        profile_id: str | Unset = UNSET
        if not isinstance(self.profile_id, Unset):
            profile_id = str(self.profile_id)

        speakers: int | None | Unset
        if isinstance(self.speakers, Unset):
            speakers = UNSET
        else:
            speakers = self.speakers

        summary: bool | None | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        topics_extraction = self.topics_extraction

        translate_languages: list[str] | None | Unset
        if isinstance(self.translate_languages, Unset):
            translate_languages = UNSET
        elif isinstance(self.translate_languages, list):
            translate_languages = self.translate_languages

        else:
            translate_languages = self.translate_languages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids": object_ids,
                "object_type": object_type,
            }
        )
        if engine is not UNSET:
            field_dict["engine"] = engine
        if force is not UNSET:
            field_dict["force"] = force
        if language is not UNSET:
            field_dict["language"] = language
        if profile_id is not UNSET:
            field_dict["profile_id"] = profile_id
        if speakers is not UNSET:
            field_dict["speakers"] = speakers
        if summary is not UNSET:
            field_dict["summary"] = summary
        if topics_extraction is not UNSET:
            field_dict["topics_extraction"] = topics_extraction
        if translate_languages is not UNSET:
            field_dict["translate_languages"] = translate_languages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        object_type = BulkTranscribeSchemaObjectType(d.pop("object_type"))

        def _parse_engine(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        engine = _parse_engine(d.pop("engine", UNSET))

        force = d.pop("force", UNSET)

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        _profile_id = d.pop("profile_id", UNSET)
        profile_id: UUID | Unset
        if isinstance(_profile_id, Unset):
            profile_id = UNSET
        else:
            profile_id = UUID(_profile_id)

        def _parse_speakers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        speakers = _parse_speakers(d.pop("speakers", UNSET))

        def _parse_summary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        topics_extraction = d.pop("topics_extraction", UNSET)

        def _parse_translate_languages(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                translate_languages_type_0 = cast(list[str], data)

                return translate_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        translate_languages = _parse_translate_languages(
            d.pop("translate_languages", UNSET)
        )

        bulk_transcribe_schema = cls(
            object_ids=object_ids,
            object_type=object_type,
            engine=engine,
            force=force,
            language=language,
            profile_id=profile_id,
            speakers=speakers,
            summary=summary,
            topics_extraction=topics_extraction,
            translate_languages=translate_languages,
        )

        bulk_transcribe_schema.additional_properties = d
        return bulk_transcribe_schema

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
