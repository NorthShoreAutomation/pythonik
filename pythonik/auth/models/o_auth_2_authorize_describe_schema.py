from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_authorize_client_schema import OAuth2AuthorizeClientSchema


T = TypeVar("T", bound="OAuth2AuthorizeDescribeSchema")


@_attrs_define
class OAuth2AuthorizeDescribeSchema:
    """
    Attributes:
        client (OAuth2AuthorizeClientSchema):
        redirect_uri (str):
        scopes (list[str]):
        state (None | str | Unset):
    """

    client: OAuth2AuthorizeClientSchema
    redirect_uri: str
    scopes: list[str]
    state: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client = self.client.to_dict()

        redirect_uri = self.redirect_uri

        scopes = self.scopes

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client": client,
                "redirect_uri": redirect_uri,
                "scopes": scopes,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_authorize_client_schema import (
            OAuth2AuthorizeClientSchema,
        )

        d = dict(src_dict)
        client = OAuth2AuthorizeClientSchema.from_dict(d.pop("client"))

        redirect_uri = d.pop("redirect_uri")

        scopes = cast(list[str], d.pop("scopes"))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        o_auth_2_authorize_describe_schema = cls(
            client=client,
            redirect_uri=redirect_uri,
            scopes=scopes,
            state=state,
        )

        o_auth_2_authorize_describe_schema.additional_properties = d
        return o_auth_2_authorize_describe_schema

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
