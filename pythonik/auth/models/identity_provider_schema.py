from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_schema_type import IdentityProviderSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_schema_saml_settings_type_0 import (
        IdentityProviderSchemaSamlSettingsType0,
    )
    from ..models.identity_provider_schema_settings import (
        IdentityProviderSchemaSettings,
    )


T = TypeVar("T", bound="IdentityProviderSchema")


@_attrs_define
class IdentityProviderSchema:
    """
    Attributes:
        settings (IdentityProviderSchemaSettings):
        type_ (IdentityProviderSchemaType):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        id (None | Unset | UUID):
        public_id (None | Unset | UUID):
        saml_settings (IdentityProviderSchemaSamlSettingsType0 | None | Unset):
        verbose_logging (bool | None | Unset):
    """

    settings: IdentityProviderSchemaSettings
    type_: IdentityProviderSchemaType
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    public_id: None | Unset | UUID = UNSET
    saml_settings: IdentityProviderSchemaSamlSettingsType0 | None | Unset = UNSET
    verbose_logging: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.identity_provider_schema_saml_settings_type_0 import (
            IdentityProviderSchemaSamlSettingsType0,
        )

        settings = self.settings.to_dict()

        type_ = self.type_.value

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        public_id: None | str | Unset
        if isinstance(self.public_id, Unset):
            public_id = UNSET
        elif isinstance(self.public_id, UUID):
            public_id = str(self.public_id)
        else:
            public_id = self.public_id

        saml_settings: dict[str, Any] | None | Unset
        if isinstance(self.saml_settings, Unset):
            saml_settings = UNSET
        elif isinstance(self.saml_settings, IdentityProviderSchemaSamlSettingsType0):
            saml_settings = self.saml_settings.to_dict()
        else:
            saml_settings = self.saml_settings

        verbose_logging: bool | None | Unset
        if isinstance(self.verbose_logging, Unset):
            verbose_logging = UNSET
        else:
            verbose_logging = self.verbose_logging

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
                "type": type_,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if id is not UNSET:
            field_dict["id"] = id
        if public_id is not UNSET:
            field_dict["public_id"] = public_id
        if saml_settings is not UNSET:
            field_dict["saml_settings"] = saml_settings
        if verbose_logging is not UNSET:
            field_dict["verbose_logging"] = verbose_logging

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_schema_saml_settings_type_0 import (
            IdentityProviderSchemaSamlSettingsType0,
        )
        from ..models.identity_provider_schema_settings import (
            IdentityProviderSchemaSettings,
        )

        d = dict(src_dict)
        settings = IdentityProviderSchemaSettings.from_dict(d.pop("settings"))

        type_ = IdentityProviderSchemaType(d.pop("type"))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

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

        def _parse_public_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                public_id_type_0 = UUID(data)

                return public_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        public_id = _parse_public_id(d.pop("public_id", UNSET))

        def _parse_saml_settings(
            data: object,
        ) -> IdentityProviderSchemaSamlSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                saml_settings_type_0 = (
                    IdentityProviderSchemaSamlSettingsType0.from_dict(data)
                )

                return saml_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IdentityProviderSchemaSamlSettingsType0 | None | Unset, data)

        saml_settings = _parse_saml_settings(d.pop("saml_settings", UNSET))

        def _parse_verbose_logging(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        verbose_logging = _parse_verbose_logging(d.pop("verbose_logging", UNSET))

        identity_provider_schema = cls(
            settings=settings,
            type_=type_,
            date_created=date_created,
            date_modified=date_modified,
            id=id,
            public_id=public_id,
            saml_settings=saml_settings,
            verbose_logging=verbose_logging,
        )

        identity_provider_schema.additional_properties = d
        return identity_provider_schema

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
