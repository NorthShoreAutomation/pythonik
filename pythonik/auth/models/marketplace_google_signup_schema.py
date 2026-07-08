from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplaceGoogleSignupSchema")


@_attrs_define
class MarketplaceGoogleSignupSchema:
    """
    Attributes:
        x_gcp_marketplace_token (None | str | Unset):
    """

    x_gcp_marketplace_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x_gcp_marketplace_token: None | str | Unset
        if isinstance(self.x_gcp_marketplace_token, Unset):
            x_gcp_marketplace_token = UNSET
        else:
            x_gcp_marketplace_token = self.x_gcp_marketplace_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x_gcp_marketplace_token is not UNSET:
            field_dict["x-gcp-marketplace-token"] = x_gcp_marketplace_token

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.x_gcp_marketplace_token, Unset):
            if isinstance(self.x_gcp_marketplace_token, str):
                files.append(
                    (
                        "x-gcp-marketplace-token",
                        (
                            None,
                            str(self.x_gcp_marketplace_token).encode(),
                            "text/plain",
                        ),
                    )
                )
            else:
                files.append(
                    (
                        "x-gcp-marketplace-token",
                        (
                            None,
                            str(self.x_gcp_marketplace_token).encode(),
                            "text/plain",
                        ),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_x_gcp_marketplace_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        x_gcp_marketplace_token = _parse_x_gcp_marketplace_token(
            d.pop("x-gcp-marketplace-token", UNSET)
        )

        marketplace_google_signup_schema = cls(
            x_gcp_marketplace_token=x_gcp_marketplace_token,
        )

        marketplace_google_signup_schema.additional_properties = d
        return marketplace_google_signup_schema

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
