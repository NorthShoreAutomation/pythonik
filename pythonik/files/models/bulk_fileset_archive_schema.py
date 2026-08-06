from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_fileset_archive_schema_object_type import (
    BulkFilesetArchiveSchemaObjectType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkFilesetArchiveSchema")


@_attrs_define
class BulkFilesetArchiveSchema:
    """
    Attributes:
        object_ids (list[UUID]):
        object_type (BulkFilesetArchiveSchemaObjectType):
        allow_duplicate_transfers (bool | None | Unset):  Default: False.
        delete_only_from_source_folder (bool | None | Unset):  Default: False.
        delete_original (bool | None | Unset):  Default: False.
        destination_directory_path (None | str | Unset):
        destination_storage_id (None | str | Unset):
        keep_collection_structure (bool | None | Unset):  Default: False.
        keep_parent_collection_structure (bool | None | Unset):  Default: False.
        preferred_original_storage_id (None | Unset | UUID):
    """

    object_ids: list[UUID]
    object_type: BulkFilesetArchiveSchemaObjectType
    allow_duplicate_transfers: bool | None | Unset = False
    delete_only_from_source_folder: bool | None | Unset = False
    delete_original: bool | None | Unset = False
    destination_directory_path: None | str | Unset = UNSET
    destination_storage_id: None | str | Unset = UNSET
    keep_collection_structure: bool | None | Unset = False
    keep_parent_collection_structure: bool | None | Unset = False
    preferred_original_storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        object_type = self.object_type.value

        allow_duplicate_transfers: bool | None | Unset
        if isinstance(self.allow_duplicate_transfers, Unset):
            allow_duplicate_transfers = UNSET
        else:
            allow_duplicate_transfers = self.allow_duplicate_transfers

        delete_only_from_source_folder: bool | None | Unset
        if isinstance(self.delete_only_from_source_folder, Unset):
            delete_only_from_source_folder = UNSET
        else:
            delete_only_from_source_folder = self.delete_only_from_source_folder

        delete_original: bool | None | Unset
        if isinstance(self.delete_original, Unset):
            delete_original = UNSET
        else:
            delete_original = self.delete_original

        destination_directory_path: None | str | Unset
        if isinstance(self.destination_directory_path, Unset):
            destination_directory_path = UNSET
        else:
            destination_directory_path = self.destination_directory_path

        destination_storage_id: None | str | Unset
        if isinstance(self.destination_storage_id, Unset):
            destination_storage_id = UNSET
        else:
            destination_storage_id = self.destination_storage_id

        keep_collection_structure: bool | None | Unset
        if isinstance(self.keep_collection_structure, Unset):
            keep_collection_structure = UNSET
        else:
            keep_collection_structure = self.keep_collection_structure

        keep_parent_collection_structure: bool | None | Unset
        if isinstance(self.keep_parent_collection_structure, Unset):
            keep_parent_collection_structure = UNSET
        else:
            keep_parent_collection_structure = self.keep_parent_collection_structure

        preferred_original_storage_id: None | str | Unset
        if isinstance(self.preferred_original_storage_id, Unset):
            preferred_original_storage_id = UNSET
        elif isinstance(self.preferred_original_storage_id, UUID):
            preferred_original_storage_id = str(self.preferred_original_storage_id)
        else:
            preferred_original_storage_id = self.preferred_original_storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids": object_ids,
                "object_type": object_type,
            }
        )
        if allow_duplicate_transfers is not UNSET:
            field_dict["allow_duplicate_transfers"] = allow_duplicate_transfers
        if delete_only_from_source_folder is not UNSET:
            field_dict["delete_only_from_source_folder"] = (
                delete_only_from_source_folder
            )
        if delete_original is not UNSET:
            field_dict["delete_original"] = delete_original
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if destination_storage_id is not UNSET:
            field_dict["destination_storage_id"] = destination_storage_id
        if keep_collection_structure is not UNSET:
            field_dict["keep_collection_structure"] = keep_collection_structure
        if keep_parent_collection_structure is not UNSET:
            field_dict["keep_parent_collection_structure"] = (
                keep_parent_collection_structure
            )
        if preferred_original_storage_id is not UNSET:
            field_dict["preferred_original_storage_id"] = preferred_original_storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

        object_type = BulkFilesetArchiveSchemaObjectType(d.pop("object_type"))

        def _parse_allow_duplicate_transfers(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_duplicate_transfers = _parse_allow_duplicate_transfers(
            d.pop("allow_duplicate_transfers", UNSET)
        )

        def _parse_delete_only_from_source_folder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_only_from_source_folder = _parse_delete_only_from_source_folder(
            d.pop("delete_only_from_source_folder", UNSET)
        )

        def _parse_delete_original(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_original = _parse_delete_original(d.pop("delete_original", UNSET))

        def _parse_destination_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_directory_path = _parse_destination_directory_path(
            d.pop("destination_directory_path", UNSET)
        )

        def _parse_destination_storage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_storage_id = _parse_destination_storage_id(
            d.pop("destination_storage_id", UNSET)
        )

        def _parse_keep_collection_structure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_collection_structure = _parse_keep_collection_structure(
            d.pop("keep_collection_structure", UNSET)
        )

        def _parse_keep_parent_collection_structure(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_parent_collection_structure = _parse_keep_parent_collection_structure(
            d.pop("keep_parent_collection_structure", UNSET)
        )

        def _parse_preferred_original_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_original_storage_id_type_0 = UUID(data)

                return preferred_original_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        preferred_original_storage_id = _parse_preferred_original_storage_id(
            d.pop("preferred_original_storage_id", UNSET)
        )

        bulk_fileset_archive_schema = cls(
            object_ids=object_ids,
            object_type=object_type,
            allow_duplicate_transfers=allow_duplicate_transfers,
            delete_only_from_source_folder=delete_only_from_source_folder,
            delete_original=delete_original,
            destination_directory_path=destination_directory_path,
            destination_storage_id=destination_storage_id,
            keep_collection_structure=keep_collection_structure,
            keep_parent_collection_structure=keep_parent_collection_structure,
            preferred_original_storage_id=preferred_original_storage_id,
        )

        bulk_fileset_archive_schema.additional_properties = d
        return bulk_fileset_archive_schema

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
