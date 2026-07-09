from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        groups_acl (list[GroupACLBase] | None | Unset):
        inherited_groups_acl (list[PropagatingGroupACL] | None | Unset):
        inherited_users_acl (list[PropagatingACL] | None | Unset):
        propagating_groups_acl (list[PropagatingGroupACL] | None | Unset):
        propagating_users_acl (list[PropagatingACL] | None | Unset):
        users_acl (list[UserACLBase] | None | Unset):
    """

    groups_acl: list[GroupACLBase] | None | Unset = UNSET
    inherited_groups_acl: list[PropagatingGroupACL] | None | Unset = UNSET
    inherited_users_acl: list[PropagatingACL] | None | Unset = UNSET
    propagating_groups_acl: list[PropagatingGroupACL] | None | Unset = UNSET
    propagating_users_acl: list[PropagatingACL] | None | Unset = UNSET
    users_acl: list[UserACLBase] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups_acl: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups_acl, Unset):
            groups_acl = UNSET
        elif isinstance(self.groups_acl, list):
            groups_acl = []
            for groups_acl_type_0_item_data in self.groups_acl:
                groups_acl_type_0_item = groups_acl_type_0_item_data.to_dict()
                groups_acl.append(groups_acl_type_0_item)

        else:
            groups_acl = self.groups_acl

        inherited_groups_acl: list[dict[str, Any]] | None | Unset
        if isinstance(self.inherited_groups_acl, Unset):
            inherited_groups_acl = UNSET
        elif isinstance(self.inherited_groups_acl, list):
            inherited_groups_acl = []
            for inherited_groups_acl_type_0_item_data in self.inherited_groups_acl:
                inherited_groups_acl_type_0_item = (
                    inherited_groups_acl_type_0_item_data.to_dict()
                )
                inherited_groups_acl.append(inherited_groups_acl_type_0_item)

        else:
            inherited_groups_acl = self.inherited_groups_acl

        inherited_users_acl: list[dict[str, Any]] | None | Unset
        if isinstance(self.inherited_users_acl, Unset):
            inherited_users_acl = UNSET
        elif isinstance(self.inherited_users_acl, list):
            inherited_users_acl = []
            for inherited_users_acl_type_0_item_data in self.inherited_users_acl:
                inherited_users_acl_type_0_item = (
                    inherited_users_acl_type_0_item_data.to_dict()
                )
                inherited_users_acl.append(inherited_users_acl_type_0_item)

        else:
            inherited_users_acl = self.inherited_users_acl

        propagating_groups_acl: list[dict[str, Any]] | None | Unset
        if isinstance(self.propagating_groups_acl, Unset):
            propagating_groups_acl = UNSET
        elif isinstance(self.propagating_groups_acl, list):
            propagating_groups_acl = []
            for propagating_groups_acl_type_0_item_data in self.propagating_groups_acl:
                propagating_groups_acl_type_0_item = (
                    propagating_groups_acl_type_0_item_data.to_dict()
                )
                propagating_groups_acl.append(propagating_groups_acl_type_0_item)

        else:
            propagating_groups_acl = self.propagating_groups_acl

        propagating_users_acl: list[dict[str, Any]] | None | Unset
        if isinstance(self.propagating_users_acl, Unset):
            propagating_users_acl = UNSET
        elif isinstance(self.propagating_users_acl, list):
            propagating_users_acl = []
            for propagating_users_acl_type_0_item_data in self.propagating_users_acl:
                propagating_users_acl_type_0_item = (
                    propagating_users_acl_type_0_item_data.to_dict()
                )
                propagating_users_acl.append(propagating_users_acl_type_0_item)

        else:
            propagating_users_acl = self.propagating_users_acl

        users_acl: list[dict[str, Any]] | None | Unset
        if isinstance(self.users_acl, Unset):
            users_acl = UNSET
        elif isinstance(self.users_acl, list):
            users_acl = []
            for users_acl_type_0_item_data in self.users_acl:
                users_acl_type_0_item = users_acl_type_0_item_data.to_dict()
                users_acl.append(users_acl_type_0_item)

        else:
            users_acl = self.users_acl

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

        def _parse_groups_acl(data: object) -> list[GroupACLBase] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_acl_type_0 = []
                _groups_acl_type_0 = data
                for groups_acl_type_0_item_data in _groups_acl_type_0:
                    groups_acl_type_0_item = GroupACLBase.from_dict(
                        groups_acl_type_0_item_data
                    )

                    groups_acl_type_0.append(groups_acl_type_0_item)

                return groups_acl_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GroupACLBase] | None | Unset, data)

        groups_acl = _parse_groups_acl(d.pop("groups_acl", UNSET))

        def _parse_inherited_groups_acl(
            data: object,
        ) -> list[PropagatingGroupACL] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inherited_groups_acl_type_0 = []
                _inherited_groups_acl_type_0 = data
                for (
                    inherited_groups_acl_type_0_item_data
                ) in _inherited_groups_acl_type_0:
                    inherited_groups_acl_type_0_item = PropagatingGroupACL.from_dict(
                        inherited_groups_acl_type_0_item_data
                    )

                    inherited_groups_acl_type_0.append(inherited_groups_acl_type_0_item)

                return inherited_groups_acl_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PropagatingGroupACL] | None | Unset, data)

        inherited_groups_acl = _parse_inherited_groups_acl(
            d.pop("inherited_groups_acl", UNSET)
        )

        def _parse_inherited_users_acl(
            data: object,
        ) -> list[PropagatingACL] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inherited_users_acl_type_0 = []
                _inherited_users_acl_type_0 = data
                for inherited_users_acl_type_0_item_data in _inherited_users_acl_type_0:
                    inherited_users_acl_type_0_item = PropagatingACL.from_dict(
                        inherited_users_acl_type_0_item_data
                    )

                    inherited_users_acl_type_0.append(inherited_users_acl_type_0_item)

                return inherited_users_acl_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PropagatingACL] | None | Unset, data)

        inherited_users_acl = _parse_inherited_users_acl(
            d.pop("inherited_users_acl", UNSET)
        )

        def _parse_propagating_groups_acl(
            data: object,
        ) -> list[PropagatingGroupACL] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                propagating_groups_acl_type_0 = []
                _propagating_groups_acl_type_0 = data
                for (
                    propagating_groups_acl_type_0_item_data
                ) in _propagating_groups_acl_type_0:
                    propagating_groups_acl_type_0_item = PropagatingGroupACL.from_dict(
                        propagating_groups_acl_type_0_item_data
                    )

                    propagating_groups_acl_type_0.append(
                        propagating_groups_acl_type_0_item
                    )

                return propagating_groups_acl_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PropagatingGroupACL] | None | Unset, data)

        propagating_groups_acl = _parse_propagating_groups_acl(
            d.pop("propagating_groups_acl", UNSET)
        )

        def _parse_propagating_users_acl(
            data: object,
        ) -> list[PropagatingACL] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                propagating_users_acl_type_0 = []
                _propagating_users_acl_type_0 = data
                for (
                    propagating_users_acl_type_0_item_data
                ) in _propagating_users_acl_type_0:
                    propagating_users_acl_type_0_item = PropagatingACL.from_dict(
                        propagating_users_acl_type_0_item_data
                    )

                    propagating_users_acl_type_0.append(
                        propagating_users_acl_type_0_item
                    )

                return propagating_users_acl_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PropagatingACL] | None | Unset, data)

        propagating_users_acl = _parse_propagating_users_acl(
            d.pop("propagating_users_acl", UNSET)
        )

        def _parse_users_acl(data: object) -> list[UserACLBase] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_acl_type_0 = []
                _users_acl_type_0 = data
                for users_acl_type_0_item_data in _users_acl_type_0:
                    users_acl_type_0_item = UserACLBase.from_dict(
                        users_acl_type_0_item_data
                    )

                    users_acl_type_0.append(users_acl_type_0_item)

                return users_acl_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UserACLBase] | None | Unset, data)

        users_acl = _parse_users_acl(d.pop("users_acl", UNSET))

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
