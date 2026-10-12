from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenExchangeRequestSchema")


@_attrs_define
class TokenExchangeRequestSchema:
    """
    Attributes:
        embed_token (str):
        requested_scopes (list[str] | None | Unset):
    """

    embed_token: str
    requested_scopes: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embed_token = self.embed_token

        requested_scopes: list[str] | None | Unset
        if isinstance(self.requested_scopes, Unset):
            requested_scopes = UNSET
        elif isinstance(self.requested_scopes, list):
            requested_scopes = self.requested_scopes

        else:
            requested_scopes = self.requested_scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embed_token": embed_token,
            }
        )
        if requested_scopes is not UNSET:
            field_dict["requested_scopes"] = requested_scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        embed_token = d.pop("embed_token")

        def _parse_requested_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requested_scopes_type_0 = cast(list[str], data)

                return requested_scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        requested_scopes = _parse_requested_scopes(d.pop("requested_scopes", UNSET))

        token_exchange_request_schema = cls(
            embed_token=embed_token,
            requested_scopes=requested_scopes,
        )

        token_exchange_request_schema.additional_properties = d
        return token_exchange_request_schema

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
