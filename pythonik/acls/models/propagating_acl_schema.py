from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropagatingACLSchema")


@_attrs_define
class PropagatingACLSchema:
    """
    Attributes:
        permissions (list[str]):
        object_key (None | str | Unset):
        object_type (None | str | Unset):
        user_id (None | Unset | UUID):
    """

    permissions: list[str]
    object_key: None | str | Unset = UNSET
    object_type: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions = self.permissions

        object_key: None | str | Unset
        if isinstance(self.object_key, Unset):
            object_key = UNSET
        else:
            object_key = self.object_key

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
            }
        )
        if object_key is not UNSET:
            field_dict["object_key"] = object_key
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = cast(list[str], d.pop("permissions"))

        def _parse_object_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_key = _parse_object_key(d.pop("object_key", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        propagating_acl_schema = cls(
            permissions=permissions,
            object_key=object_key,
            object_type=object_type,
            user_id=user_id,
        )

        propagating_acl_schema.additional_properties = d
        return propagating_acl_schema

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
