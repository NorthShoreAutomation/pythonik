from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_oauth_token_body_grant_type import PostOauthTokenBodyGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOauthTokenBody")


@_attrs_define
class PostOauthTokenBody:
    """
    Attributes:
        grant_type (PostOauthTokenBodyGrantType): The OAuth2 grant type
        client_id (None | str | Unset): The OAuth2 client ID (application ID). Required unless the client authenticates
            with HTTP Basic.
        client_secret (None | str | Unset): The OAuth2 client secret (required for the client_credentials grant unless
            sent as HTTP Basic credentials)
        code (None | str | Unset): The authorization code (required for authorization_code grant)
        code_verifier (None | str | Unset): The PKCE code verifier (required for authorization_code grant)
        redirect_uri (None | str | Unset): The redirect URI used in the authorization request (required for
            authorization_code grant)
        refresh_token (None | str | Unset): The refresh token (required for refresh_token grant)
        scope (None | str | Unset): The requested scope. Used by the client_credentials grant, and by the refresh_token
            grant to request a subset of the scope already granted (a broader scope is rejected).
    """

    grant_type: PostOauthTokenBodyGrantType
    client_id: None | str | Unset = UNSET
    client_secret: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    code_verifier: None | str | Unset = UNSET
    redirect_uri: None | str | Unset = UNSET
    refresh_token: None | str | Unset = UNSET
    scope: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        client_id: None | str | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        code_verifier: None | str | Unset
        if isinstance(self.code_verifier, Unset):
            code_verifier = UNSET
        else:
            code_verifier = self.code_verifier

        redirect_uri: None | str | Unset
        if isinstance(self.redirect_uri, Unset):
            redirect_uri = UNSET
        else:
            redirect_uri = self.redirect_uri

        refresh_token: None | str | Unset
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if code is not UNSET:
            field_dict["code"] = code
        if code_verifier is not UNSET:
            field_dict["code_verifier"] = code_verifier
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = PostOauthTokenBodyGrantType(d.pop("grant_type"))

        def _parse_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_code_verifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_verifier = _parse_code_verifier(d.pop("code_verifier", UNSET))

        def _parse_redirect_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_uri = _parse_redirect_uri(d.pop("redirect_uri", UNSET))

        def _parse_refresh_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        post_oauth_token_body = cls(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            code_verifier=code_verifier,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            scope=scope,
        )

        post_oauth_token_body.additional_properties = d
        return post_oauth_token_body

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
