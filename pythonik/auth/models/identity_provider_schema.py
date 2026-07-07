from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_schema_type import IdentityProviderSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_schema_saml_settings import (
        IdentityProviderSchemaSamlSettings,
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
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        id (UUID | Unset):
        public_id (UUID | Unset):
        saml_settings (IdentityProviderSchemaSamlSettings | Unset):
        verbose_logging (bool | Unset):
    """

    settings: IdentityProviderSchemaSettings
    type_: IdentityProviderSchemaType
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    public_id: UUID | Unset = UNSET
    saml_settings: IdentityProviderSchemaSamlSettings | Unset = UNSET
    verbose_logging: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = self.settings.to_dict()

        type_ = self.type_.value

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        public_id: str | Unset = UNSET
        if not isinstance(self.public_id, Unset):
            public_id = str(self.public_id)

        saml_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.saml_settings, Unset):
            saml_settings = self.saml_settings.to_dict()

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
        from ..models.identity_provider_schema_saml_settings import (
            IdentityProviderSchemaSamlSettings,
        )
        from ..models.identity_provider_schema_settings import (
            IdentityProviderSchemaSettings,
        )

        d = dict(src_dict)
        settings = IdentityProviderSchemaSettings.from_dict(d.pop("settings"))

        type_ = IdentityProviderSchemaType(d.pop("type"))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _public_id = d.pop("public_id", UNSET)
        public_id: UUID | Unset
        if isinstance(_public_id, Unset):
            public_id = UNSET
        else:
            public_id = UUID(_public_id)

        _saml_settings = d.pop("saml_settings", UNSET)
        saml_settings: IdentityProviderSchemaSamlSettings | Unset
        if isinstance(_saml_settings, Unset):
            saml_settings = UNSET
        else:
            saml_settings = IdentityProviderSchemaSamlSettings.from_dict(_saml_settings)

        verbose_logging = d.pop("verbose_logging", UNSET)

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
