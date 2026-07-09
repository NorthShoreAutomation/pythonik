from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupIDsSchema")


@_attrs_define
class GroupIDsSchema:
    """
    Attributes:
        group_ids (list[UUID] | None | Unset):
    """

    group_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        group_i_ds_schema = cls(
            group_ids=group_ids,
        )

        group_i_ds_schema.additional_properties = d
        return group_i_ds_schema

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
