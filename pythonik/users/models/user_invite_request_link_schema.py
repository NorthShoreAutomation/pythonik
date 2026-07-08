from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_invite_request_link_schema_type_type_1 import (
        UserInviteRequestLinkSchemaTypeType1,
    )


T = TypeVar("T", bound="UserInviteRequestLinkSchema")


@_attrs_define
class UserInviteRequestLinkSchema:
    """
    Attributes:
        primary_group (UUID):
        groups (list[UUID] | None | Unset):
        is_admin (bool | None | Unset):  Default: False.
        type_ (None | Unset | UserInviteRequestLinkSchemaTypeType1):
    """

    primary_group: UUID
    groups: list[UUID] | None | Unset = UNSET
    is_admin: bool | None | Unset = False
    type_: None | Unset | UserInviteRequestLinkSchemaTypeType1 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_invite_request_link_schema_type_type_1 import (
            UserInviteRequestLinkSchemaTypeType1,
        )

        primary_group = str(self.primary_group)

        groups: list[str] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = str(groups_type_0_item_data)
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        is_admin: bool | None | Unset
        if isinstance(self.is_admin, Unset):
            is_admin = UNSET
        else:
            is_admin = self.is_admin

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, UserInviteRequestLinkSchemaTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

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
        from ..models.user_invite_request_link_schema_type_type_1 import (
            UserInviteRequestLinkSchemaTypeType1,
        )

        d = dict(src_dict)
        primary_group = UUID(d.pop("primary_group"))

        def _parse_groups(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = UUID(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_is_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_admin = _parse_is_admin(d.pop("is_admin", UNSET))

        def _parse_type_(
            data: object,
        ) -> None | Unset | UserInviteRequestLinkSchemaTypeType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = UserInviteRequestLinkSchemaTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserInviteRequestLinkSchemaTypeType1, data)

        type_ = _parse_type_(d.pop("type", UNSET))

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
