from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_context import SourceContext


T = TypeVar("T", bound="ArchiveCollectionRequestSchema")


@_attrs_define
class ArchiveCollectionRequestSchema:
    """
    Attributes:
        id (UUID): ID of the object to transfer.
        all_versions (bool | Unset):  Default: False.
        delete_only_from_source (bool | Unset):  Default: False.
        delete_only_from_source_context (SourceContext | Unset):
        delete_original (bool | Unset):  Default: False.
        destination_directory_path (None | str | Unset):
        formats (list[str] | Unset): List of format names to transfer. If not specified, all formats will be
            transferred.
        keep_collection_structure (bool | Unset): Whether to keep the collection structure when archiving collections.
            Default: False.
        keep_parent_collection_structure (bool | Unset): Whether to keep the parent collection structure when archiving
            collections. Default: False.
        preferred_original_storage_id (None | Unset | UUID):
    """

    id: UUID
    all_versions: bool | Unset = False
    delete_only_from_source: bool | Unset = False
    delete_only_from_source_context: SourceContext | Unset = UNSET
    delete_original: bool | Unset = False
    destination_directory_path: None | str | Unset = UNSET
    formats: list[str] | Unset = UNSET
    keep_collection_structure: bool | Unset = False
    keep_parent_collection_structure: bool | Unset = False
    preferred_original_storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        all_versions = self.all_versions

        delete_only_from_source = self.delete_only_from_source

        delete_only_from_source_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_only_from_source_context, Unset):
            delete_only_from_source_context = (
                self.delete_only_from_source_context.to_dict()
            )

        delete_original = self.delete_original

        destination_directory_path: None | str | Unset
        if isinstance(self.destination_directory_path, Unset):
            destination_directory_path = UNSET
        else:
            destination_directory_path = self.destination_directory_path

        formats: list[str] | Unset = UNSET
        if not isinstance(self.formats, Unset):
            formats = self.formats

        keep_collection_structure = self.keep_collection_structure

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
                "id": id,
            }
        )
        if all_versions is not UNSET:
            field_dict["all_versions"] = all_versions
        if delete_only_from_source is not UNSET:
            field_dict["delete_only_from_source"] = delete_only_from_source
        if delete_only_from_source_context is not UNSET:
            field_dict["delete_only_from_source_context"] = (
                delete_only_from_source_context
            )
        if delete_original is not UNSET:
            field_dict["delete_original"] = delete_original
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if formats is not UNSET:
            field_dict["formats"] = formats
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
        from ..models.source_context import SourceContext

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        all_versions = d.pop("all_versions", UNSET)

        delete_only_from_source = d.pop("delete_only_from_source", UNSET)

        _delete_only_from_source_context = d.pop(
            "delete_only_from_source_context", UNSET
        )
        delete_only_from_source_context: SourceContext | Unset
        if isinstance(_delete_only_from_source_context, Unset):
            delete_only_from_source_context = UNSET
        else:
            delete_only_from_source_context = SourceContext.from_dict(
                _delete_only_from_source_context
            )

        delete_original = d.pop("delete_original", UNSET)

        def _parse_destination_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_directory_path = _parse_destination_directory_path(
            d.pop("destination_directory_path", UNSET)
        )

        formats = cast(list[str], d.pop("formats", UNSET))

        keep_collection_structure = d.pop("keep_collection_structure", UNSET)

        keep_parent_collection_structure = d.pop(
            "keep_parent_collection_structure", UNSET
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

        archive_collection_request_schema = cls(
            id=id,
            all_versions=all_versions,
            delete_only_from_source=delete_only_from_source,
            delete_only_from_source_context=delete_only_from_source_context,
            delete_original=delete_original,
            destination_directory_path=destination_directory_path,
            formats=formats,
            keep_collection_structure=keep_collection_structure,
            keep_parent_collection_structure=keep_parent_collection_structure,
            preferred_original_storage_id=preferred_original_storage_id,
        )

        archive_collection_request_schema.additional_properties = d
        return archive_collection_request_schema

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
