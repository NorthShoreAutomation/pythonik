from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invitation_response_schema_domain_status import (
    InvitationResponseSchemaDomainStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_login_schema import AutoLoginSchema


T = TypeVar("T", bound="InvitationResponseSchema")


@_attrs_define
class InvitationResponseSchema:
    """
    Attributes:
        auto_login (bool | Unset):
        domain_status (InvitationResponseSchemaDomainStatus | Unset):
        login_data (AutoLoginSchema | Unset):
        user_id (UUID | Unset):
    """

    auto_login: bool | Unset = UNSET
    domain_status: InvitationResponseSchemaDomainStatus | Unset = UNSET
    login_data: AutoLoginSchema | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_login = self.auto_login

        domain_status: str | Unset = UNSET
        if not isinstance(self.domain_status, Unset):
            domain_status = self.domain_status.value

        login_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.login_data, Unset):
            login_data = self.login_data.to_dict()

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_login is not UNSET:
            field_dict["auto_login"] = auto_login
        if domain_status is not UNSET:
            field_dict["domain_status"] = domain_status
        if login_data is not UNSET:
            field_dict["login_data"] = login_data
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_login_schema import AutoLoginSchema

        d = dict(src_dict)
        auto_login = d.pop("auto_login", UNSET)

        _domain_status = d.pop("domain_status", UNSET)
        domain_status: InvitationResponseSchemaDomainStatus | Unset
        if isinstance(_domain_status, Unset):
            domain_status = UNSET
        else:
            domain_status = InvitationResponseSchemaDomainStatus(_domain_status)

        _login_data = d.pop("login_data", UNSET)
        login_data: AutoLoginSchema | Unset
        if isinstance(_login_data, Unset):
            login_data = UNSET
        else:
            login_data = AutoLoginSchema.from_dict(_login_data)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        invitation_response_schema = cls(
            auto_login=auto_login,
            domain_status=domain_status,
            login_data=login_data,
            user_id=user_id,
        )

        invitation_response_schema.additional_properties = d
        return invitation_response_schema

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
