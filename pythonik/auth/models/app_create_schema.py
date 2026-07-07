from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_create_schema_oauth_client_type import AppCreateSchemaOauthClientType
from ..models.app_create_schema_type import AppCreateSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppCreateSchema")


@_attrs_define
class AppCreateSchema:
    """
    Attributes:
        name (str):
        allowed_scopes (list[str] | Unset):
        client_secret (str | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        default_user_id (None | Unset | UUID):
        description (None | str | Unset):
        id (UUID | Unset):
        oauth_client_type (AppCreateSchemaOauthClientType | Unset):
        redirect_uris (list[str] | Unset):
        system_domain_id (UUID | Unset):
        type_ (AppCreateSchemaType | Unset):
        url (None | str | Unset):
    """

    name: str
    allowed_scopes: list[str] | Unset = UNSET
    client_secret: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    default_user_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    oauth_client_type: AppCreateSchemaOauthClientType | Unset = UNSET
    redirect_uris: list[str] | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    type_: AppCreateSchemaType | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        allowed_scopes: list[str] | Unset = UNSET
        if not isinstance(self.allowed_scopes, Unset):
            allowed_scopes = self.allowed_scopes

        client_secret = self.client_secret

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

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

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        oauth_client_type: str | Unset = UNSET
        if not isinstance(self.oauth_client_type, Unset):
            oauth_client_type = self.oauth_client_type.value

        redirect_uris: list[str] | Unset = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
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

        allowed_scopes = cast(list[str], d.pop("allowed_scopes", UNSET))

        client_secret = d.pop("client_secret", UNSET)

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

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _oauth_client_type = d.pop("oauth_client_type", UNSET)
        oauth_client_type: AppCreateSchemaOauthClientType | Unset
        if isinstance(_oauth_client_type, Unset):
            oauth_client_type = UNSET
        else:
            oauth_client_type = AppCreateSchemaOauthClientType(_oauth_client_type)

        redirect_uris = cast(list[str], d.pop("redirect_uris", UNSET))

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _type_ = d.pop("type", UNSET)
        type_: AppCreateSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppCreateSchemaType(_type_)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        app_create_schema = cls(
            name=name,
            allowed_scopes=allowed_scopes,
            client_secret=client_secret,
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

        app_create_schema.additional_properties = d
        return app_create_schema

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
