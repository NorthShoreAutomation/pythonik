from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiPartURLsSchema")


@_attrs_define
class MultiPartURLsSchema:
    """
    Attributes:
        abort_url (str | Unset):
        complete_url (str | Unset):
        list_parts_url (list[str] | Unset):
    """

    abort_url: str | Unset = UNSET
    complete_url: str | Unset = UNSET
    list_parts_url: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abort_url = self.abort_url

        complete_url = self.complete_url

        list_parts_url: list[str] | Unset = UNSET
        if not isinstance(self.list_parts_url, Unset):
            list_parts_url = self.list_parts_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abort_url is not UNSET:
            field_dict["abort_url"] = abort_url
        if complete_url is not UNSET:
            field_dict["complete_url"] = complete_url
        if list_parts_url is not UNSET:
            field_dict["list_parts_url"] = list_parts_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abort_url = d.pop("abort_url", UNSET)

        complete_url = d.pop("complete_url", UNSET)

        list_parts_url = cast(list[str], d.pop("list_parts_url", UNSET))

        multi_part_ur_ls_schema = cls(
            abort_url=abort_url,
            complete_url=complete_url,
            list_parts_url=list_parts_url,
        )

        multi_part_ur_ls_schema.additional_properties = d
        return multi_part_ur_ls_schema

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
