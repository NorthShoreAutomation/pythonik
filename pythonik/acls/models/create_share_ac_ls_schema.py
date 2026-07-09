from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateShareACLsSchema")


@_attrs_define
class CreateShareACLsSchema:
    """
    Attributes:
        permissions (list[str]):
        object_keys (list[str] | None | Unset): The number of object_keys in the list is limited to a min of 0 and a
            maximum of 500
        object_type (None | str | Unset):
        share_id (None | Unset | UUID):
    """

    permissions: list[str]
    object_keys: list[str] | None | Unset = UNSET
    object_type: None | str | Unset = UNSET
    share_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions = self.permissions

        object_keys: list[str] | None | Unset
        if isinstance(self.object_keys, Unset):
            object_keys = UNSET
        elif isinstance(self.object_keys, list):
            object_keys = self.object_keys

        else:
            object_keys = self.object_keys

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        share_id: None | str | Unset
        if isinstance(self.share_id, Unset):
            share_id = UNSET
        elif isinstance(self.share_id, UUID):
            share_id = str(self.share_id)
        else:
            share_id = self.share_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
            }
        )
        if object_keys is not UNSET:
            field_dict["object_keys"] = object_keys
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if share_id is not UNSET:
            field_dict["share_id"] = share_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = cast(list[str], d.pop("permissions"))

        def _parse_object_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                object_keys_type_0 = cast(list[str], data)

                return object_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        object_keys = _parse_object_keys(d.pop("object_keys", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_share_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_id_type_0 = UUID(data)

                return share_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        share_id = _parse_share_id(d.pop("share_id", UNSET))

        create_share_ac_ls_schema = cls(
            permissions=permissions,
            object_keys=object_keys,
            object_type=object_type,
            share_id=share_id,
        )

        create_share_ac_ls_schema.additional_properties = d
        return create_share_ac_ls_schema

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
