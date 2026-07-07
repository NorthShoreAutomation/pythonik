from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_action_callback_schema_metadata_values import (
        CustomActionCallbackSchemaMetadataValues,
    )


T = TypeVar("T", bound="CustomActionCallbackSchema")


@_attrs_define
class CustomActionCallbackSchema:
    """
    Attributes:
        asset_ids (list[UUID] | Unset):
        collection_ids (list[UUID] | Unset):
        from_collection_id (None | Unset | UUID): ID of a collection that the custom action was triggered from
        metadata_values (CustomActionCallbackSchemaMetadataValues | Unset):
        metadata_view_id (None | Unset | UUID):
        playlist_ids (list[UUID] | Unset):
        saved_search_ids (list[UUID] | Unset):
    """

    asset_ids: list[UUID] | Unset = UNSET
    collection_ids: list[UUID] | Unset = UNSET
    from_collection_id: None | Unset | UUID = UNSET
    metadata_values: CustomActionCallbackSchemaMetadataValues | Unset = UNSET
    metadata_view_id: None | Unset | UUID = UNSET
    playlist_ids: list[UUID] | Unset = UNSET
    saved_search_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids: list[str] | Unset = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = []
            for asset_ids_item_data in self.asset_ids:
                asset_ids_item = str(asset_ids_item_data)
                asset_ids.append(asset_ids_item)

        collection_ids: list[str] | Unset = UNSET
        if not isinstance(self.collection_ids, Unset):
            collection_ids = []
            for collection_ids_item_data in self.collection_ids:
                collection_ids_item = str(collection_ids_item_data)
                collection_ids.append(collection_ids_item)

        from_collection_id: None | str | Unset
        if isinstance(self.from_collection_id, Unset):
            from_collection_id = UNSET
        elif isinstance(self.from_collection_id, UUID):
            from_collection_id = str(self.from_collection_id)
        else:
            from_collection_id = self.from_collection_id

        metadata_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_values, Unset):
            metadata_values = self.metadata_values.to_dict()

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        elif isinstance(self.metadata_view_id, UUID):
            metadata_view_id = str(self.metadata_view_id)
        else:
            metadata_view_id = self.metadata_view_id

        playlist_ids: list[str] | Unset = UNSET
        if not isinstance(self.playlist_ids, Unset):
            playlist_ids = []
            for playlist_ids_item_data in self.playlist_ids:
                playlist_ids_item = str(playlist_ids_item_data)
                playlist_ids.append(playlist_ids_item)

        saved_search_ids: list[str] | Unset = UNSET
        if not isinstance(self.saved_search_ids, Unset):
            saved_search_ids = []
            for saved_search_ids_item_data in self.saved_search_ids:
                saved_search_ids_item = str(saved_search_ids_item_data)
                saved_search_ids.append(saved_search_ids_item)

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
        from ..models.custom_action_callback_schema_metadata_values import (
            CustomActionCallbackSchemaMetadataValues,
        )

        d = dict(src_dict)
        _asset_ids = d.pop("asset_ids", UNSET)
        asset_ids: list[UUID] | Unset = UNSET
        if _asset_ids is not UNSET:
            asset_ids = []
            for asset_ids_item_data in _asset_ids:
                asset_ids_item = UUID(asset_ids_item_data)

                asset_ids.append(asset_ids_item)

        _collection_ids = d.pop("collection_ids", UNSET)
        collection_ids: list[UUID] | Unset = UNSET
        if _collection_ids is not UNSET:
            collection_ids = []
            for collection_ids_item_data in _collection_ids:
                collection_ids_item = UUID(collection_ids_item_data)

                collection_ids.append(collection_ids_item)

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

        _metadata_values = d.pop("metadata_values", UNSET)
        metadata_values: CustomActionCallbackSchemaMetadataValues | Unset
        if isinstance(_metadata_values, Unset):
            metadata_values = UNSET
        else:
            metadata_values = CustomActionCallbackSchemaMetadataValues.from_dict(
                _metadata_values
            )

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

        _playlist_ids = d.pop("playlist_ids", UNSET)
        playlist_ids: list[UUID] | Unset = UNSET
        if _playlist_ids is not UNSET:
            playlist_ids = []
            for playlist_ids_item_data in _playlist_ids:
                playlist_ids_item = UUID(playlist_ids_item_data)

                playlist_ids.append(playlist_ids_item)

        _saved_search_ids = d.pop("saved_search_ids", UNSET)
        saved_search_ids: list[UUID] | Unset = UNSET
        if _saved_search_ids is not UNSET:
            saved_search_ids = []
            for saved_search_ids_item_data in _saved_search_ids:
                saved_search_ids_item = UUID(saved_search_ids_item_data)

                saved_search_ids.append(saved_search_ids_item)

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
