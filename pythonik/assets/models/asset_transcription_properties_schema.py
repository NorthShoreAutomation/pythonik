from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_transcription_properties_schema_speaker_labels import (
        AssetTranscriptionPropertiesSchemaSpeakerLabels,
    )


T = TypeVar("T", bound="AssetTranscriptionPropertiesSchema")


@_attrs_define
class AssetTranscriptionPropertiesSchema:
    """
    Attributes:
        asset_id (UUID | Unset):
        id (UUID | Unset):
        language (str | Unset):
        speaker_labels (AssetTranscriptionPropertiesSchemaSpeakerLabels | Unset):
        system_domain_id (UUID | Unset):
        version_id (UUID | Unset):
    """

    asset_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    language: str | Unset = UNSET
    speaker_labels: AssetTranscriptionPropertiesSchemaSpeakerLabels | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        language = self.language

        speaker_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.speaker_labels, Unset):
            speaker_labels = self.speaker_labels.to_dict()

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

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
        from ..models.asset_transcription_properties_schema_speaker_labels import (
            AssetTranscriptionPropertiesSchemaSpeakerLabels,
        )

        d = dict(src_dict)
        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        language = d.pop("language", UNSET)

        _speaker_labels = d.pop("speaker_labels", UNSET)
        speaker_labels: AssetTranscriptionPropertiesSchemaSpeakerLabels | Unset
        if isinstance(_speaker_labels, Unset):
            speaker_labels = UNSET
        else:
            speaker_labels = AssetTranscriptionPropertiesSchemaSpeakerLabels.from_dict(
                _speaker_labels
            )

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

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
