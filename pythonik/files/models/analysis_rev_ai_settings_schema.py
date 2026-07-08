from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisRevAISettingsSchema")


@_attrs_define
class AnalysisRevAISettingsSchema:
    """
    Attributes:
        access_token (str):
        custom_vocabulary (list[str] | None | Unset):
        is_system (bool | None | Unset):
        metadata_view_id (None | str | Unset): View in which to save topic extraction time-based metadata
        summary_metadata_field (None | str | Unset): If a transcription summary is requested, save it to this metadata
            field
        topics_metadata_field (None | str | Unset): If topics extraction is requested, save result to this metadata
            field
    """

    access_token: str
    custom_vocabulary: list[str] | None | Unset = UNSET
    is_system: bool | None | Unset = UNSET
    metadata_view_id: None | str | Unset = UNSET
    summary_metadata_field: None | str | Unset = UNSET
    topics_metadata_field: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        custom_vocabulary: list[str] | None | Unset
        if isinstance(self.custom_vocabulary, Unset):
            custom_vocabulary = UNSET
        elif isinstance(self.custom_vocabulary, list):
            custom_vocabulary = self.custom_vocabulary

        else:
            custom_vocabulary = self.custom_vocabulary

        is_system: bool | None | Unset
        if isinstance(self.is_system, Unset):
            is_system = UNSET
        else:
            is_system = self.is_system

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        else:
            metadata_view_id = self.metadata_view_id

        summary_metadata_field: None | str | Unset
        if isinstance(self.summary_metadata_field, Unset):
            summary_metadata_field = UNSET
        else:
            summary_metadata_field = self.summary_metadata_field

        topics_metadata_field: None | str | Unset
        if isinstance(self.topics_metadata_field, Unset):
            topics_metadata_field = UNSET
        else:
            topics_metadata_field = self.topics_metadata_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
            }
        )
        if custom_vocabulary is not UNSET:
            field_dict["custom_vocabulary"] = custom_vocabulary
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if metadata_view_id is not UNSET:
            field_dict["metadata_view_id"] = metadata_view_id
        if summary_metadata_field is not UNSET:
            field_dict["summary_metadata_field"] = summary_metadata_field
        if topics_metadata_field is not UNSET:
            field_dict["topics_metadata_field"] = topics_metadata_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token")

        def _parse_custom_vocabulary(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_vocabulary_type_0 = cast(list[str], data)

                return custom_vocabulary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        custom_vocabulary = _parse_custom_vocabulary(d.pop("custom_vocabulary", UNSET))

        def _parse_is_system(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_system = _parse_is_system(d.pop("is_system", UNSET))

        def _parse_metadata_view_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_view_id = _parse_metadata_view_id(d.pop("metadata_view_id", UNSET))

        def _parse_summary_metadata_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary_metadata_field = _parse_summary_metadata_field(
            d.pop("summary_metadata_field", UNSET)
        )

        def _parse_topics_metadata_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        topics_metadata_field = _parse_topics_metadata_field(
            d.pop("topics_metadata_field", UNSET)
        )

        analysis_rev_ai_settings_schema = cls(
            access_token=access_token,
            custom_vocabulary=custom_vocabulary,
            is_system=is_system,
            metadata_view_id=metadata_view_id,
            summary_metadata_field=summary_metadata_field,
            topics_metadata_field=topics_metadata_field,
        )

        analysis_rev_ai_settings_schema.additional_properties = d
        return analysis_rev_ai_settings_schema

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
