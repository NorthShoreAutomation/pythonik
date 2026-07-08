from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_transcription_settings_schema_media_type import (
    AnalysisTranscriptionSettingsSchemaMediaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_transcription_settings_schema_analysis_service_account_settings_type_0 import (
        AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0,
    )
    from ..models.analysis_transcription_settings_schema_service_type_type_1 import (
        AnalysisTranscriptionSettingsSchemaServiceTypeType1,
    )
    from ..models.analysis_transcription_settings_schema_settings_type_0 import (
        AnalysisTranscriptionSettingsSchemaSettingsType0,
    )


T = TypeVar("T", bound="AnalysisTranscriptionSettingsSchema")


@_attrs_define
class AnalysisTranscriptionSettingsSchema:
    """
    Attributes:
        analysis_service_account_id (UUID):
        media_type (AnalysisTranscriptionSettingsSchemaMediaType):
        name (str):
        analysis_service_account_settings (AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0 | None
            | Unset):
        enabled (bool | None | Unset):
        id (None | Unset | UUID):
        is_default (bool | None | Unset):
        service_type (AnalysisTranscriptionSettingsSchemaServiceTypeType1 | None | Unset):
        settings (AnalysisTranscriptionSettingsSchemaSettingsType0 | None | Unset):
    """

    analysis_service_account_id: UUID
    media_type: AnalysisTranscriptionSettingsSchemaMediaType
    name: str
    analysis_service_account_settings: (
        AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0
        | None
        | Unset
    ) = UNSET
    enabled: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_default: bool | None | Unset = UNSET
    service_type: AnalysisTranscriptionSettingsSchemaServiceTypeType1 | None | Unset = (
        UNSET
    )
    settings: AnalysisTranscriptionSettingsSchemaSettingsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analysis_transcription_settings_schema_analysis_service_account_settings_type_0 import (
            AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0,
        )
        from ..models.analysis_transcription_settings_schema_service_type_type_1 import (
            AnalysisTranscriptionSettingsSchemaServiceTypeType1,
        )
        from ..models.analysis_transcription_settings_schema_settings_type_0 import (
            AnalysisTranscriptionSettingsSchemaSettingsType0,
        )

        analysis_service_account_id = str(self.analysis_service_account_id)

        media_type = self.media_type.value

        name = self.name

        analysis_service_account_settings: dict[str, Any] | None | Unset
        if isinstance(self.analysis_service_account_settings, Unset):
            analysis_service_account_settings = UNSET
        elif isinstance(
            self.analysis_service_account_settings,
            AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0,
        ):
            analysis_service_account_settings = (
                self.analysis_service_account_settings.to_dict()
            )
        else:
            analysis_service_account_settings = self.analysis_service_account_settings

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_default: bool | None | Unset
        if isinstance(self.is_default, Unset):
            is_default = UNSET
        else:
            is_default = self.is_default

        service_type: dict[str, Any] | None | Unset
        if isinstance(self.service_type, Unset):
            service_type = UNSET
        elif isinstance(
            self.service_type, AnalysisTranscriptionSettingsSchemaServiceTypeType1
        ):
            service_type = self.service_type.to_dict()
        else:
            service_type = self.service_type

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(
            self.settings, AnalysisTranscriptionSettingsSchemaSettingsType0
        ):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysis_service_account_id": analysis_service_account_id,
                "media_type": media_type,
                "name": name,
            }
        )
        if analysis_service_account_settings is not UNSET:
            field_dict["analysis_service_account_settings"] = (
                analysis_service_account_settings
            )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if service_type is not UNSET:
            field_dict["service_type"] = service_type
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analysis_transcription_settings_schema_analysis_service_account_settings_type_0 import (
            AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0,
        )
        from ..models.analysis_transcription_settings_schema_service_type_type_1 import (
            AnalysisTranscriptionSettingsSchemaServiceTypeType1,
        )
        from ..models.analysis_transcription_settings_schema_settings_type_0 import (
            AnalysisTranscriptionSettingsSchemaSettingsType0,
        )

        d = dict(src_dict)
        analysis_service_account_id = UUID(d.pop("analysis_service_account_id"))

        media_type = AnalysisTranscriptionSettingsSchemaMediaType(d.pop("media_type"))

        name = d.pop("name")

        def _parse_analysis_service_account_settings(
            data: object,
        ) -> (
            AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                analysis_service_account_settings_type_0 = AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0.from_dict(
                    data
                )

                return analysis_service_account_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AnalysisTranscriptionSettingsSchemaAnalysisServiceAccountSettingsType0
                | None
                | Unset,
                data,
            )

        analysis_service_account_settings = _parse_analysis_service_account_settings(
            d.pop("analysis_service_account_settings", UNSET)
        )

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

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

        def _parse_is_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_default = _parse_is_default(d.pop("is_default", UNSET))

        def _parse_service_type(
            data: object,
        ) -> AnalysisTranscriptionSettingsSchemaServiceTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                service_type_type_1 = (
                    AnalysisTranscriptionSettingsSchemaServiceTypeType1.from_dict(data)
                )

                return service_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AnalysisTranscriptionSettingsSchemaServiceTypeType1 | None | Unset, data
            )

        service_type = _parse_service_type(d.pop("service_type", UNSET))

        def _parse_settings(
            data: object,
        ) -> AnalysisTranscriptionSettingsSchemaSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = (
                    AnalysisTranscriptionSettingsSchemaSettingsType0.from_dict(data)
                )

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AnalysisTranscriptionSettingsSchemaSettingsType0 | None | Unset, data
            )

        settings = _parse_settings(d.pop("settings", UNSET))

        analysis_transcription_settings_schema = cls(
            analysis_service_account_id=analysis_service_account_id,
            media_type=media_type,
            name=name,
            analysis_service_account_settings=analysis_service_account_settings,
            enabled=enabled,
            id=id,
            is_default=is_default,
            service_type=service_type,
            settings=settings,
        )

        analysis_transcription_settings_schema.additional_properties = d
        return analysis_transcription_settings_schema

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
