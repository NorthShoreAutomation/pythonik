from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_authenticate_user_schema_user import (
        InternalAuthenticateUserSchemaUser,
    )


T = TypeVar("T", bound="InternalAuthenticateUserSchema")


@_attrs_define
class InternalAuthenticateUserSchema:
    """
    Attributes:
        app_name (str):
        user (InternalAuthenticateUserSchemaUser):
        marketplace_signup_nonce (None | str | Unset):
    """

    app_name: str
    user: InternalAuthenticateUserSchemaUser
    marketplace_signup_nonce: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        user = self.user.to_dict()

        marketplace_signup_nonce: None | str | Unset
        if isinstance(self.marketplace_signup_nonce, Unset):
            marketplace_signup_nonce = UNSET
        else:
            marketplace_signup_nonce = self.marketplace_signup_nonce

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_name": app_name,
                "user": user,
            }
        )
        if marketplace_signup_nonce is not UNSET:
            field_dict["marketplace_signup_nonce"] = marketplace_signup_nonce

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_authenticate_user_schema_user import (
            InternalAuthenticateUserSchemaUser,
        )

        d = dict(src_dict)
        app_name = d.pop("app_name")

        user = InternalAuthenticateUserSchemaUser.from_dict(d.pop("user"))

        def _parse_marketplace_signup_nonce(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marketplace_signup_nonce = _parse_marketplace_signup_nonce(
            d.pop("marketplace_signup_nonce", UNSET)
        )

        internal_authenticate_user_schema = cls(
            app_name=app_name,
            user=user,
            marketplace_signup_nonce=marketplace_signup_nonce,
        )

        internal_authenticate_user_schema.additional_properties = d
        return internal_authenticate_user_schema

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
