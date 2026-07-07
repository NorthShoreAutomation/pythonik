from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_oauth_token_body_grant_type import PostOauthTokenBodyGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOauthTokenBody")


@_attrs_define
class PostOauthTokenBody:
    """
    Attributes:
        client_id (str): The OAuth2 client ID (application ID)
        grant_type (PostOauthTokenBodyGrantType): The OAuth2 grant type
        client_secret (str | Unset): The OAuth2 client secret (required for client_credentials grant)
        code (str | Unset): The authorization code (required for authorization_code grant)
        code_verifier (str | Unset): The PKCE code verifier (required for authorization_code grant)
        redirect_uri (str | Unset): The redirect URI used in the authorization request (required for authorization_code
            grant)
        scope (str | Unset): The requested scope (used for client_credentials grant)
    """

    client_id: str
    grant_type: PostOauthTokenBodyGrantType
    client_secret: str | Unset = UNSET
    code: str | Unset = UNSET
    code_verifier: str | Unset = UNSET
    redirect_uri: str | Unset = UNSET
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        grant_type = self.grant_type.value

        client_secret = self.client_secret

        code = self.code

        code_verifier = self.code_verifier

        redirect_uri = self.redirect_uri

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "grant_type": grant_type,
            }
        )
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if code is not UNSET:
            field_dict["code"] = code
        if code_verifier is not UNSET:
            field_dict["code_verifier"] = code_verifier
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        grant_type = PostOauthTokenBodyGrantType(d.pop("grant_type"))

        client_secret = d.pop("client_secret", UNSET)

        code = d.pop("code", UNSET)

        code_verifier = d.pop("code_verifier", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        scope = d.pop("scope", UNSET)

        post_oauth_token_body = cls(
            client_id=client_id,
            grant_type=grant_type,
            client_secret=client_secret,
            code=code,
            code_verifier=code_verifier,
            redirect_uri=redirect_uri,
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
