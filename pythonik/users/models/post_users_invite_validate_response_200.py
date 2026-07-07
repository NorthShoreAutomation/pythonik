from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersInviteValidateResponse200")


@_attrs_define
class PostUsersInviteValidateResponse200:
    """
    Attributes:
        system_domain_name (str | Unset): The system domain name
    """

    system_domain_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_domain_name = self.system_domain_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if system_domain_name is not UNSET:
            field_dict["system_domain_name"] = system_domain_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system_domain_name = d.pop("system_domain_name", UNSET)

        post_users_invite_validate_response_200 = cls(
            system_domain_name=system_domain_name,
        )

        post_users_invite_validate_response_200.additional_properties = d
        return post_users_invite_validate_response_200

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
