from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_content_info_internal_schema_media_formats_type_0_item import (
        SearchContentInfoInternalSchemaMediaFormatsType0Item,
    )
    from ..models.search_content_info_internal_schema_media_types_type_0_item import (
        SearchContentInfoInternalSchemaMediaTypesType0Item,
    )
    from ..models.storage_content_info import StorageContentInfo


T = TypeVar("T", bound="SearchContentInfoInternalSchema")


@_attrs_define
class SearchContentInfoInternalSchema:
    """
    Attributes:
        assets_count (int | None | Unset):
        collections_count (int | None | Unset):
        media_formats (list[SearchContentInfoInternalSchemaMediaFormatsType0Item] | None | Unset):
        media_types (list[SearchContentInfoInternalSchemaMediaTypesType0Item] | None | Unset):
        storage_info (list[StorageContentInfo] | None | Unset):
        title (None | str | Unset):
        total_duration_milliseconds (int | None | Unset):
        total_size (int | None | Unset):
    """

    assets_count: int | None | Unset = UNSET
    collections_count: int | None | Unset = UNSET
    media_formats: (
        list[SearchContentInfoInternalSchemaMediaFormatsType0Item] | None | Unset
    ) = UNSET
    media_types: (
        list[SearchContentInfoInternalSchemaMediaTypesType0Item] | None | Unset
    ) = UNSET
    storage_info: list[StorageContentInfo] | None | Unset = UNSET
    title: None | str | Unset = UNSET
    total_duration_milliseconds: int | None | Unset = UNSET
    total_size: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets_count: int | None | Unset
        if isinstance(self.assets_count, Unset):
            assets_count = UNSET
        else:
            assets_count = self.assets_count

        collections_count: int | None | Unset
        if isinstance(self.collections_count, Unset):
            collections_count = UNSET
        else:
            collections_count = self.collections_count

        media_formats: list[dict[str, Any]] | None | Unset
        if isinstance(self.media_formats, Unset):
            media_formats = UNSET
        elif isinstance(self.media_formats, list):
            media_formats = []
            for media_formats_type_0_item_data in self.media_formats:
                media_formats_type_0_item = media_formats_type_0_item_data.to_dict()
                media_formats.append(media_formats_type_0_item)

        else:
            media_formats = self.media_formats

        media_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.media_types, Unset):
            media_types = UNSET
        elif isinstance(self.media_types, list):
            media_types = []
            for media_types_type_0_item_data in self.media_types:
                media_types_type_0_item = media_types_type_0_item_data.to_dict()
                media_types.append(media_types_type_0_item)

        else:
            media_types = self.media_types

        storage_info: list[dict[str, Any]] | None | Unset
        if isinstance(self.storage_info, Unset):
            storage_info = UNSET
        elif isinstance(self.storage_info, list):
            storage_info = []
            for storage_info_type_0_item_data in self.storage_info:
                storage_info_type_0_item = storage_info_type_0_item_data.to_dict()
                storage_info.append(storage_info_type_0_item)

        else:
            storage_info = self.storage_info

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        total_duration_milliseconds: int | None | Unset
        if isinstance(self.total_duration_milliseconds, Unset):
            total_duration_milliseconds = UNSET
        else:
            total_duration_milliseconds = self.total_duration_milliseconds

        total_size: int | None | Unset
        if isinstance(self.total_size, Unset):
            total_size = UNSET
        else:
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
        from ..models.search_content_info_internal_schema_media_formats_type_0_item import (
            SearchContentInfoInternalSchemaMediaFormatsType0Item,
        )
        from ..models.search_content_info_internal_schema_media_types_type_0_item import (
            SearchContentInfoInternalSchemaMediaTypesType0Item,
        )
        from ..models.storage_content_info import StorageContentInfo

        d = dict(src_dict)

        def _parse_assets_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assets_count = _parse_assets_count(d.pop("assets_count", UNSET))

        def _parse_collections_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        collections_count = _parse_collections_count(d.pop("collections_count", UNSET))

        def _parse_media_formats(
            data: object,
        ) -> list[SearchContentInfoInternalSchemaMediaFormatsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_formats_type_0 = []
                _media_formats_type_0 = data
                for media_formats_type_0_item_data in _media_formats_type_0:
                    media_formats_type_0_item = (
                        SearchContentInfoInternalSchemaMediaFormatsType0Item.from_dict(
                            media_formats_type_0_item_data
                        )
                    )

                    media_formats_type_0.append(media_formats_type_0_item)

                return media_formats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SearchContentInfoInternalSchemaMediaFormatsType0Item]
                | None
                | Unset,
                data,
            )

        media_formats = _parse_media_formats(d.pop("media_formats", UNSET))

        def _parse_media_types(
            data: object,
        ) -> list[SearchContentInfoInternalSchemaMediaTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_types_type_0 = []
                _media_types_type_0 = data
                for media_types_type_0_item_data in _media_types_type_0:
                    media_types_type_0_item = (
                        SearchContentInfoInternalSchemaMediaTypesType0Item.from_dict(
                            media_types_type_0_item_data
                        )
                    )

                    media_types_type_0.append(media_types_type_0_item)

                return media_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SearchContentInfoInternalSchemaMediaTypesType0Item] | None | Unset,
                data,
            )

        media_types = _parse_media_types(d.pop("media_types", UNSET))

        def _parse_storage_info(
            data: object,
        ) -> list[StorageContentInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                storage_info_type_0 = []
                _storage_info_type_0 = data
                for storage_info_type_0_item_data in _storage_info_type_0:
                    storage_info_type_0_item = StorageContentInfo.from_dict(
                        storage_info_type_0_item_data
                    )

                    storage_info_type_0.append(storage_info_type_0_item)

                return storage_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StorageContentInfo] | None | Unset, data)

        storage_info = _parse_storage_info(d.pop("storage_info", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_total_duration_milliseconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_duration_milliseconds = _parse_total_duration_milliseconds(
            d.pop("total_duration_milliseconds", UNSET)
        )

        def _parse_total_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_size = _parse_total_size(d.pop("total_size", UNSET))

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
