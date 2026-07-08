from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_base_schema_custom_order_status_type_1 import (
        CollectionBaseSchemaCustomOrderStatusType1,
    )
    from ..models.collection_base_schema_keyframes_type_0_item import (
        CollectionBaseSchemaKeyframesType0Item,
    )
    from ..models.collection_base_schema_metadata_type_0 import (
        CollectionBaseSchemaMetadataType0,
    )
    from ..models.collection_base_schema_status_type_1 import (
        CollectionBaseSchemaStatusType1,
    )


T = TypeVar("T", bound="CollectionBaseSchema")


@_attrs_define
class CollectionBaseSchema:
    """
    Attributes:
        title (str):
        category (None | str | Unset):
        created_by_user (None | Unset | UUID):
        custom_keyframe (None | Unset | UUID):
        custom_order_status (CollectionBaseSchemaCustomOrderStatusType1 | None | Unset):
        custom_poster (None | Unset | UUID):
        deleted_by_user (None | Unset | UUID):
        external_id (None | str | Unset):
        favoured (bool | None | Unset):
        id (None | Unset | UUID):
        in_collections (list[UUID] | None | Unset):
        is_root (bool | None | Unset):
        keyframe_asset_ids (list[UUID] | None | Unset):
        keyframes (list[CollectionBaseSchemaKeyframesType0Item] | None | Unset):
        metadata (CollectionBaseSchemaMetadataType0 | None | Unset):
        object_type (None | str | Unset):
        parent_id (None | Unset | UUID):
        parents (list[UUID] | None | Unset):
        permissions (list[str] | None | Unset):
        position (int | None | Unset):
        project_id (None | Unset | UUID):
        status (CollectionBaseSchemaStatusType1 | None | Unset):
        storage_id (None | Unset | UUID):
    """

    title: str
    category: None | str | Unset = UNSET
    created_by_user: None | Unset | UUID = UNSET
    custom_keyframe: None | Unset | UUID = UNSET
    custom_order_status: CollectionBaseSchemaCustomOrderStatusType1 | None | Unset = (
        UNSET
    )
    custom_poster: None | Unset | UUID = UNSET
    deleted_by_user: None | Unset | UUID = UNSET
    external_id: None | str | Unset = UNSET
    favoured: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    in_collections: list[UUID] | None | Unset = UNSET
    is_root: bool | None | Unset = UNSET
    keyframe_asset_ids: list[UUID] | None | Unset = UNSET
    keyframes: list[CollectionBaseSchemaKeyframesType0Item] | None | Unset = UNSET
    metadata: CollectionBaseSchemaMetadataType0 | None | Unset = UNSET
    object_type: None | str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    parents: list[UUID] | None | Unset = UNSET
    permissions: list[str] | None | Unset = UNSET
    position: int | None | Unset = UNSET
    project_id: None | Unset | UUID = UNSET
    status: CollectionBaseSchemaStatusType1 | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.collection_base_schema_custom_order_status_type_1 import (
            CollectionBaseSchemaCustomOrderStatusType1,
        )
        from ..models.collection_base_schema_metadata_type_0 import (
            CollectionBaseSchemaMetadataType0,
        )
        from ..models.collection_base_schema_status_type_1 import (
            CollectionBaseSchemaStatusType1,
        )

        title = self.title

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

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

        custom_order_status: dict[str, Any] | None | Unset
        if isinstance(self.custom_order_status, Unset):
            custom_order_status = UNSET
        elif isinstance(
            self.custom_order_status, CollectionBaseSchemaCustomOrderStatusType1
        ):
            custom_order_status = self.custom_order_status.to_dict()
        else:
            custom_order_status = self.custom_order_status

        custom_poster: None | str | Unset
        if isinstance(self.custom_poster, Unset):
            custom_poster = UNSET
        elif isinstance(self.custom_poster, UUID):
            custom_poster = str(self.custom_poster)
        else:
            custom_poster = self.custom_poster

        deleted_by_user: None | str | Unset
        if isinstance(self.deleted_by_user, Unset):
            deleted_by_user = UNSET
        elif isinstance(self.deleted_by_user, UUID):
            deleted_by_user = str(self.deleted_by_user)
        else:
            deleted_by_user = self.deleted_by_user

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        favoured: bool | None | Unset
        if isinstance(self.favoured, Unset):
            favoured = UNSET
        else:
            favoured = self.favoured

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        in_collections: list[str] | None | Unset
        if isinstance(self.in_collections, Unset):
            in_collections = UNSET
        elif isinstance(self.in_collections, list):
            in_collections = []
            for in_collections_type_0_item_data in self.in_collections:
                in_collections_type_0_item = str(in_collections_type_0_item_data)
                in_collections.append(in_collections_type_0_item)

        else:
            in_collections = self.in_collections

        is_root: bool | None | Unset
        if isinstance(self.is_root, Unset):
            is_root = UNSET
        else:
            is_root = self.is_root

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

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CollectionBaseSchemaMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        parents: list[str] | None | Unset
        if isinstance(self.parents, Unset):
            parents = UNSET
        elif isinstance(self.parents, list):
            parents = []
            for parents_type_0_item_data in self.parents:
                parents_type_0_item = str(parents_type_0_item_data)
                parents.append(parents_type_0_item)

        else:
            parents = self.parents

        permissions: list[str] | None | Unset
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = self.permissions

        else:
            permissions = self.permissions

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, CollectionBaseSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

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
        from ..models.collection_base_schema_custom_order_status_type_1 import (
            CollectionBaseSchemaCustomOrderStatusType1,
        )
        from ..models.collection_base_schema_keyframes_type_0_item import (
            CollectionBaseSchemaKeyframesType0Item,
        )
        from ..models.collection_base_schema_metadata_type_0 import (
            CollectionBaseSchemaMetadataType0,
        )
        from ..models.collection_base_schema_status_type_1 import (
            CollectionBaseSchemaStatusType1,
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

        def _parse_custom_order_status(
            data: object,
        ) -> CollectionBaseSchemaCustomOrderStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_order_status_type_1 = (
                    CollectionBaseSchemaCustomOrderStatusType1.from_dict(data)
                )

                return custom_order_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CollectionBaseSchemaCustomOrderStatusType1 | None | Unset, data)

        custom_order_status = _parse_custom_order_status(
            d.pop("custom_order_status", UNSET)
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

        def _parse_deleted_by_user(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_by_user_type_0 = UUID(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_favoured(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        favoured = _parse_favoured(d.pop("favoured", UNSET))

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

        def _parse_in_collections(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                in_collections_type_0 = []
                _in_collections_type_0 = data
                for in_collections_type_0_item_data in _in_collections_type_0:
                    in_collections_type_0_item = UUID(in_collections_type_0_item_data)

                    in_collections_type_0.append(in_collections_type_0_item)

                return in_collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        in_collections = _parse_in_collections(d.pop("in_collections", UNSET))

        def _parse_is_root(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_root = _parse_is_root(d.pop("is_root", UNSET))

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
        ) -> list[CollectionBaseSchemaKeyframesType0Item] | None | Unset:
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
                    keyframes_type_0_item = (
                        CollectionBaseSchemaKeyframesType0Item.from_dict(
                            keyframes_type_0_item_data
                        )
                    )

                    keyframes_type_0.append(keyframes_type_0_item)

                return keyframes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CollectionBaseSchemaKeyframesType0Item] | None | Unset, data
            )

        keyframes = _parse_keyframes(d.pop("keyframes", UNSET))

        def _parse_metadata(
            data: object,
        ) -> CollectionBaseSchemaMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CollectionBaseSchemaMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CollectionBaseSchemaMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

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

        def _parse_parents(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parents_type_0 = []
                _parents_type_0 = data
                for parents_type_0_item_data in _parents_type_0:
                    parents_type_0_item = UUID(parents_type_0_item_data)

                    parents_type_0.append(parents_type_0_item)

                return parents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        parents = _parse_parents(d.pop("parents", UNSET))

        def _parse_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = cast(list[str], data)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

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

        def _parse_status(
            data: object,
        ) -> CollectionBaseSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = CollectionBaseSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CollectionBaseSchemaStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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
