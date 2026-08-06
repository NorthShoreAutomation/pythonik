from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_action_callback_schema_metadata_values_type_0 import (
        CustomActionCallbackSchemaMetadataValuesType0,
    )


T = TypeVar("T", bound="CustomActionCallbackSchema")


@_attrs_define
class CustomActionCallbackSchema:
    """
    Attributes:
        asset_ids (list[UUID] | None | Unset):
        collection_ids (list[UUID] | None | Unset):
        from_collection_id (None | Unset | UUID): ID of a collection that the custom action was triggered from
        metadata_values (CustomActionCallbackSchemaMetadataValuesType0 | None | Unset):
        metadata_view_id (None | Unset | UUID):
        playlist_ids (list[UUID] | None | Unset):
        saved_search_ids (list[UUID] | None | Unset):
    """

    asset_ids: list[UUID] | None | Unset = UNSET
    collection_ids: list[UUID] | None | Unset = UNSET
    from_collection_id: None | Unset | UUID = UNSET
    metadata_values: CustomActionCallbackSchemaMetadataValuesType0 | None | Unset = (
        UNSET
    )
    metadata_view_id: None | Unset | UUID = UNSET
    playlist_ids: list[UUID] | None | Unset = UNSET
    saved_search_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_action_callback_schema_metadata_values_type_0 import (
            CustomActionCallbackSchemaMetadataValuesType0,
        )

        asset_ids: list[str] | None | Unset
        if isinstance(self.asset_ids, Unset):
            asset_ids = UNSET
        elif isinstance(self.asset_ids, list):
            asset_ids = []
            for asset_ids_type_0_item_data in self.asset_ids:
                asset_ids_type_0_item = str(asset_ids_type_0_item_data)
                asset_ids.append(asset_ids_type_0_item)

        else:
            asset_ids = self.asset_ids

        collection_ids: list[str] | None | Unset
        if isinstance(self.collection_ids, Unset):
            collection_ids = UNSET
        elif isinstance(self.collection_ids, list):
            collection_ids = []
            for collection_ids_type_0_item_data in self.collection_ids:
                collection_ids_type_0_item = str(collection_ids_type_0_item_data)
                collection_ids.append(collection_ids_type_0_item)

        else:
            collection_ids = self.collection_ids

        from_collection_id: None | str | Unset
        if isinstance(self.from_collection_id, Unset):
            from_collection_id = UNSET
        elif isinstance(self.from_collection_id, UUID):
            from_collection_id = str(self.from_collection_id)
        else:
            from_collection_id = self.from_collection_id

        metadata_values: dict[str, Any] | None | Unset
        if isinstance(self.metadata_values, Unset):
            metadata_values = UNSET
        elif isinstance(
            self.metadata_values, CustomActionCallbackSchemaMetadataValuesType0
        ):
            metadata_values = self.metadata_values.to_dict()
        else:
            metadata_values = self.metadata_values

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        elif isinstance(self.metadata_view_id, UUID):
            metadata_view_id = str(self.metadata_view_id)
        else:
            metadata_view_id = self.metadata_view_id

        playlist_ids: list[str] | None | Unset
        if isinstance(self.playlist_ids, Unset):
            playlist_ids = UNSET
        elif isinstance(self.playlist_ids, list):
            playlist_ids = []
            for playlist_ids_type_0_item_data in self.playlist_ids:
                playlist_ids_type_0_item = str(playlist_ids_type_0_item_data)
                playlist_ids.append(playlist_ids_type_0_item)

        else:
            playlist_ids = self.playlist_ids

        saved_search_ids: list[str] | None | Unset
        if isinstance(self.saved_search_ids, Unset):
            saved_search_ids = UNSET
        elif isinstance(self.saved_search_ids, list):
            saved_search_ids = []
            for saved_search_ids_type_0_item_data in self.saved_search_ids:
                saved_search_ids_type_0_item = str(saved_search_ids_type_0_item_data)
                saved_search_ids.append(saved_search_ids_type_0_item)

        else:
            saved_search_ids = self.saved_search_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_ids is not UNSET:
            field_dict["asset_ids"] = asset_ids
        if collection_ids is not UNSET:
            field_dict["collection_ids"] = collection_ids
        if from_collection_id is not UNSET:
            field_dict["from_collection_id"] = from_collection_id
        if metadata_values is not UNSET:
            field_dict["metadata_values"] = metadata_values
        if metadata_view_id is not UNSET:
            field_dict["metadata_view_id"] = metadata_view_id
        if playlist_ids is not UNSET:
            field_dict["playlist_ids"] = playlist_ids
        if saved_search_ids is not UNSET:
            field_dict["saved_search_ids"] = saved_search_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_action_callback_schema_metadata_values_type_0 import (
            CustomActionCallbackSchemaMetadataValuesType0,
        )

        d = dict(src_dict)

        def _parse_asset_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_ids_type_0 = []
                _asset_ids_type_0 = data
                for asset_ids_type_0_item_data in _asset_ids_type_0:
                    asset_ids_type_0_item = UUID(asset_ids_type_0_item_data)

                    asset_ids_type_0.append(asset_ids_type_0_item)

                return asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        asset_ids = _parse_asset_ids(d.pop("asset_ids", UNSET))

        def _parse_collection_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collection_ids_type_0 = []
                _collection_ids_type_0 = data
                for collection_ids_type_0_item_data in _collection_ids_type_0:
                    collection_ids_type_0_item = UUID(collection_ids_type_0_item_data)

                    collection_ids_type_0.append(collection_ids_type_0_item)

                return collection_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        collection_ids = _parse_collection_ids(d.pop("collection_ids", UNSET))

        def _parse_from_collection_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_collection_id_type_0 = UUID(data)

                return from_collection_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        from_collection_id = _parse_from_collection_id(
            d.pop("from_collection_id", UNSET)
        )

        def _parse_metadata_values(
            data: object,
        ) -> CustomActionCallbackSchemaMetadataValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_values_type_0 = (
                    CustomActionCallbackSchemaMetadataValuesType0.from_dict(data)
                )

                return metadata_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CustomActionCallbackSchemaMetadataValuesType0 | None | Unset, data
            )

        metadata_values = _parse_metadata_values(d.pop("metadata_values", UNSET))

        def _parse_metadata_view_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_view_id_type_0 = UUID(data)

                return metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        metadata_view_id = _parse_metadata_view_id(d.pop("metadata_view_id", UNSET))

        def _parse_playlist_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                playlist_ids_type_0 = []
                _playlist_ids_type_0 = data
                for playlist_ids_type_0_item_data in _playlist_ids_type_0:
                    playlist_ids_type_0_item = UUID(playlist_ids_type_0_item_data)

                    playlist_ids_type_0.append(playlist_ids_type_0_item)

                return playlist_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        playlist_ids = _parse_playlist_ids(d.pop("playlist_ids", UNSET))

        def _parse_saved_search_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                saved_search_ids_type_0 = []
                _saved_search_ids_type_0 = data
                for saved_search_ids_type_0_item_data in _saved_search_ids_type_0:
                    saved_search_ids_type_0_item = UUID(
                        saved_search_ids_type_0_item_data
                    )

                    saved_search_ids_type_0.append(saved_search_ids_type_0_item)

                return saved_search_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        saved_search_ids = _parse_saved_search_ids(d.pop("saved_search_ids", UNSET))

        custom_action_callback_schema = cls(
            asset_ids=asset_ids,
            collection_ids=collection_ids,
            from_collection_id=from_collection_id,
            metadata_values=metadata_values,
            metadata_view_id=metadata_view_id,
            playlist_ids=playlist_ids,
            saved_search_ids=saved_search_ids,
        )

        custom_action_callback_schema.additional_properties = d
        return custom_action_callback_schema

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
