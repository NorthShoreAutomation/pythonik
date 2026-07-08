from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionsQueryParamsSchema")


@_attrs_define
class CollectionsQueryParamsSchema:
    """
    Attributes:
        favoured_by (None | str | Unset): A user UUID who has favorited the collections
        include_keyframes (bool | None | Unset):  Default: True.
        page (int | None | Unset): Which page number to fetch Default: 1.
        per_page (int | None | Unset): The number of items for each page Default: 10.
        scroll (bool | None | Unset):
        scroll_id (None | Unset | UUID):
        sort (None | str | Unset): A comma separated list of fieldnames with order (asc/desc)
    """

    favoured_by: None | str | Unset = UNSET
    include_keyframes: bool | None | Unset = True
    page: int | None | Unset = 1
    per_page: int | None | Unset = 10
    scroll: bool | None | Unset = UNSET
    scroll_id: None | Unset | UUID = UNSET
    sort: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        favoured_by: None | str | Unset
        if isinstance(self.favoured_by, Unset):
            favoured_by = UNSET
        else:
            favoured_by = self.favoured_by

        include_keyframes: bool | None | Unset
        if isinstance(self.include_keyframes, Unset):
            include_keyframes = UNSET
        else:
            include_keyframes = self.include_keyframes

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
        if favoured_by is not UNSET:
            field_dict["favoured_by"] = favoured_by
        if include_keyframes is not UNSET:
            field_dict["include_keyframes"] = include_keyframes
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

        def _parse_favoured_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        favoured_by = _parse_favoured_by(d.pop("favoured_by", UNSET))

        def _parse_include_keyframes(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_keyframes = _parse_include_keyframes(d.pop("include_keyframes", UNSET))

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

        collections_query_params_schema = cls(
            favoured_by=favoured_by,
            include_keyframes=include_keyframes,
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
        )

        collections_query_params_schema.additional_properties = d
        return collections_query_params_schema

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
