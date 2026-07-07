from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_base_schema_custom_order_status import (
    CollectionBaseSchemaCustomOrderStatus,
)
from ..models.collection_base_schema_status import CollectionBaseSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_base_schema_keyframes_item import (
        CollectionBaseSchemaKeyframesItem,
    )
    from ..models.collection_base_schema_metadata import CollectionBaseSchemaMetadata


T = TypeVar("T", bound="CollectionBaseSchema")


@_attrs_define
class CollectionBaseSchema:
    """
    Attributes:
        title (str):
        category (None | str | Unset):
        created_by_user (UUID | Unset):
        custom_keyframe (None | Unset | UUID):
        custom_order_status (CollectionBaseSchemaCustomOrderStatus | Unset):
        custom_poster (None | Unset | UUID):
        deleted_by_user (UUID | Unset):
        external_id (None | str | Unset):
        favoured (bool | Unset):
        id (UUID | Unset):
        in_collections (list[UUID] | Unset):
        is_root (bool | Unset):
        keyframe_asset_ids (list[UUID] | Unset):
        keyframes (list[CollectionBaseSchemaKeyframesItem] | Unset):
        metadata (CollectionBaseSchemaMetadata | Unset):
        object_type (str | Unset):
        parent_id (None | Unset | UUID):
        parents (list[UUID] | Unset):
        permissions (list[str] | Unset):
        position (int | Unset):
        project_id (UUID | Unset):
        status (CollectionBaseSchemaStatus | Unset):
        storage_id (None | Unset | UUID):
    """

    title: str
    category: None | str | Unset = UNSET
    created_by_user: UUID | Unset = UNSET
    custom_keyframe: None | Unset | UUID = UNSET
    custom_order_status: CollectionBaseSchemaCustomOrderStatus | Unset = UNSET
    custom_poster: None | Unset | UUID = UNSET
    deleted_by_user: UUID | Unset = UNSET
    external_id: None | str | Unset = UNSET
    favoured: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    in_collections: list[UUID] | Unset = UNSET
    is_root: bool | Unset = UNSET
    keyframe_asset_ids: list[UUID] | Unset = UNSET
    keyframes: list[CollectionBaseSchemaKeyframesItem] | Unset = UNSET
    metadata: CollectionBaseSchemaMetadata | Unset = UNSET
    object_type: str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    parents: list[UUID] | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    position: int | Unset = UNSET
    project_id: UUID | Unset = UNSET
    status: CollectionBaseSchemaStatus | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

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

        custom_order_status: str | Unset = UNSET
        if not isinstance(self.custom_order_status, Unset):
            custom_order_status = self.custom_order_status.value

        custom_poster: None | str | Unset
        if isinstance(self.custom_poster, Unset):
            custom_poster = UNSET
        elif isinstance(self.custom_poster, UUID):
            custom_poster = str(self.custom_poster)
        else:
            custom_poster = self.custom_poster

        deleted_by_user: str | Unset = UNSET
        if not isinstance(self.deleted_by_user, Unset):
            deleted_by_user = str(self.deleted_by_user)

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        favoured = self.favoured

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        in_collections: list[str] | Unset = UNSET
        if not isinstance(self.in_collections, Unset):
            in_collections = []
            for in_collections_item_data in self.in_collections:
                in_collections_item = str(in_collections_item_data)
                in_collections.append(in_collections_item)

        is_root = self.is_root

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

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        object_type = self.object_type

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        parents: list[str] | Unset = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = str(parents_item_data)
                parents.append(parents_item)

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        position = self.position

        project_id: str | Unset = UNSET
        if not isinstance(self.project_id, Unset):
            project_id = str(self.project_id)

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
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if custom_keyframe is not UNSET:
            field_dict["custom_keyframe"] = custom_keyframe
        if custom_order_status is not UNSET:
            field_dict["custom_order_status"] = custom_order_status
        if custom_poster is not UNSET:
            field_dict["custom_poster"] = custom_poster
        if deleted_by_user is not UNSET:
            field_dict["deleted_by_user"] = deleted_by_user
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if favoured is not UNSET:
            field_dict["favoured"] = favoured
        if id is not UNSET:
            field_dict["id"] = id
        if in_collections is not UNSET:
            field_dict["in_collections"] = in_collections
        if is_root is not UNSET:
            field_dict["is_root"] = is_root
        if keyframe_asset_ids is not UNSET:
            field_dict["keyframe_asset_ids"] = keyframe_asset_ids
        if keyframes is not UNSET:
            field_dict["keyframes"] = keyframes
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if parents is not UNSET:
            field_dict["parents"] = parents
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if position is not UNSET:
            field_dict["position"] = position
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_base_schema_keyframes_item import (
            CollectionBaseSchemaKeyframesItem,
        )
        from ..models.collection_base_schema_metadata import (
            CollectionBaseSchemaMetadata,
        )

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

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

        _custom_order_status = d.pop("custom_order_status", UNSET)
        custom_order_status: CollectionBaseSchemaCustomOrderStatus | Unset
        if isinstance(_custom_order_status, Unset):
            custom_order_status = UNSET
        else:
            custom_order_status = CollectionBaseSchemaCustomOrderStatus(
                _custom_order_status
            )

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

        _deleted_by_user = d.pop("deleted_by_user", UNSET)
        deleted_by_user: UUID | Unset
        if isinstance(_deleted_by_user, Unset):
            deleted_by_user = UNSET
        else:
            deleted_by_user = UUID(_deleted_by_user)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        favoured = d.pop("favoured", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _in_collections = d.pop("in_collections", UNSET)
        in_collections: list[UUID] | Unset = UNSET
        if _in_collections is not UNSET:
            in_collections = []
            for in_collections_item_data in _in_collections:
                in_collections_item = UUID(in_collections_item_data)

                in_collections.append(in_collections_item)

        is_root = d.pop("is_root", UNSET)

        _keyframe_asset_ids = d.pop("keyframe_asset_ids", UNSET)
        keyframe_asset_ids: list[UUID] | Unset = UNSET
        if _keyframe_asset_ids is not UNSET:
            keyframe_asset_ids = []
            for keyframe_asset_ids_item_data in _keyframe_asset_ids:
                keyframe_asset_ids_item = UUID(keyframe_asset_ids_item_data)

                keyframe_asset_ids.append(keyframe_asset_ids_item)

        _keyframes = d.pop("keyframes", UNSET)
        keyframes: list[CollectionBaseSchemaKeyframesItem] | Unset = UNSET
        if _keyframes is not UNSET:
            keyframes = []
            for keyframes_item_data in _keyframes:
                keyframes_item = CollectionBaseSchemaKeyframesItem.from_dict(
                    keyframes_item_data
                )

                keyframes.append(keyframes_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: CollectionBaseSchemaMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CollectionBaseSchemaMetadata.from_dict(_metadata)

        object_type = d.pop("object_type", UNSET)

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

        _parents = d.pop("parents", UNSET)
        parents: list[UUID] | Unset = UNSET
        if _parents is not UNSET:
            parents = []
            for parents_item_data in _parents:
                parents_item = UUID(parents_item_data)

                parents.append(parents_item)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        position = d.pop("position", UNSET)

        _project_id = d.pop("project_id", UNSET)
        project_id: UUID | Unset
        if isinstance(_project_id, Unset):
            project_id = UNSET
        else:
            project_id = UUID(_project_id)

        _status = d.pop("status", UNSET)
        status: CollectionBaseSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CollectionBaseSchemaStatus(_status)

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

        collection_base_schema = cls(
            title=title,
            category=category,
            created_by_user=created_by_user,
            custom_keyframe=custom_keyframe,
            custom_order_status=custom_order_status,
            custom_poster=custom_poster,
            deleted_by_user=deleted_by_user,
            external_id=external_id,
            favoured=favoured,
            id=id,
            in_collections=in_collections,
            is_root=is_root,
            keyframe_asset_ids=keyframe_asset_ids,
            keyframes=keyframes,
            metadata=metadata,
            object_type=object_type,
            parent_id=parent_id,
            parents=parents,
            permissions=permissions,
            position=position,
            project_id=project_id,
            status=status,
            storage_id=storage_id,
        )

        collection_base_schema.additional_properties = d
        return collection_base_schema

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
