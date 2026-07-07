from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_content_info_internal_schema_media_formats_item import (
        SearchContentInfoInternalSchemaMediaFormatsItem,
    )
    from ..models.search_content_info_internal_schema_media_types_item import (
        SearchContentInfoInternalSchemaMediaTypesItem,
    )
    from ..models.storage_content_info import StorageContentInfo


T = TypeVar("T", bound="SearchContentInfoInternalSchema")


@_attrs_define
class SearchContentInfoInternalSchema:
    """
    Attributes:
        assets_count (int | Unset):
        collections_count (int | Unset):
        media_formats (list[SearchContentInfoInternalSchemaMediaFormatsItem] | Unset):
        media_types (list[SearchContentInfoInternalSchemaMediaTypesItem] | Unset):
        storage_info (list[StorageContentInfo] | Unset):
        title (str | Unset):
        total_duration_milliseconds (int | Unset):
        total_size (int | Unset):
    """

    assets_count: int | Unset = UNSET
    collections_count: int | Unset = UNSET
    media_formats: list[SearchContentInfoInternalSchemaMediaFormatsItem] | Unset = UNSET
    media_types: list[SearchContentInfoInternalSchemaMediaTypesItem] | Unset = UNSET
    storage_info: list[StorageContentInfo] | Unset = UNSET
    title: str | Unset = UNSET
    total_duration_milliseconds: int | Unset = UNSET
    total_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets_count = self.assets_count

        collections_count = self.collections_count

        media_formats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media_formats, Unset):
            media_formats = []
            for media_formats_item_data in self.media_formats:
                media_formats_item = media_formats_item_data.to_dict()
                media_formats.append(media_formats_item)

        media_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media_types, Unset):
            media_types = []
            for media_types_item_data in self.media_types:
                media_types_item = media_types_item_data.to_dict()
                media_types.append(media_types_item)

        storage_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.storage_info, Unset):
            storage_info = []
            for storage_info_item_data in self.storage_info:
                storage_info_item = storage_info_item_data.to_dict()
                storage_info.append(storage_info_item)

        title = self.title

        total_duration_milliseconds = self.total_duration_milliseconds

        total_size = self.total_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets_count is not UNSET:
            field_dict["assets_count"] = assets_count
        if collections_count is not UNSET:
            field_dict["collections_count"] = collections_count
        if media_formats is not UNSET:
            field_dict["media_formats"] = media_formats
        if media_types is not UNSET:
            field_dict["media_types"] = media_types
        if storage_info is not UNSET:
            field_dict["storage_info"] = storage_info
        if title is not UNSET:
            field_dict["title"] = title
        if total_duration_milliseconds is not UNSET:
            field_dict["total_duration_milliseconds"] = total_duration_milliseconds
        if total_size is not UNSET:
            field_dict["total_size"] = total_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_content_info_internal_schema_media_formats_item import (
            SearchContentInfoInternalSchemaMediaFormatsItem,
        )
        from ..models.search_content_info_internal_schema_media_types_item import (
            SearchContentInfoInternalSchemaMediaTypesItem,
        )
        from ..models.storage_content_info import StorageContentInfo

        d = dict(src_dict)
        assets_count = d.pop("assets_count", UNSET)

        collections_count = d.pop("collections_count", UNSET)

        _media_formats = d.pop("media_formats", UNSET)
        media_formats: list[SearchContentInfoInternalSchemaMediaFormatsItem] | Unset = (
            UNSET
        )
        if _media_formats is not UNSET:
            media_formats = []
            for media_formats_item_data in _media_formats:
                media_formats_item = (
                    SearchContentInfoInternalSchemaMediaFormatsItem.from_dict(
                        media_formats_item_data
                    )
                )

                media_formats.append(media_formats_item)

        _media_types = d.pop("media_types", UNSET)
        media_types: list[SearchContentInfoInternalSchemaMediaTypesItem] | Unset = UNSET
        if _media_types is not UNSET:
            media_types = []
            for media_types_item_data in _media_types:
                media_types_item = (
                    SearchContentInfoInternalSchemaMediaTypesItem.from_dict(
                        media_types_item_data
                    )
                )

                media_types.append(media_types_item)

        _storage_info = d.pop("storage_info", UNSET)
        storage_info: list[StorageContentInfo] | Unset = UNSET
        if _storage_info is not UNSET:
            storage_info = []
            for storage_info_item_data in _storage_info:
                storage_info_item = StorageContentInfo.from_dict(storage_info_item_data)

                storage_info.append(storage_info_item)

        title = d.pop("title", UNSET)

        total_duration_milliseconds = d.pop("total_duration_milliseconds", UNSET)

        total_size = d.pop("total_size", UNSET)

        search_content_info_internal_schema = cls(
            assets_count=assets_count,
            collections_count=collections_count,
            media_formats=media_formats,
            media_types=media_types,
            storage_info=storage_info,
            title=title,
            total_duration_milliseconds=total_duration_milliseconds,
            total_size=total_size,
        )

        search_content_info_internal_schema.additional_properties = d
        return search_content_info_internal_schema

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
