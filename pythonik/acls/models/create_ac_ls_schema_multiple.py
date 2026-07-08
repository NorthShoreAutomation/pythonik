from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_ac_ls_schema_multiple_mode_type_1 import (
        CreateACLsSchemaMultipleModeType1,
    )


T = TypeVar("T", bound="CreateACLsSchemaMultiple")


@_attrs_define
class CreateACLsSchemaMultiple:
    """
    Attributes:
        object_keys (list[str]): The number of object_keys in the list is limited to a minimum of 1 and a maximum of 1
        permissions (list[str]):
        group_ids (list[UUID] | None | Unset):
        mode (CreateACLsSchemaMultipleModeType1 | None | Unset):
        object_type (None | str | Unset):
        user_ids (list[UUID] | None | Unset):
    """

    object_keys: list[str]
    permissions: list[str]
    group_ids: list[UUID] | None | Unset = UNSET
    mode: CreateACLsSchemaMultipleModeType1 | None | Unset = UNSET
    object_type: None | str | Unset = UNSET
    user_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_ac_ls_schema_multiple_mode_type_1 import (
            CreateACLsSchemaMultipleModeType1,
        )

        object_keys = self.object_keys

        permissions = self.permissions

        group_ids: list[str] | None | Unset
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = []
            for group_ids_type_0_item_data in self.group_ids:
                group_ids_type_0_item = str(group_ids_type_0_item_data)
                group_ids.append(group_ids_type_0_item)

        else:
            group_ids = self.group_ids

        mode: dict[str, Any] | None | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, CreateACLsSchemaMultipleModeType1):
            mode = self.mode.to_dict()
        else:
            mode = self.mode

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        user_ids: list[str] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = []
            for user_ids_type_0_item_data in self.user_ids:
                user_ids_type_0_item = str(user_ids_type_0_item_data)
                user_ids.append(user_ids_type_0_item)

        else:
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_keys": object_keys,
                "permissions": permissions,
            }
        )
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if mode is not UNSET:
            field_dict["mode"] = mode
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_ac_ls_schema_multiple_mode_type_1 import (
            CreateACLsSchemaMultipleModeType1,
        )

        d = dict(src_dict)
        object_keys = cast(list[str], d.pop("object_keys"))

        permissions = cast(list[str], d.pop("permissions"))

        def _parse_group_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = []
                _group_ids_type_0 = data
                for group_ids_type_0_item_data in _group_ids_type_0:
                    group_ids_type_0_item = UUID(group_ids_type_0_item_data)

                    group_ids_type_0.append(group_ids_type_0_item)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_mode(
            data: object,
        ) -> CreateACLsSchemaMultipleModeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mode_type_1 = CreateACLsSchemaMultipleModeType1.from_dict(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateACLsSchemaMultipleModeType1 | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = []
                _user_ids_type_0 = data
                for user_ids_type_0_item_data in _user_ids_type_0:
                    user_ids_type_0_item = UUID(user_ids_type_0_item_data)

                    user_ids_type_0.append(user_ids_type_0_item)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))

        create_ac_ls_schema_multiple = cls(
            object_keys=object_keys,
            permissions=permissions,
            group_ids=group_ids,
            mode=mode,
            object_type=object_type,
            user_ids=user_ids,
        )

        create_ac_ls_schema_multiple.additional_properties = d
        return create_ac_ls_schema_multiple

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
