from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_multiplatform_login_schema_system_domain_status import (
    TokenMultiplatformLoginSchemaSystemDomainStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_platform_domain_user_system_schema import (
        MultiPlatformDomainUserSystemSchema,
    )


T = TypeVar("T", bound="TokenMultiplatformLoginSchema")


@_attrs_define
class TokenMultiplatformLoginSchema:
    """
    Attributes:
        app_id (None | Unset | UUID):
        auth_system_domains (list[MultiPlatformDomainUserSystemSchema] | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        expires (datetime.datetime | None | Unset):
        id (None | Unset | UUID):
        is_admin (bool | None | Unset):
        is_mfa_authenticated (bool | None | Unset):
        is_saml_authenticated (bool | None | Unset):
        is_super_admin (bool | None | Unset):
        is_super_admin_light (bool | None | Unset):
        system_domain_id (None | Unset | UUID):
        system_domain_is_plg (bool | None | Unset):
        system_domain_status (None | TokenMultiplatformLoginSchemaSystemDomainStatus | Unset):
        system_domain_type (None | str | Unset):
        system_domain_warning_message (None | str | Unset):
        system_domains (list[UUID] | None | Unset):
        token (None | str | Unset): Deprecated field. Use the token field from the `auth_system_domains` items instead.
        user_id (None | Unset | UUID):
    """

    app_id: None | Unset | UUID = UNSET
    auth_system_domains: list[MultiPlatformDomainUserSystemSchema] | None | Unset = (
        UNSET
    )
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    expires: datetime.datetime | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_admin: bool | None | Unset = UNSET
    is_mfa_authenticated: bool | None | Unset = UNSET
    is_saml_authenticated: bool | None | Unset = UNSET
    is_super_admin: bool | None | Unset = UNSET
    is_super_admin_light: bool | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    system_domain_is_plg: bool | None | Unset = UNSET
    system_domain_status: (
        None | TokenMultiplatformLoginSchemaSystemDomainStatus | Unset
    ) = UNSET
    system_domain_type: None | str | Unset = UNSET
    system_domain_warning_message: None | str | Unset = UNSET
    system_domains: list[UUID] | None | Unset = UNSET
    token: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        elif isinstance(self.app_id, UUID):
            app_id = str(self.app_id)
        else:
            app_id = self.app_id

        auth_system_domains: list[dict[str, Any]] | None | Unset
        if isinstance(self.auth_system_domains, Unset):
            auth_system_domains = UNSET
        elif isinstance(self.auth_system_domains, list):
            auth_system_domains = []
            for auth_system_domains_type_0_item_data in self.auth_system_domains:
                auth_system_domains_type_0_item = (
                    auth_system_domains_type_0_item_data.to_dict()
                )
                auth_system_domains.append(auth_system_domains_type_0_item)

        else:
            auth_system_domains = self.auth_system_domains

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

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_admin: bool | None | Unset
        if isinstance(self.is_admin, Unset):
            is_admin = UNSET
        else:
            is_admin = self.is_admin

        is_mfa_authenticated: bool | None | Unset
        if isinstance(self.is_mfa_authenticated, Unset):
            is_mfa_authenticated = UNSET
        else:
            is_mfa_authenticated = self.is_mfa_authenticated

        is_saml_authenticated: bool | None | Unset
        if isinstance(self.is_saml_authenticated, Unset):
            is_saml_authenticated = UNSET
        else:
            is_saml_authenticated = self.is_saml_authenticated

        is_super_admin: bool | None | Unset
        if isinstance(self.is_super_admin, Unset):
            is_super_admin = UNSET
        else:
            is_super_admin = self.is_super_admin

        is_super_admin_light: bool | None | Unset
        if isinstance(self.is_super_admin_light, Unset):
            is_super_admin_light = UNSET
        else:
            is_super_admin_light = self.is_super_admin_light

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        system_domain_is_plg: bool | None | Unset
        if isinstance(self.system_domain_is_plg, Unset):
            system_domain_is_plg = UNSET
        else:
            system_domain_is_plg = self.system_domain_is_plg

        system_domain_status: None | str | Unset
        if isinstance(self.system_domain_status, Unset):
            system_domain_status = UNSET
        elif isinstance(
            self.system_domain_status, TokenMultiplatformLoginSchemaSystemDomainStatus
        ):
            system_domain_status = self.system_domain_status.value
        else:
            system_domain_status = self.system_domain_status

        system_domain_type: None | str | Unset
        if isinstance(self.system_domain_type, Unset):
            system_domain_type = UNSET
        else:
            system_domain_type = self.system_domain_type

        system_domain_warning_message: None | str | Unset
        if isinstance(self.system_domain_warning_message, Unset):
            system_domain_warning_message = UNSET
        else:
            system_domain_warning_message = self.system_domain_warning_message

        system_domains: list[str] | None | Unset
        if isinstance(self.system_domains, Unset):
            system_domains = UNSET
        elif isinstance(self.system_domains, list):
            system_domains = []
            for system_domains_type_0_item_data in self.system_domains:
                system_domains_type_0_item = str(system_domains_type_0_item_data)
                system_domains.append(system_domains_type_0_item)

        else:
            system_domains = self.system_domains

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

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
        if token is not UNSET:
            field_dict["token"] = token
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_platform_domain_user_system_schema import (
            MultiPlatformDomainUserSystemSchema,
        )

        d = dict(src_dict)

        def _parse_app_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                app_id_type_0 = UUID(data)

                return app_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

        def _parse_auth_system_domains(
            data: object,
        ) -> list[MultiPlatformDomainUserSystemSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                auth_system_domains_type_0 = []
                _auth_system_domains_type_0 = data
                for auth_system_domains_type_0_item_data in _auth_system_domains_type_0:
                    auth_system_domains_type_0_item = (
                        MultiPlatformDomainUserSystemSchema.from_dict(
                            auth_system_domains_type_0_item_data
                        )
                    )

                    auth_system_domains_type_0.append(auth_system_domains_type_0_item)

                return auth_system_domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MultiPlatformDomainUserSystemSchema] | None | Unset, data)

        auth_system_domains = _parse_auth_system_domains(
            d.pop("auth_system_domains", UNSET)
        )

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

        def _parse_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = datetime.datetime.fromisoformat(data)

                return expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))

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

        def _parse_is_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_admin = _parse_is_admin(d.pop("is_admin", UNSET))

        def _parse_is_mfa_authenticated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_mfa_authenticated = _parse_is_mfa_authenticated(
            d.pop("is_mfa_authenticated", UNSET)
        )

        def _parse_is_saml_authenticated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_saml_authenticated = _parse_is_saml_authenticated(
            d.pop("is_saml_authenticated", UNSET)
        )

        def _parse_is_super_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_super_admin = _parse_is_super_admin(d.pop("is_super_admin", UNSET))

        def _parse_is_super_admin_light(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_super_admin_light = _parse_is_super_admin_light(
            d.pop("is_super_admin_light", UNSET)
        )

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

        def _parse_system_domain_is_plg(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_domain_is_plg = _parse_system_domain_is_plg(
            d.pop("system_domain_is_plg", UNSET)
        )

        def _parse_system_domain_status(
            data: object,
        ) -> None | TokenMultiplatformLoginSchemaSystemDomainStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_status_type_1 = (
                    TokenMultiplatformLoginSchemaSystemDomainStatus(data)
                )

                return system_domain_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TokenMultiplatformLoginSchemaSystemDomainStatus | Unset, data
            )

        system_domain_status = _parse_system_domain_status(
            d.pop("system_domain_status", UNSET)
        )

        def _parse_system_domain_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_domain_type = _parse_system_domain_type(
            d.pop("system_domain_type", UNSET)
        )

        def _parse_system_domain_warning_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_domain_warning_message = _parse_system_domain_warning_message(
            d.pop("system_domain_warning_message", UNSET)
        )

        def _parse_system_domains(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                system_domains_type_0 = []
                _system_domains_type_0 = data
                for system_domains_type_0_item_data in _system_domains_type_0:
                    system_domains_type_0_item = UUID(system_domains_type_0_item_data)

                    system_domains_type_0.append(system_domains_type_0_item)

                return system_domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        system_domains = _parse_system_domains(d.pop("system_domains", UNSET))

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        token_multiplatform_login_schema = cls(
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
            token=token,
            user_id=user_id,
        )

        token_multiplatform_login_schema.additional_properties = d
        return token_multiplatform_login_schema

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
