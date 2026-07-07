from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateACLsResultSchema")


@_attrs_define
class CreateACLsResultSchema:
    """
    Attributes:
        updated_object_keys (list[str] | Unset):
    """

    updated_object_keys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_object_keys: list[str] | Unset = UNSET
        if not isinstance(self.updated_object_keys, Unset):
            updated_object_keys = self.updated_object_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated_object_keys is not UNSET:
            field_dict["updated_object_keys"] = updated_object_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_object_keys = cast(list[str], d.pop("updated_object_keys", UNSET))

        create_ac_ls_result_schema = cls(
            updated_object_keys=updated_object_keys,
        )

        create_ac_ls_result_schema.additional_properties = d
        return create_ac_ls_result_schema

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
