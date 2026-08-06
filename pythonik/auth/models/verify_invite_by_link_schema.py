from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VerifyInviteByLinkSchema")


@_attrs_define
class VerifyInviteByLinkSchema:
    """
    Attributes:
        inviter_email (str):
        local_user_exists (bool):
        new_user_email (str):
        new_user_first_name (str):
        system_domain_id (UUID):
    """

    inviter_email: str
    local_user_exists: bool
    new_user_email: str
    new_user_first_name: str
    system_domain_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inviter_email = self.inviter_email

        local_user_exists = self.local_user_exists

        new_user_email = self.new_user_email

        new_user_first_name = self.new_user_first_name

        system_domain_id = str(self.system_domain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inviter_email": inviter_email,
                "local_user_exists": local_user_exists,
                "new_user_email": new_user_email,
                "new_user_first_name": new_user_first_name,
                "system_domain_id": system_domain_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inviter_email = d.pop("inviter_email")

        local_user_exists = d.pop("local_user_exists")

        new_user_email = d.pop("new_user_email")

        new_user_first_name = d.pop("new_user_first_name")

        system_domain_id = UUID(d.pop("system_domain_id"))

        verify_invite_by_link_schema = cls(
            inviter_email=inviter_email,
            local_user_exists=local_user_exists,
            new_user_email=new_user_email,
            new_user_first_name=new_user_first_name,
            system_domain_id=system_domain_id,
        )

        verify_invite_by_link_schema.additional_properties = d
        return verify_invite_by_link_schema

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
