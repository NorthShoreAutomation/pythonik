from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.playlist_schema_status import PlaylistSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playlist_item_schema import PlaylistItemSchema
    from ..models.playlist_schema_keyframes_type_0_item import (
        PlaylistSchemaKeyframesType0Item,
    )


T = TypeVar("T", bound="PlaylistSchema")


@_attrs_define
class PlaylistSchema:
    """
    Attributes:
        name (str):
        created_by_user (None | Unset | UUID):
        custom_keyframe (None | Unset | UUID):
        custom_poster (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        id (None | Unset | UUID):
        item_count (int | None | Unset):
        keyframe_asset_ids (list[UUID] | None | Unset):
        keyframes (list[PlaylistSchemaKeyframesType0Item] | None | Unset):
        playlist_items (list[PlaylistItemSchema] | None | Unset):
        project_id (None | Unset | UUID):
        status (None | PlaylistSchemaStatus | Unset):
        system_domain_id (None | Unset | UUID):
    """

    name: str
    created_by_user: None | Unset | UUID = UNSET
    custom_keyframe: None | Unset | UUID = UNSET
    custom_poster: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    item_count: int | None | Unset = UNSET
    keyframe_asset_ids: list[UUID] | None | Unset = UNSET
    keyframes: list[PlaylistSchemaKeyframesType0Item] | None | Unset = UNSET
    playlist_items: list[PlaylistItemSchema] | None | Unset = UNSET
    project_id: None | Unset | UUID = UNSET
    status: None | PlaylistSchemaStatus | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_by_user: None | str | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        elif isinstance(self.created_by_user, UUID):
            created_by_user = str(self.created_by_user)
        else:
            created_by_user = self.created_by_user

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

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        item_count: int | None | Unset
        if isinstance(self.item_count, Unset):
            item_count = UNSET
        else:
            item_count = self.item_count

        keyframe_asset_ids: list[str] | None | Unset
        if isinstance(self.keyframe_asset_ids, Unset):
            keyframe_asset_ids = UNSET
        elif isinstance(self.keyframe_asset_ids, list):
            keyframe_asset_ids = []
            for keyframe_asset_ids_type_0_item_data in self.keyframe_asset_ids:
                keyframe_asset_ids_type_0_item = str(
                    keyframe_asset_ids_type_0_item_data
                )
                keyframe_asset_ids.append(keyframe_asset_ids_type_0_item)

        else:
            keyframe_asset_ids = self.keyframe_asset_ids

        keyframes: list[dict[str, Any]] | None | Unset
        if isinstance(self.keyframes, Unset):
            keyframes = UNSET
        elif isinstance(self.keyframes, list):
            keyframes = []
            for keyframes_type_0_item_data in self.keyframes:
                keyframes_type_0_item = keyframes_type_0_item_data.to_dict()
                keyframes.append(keyframes_type_0_item)

        else:
            keyframes = self.keyframes

        playlist_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.playlist_items, Unset):
            playlist_items = UNSET
        elif isinstance(self.playlist_items, list):
            playlist_items = []
            for playlist_items_type_0_item_data in self.playlist_items:
                playlist_items_type_0_item = playlist_items_type_0_item_data.to_dict()
                playlist_items.append(playlist_items_type_0_item)

        else:
            playlist_items = self.playlist_items

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, PlaylistSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if custom_keyframe is not UNSET:
            field_dict["custom_keyframe"] = custom_keyframe
        if custom_poster is not UNSET:
            field_dict["custom_poster"] = custom_poster
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if id is not UNSET:
            field_dict["id"] = id
        if item_count is not UNSET:
            field_dict["item_count"] = item_count
        if keyframe_asset_ids is not UNSET:
            field_dict["keyframe_asset_ids"] = keyframe_asset_ids
        if keyframes is not UNSET:
            field_dict["keyframes"] = keyframes
        if playlist_items is not UNSET:
            field_dict["playlist_items"] = playlist_items
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if status is not UNSET:
            field_dict["status"] = status
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.playlist_item_schema import PlaylistItemSchema
        from ..models.playlist_schema_keyframes_type_0_item import (
            PlaylistSchemaKeyframesType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_created_by_user(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_user_type_0 = UUID(data)

                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user", UNSET))

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

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_item_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        item_count = _parse_item_count(d.pop("item_count", UNSET))

        def _parse_keyframe_asset_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyframe_asset_ids_type_0 = []
                _keyframe_asset_ids_type_0 = data
                for keyframe_asset_ids_type_0_item_data in _keyframe_asset_ids_type_0:
                    keyframe_asset_ids_type_0_item = UUID(
                        keyframe_asset_ids_type_0_item_data
                    )

                    keyframe_asset_ids_type_0.append(keyframe_asset_ids_type_0_item)

                return keyframe_asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        keyframe_asset_ids = _parse_keyframe_asset_ids(
            d.pop("keyframe_asset_ids", UNSET)
        )

        def _parse_keyframes(
            data: object,
        ) -> list[PlaylistSchemaKeyframesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyframes_type_0 = []
                _keyframes_type_0 = data
                for keyframes_type_0_item_data in _keyframes_type_0:
                    keyframes_type_0_item = PlaylistSchemaKeyframesType0Item.from_dict(
                        keyframes_type_0_item_data
                    )

                    keyframes_type_0.append(keyframes_type_0_item)

                return keyframes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PlaylistSchemaKeyframesType0Item] | None | Unset, data)

        keyframes = _parse_keyframes(d.pop("keyframes", UNSET))

        def _parse_playlist_items(
            data: object,
        ) -> list[PlaylistItemSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                playlist_items_type_0 = []
                _playlist_items_type_0 = data
                for playlist_items_type_0_item_data in _playlist_items_type_0:
                    playlist_items_type_0_item = PlaylistItemSchema.from_dict(
                        playlist_items_type_0_item_data
                    )

                    playlist_items_type_0.append(playlist_items_type_0_item)

                return playlist_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PlaylistItemSchema] | None | Unset, data)

        playlist_items = _parse_playlist_items(d.pop("playlist_items", UNSET))

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_status(data: object) -> None | PlaylistSchemaStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = PlaylistSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaylistSchemaStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        playlist_schema = cls(
            name=name,
            created_by_user=created_by_user,
            custom_keyframe=custom_keyframe,
            custom_poster=custom_poster,
            date_created=date_created,
            date_modified=date_modified,
            id=id,
            item_count=item_count,
            keyframe_asset_ids=keyframe_asset_ids,
            keyframes=keyframes,
            playlist_items=playlist_items,
            project_id=project_id,
            status=status,
            system_domain_id=system_domain_id,
        )

        playlist_schema.additional_properties = d
        return playlist_schema

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
