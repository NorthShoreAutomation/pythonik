from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListObjectsSchema")


@_attrs_define
class ListObjectsSchema:
    """
    Attributes:
        first_url (None | str | Unset):
        last_url (None | str | Unset):
        next_url (None | str | Unset):
        page (int | None | Unset):
        pages (int | None | Unset):
        per_page (int | None | Unset):
        prev_url (None | str | Unset):
        total (int | None | Unset):
    """

    first_url: None | str | Unset = UNSET
    last_url: None | str | Unset = UNSET
    next_url: None | str | Unset = UNSET
    page: int | None | Unset = UNSET
    pages: int | None | Unset = UNSET
    per_page: int | None | Unset = UNSET
    prev_url: None | str | Unset = UNSET
    total: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_url: None | str | Unset
        if isinstance(self.first_url, Unset):
            first_url = UNSET
        else:
            first_url = self.first_url

        last_url: None | str | Unset
        if isinstance(self.last_url, Unset):
            last_url = UNSET
        else:
            last_url = self.last_url

        next_url: None | str | Unset
        if isinstance(self.next_url, Unset):
            next_url = UNSET
        else:
            next_url = self.next_url

        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        pages: int | None | Unset
        if isinstance(self.pages, Unset):
            pages = UNSET
        else:
            pages = self.pages

        per_page: int | None | Unset
        if isinstance(self.per_page, Unset):
            per_page = UNSET
        else:
            per_page = self.per_page

        prev_url: None | str | Unset
        if isinstance(self.prev_url, Unset):
            prev_url = UNSET
        else:
            prev_url = self.prev_url

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
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

        def _parse_first_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_url = _parse_first_url(d.pop("first_url", UNSET))

        def _parse_last_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_url = _parse_last_url(d.pop("last_url", UNSET))

        def _parse_next_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_url = _parse_next_url(d.pop("next_url", UNSET))

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        def _parse_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pages = _parse_pages(d.pop("pages", UNSET))

        def _parse_per_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        per_page = _parse_per_page(d.pop("per_page", UNSET))

        def _parse_prev_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prev_url = _parse_prev_url(d.pop("prev_url", UNSET))

        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

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
