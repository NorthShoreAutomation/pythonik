from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_metadata_values_batch_schema_metadata_values import (
        CollectionMetadataValuesBatchSchemaMetadataValues,
    )


T = TypeVar("T", bound="CollectionMetadataValuesBatchSchema")


@_attrs_define
class CollectionMetadataValuesBatchSchema:
    """
    Attributes:
        include_assets (bool):
        include_collections (bool):
        metadata_values (CollectionMetadataValuesBatchSchemaMetadataValues):
        object_ids (list[UUID]):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        object_type (None | str | Unset):
    """

    include_assets: bool
    include_collections: bool
    metadata_values: CollectionMetadataValuesBatchSchemaMetadataValues
    object_ids: list[UUID]
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    object_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_assets = self.include_assets

        include_collections = self.include_collections

        metadata_values = self.metadata_values.to_dict()

        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

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

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "include_assets": include_assets,
                "include_collections": include_collections,
                "metadata_values": metadata_values,
                "object_ids": object_ids,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if object_type is not UNSET:
            field_dict["object_type"] = object_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_metadata_values_batch_schema_metadata_values import (
            CollectionMetadataValuesBatchSchemaMetadataValues,
        )

        d = dict(src_dict)
        include_assets = d.pop("include_assets")

        include_collections = d.pop("include_collections")

        metadata_values = CollectionMetadataValuesBatchSchemaMetadataValues.from_dict(
            d.pop("metadata_values")
        )

        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

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

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        collection_metadata_values_batch_schema = cls(
            include_assets=include_assets,
            include_collections=include_collections,
            metadata_values=metadata_values,
            object_ids=object_ids,
            date_created=date_created,
            date_modified=date_modified,
            object_type=object_type,
        )

        collection_metadata_values_batch_schema.additional_properties = d
        return collection_metadata_values_batch_schema

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
