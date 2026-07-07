from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_acl_base import GroupACLBase
    from ..models.propagating_acl import PropagatingACL
    from ..models.propagating_group_acl import PropagatingGroupACL
    from ..models.user_acl_base import UserACLBase


T = TypeVar("T", bound="ACLSchema")


@_attrs_define
class ACLSchema:
    """
    Attributes:
        groups_acl (list[GroupACLBase] | Unset):
        inherited_groups_acl (list[PropagatingGroupACL] | Unset):
        inherited_users_acl (list[PropagatingACL] | Unset):
        propagating_groups_acl (list[PropagatingGroupACL] | Unset):
        propagating_users_acl (list[PropagatingACL] | Unset):
        users_acl (list[UserACLBase] | Unset):
    """

    groups_acl: list[GroupACLBase] | Unset = UNSET
    inherited_groups_acl: list[PropagatingGroupACL] | Unset = UNSET
    inherited_users_acl: list[PropagatingACL] | Unset = UNSET
    propagating_groups_acl: list[PropagatingGroupACL] | Unset = UNSET
    propagating_users_acl: list[PropagatingACL] | Unset = UNSET
    users_acl: list[UserACLBase] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups_acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups_acl, Unset):
            groups_acl = []
            for groups_acl_item_data in self.groups_acl:
                groups_acl_item = groups_acl_item_data.to_dict()
                groups_acl.append(groups_acl_item)

        inherited_groups_acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inherited_groups_acl, Unset):
            inherited_groups_acl = []
            for inherited_groups_acl_item_data in self.inherited_groups_acl:
                inherited_groups_acl_item = inherited_groups_acl_item_data.to_dict()
                inherited_groups_acl.append(inherited_groups_acl_item)

        inherited_users_acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inherited_users_acl, Unset):
            inherited_users_acl = []
            for inherited_users_acl_item_data in self.inherited_users_acl:
                inherited_users_acl_item = inherited_users_acl_item_data.to_dict()
                inherited_users_acl.append(inherited_users_acl_item)

        propagating_groups_acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.propagating_groups_acl, Unset):
            propagating_groups_acl = []
            for propagating_groups_acl_item_data in self.propagating_groups_acl:
                propagating_groups_acl_item = propagating_groups_acl_item_data.to_dict()
                propagating_groups_acl.append(propagating_groups_acl_item)

        propagating_users_acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.propagating_users_acl, Unset):
            propagating_users_acl = []
            for propagating_users_acl_item_data in self.propagating_users_acl:
                propagating_users_acl_item = propagating_users_acl_item_data.to_dict()
                propagating_users_acl.append(propagating_users_acl_item)

        users_acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users_acl, Unset):
            users_acl = []
            for users_acl_item_data in self.users_acl:
                users_acl_item = users_acl_item_data.to_dict()
                users_acl.append(users_acl_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups_acl is not UNSET:
            field_dict["groups_acl"] = groups_acl
        if inherited_groups_acl is not UNSET:
            field_dict["inherited_groups_acl"] = inherited_groups_acl
        if inherited_users_acl is not UNSET:
            field_dict["inherited_users_acl"] = inherited_users_acl
        if propagating_groups_acl is not UNSET:
            field_dict["propagating_groups_acl"] = propagating_groups_acl
        if propagating_users_acl is not UNSET:
            field_dict["propagating_users_acl"] = propagating_users_acl
        if users_acl is not UNSET:
            field_dict["users_acl"] = users_acl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_acl_base import GroupACLBase
        from ..models.propagating_acl import PropagatingACL
        from ..models.propagating_group_acl import PropagatingGroupACL
        from ..models.user_acl_base import UserACLBase

        d = dict(src_dict)
        _groups_acl = d.pop("groups_acl", UNSET)
        groups_acl: list[GroupACLBase] | Unset = UNSET
        if _groups_acl is not UNSET:
            groups_acl = []
            for groups_acl_item_data in _groups_acl:
                groups_acl_item = GroupACLBase.from_dict(groups_acl_item_data)

                groups_acl.append(groups_acl_item)

        _inherited_groups_acl = d.pop("inherited_groups_acl", UNSET)
        inherited_groups_acl: list[PropagatingGroupACL] | Unset = UNSET
        if _inherited_groups_acl is not UNSET:
            inherited_groups_acl = []
            for inherited_groups_acl_item_data in _inherited_groups_acl:
                inherited_groups_acl_item = PropagatingGroupACL.from_dict(
                    inherited_groups_acl_item_data
                )

                inherited_groups_acl.append(inherited_groups_acl_item)

        _inherited_users_acl = d.pop("inherited_users_acl", UNSET)
        inherited_users_acl: list[PropagatingACL] | Unset = UNSET
        if _inherited_users_acl is not UNSET:
            inherited_users_acl = []
            for inherited_users_acl_item_data in _inherited_users_acl:
                inherited_users_acl_item = PropagatingACL.from_dict(
                    inherited_users_acl_item_data
                )

                inherited_users_acl.append(inherited_users_acl_item)

        _propagating_groups_acl = d.pop("propagating_groups_acl", UNSET)
        propagating_groups_acl: list[PropagatingGroupACL] | Unset = UNSET
        if _propagating_groups_acl is not UNSET:
            propagating_groups_acl = []
            for propagating_groups_acl_item_data in _propagating_groups_acl:
                propagating_groups_acl_item = PropagatingGroupACL.from_dict(
                    propagating_groups_acl_item_data
                )

                propagating_groups_acl.append(propagating_groups_acl_item)

        _propagating_users_acl = d.pop("propagating_users_acl", UNSET)
        propagating_users_acl: list[PropagatingACL] | Unset = UNSET
        if _propagating_users_acl is not UNSET:
            propagating_users_acl = []
            for propagating_users_acl_item_data in _propagating_users_acl:
                propagating_users_acl_item = PropagatingACL.from_dict(
                    propagating_users_acl_item_data
                )

                propagating_users_acl.append(propagating_users_acl_item)

        _users_acl = d.pop("users_acl", UNSET)
        users_acl: list[UserACLBase] | Unset = UNSET
        if _users_acl is not UNSET:
            users_acl = []
            for users_acl_item_data in _users_acl:
                users_acl_item = UserACLBase.from_dict(users_acl_item_data)

                users_acl.append(users_acl_item)

        acl_schema = cls(
            groups_acl=groups_acl,
            inherited_groups_acl=inherited_groups_acl,
            inherited_users_acl=inherited_users_acl,
            propagating_groups_acl=propagating_groups_acl,
            propagating_users_acl=propagating_users_acl,
            users_acl=users_acl,
        )

        acl_schema.additional_properties = d
        return acl_schema

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
