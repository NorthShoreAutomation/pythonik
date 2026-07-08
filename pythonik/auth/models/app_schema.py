from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_schema_oauth_client_type import AppSchemaOauthClientType
from ..models.app_schema_type import AppSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppSchema")


@_attrs_define
class AppSchema:
    """
    Attributes:
        name (str):
        allowed_scopes (list[str] | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        default_user_id (None | Unset | UUID):
        description (None | str | Unset):
        id (None | Unset | UUID):
        oauth_client_type (AppSchemaOauthClientType | None | Unset):
        redirect_uris (list[str] | None | Unset):
        system_domain_id (None | Unset | UUID):
        type_ (AppSchemaType | None | Unset):
        url (None | str | Unset):
    """

    name: str
    allowed_scopes: list[str] | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    default_user_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    oauth_client_type: AppSchemaOauthClientType | None | Unset = UNSET
    redirect_uris: list[str] | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    type_: AppSchemaType | None | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        allowed_scopes: list[str] | None | Unset
        if isinstance(self.allowed_scopes, Unset):
            allowed_scopes = UNSET
        elif isinstance(self.allowed_scopes, list):
            allowed_scopes = self.allowed_scopes

        else:
            allowed_scopes = self.allowed_scopes

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

        default_user_id: None | str | Unset
        if isinstance(self.default_user_id, Unset):
            default_user_id = UNSET
        elif isinstance(self.default_user_id, UUID):
            default_user_id = str(self.default_user_id)
        else:
            default_user_id = self.default_user_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        oauth_client_type: None | str | Unset
        if isinstance(self.oauth_client_type, Unset):
            oauth_client_type = UNSET
        elif isinstance(self.oauth_client_type, AppSchemaOauthClientType):
            oauth_client_type = self.oauth_client_type.value
        else:
            oauth_client_type = self.oauth_client_type

        redirect_uris: list[str] | None | Unset
        if isinstance(self.redirect_uris, Unset):
            redirect_uris = UNSET
        elif isinstance(self.redirect_uris, list):
            redirect_uris = self.redirect_uris

        else:
            redirect_uris = self.redirect_uris

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, AppSchemaType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if allowed_scopes is not UNSET:
            field_dict["allowed_scopes"] = allowed_scopes
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if default_user_id is not UNSET:
            field_dict["default_user_id"] = default_user_id
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if oauth_client_type is not UNSET:
            field_dict["oauth_client_type"] = oauth_client_type
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_allowed_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_scopes_type_0 = cast(list[str], data)

                return allowed_scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_scopes = _parse_allowed_scopes(d.pop("allowed_scopes", UNSET))

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

        def _parse_default_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_user_id_type_0 = UUID(data)

                return default_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_user_id = _parse_default_user_id(d.pop("default_user_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_oauth_client_type(
            data: object,
        ) -> AppSchemaOauthClientType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oauth_client_type_type_1 = AppSchemaOauthClientType(data)

                return oauth_client_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AppSchemaOauthClientType | None | Unset, data)

        oauth_client_type = _parse_oauth_client_type(d.pop("oauth_client_type", UNSET))

        def _parse_redirect_uris(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                redirect_uris_type_0 = cast(list[str], data)

                return redirect_uris_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        redirect_uris = _parse_redirect_uris(d.pop("redirect_uris", UNSET))

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

        def _parse_type_(data: object) -> AppSchemaType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = AppSchemaType(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AppSchemaType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        app_schema = cls(
            name=name,
            allowed_scopes=allowed_scopes,
            date_created=date_created,
            date_modified=date_modified,
            default_user_id=default_user_id,
            description=description,
            id=id,
            oauth_client_type=oauth_client_type,
            redirect_uris=redirect_uris,
            system_domain_id=system_domain_id,
            type_=type_,
            url=url,
        )

        app_schema.additional_properties = d
        return app_schema

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
