from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListObjectsSchema")


@_attrs_define
class ListObjectsSchema:
    """
    Attributes:
        first_url (str | Unset):
        last_url (str | Unset):
        next_url (str | Unset):
        page (int | Unset):
        pages (int | Unset):
        per_page (int | Unset):
        prev_url (str | Unset):
        total (int | Unset):
    """

    first_url: str | Unset = UNSET
    last_url: str | Unset = UNSET
    next_url: str | Unset = UNSET
    page: int | Unset = UNSET
    pages: int | Unset = UNSET
    per_page: int | Unset = UNSET
    prev_url: str | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_url = self.first_url

        last_url = self.last_url

        next_url = self.next_url

        page = self.page

        pages = self.pages

        per_page = self.per_page

        prev_url = self.prev_url

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_url is not UNSET:
            field_dict["first_url"] = first_url
        if last_url is not UNSET:
            field_dict["last_url"] = last_url
        if next_url is not UNSET:
            field_dict["next_url"] = next_url
        if page is not UNSET:
            field_dict["page"] = page
        if pages is not UNSET:
            field_dict["pages"] = pages
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if prev_url is not UNSET:
            field_dict["prev_url"] = prev_url
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_url = d.pop("first_url", UNSET)

        last_url = d.pop("last_url", UNSET)

        next_url = d.pop("next_url", UNSET)

        page = d.pop("page", UNSET)

        pages = d.pop("pages", UNSET)

        per_page = d.pop("per_page", UNSET)

        prev_url = d.pop("prev_url", UNSET)

        total = d.pop("total", UNSET)

        list_objects_schema = cls(
            first_url=first_url,
            last_url=last_url,
            next_url=next_url,
            page=page,
            pages=pages,
            per_page=per_page,
            prev_url=prev_url,
            total=total,
        )

        list_objects_schema.additional_properties = d
        return list_objects_schema

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
