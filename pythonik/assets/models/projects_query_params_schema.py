from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsQueryParamsSchema")


@_attrs_define
class ProjectsQueryParamsSchema:
    """
    Attributes:
        page (int | None | Unset): Which page number to fetch Default: 1.
        per_page (int | None | Unset): The number of items for each page Default: 10.
        scroll (bool | None | Unset):
        scroll_id (None | Unset | UUID):
        sort (None | str | Unset): A comma separated list of fieldnames with order (asc/desc)
    """

    page: int | None | Unset = 1
    per_page: int | None | Unset = 10
    scroll: bool | None | Unset = UNSET
    scroll_id: None | Unset | UUID = UNSET
    sort: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        per_page: int | None | Unset
        if isinstance(self.per_page, Unset):
            per_page = UNSET
        else:
            per_page = self.per_page

        scroll: bool | None | Unset
        if isinstance(self.scroll, Unset):
            scroll = UNSET
        else:
            scroll = self.scroll

        scroll_id: None | str | Unset
        if isinstance(self.scroll_id, Unset):
            scroll_id = UNSET
        elif isinstance(self.scroll_id, UUID):
            scroll_id = str(self.scroll_id)
        else:
            scroll_id = self.scroll_id

        sort: None | str | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        else:
            sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if scroll is not UNSET:
            field_dict["scroll"] = scroll
        if scroll_id is not UNSET:
            field_dict["scroll_id"] = scroll_id
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        def _parse_per_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        per_page = _parse_per_page(d.pop("per_page", UNSET))

        def _parse_scroll(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        scroll = _parse_scroll(d.pop("scroll", UNSET))

        def _parse_scroll_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scroll_id_type_0 = UUID(data)

                return scroll_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        scroll_id = _parse_scroll_id(d.pop("scroll_id", UNSET))

        def _parse_sort(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        projects_query_params_schema = cls(
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
        )

        projects_query_params_schema.additional_properties = d
        return projects_query_params_schema

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
