from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_input_schema_status import CollectionInputSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionInputSchema")


@_attrs_define
class CollectionInputSchema:
    """
    Attributes:
        title (str):
        category (None | str | Unset):
        custom_keyframe (None | Unset | UUID):
        custom_poster (None | Unset | UUID):
        date_created (datetime.datetime | Unset):
        external_id (None | str | Unset):
        is_root (bool | Unset):
        keyframe_asset_ids (list[UUID] | Unset):
        parent_id (None | Unset | UUID):
        status (CollectionInputSchemaStatus | Unset):
        storage_id (None | Unset | UUID):
    """

    title: str
    category: None | str | Unset = UNSET
    custom_keyframe: None | Unset | UUID = UNSET
    custom_poster: None | Unset | UUID = UNSET
    date_created: datetime.datetime | Unset = UNSET
    external_id: None | str | Unset = UNSET
    is_root: bool | Unset = UNSET
    keyframe_asset_ids: list[UUID] | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    status: CollectionInputSchemaStatus | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        custom_keyframe: None | str | Unset
        if isinstance(self.custom_keyframe, Unset):
            custom_keyframe = UNSET
        elif isinstance(self.custom_keyframe, UUID):
            custom_keyframe = str(self.custom_keyframe)
        else:
            custom_keyframe = self.custom_keyframe

        custom_poster: None | str | Unset
        if isinstance(self.custom_poster, Unset):
            custom_poster = UNSET
        elif isinstance(self.custom_poster, UUID):
            custom_poster = str(self.custom_poster)
        else:
            custom_poster = self.custom_poster

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        is_root = self.is_root

        keyframe_asset_ids: list[str] | Unset = UNSET
        if not isinstance(self.keyframe_asset_ids, Unset):
            keyframe_asset_ids = []
            for keyframe_asset_ids_item_data in self.keyframe_asset_ids:
                keyframe_asset_ids_item = str(keyframe_asset_ids_item_data)
                keyframe_asset_ids.append(keyframe_asset_ids_item)

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if custom_keyframe is not UNSET:
            field_dict["custom_keyframe"] = custom_keyframe
        if custom_poster is not UNSET:
            field_dict["custom_poster"] = custom_poster
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if is_root is not UNSET:
            field_dict["is_root"] = is_root
        if keyframe_asset_ids is not UNSET:
            field_dict["keyframe_asset_ids"] = keyframe_asset_ids
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_custom_keyframe(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                custom_keyframe_type_0 = UUID(data)

                return custom_keyframe_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        custom_keyframe = _parse_custom_keyframe(d.pop("custom_keyframe", UNSET))

        def _parse_custom_poster(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                custom_poster_type_0 = UUID(data)

                return custom_poster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        custom_poster = _parse_custom_poster(d.pop("custom_poster", UNSET))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        is_root = d.pop("is_root", UNSET)

        _keyframe_asset_ids = d.pop("keyframe_asset_ids", UNSET)
        keyframe_asset_ids: list[UUID] | Unset = UNSET
        if _keyframe_asset_ids is not UNSET:
            keyframe_asset_ids = []
            for keyframe_asset_ids_item_data in _keyframe_asset_ids:
                keyframe_asset_ids_item = UUID(keyframe_asset_ids_item_data)

                keyframe_asset_ids.append(keyframe_asset_ids_item)

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        _status = d.pop("status", UNSET)
        status: CollectionInputSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CollectionInputSchemaStatus(_status)

        def _parse_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_id_type_0 = UUID(data)

                return storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_id = _parse_storage_id(d.pop("storage_id", UNSET))

        collection_input_schema = cls(
            title=title,
            category=category,
            custom_keyframe=custom_keyframe,
            custom_poster=custom_poster,
            date_created=date_created,
            external_id=external_id,
            is_root=is_root,
            keyframe_asset_ids=keyframe_asset_ids,
            parent_id=parent_id,
            status=status,
            storage_id=storage_id,
        )

        collection_input_schema.additional_properties = d
        return collection_input_schema

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
