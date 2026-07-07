from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_profile_schema_media_type import AnalysisProfileSchemaMediaType
from ..models.analysis_profile_schema_service_type import (
    AnalysisProfileSchemaServiceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_profile_schema_settings import AnalysisProfileSchemaSettings


T = TypeVar("T", bound="AnalysisProfileSchema")


@_attrs_define
class AnalysisProfileSchema:
    """
    Attributes:
        analysis_service_account_id (UUID):
        media_type (AnalysisProfileSchemaMediaType):
        name (str):
        enabled (bool | Unset):
        id (UUID | Unset):
        is_default (bool | Unset):
        service_type (AnalysisProfileSchemaServiceType | Unset):
        settings (AnalysisProfileSchemaSettings | Unset):
    """

    analysis_service_account_id: UUID
    media_type: AnalysisProfileSchemaMediaType
    name: str
    enabled: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    is_default: bool | Unset = UNSET
    service_type: AnalysisProfileSchemaServiceType | Unset = UNSET
    settings: AnalysisProfileSchemaSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis_service_account_id = str(self.analysis_service_account_id)

        media_type = self.media_type.value

        name = self.name

        enabled = self.enabled

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_default = self.is_default

        service_type: str | Unset = UNSET
        if not isinstance(self.service_type, Unset):
            service_type = self.service_type.value

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysis_service_account_id": analysis_service_account_id,
                "media_type": media_type,
                "name": name,
            }
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
        from ..models.analysis_profile_schema_settings import (
            AnalysisProfileSchemaSettings,
        )

        d = dict(src_dict)
        analysis_service_account_id = UUID(d.pop("analysis_service_account_id"))

        media_type = AnalysisProfileSchemaMediaType(d.pop("media_type"))

        name = d.pop("name")

        enabled = d.pop("enabled", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_default = d.pop("is_default", UNSET)

        _service_type = d.pop("service_type", UNSET)
        service_type: AnalysisProfileSchemaServiceType | Unset
        if isinstance(_service_type, Unset):
            service_type = UNSET
        else:
            service_type = AnalysisProfileSchemaServiceType(_service_type)

        _settings = d.pop("settings", UNSET)
        settings: AnalysisProfileSchemaSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = AnalysisProfileSchemaSettings.from_dict(_settings)

        analysis_profile_schema = cls(
            analysis_service_account_id=analysis_service_account_id,
            media_type=media_type,
            name=name,
            enabled=enabled,
            id=id,
            is_default=is_default,
            service_type=service_type,
            settings=settings,
        )

        analysis_profile_schema.additional_properties = d
        return analysis_profile_schema

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
