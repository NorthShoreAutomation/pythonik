from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbedTokenResponseSchema")


@_attrs_define
class EmbedTokenResponseSchema:
    """
    Attributes:
        app_id (None | str | Unset):
        embed_token (None | str | Unset):
        expires (None | str | Unset):
    """

    app_id: None | str | Unset = UNSET
    embed_token: None | str | Unset = UNSET
    expires: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        embed_token: None | str | Unset
        if isinstance(self.embed_token, Unset):
            embed_token = UNSET
        else:
            embed_token = self.embed_token

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        else:
            expires = self.expires

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if embed_token is not UNSET:
            field_dict["embed_token"] = embed_token
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_app_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

        def _parse_embed_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embed_token = _parse_embed_token(d.pop("embed_token", UNSET))

        def _parse_expires(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))

        embed_token_response_schema = cls(
            app_id=app_id,
            embed_token=embed_token,
            expires=expires,
        )

        embed_token_response_schema.additional_properties = d
        return embed_token_response_schema

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
