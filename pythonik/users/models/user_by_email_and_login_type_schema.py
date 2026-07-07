from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_by_email_and_login_type_schema_login_type import (
    UserByEmailAndLoginTypeSchemaLoginType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserByEmailAndLoginTypeSchema")


@_attrs_define
class UserByEmailAndLoginTypeSchema:
    """
    Attributes:
        email (str):
        login_type (UserByEmailAndLoginTypeSchemaLoginType | Unset):
    """

    email: str
    login_type: UserByEmailAndLoginTypeSchemaLoginType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        login_type: str | Unset = UNSET
        if not isinstance(self.login_type, Unset):
            login_type = self.login_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if login_type is not UNSET:
            field_dict["login_type"] = login_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        _login_type = d.pop("login_type", UNSET)
        login_type: UserByEmailAndLoginTypeSchemaLoginType | Unset
        if isinstance(_login_type, Unset):
            login_type = UNSET
        else:
            login_type = UserByEmailAndLoginTypeSchemaLoginType(_login_type)

        user_by_email_and_login_type_schema = cls(
            email=email,
            login_type=login_type,
        )

        user_by_email_and_login_type_schema.additional_properties = d
        return user_by_email_and_login_type_schema

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
