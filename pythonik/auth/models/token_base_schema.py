from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_base_schema_system_domain_status import (
    TokenBaseSchemaSystemDomainStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_domain_user_system_schema import MultiDomainUserSystemSchema


T = TypeVar("T", bound="TokenBaseSchema")


@_attrs_define
class TokenBaseSchema:
    """
    Attributes:
        app_id (UUID | Unset):
        auth_system_domains (list[MultiDomainUserSystemSchema] | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        expires (datetime.datetime | Unset):
        id (UUID | Unset):
        is_admin (bool | Unset):
        is_mfa_authenticated (bool | Unset):
        is_saml_authenticated (bool | Unset):
        is_super_admin (bool | Unset):
        is_super_admin_light (bool | Unset):
        system_domain_id (UUID | Unset):
        system_domain_is_plg (bool | Unset):
        system_domain_status (TokenBaseSchemaSystemDomainStatus | Unset):
        system_domain_type (str | Unset):
        system_domain_warning_message (str | Unset):
        system_domains (list[UUID] | Unset):
        user_id (UUID | Unset):
    """

    app_id: UUID | Unset = UNSET
    auth_system_domains: list[MultiDomainUserSystemSchema] | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    expires: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    is_admin: bool | Unset = UNSET
    is_mfa_authenticated: bool | Unset = UNSET
    is_saml_authenticated: bool | Unset = UNSET
    is_super_admin: bool | Unset = UNSET
    is_super_admin_light: bool | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    system_domain_is_plg: bool | Unset = UNSET
    system_domain_status: TokenBaseSchemaSystemDomainStatus | Unset = UNSET
    system_domain_type: str | Unset = UNSET
    system_domain_warning_message: str | Unset = UNSET
    system_domains: list[UUID] | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id: str | Unset = UNSET
        if not isinstance(self.app_id, Unset):
            app_id = str(self.app_id)

        auth_system_domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auth_system_domains, Unset):
            auth_system_domains = []
            for auth_system_domains_item_data in self.auth_system_domains:
                auth_system_domains_item = auth_system_domains_item_data.to_dict()
                auth_system_domains.append(auth_system_domains_item)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        expires: str | Unset = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_admin = self.is_admin

        is_mfa_authenticated = self.is_mfa_authenticated

        is_saml_authenticated = self.is_saml_authenticated

        is_super_admin = self.is_super_admin

        is_super_admin_light = self.is_super_admin_light

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        system_domain_is_plg = self.system_domain_is_plg

        system_domain_status: str | Unset = UNSET
        if not isinstance(self.system_domain_status, Unset):
            system_domain_status = self.system_domain_status.value

        system_domain_type = self.system_domain_type

        system_domain_warning_message = self.system_domain_warning_message

        system_domains: list[str] | Unset = UNSET
        if not isinstance(self.system_domains, Unset):
            system_domains = []
            for system_domains_item_data in self.system_domains:
                system_domains_item = str(system_domains_item_data)
                system_domains.append(system_domains_item)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if auth_system_domains is not UNSET:
            field_dict["auth_system_domains"] = auth_system_domains
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if expires is not UNSET:
            field_dict["expires"] = expires
        if id is not UNSET:
            field_dict["id"] = id
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if is_mfa_authenticated is not UNSET:
            field_dict["is_mfa_authenticated"] = is_mfa_authenticated
        if is_saml_authenticated is not UNSET:
            field_dict["is_saml_authenticated"] = is_saml_authenticated
        if is_super_admin is not UNSET:
            field_dict["is_super_admin"] = is_super_admin
        if is_super_admin_light is not UNSET:
            field_dict["is_super_admin_light"] = is_super_admin_light
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if system_domain_is_plg is not UNSET:
            field_dict["system_domain_is_plg"] = system_domain_is_plg
        if system_domain_status is not UNSET:
            field_dict["system_domain_status"] = system_domain_status
        if system_domain_type is not UNSET:
            field_dict["system_domain_type"] = system_domain_type
        if system_domain_warning_message is not UNSET:
            field_dict["system_domain_warning_message"] = system_domain_warning_message
        if system_domains is not UNSET:
            field_dict["system_domains"] = system_domains
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_domain_user_system_schema import MultiDomainUserSystemSchema

        d = dict(src_dict)
        _app_id = d.pop("app_id", UNSET)
        app_id: UUID | Unset
        if isinstance(_app_id, Unset):
            app_id = UNSET
        else:
            app_id = UUID(_app_id)

        _auth_system_domains = d.pop("auth_system_domains", UNSET)
        auth_system_domains: list[MultiDomainUserSystemSchema] | Unset = UNSET
        if _auth_system_domains is not UNSET:
            auth_system_domains = []
            for auth_system_domains_item_data in _auth_system_domains:
                auth_system_domains_item = MultiDomainUserSystemSchema.from_dict(
                    auth_system_domains_item_data
                )

                auth_system_domains.append(auth_system_domains_item)

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

        _expires = d.pop("expires", UNSET)
        expires: datetime.datetime | Unset
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = datetime.datetime.fromisoformat(_expires)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_admin = d.pop("is_admin", UNSET)

        is_mfa_authenticated = d.pop("is_mfa_authenticated", UNSET)

        is_saml_authenticated = d.pop("is_saml_authenticated", UNSET)

        is_super_admin = d.pop("is_super_admin", UNSET)

        is_super_admin_light = d.pop("is_super_admin_light", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        system_domain_is_plg = d.pop("system_domain_is_plg", UNSET)

        _system_domain_status = d.pop("system_domain_status", UNSET)
        system_domain_status: TokenBaseSchemaSystemDomainStatus | Unset
        if isinstance(_system_domain_status, Unset):
            system_domain_status = UNSET
        else:
            system_domain_status = TokenBaseSchemaSystemDomainStatus(
                _system_domain_status
            )

        system_domain_type = d.pop("system_domain_type", UNSET)

        system_domain_warning_message = d.pop("system_domain_warning_message", UNSET)

        _system_domains = d.pop("system_domains", UNSET)
        system_domains: list[UUID] | Unset = UNSET
        if _system_domains is not UNSET:
            system_domains = []
            for system_domains_item_data in _system_domains:
                system_domains_item = UUID(system_domains_item_data)

                system_domains.append(system_domains_item)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        token_base_schema = cls(
            app_id=app_id,
            auth_system_domains=auth_system_domains,
            date_created=date_created,
            date_modified=date_modified,
            expires=expires,
            id=id,
            is_admin=is_admin,
            is_mfa_authenticated=is_mfa_authenticated,
            is_saml_authenticated=is_saml_authenticated,
            is_super_admin=is_super_admin,
            is_super_admin_light=is_super_admin_light,
            system_domain_id=system_domain_id,
            system_domain_is_plg=system_domain_is_plg,
            system_domain_status=system_domain_status,
            system_domain_type=system_domain_type,
            system_domain_warning_message=system_domain_warning_message,
            system_domains=system_domains,
            user_id=user_id,
        )

        token_base_schema.additional_properties = d
        return token_base_schema

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
