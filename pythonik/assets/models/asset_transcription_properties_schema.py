from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_transcription_properties_schema_speaker_labels_type_0 import (
        AssetTranscriptionPropertiesSchemaSpeakerLabelsType0,
    )


T = TypeVar("T", bound="AssetTranscriptionPropertiesSchema")


@_attrs_define
class AssetTranscriptionPropertiesSchema:
    """
    Attributes:
        asset_id (None | Unset | UUID):
        id (None | Unset | UUID):
        language (None | str | Unset):
        speaker_labels (AssetTranscriptionPropertiesSchemaSpeakerLabelsType0 | None | Unset):
        system_domain_id (None | Unset | UUID):
        version_id (None | Unset | UUID):
    """

    asset_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    language: None | str | Unset = UNSET
    speaker_labels: (
        AssetTranscriptionPropertiesSchemaSpeakerLabelsType0 | None | Unset
    ) = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_transcription_properties_schema_speaker_labels_type_0 import (
            AssetTranscriptionPropertiesSchemaSpeakerLabelsType0,
        )

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        speaker_labels: dict[str, Any] | None | Unset
        if isinstance(self.speaker_labels, Unset):
            speaker_labels = UNSET
        elif isinstance(
            self.speaker_labels, AssetTranscriptionPropertiesSchemaSpeakerLabelsType0
        ):
            speaker_labels = self.speaker_labels.to_dict()
        else:
            speaker_labels = self.speaker_labels

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if speaker_labels is not UNSET:
            field_dict["speaker_labels"] = speaker_labels
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_transcription_properties_schema_speaker_labels_type_0 import (
            AssetTranscriptionPropertiesSchemaSpeakerLabelsType0,
        )

        d = dict(src_dict)

        def _parse_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_id_type_0 = UUID(data)

                return asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_speaker_labels(
            data: object,
        ) -> AssetTranscriptionPropertiesSchemaSpeakerLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                speaker_labels_type_0 = (
                    AssetTranscriptionPropertiesSchemaSpeakerLabelsType0.from_dict(data)
                )

                return speaker_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AssetTranscriptionPropertiesSchemaSpeakerLabelsType0 | None | Unset,
                data,
            )

        speaker_labels = _parse_speaker_labels(d.pop("speaker_labels", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        asset_transcription_properties_schema = cls(
            asset_id=asset_id,
            id=id,
            language=language,
            speaker_labels=speaker_labels,
            system_domain_id=system_domain_id,
            version_id=version_id,
        )

        asset_transcription_properties_schema.additional_properties = d
        return asset_transcription_properties_schema

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
