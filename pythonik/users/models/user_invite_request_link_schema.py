from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_invite_request_link_schema_type import (
    UserInviteRequestLinkSchemaType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserInviteRequestLinkSchema")


@_attrs_define
class UserInviteRequestLinkSchema:
    """
    Attributes:
        primary_group (UUID):
        groups (list[UUID] | Unset):
        is_admin (bool | Unset):  Default: False.
        type_ (UserInviteRequestLinkSchemaType | Unset):  Default: UserInviteRequestLinkSchemaType.STANDARD.
    """

    primary_group: UUID
    groups: list[UUID] | Unset = UNSET
    is_admin: bool | Unset = False
    type_: UserInviteRequestLinkSchemaType | Unset = (
        UserInviteRequestLinkSchemaType.STANDARD
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary_group = str(self.primary_group)

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = str(groups_item_data)
                groups.append(groups_item)

        is_admin = self.is_admin

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "primary_group": primary_group,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        primary_group = UUID(d.pop("primary_group"))

        _groups = d.pop("groups", UNSET)
        groups: list[UUID] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = UUID(groups_item_data)

                groups.append(groups_item)

        is_admin = d.pop("is_admin", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UserInviteRequestLinkSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UserInviteRequestLinkSchemaType(_type_)

        user_invite_request_link_schema = cls(
            primary_group=primary_group,
            groups=groups,
            is_admin=is_admin,
            type_=type_,
        )

        user_invite_request_link_schema.additional_properties = d
        return user_invite_request_link_schema

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
