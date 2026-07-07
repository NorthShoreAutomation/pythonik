from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_collection_metadata_update_schema_callback_data_request_type_0 import (
        BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0,
    )
    from ..models.bulk_collection_metadata_update_schema_callback_data_type_0 import (
        BulkCollectionMetadataUpdateSchemaCallbackDataType0,
    )


T = TypeVar("T", bound="BulkCollectionMetadataUpdateSchema")


@_attrs_define
class BulkCollectionMetadataUpdateSchema:
    """
    Attributes:
        collection_ids (list[UUID]):
        include_assets (bool):
        include_collections (bool):
        job_id (UUID):
        callback_chunk_size (int | Unset):
        callback_data (BulkCollectionMetadataUpdateSchemaCallbackDataType0 | None | Unset):
        callback_data_request (BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0 | None | Unset):
        callback_url (str | Unset):
    """

    collection_ids: list[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID
    callback_chunk_size: int | Unset = UNSET
    callback_data: (
        BulkCollectionMetadataUpdateSchemaCallbackDataType0 | None | Unset
    ) = UNSET
    callback_data_request: (
        BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0 | None | Unset
    ) = UNSET
    callback_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_collection_metadata_update_schema_callback_data_request_type_0 import (
            BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0,
        )
        from ..models.bulk_collection_metadata_update_schema_callback_data_type_0 import (
            BulkCollectionMetadataUpdateSchemaCallbackDataType0,
        )

        collection_ids = []
        for collection_ids_item_data in self.collection_ids:
            collection_ids_item = str(collection_ids_item_data)
            collection_ids.append(collection_ids_item)

        include_assets = self.include_assets

        include_collections = self.include_collections

        job_id = str(self.job_id)

        callback_chunk_size = self.callback_chunk_size

        callback_data: dict[str, Any] | None | Unset
        if isinstance(self.callback_data, Unset):
            callback_data = UNSET
        elif isinstance(
            self.callback_data, BulkCollectionMetadataUpdateSchemaCallbackDataType0
        ):
            callback_data = self.callback_data.to_dict()
        else:
            callback_data = self.callback_data

        callback_data_request: dict[str, Any] | None | Unset
        if isinstance(self.callback_data_request, Unset):
            callback_data_request = UNSET
        elif isinstance(
            self.callback_data_request,
            BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0,
        ):
            callback_data_request = self.callback_data_request.to_dict()
        else:
            callback_data_request = self.callback_data_request

        callback_url = self.callback_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_ids": collection_ids,
                "include_assets": include_assets,
                "include_collections": include_collections,
                "job_id": job_id,
            }
        )
        if callback_chunk_size is not UNSET:
            field_dict["callback_chunk_size"] = callback_chunk_size
        if callback_data is not UNSET:
            field_dict["callback_data"] = callback_data
        if callback_data_request is not UNSET:
            field_dict["callback_data_request"] = callback_data_request
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_collection_metadata_update_schema_callback_data_request_type_0 import (
            BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0,
        )
        from ..models.bulk_collection_metadata_update_schema_callback_data_type_0 import (
            BulkCollectionMetadataUpdateSchemaCallbackDataType0,
        )

        d = dict(src_dict)
        collection_ids = []
        _collection_ids = d.pop("collection_ids")
        for collection_ids_item_data in _collection_ids:
            collection_ids_item = UUID(collection_ids_item_data)

            collection_ids.append(collection_ids_item)

        include_assets = d.pop("include_assets")

        include_collections = d.pop("include_collections")

        job_id = UUID(d.pop("job_id"))

        callback_chunk_size = d.pop("callback_chunk_size", UNSET)

        def _parse_callback_data(
            data: object,
        ) -> BulkCollectionMetadataUpdateSchemaCallbackDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_data_type_0 = (
                    BulkCollectionMetadataUpdateSchemaCallbackDataType0.from_dict(data)
                )

                return callback_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BulkCollectionMetadataUpdateSchemaCallbackDataType0 | None | Unset, data
            )

        callback_data = _parse_callback_data(d.pop("callback_data", UNSET))

        def _parse_callback_data_request(
            data: object,
        ) -> BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_data_request_type_0 = BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0.from_dict(
                    data
                )

                return callback_data_request_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BulkCollectionMetadataUpdateSchemaCallbackDataRequestType0
                | None
                | Unset,
                data,
            )

        callback_data_request = _parse_callback_data_request(
            d.pop("callback_data_request", UNSET)
        )

        callback_url = d.pop("callback_url", UNSET)

        bulk_collection_metadata_update_schema = cls(
            collection_ids=collection_ids,
            include_assets=include_assets,
            include_collections=include_collections,
            job_id=job_id,
            callback_chunk_size=callback_chunk_size,
            callback_data=callback_data,
            callback_data_request=callback_data_request,
            callback_url=callback_url,
        )

        bulk_collection_metadata_update_schema.additional_properties = d
        return bulk_collection_metadata_update_schema

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
