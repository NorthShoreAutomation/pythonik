from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_content_query_params_schema_types_item import (
    CollectionContentQueryParamsSchemaTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionContentQueryParamsSchema")


@_attrs_define
class CollectionContentQueryParamsSchema:
    """
    Attributes:
        include_keyframes (bool | Unset):  Default: True.
        page (int | None | Unset): Which page number to fetch Default: 1.
        per_page (int | None | Unset): The number of items for each page Default: 10.
        sort (str | Unset): A comma separated list of fieldnames with order (asc/desc)
        types (list[CollectionContentQueryParamsSchemaTypesItem] | Unset): Comma-separated list of asset types to
            include in results. Defaults to all except POST.
    """

    include_keyframes: bool | Unset = True
    page: int | None | Unset = 1
    per_page: int | None | Unset = 10
    sort: str | Unset = UNSET
    types: list[CollectionContentQueryParamsSchemaTypesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        sort = self.sort

        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item = types_item_data.value
                types.append(types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_keyframes is not UNSET:
            field_dict["include_keyframes"] = include_keyframes
        if page is not UNSET:
            field_dict["page"] = page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if sort is not UNSET:
            field_dict["sort"] = sort
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_keyframes = d.pop("include_keyframes", UNSET)

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

        sort = d.pop("sort", UNSET)

        _types = d.pop("types", UNSET)
        types: list[CollectionContentQueryParamsSchemaTypesItem] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = CollectionContentQueryParamsSchemaTypesItem(
                    types_item_data
                )

                types.append(types_item)

        collection_content_query_params_schema = cls(
            include_keyframes=include_keyframes,
            page=page,
            per_page=per_page,
            sort=sort,
            types=types,
        )

        collection_content_query_params_schema.additional_properties = d
        return collection_content_query_params_schema

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
