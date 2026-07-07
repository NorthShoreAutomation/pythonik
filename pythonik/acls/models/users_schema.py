from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.users_check_acl_schema import UsersCheckAclSchema


T = TypeVar("T", bound="UsersSchema")


@_attrs_define
class UsersSchema:
    """
    Attributes:
        users (list[UsersCheckAclSchema] | Unset):
    """

    users: list[UsersCheckAclSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.users_check_acl_schema import UsersCheckAclSchema

        d = dict(src_dict)
        _users = d.pop("users", UNSET)
        users: list[UsersCheckAclSchema] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UsersCheckAclSchema.from_dict(users_item_data)

                users.append(users_item)

        users_schema = cls(
            users=users,
        )

        users_schema.additional_properties = d
        return users_schema

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
