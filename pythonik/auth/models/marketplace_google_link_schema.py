from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarketplaceGoogleLinkSchema")


@_attrs_define
class MarketplaceGoogleLinkSchema:
    """
    Attributes:
        marketplace_signup_nonce (str):
    """

    marketplace_signup_nonce: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        marketplace_signup_nonce = self.marketplace_signup_nonce

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplace_signup_nonce": marketplace_signup_nonce,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        marketplace_signup_nonce = d.pop("marketplace_signup_nonce")

        marketplace_google_link_schema = cls(
            marketplace_signup_nonce=marketplace_signup_nonce,
        )

        marketplace_google_link_schema.additional_properties = d
        return marketplace_google_link_schema

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
