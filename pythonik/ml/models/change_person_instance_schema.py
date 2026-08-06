from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePersonInstanceSchema")


@_attrs_define
class ChangePersonInstanceSchema:
    """
    Attributes:
        new_person_id (None | Unset | UUID):
        new_person_name (None | str | Unset):
    """

    new_person_id: None | Unset | UUID = UNSET
    new_person_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_person_id: None | str | Unset
        if isinstance(self.new_person_id, Unset):
            new_person_id = UNSET
        elif isinstance(self.new_person_id, UUID):
            new_person_id = str(self.new_person_id)
        else:
            new_person_id = self.new_person_id

        new_person_name: None | str | Unset
        if isinstance(self.new_person_name, Unset):
            new_person_name = UNSET
        else:
            new_person_name = self.new_person_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_person_id is not UNSET:
            field_dict["new_person_id"] = new_person_id
        if new_person_name is not UNSET:
            field_dict["new_person_name"] = new_person_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_new_person_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                new_person_id_type_0 = UUID(data)

                return new_person_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        new_person_id = _parse_new_person_id(d.pop("new_person_id", UNSET))

        def _parse_new_person_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_person_name = _parse_new_person_name(d.pop("new_person_name", UNSET))

        change_person_instance_schema = cls(
            new_person_id=new_person_id,
            new_person_name=new_person_name,
        )

        change_person_instance_schema.additional_properties = d
        return change_person_instance_schema

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
