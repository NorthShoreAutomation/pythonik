from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACLsSchema")


@_attrs_define
class ACLsSchema:
    """
    Attributes:
        object_keys (list[str] | None | Unset): The number of object_keys in the list is limited to a minimum of 0 and a
            maximum of 500
    """

    object_keys: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_keys: list[str] | None | Unset
        if isinstance(self.object_keys, Unset):
            object_keys = UNSET
        elif isinstance(self.object_keys, list):
            object_keys = self.object_keys

        else:
            object_keys = self.object_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_keys is not UNSET:
            field_dict["object_keys"] = object_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        ac_ls_schema = cls(
            object_keys=object_keys,
        )

        ac_ls_schema.additional_properties = d
        return ac_ls_schema

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
