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
    from ..models.playlist_schema_keyframes_item import PlaylistSchemaKeyframesItem


T = TypeVar("T", bound="PlaylistSchema")


@_attrs_define
class PlaylistSchema:
    """
    Attributes:
        name (str):
        created_by_user (UUID | Unset):
        custom_keyframe (None | Unset | UUID):
        custom_poster (None | Unset | UUID):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        id (UUID | Unset):
        item_count (int | Unset):
        keyframe_asset_ids (list[UUID] | Unset):
        keyframes (list[PlaylistSchemaKeyframesItem] | Unset):
        playlist_items (list[PlaylistItemSchema] | Unset):
        project_id (UUID | Unset):
        status (PlaylistSchemaStatus | Unset):
        system_domain_id (UUID | Unset):
    """

    name: str
    created_by_user: UUID | Unset = UNSET
    custom_keyframe: None | Unset | UUID = UNSET
    custom_poster: None | Unset | UUID = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    item_count: int | Unset = UNSET
    keyframe_asset_ids: list[UUID] | Unset = UNSET
    keyframes: list[PlaylistSchemaKeyframesItem] | Unset = UNSET
    playlist_items: list[PlaylistItemSchema] | Unset = UNSET
    project_id: UUID | Unset = UNSET
    status: PlaylistSchemaStatus | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_by_user: str | Unset = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = str(self.created_by_user)

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

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        item_count = self.item_count

        keyframe_asset_ids: list[str] | Unset = UNSET
        if not isinstance(self.keyframe_asset_ids, Unset):
            keyframe_asset_ids = []
            for keyframe_asset_ids_item_data in self.keyframe_asset_ids:
                keyframe_asset_ids_item = str(keyframe_asset_ids_item_data)
                keyframe_asset_ids.append(keyframe_asset_ids_item)

        keyframes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keyframes, Unset):
            keyframes = []
            for keyframes_item_data in self.keyframes:
                keyframes_item = keyframes_item_data.to_dict()
                keyframes.append(keyframes_item)

        playlist_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.playlist_items, Unset):
            playlist_items = []
            for playlist_items_item_data in self.playlist_items:
                playlist_items_item = playlist_items_item_data.to_dict()
                playlist_items.append(playlist_items_item)

        project_id: str | Unset = UNSET
        if not isinstance(self.project_id, Unset):
            project_id = str(self.project_id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

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
        from ..models.playlist_schema_keyframes_item import PlaylistSchemaKeyframesItem

        d = dict(src_dict)
        name = d.pop("name")

        _created_by_user = d.pop("created_by_user", UNSET)
        created_by_user: UUID | Unset
        if isinstance(_created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = UUID(_created_by_user)

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

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        item_count = d.pop("item_count", UNSET)

        _keyframe_asset_ids = d.pop("keyframe_asset_ids", UNSET)
        keyframe_asset_ids: list[UUID] | Unset = UNSET
        if _keyframe_asset_ids is not UNSET:
            keyframe_asset_ids = []
            for keyframe_asset_ids_item_data in _keyframe_asset_ids:
                keyframe_asset_ids_item = UUID(keyframe_asset_ids_item_data)

                keyframe_asset_ids.append(keyframe_asset_ids_item)

        _keyframes = d.pop("keyframes", UNSET)
        keyframes: list[PlaylistSchemaKeyframesItem] | Unset = UNSET
        if _keyframes is not UNSET:
            keyframes = []
            for keyframes_item_data in _keyframes:
                keyframes_item = PlaylistSchemaKeyframesItem.from_dict(
                    keyframes_item_data
                )

                keyframes.append(keyframes_item)

        _playlist_items = d.pop("playlist_items", UNSET)
        playlist_items: list[PlaylistItemSchema] | Unset = UNSET
        if _playlist_items is not UNSET:
            playlist_items = []
            for playlist_items_item_data in _playlist_items:
                playlist_items_item = PlaylistItemSchema.from_dict(
                    playlist_items_item_data
                )

                playlist_items.append(playlist_items_item)

        _project_id = d.pop("project_id", UNSET)
        project_id: UUID | Unset
        if isinstance(_project_id, Unset):
            project_id = UNSET
        else:
            project_id = UUID(_project_id)

        _status = d.pop("status", UNSET)
        status: PlaylistSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PlaylistSchemaStatus(_status)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

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
