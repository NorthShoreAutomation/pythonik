from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSamlUpdateSchema")


@_attrs_define
class UserSamlUpdateSchema:
    """
    Attributes:
        email (str):
        first_name (str | Unset):
        group_names (list[str] | Unset):
        identity_provider_id (UUID | Unset):
        last_name (str | Unset):
    """

    email: str
    first_name: str | Unset = UNSET
    group_names: list[str] | Unset = UNSET
    identity_provider_id: UUID | Unset = UNSET
    last_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        group_names: list[str] | Unset = UNSET
        if not isinstance(self.group_names, Unset):
            group_names = self.group_names

        identity_provider_id: str | Unset = UNSET
        if not isinstance(self.identity_provider_id, Unset):
            identity_provider_id = str(self.identity_provider_id)

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if group_names is not UNSET:
            field_dict["group_names"] = group_names
        if identity_provider_id is not UNSET:
            field_dict["identity_provider_id"] = identity_provider_id
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        first_name = d.pop("first_name", UNSET)

        group_names = cast(list[str], d.pop("group_names", UNSET))

        _identity_provider_id = d.pop("identity_provider_id", UNSET)
        identity_provider_id: UUID | Unset
        if isinstance(_identity_provider_id, Unset):
            identity_provider_id = UNSET
        else:
            identity_provider_id = UUID(_identity_provider_id)

        last_name = d.pop("last_name", UNSET)

        user_saml_update_schema = cls(
            email=email,
            first_name=first_name,
            group_names=group_names,
            identity_provider_id=identity_provider_id,
            last_name=last_name,
        )

        user_saml_update_schema.additional_properties = d
        return user_saml_update_schema

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
