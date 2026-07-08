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
        abort_url (None | str | Unset):
        complete_url (None | str | Unset):
        list_parts_url (list[str] | None | Unset):
    """

    abort_url: None | str | Unset = UNSET
    complete_url: None | str | Unset = UNSET
    list_parts_url: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abort_url: None | str | Unset
        if isinstance(self.abort_url, Unset):
            abort_url = UNSET
        else:
            abort_url = self.abort_url

        complete_url: None | str | Unset
        if isinstance(self.complete_url, Unset):
            complete_url = UNSET
        else:
            complete_url = self.complete_url

        list_parts_url: list[str] | None | Unset
        if isinstance(self.list_parts_url, Unset):
            list_parts_url = UNSET
        elif isinstance(self.list_parts_url, list):
            list_parts_url = self.list_parts_url

        else:
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

        def _parse_abort_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abort_url = _parse_abort_url(d.pop("abort_url", UNSET))

        def _parse_complete_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        complete_url = _parse_complete_url(d.pop("complete_url", UNSET))

        def _parse_list_parts_url(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                list_parts_url_type_0 = cast(list[str], data)

                return list_parts_url_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        list_parts_url = _parse_list_parts_url(d.pop("list_parts_url", UNSET))

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
