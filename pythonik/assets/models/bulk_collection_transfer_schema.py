from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_collection_transfer_schema_callback_data_request_type_0 import (
        BulkCollectionTransferSchemaCallbackDataRequestType0,
    )
    from ..models.bulk_collection_transfer_schema_callback_data_type_0 import (
        BulkCollectionTransferSchemaCallbackDataType0,
    )


T = TypeVar("T", bound="BulkCollectionTransferSchema")


@_attrs_define
class BulkCollectionTransferSchema:
    """
    Attributes:
        collection_ids (list[UUID]):
        include_assets (bool):
        include_collections (bool):
        job_id (UUID):
        callback_chunk_size (int | Unset):
        callback_data (BulkCollectionTransferSchemaCallbackDataType0 | None | Unset):
        callback_data_request (BulkCollectionTransferSchemaCallbackDataRequestType0 | None | Unset):
        callback_url (str | Unset):
        destination_directory_path (str | Unset):
        keep_collection_structure (bool | Unset):
        keep_parent_collection_structure (bool | Unset):
    """

    collection_ids: list[UUID]
    include_assets: bool
    include_collections: bool
    job_id: UUID
    callback_chunk_size: int | Unset = UNSET
    callback_data: BulkCollectionTransferSchemaCallbackDataType0 | None | Unset = UNSET
    callback_data_request: (
        BulkCollectionTransferSchemaCallbackDataRequestType0 | None | Unset
    ) = UNSET
    callback_url: str | Unset = UNSET
    destination_directory_path: str | Unset = UNSET
    keep_collection_structure: bool | Unset = UNSET
    keep_parent_collection_structure: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_collection_transfer_schema_callback_data_request_type_0 import (
            BulkCollectionTransferSchemaCallbackDataRequestType0,
        )
        from ..models.bulk_collection_transfer_schema_callback_data_type_0 import (
            BulkCollectionTransferSchemaCallbackDataType0,
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
            self.callback_data, BulkCollectionTransferSchemaCallbackDataType0
        ):
            callback_data = self.callback_data.to_dict()
        else:
            callback_data = self.callback_data

        callback_data_request: dict[str, Any] | None | Unset
        if isinstance(self.callback_data_request, Unset):
            callback_data_request = UNSET
        elif isinstance(
            self.callback_data_request,
            BulkCollectionTransferSchemaCallbackDataRequestType0,
        ):
            callback_data_request = self.callback_data_request.to_dict()
        else:
            callback_data_request = self.callback_data_request

        callback_url = self.callback_url

        destination_directory_path = self.destination_directory_path

        keep_collection_structure = self.keep_collection_structure

        keep_parent_collection_structure = self.keep_parent_collection_structure

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
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if keep_collection_structure is not UNSET:
            field_dict["keep_collection_structure"] = keep_collection_structure
        if keep_parent_collection_structure is not UNSET:
            field_dict["keep_parent_collection_structure"] = (
                keep_parent_collection_structure
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_collection_transfer_schema_callback_data_request_type_0 import (
            BulkCollectionTransferSchemaCallbackDataRequestType0,
        )
        from ..models.bulk_collection_transfer_schema_callback_data_type_0 import (
            BulkCollectionTransferSchemaCallbackDataType0,
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
        ) -> BulkCollectionTransferSchemaCallbackDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_data_type_0 = (
                    BulkCollectionTransferSchemaCallbackDataType0.from_dict(data)
                )

                return callback_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BulkCollectionTransferSchemaCallbackDataType0 | None | Unset, data
            )

        callback_data = _parse_callback_data(d.pop("callback_data", UNSET))

        def _parse_callback_data_request(
            data: object,
        ) -> BulkCollectionTransferSchemaCallbackDataRequestType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_data_request_type_0 = (
                    BulkCollectionTransferSchemaCallbackDataRequestType0.from_dict(data)
                )

                return callback_data_request_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BulkCollectionTransferSchemaCallbackDataRequestType0 | None | Unset,
                data,
            )

        callback_data_request = _parse_callback_data_request(
            d.pop("callback_data_request", UNSET)
        )

        callback_url = d.pop("callback_url", UNSET)

        destination_directory_path = d.pop("destination_directory_path", UNSET)

        keep_collection_structure = d.pop("keep_collection_structure", UNSET)

        keep_parent_collection_structure = d.pop(
            "keep_parent_collection_structure", UNSET
        )

        bulk_collection_transfer_schema = cls(
            collection_ids=collection_ids,
            include_assets=include_assets,
            include_collections=include_collections,
            job_id=job_id,
            callback_chunk_size=callback_chunk_size,
            callback_data=callback_data,
            callback_data_request=callback_data_request,
            callback_url=callback_url,
            destination_directory_path=destination_directory_path,
            keep_collection_structure=keep_collection_structure,
            keep_parent_collection_structure=keep_parent_collection_structure,
        )

        bulk_collection_transfer_schema.additional_properties = d
        return bulk_collection_transfer_schema

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
