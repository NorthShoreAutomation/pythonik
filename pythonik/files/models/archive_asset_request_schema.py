from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_context import SourceContext


T = TypeVar("T", bound="ArchiveAssetRequestSchema")


@_attrs_define
class ArchiveAssetRequestSchema:
    """
    Attributes:
        id (UUID): ID of the object to transfer.
        all_versions (bool | None | Unset):  Default: False.
        delete_only_from_source (bool | None | Unset):  Default: False.
        delete_only_from_source_context (None | SourceContext | Unset):
        delete_original (bool | None | Unset):  Default: False.
        destination_directory_path (None | str | Unset):
        formats (list[str] | None | Unset): List of format names to transfer. If not specified, all formats will be
            transferred.
        preferred_original_storage_id (None | Unset | UUID):
        version_ids (list[UUID] | None | Unset): List of version IDs to transfer.
    """

    id: UUID
    all_versions: bool | None | Unset = False
    delete_only_from_source: bool | None | Unset = False
    delete_only_from_source_context: None | SourceContext | Unset = UNSET
    delete_original: bool | None | Unset = False
    destination_directory_path: None | str | Unset = UNSET
    formats: list[str] | None | Unset = UNSET
    preferred_original_storage_id: None | Unset | UUID = UNSET
    version_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.source_context import SourceContext

        id = str(self.id)

        all_versions: bool | None | Unset
        if isinstance(self.all_versions, Unset):
            all_versions = UNSET
        else:
            all_versions = self.all_versions

        delete_only_from_source: bool | None | Unset
        if isinstance(self.delete_only_from_source, Unset):
            delete_only_from_source = UNSET
        else:
            delete_only_from_source = self.delete_only_from_source

        delete_only_from_source_context: dict[str, Any] | None | Unset
        if isinstance(self.delete_only_from_source_context, Unset):
            delete_only_from_source_context = UNSET
        elif isinstance(self.delete_only_from_source_context, SourceContext):
            delete_only_from_source_context = (
                self.delete_only_from_source_context.to_dict()
            )
        else:
            delete_only_from_source_context = self.delete_only_from_source_context

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

        formats: list[str] | None | Unset
        if isinstance(self.formats, Unset):
            formats = UNSET
        elif isinstance(self.formats, list):
            formats = self.formats

        else:
            formats = self.formats

        preferred_original_storage_id: None | str | Unset
        if isinstance(self.preferred_original_storage_id, Unset):
            preferred_original_storage_id = UNSET
        elif isinstance(self.preferred_original_storage_id, UUID):
            preferred_original_storage_id = str(self.preferred_original_storage_id)
        else:
            preferred_original_storage_id = self.preferred_original_storage_id

        version_ids: list[str] | None | Unset
        if isinstance(self.version_ids, Unset):
            version_ids = UNSET
        elif isinstance(self.version_ids, list):
            version_ids = []
            for version_ids_type_0_item_data in self.version_ids:
                version_ids_type_0_item = str(version_ids_type_0_item_data)
                version_ids.append(version_ids_type_0_item)

        else:
            version_ids = self.version_ids

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
        if preferred_original_storage_id is not UNSET:
            field_dict["preferred_original_storage_id"] = preferred_original_storage_id
        if version_ids is not UNSET:
            field_dict["version_ids"] = version_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_context import SourceContext

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_all_versions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_versions = _parse_all_versions(d.pop("all_versions", UNSET))

        def _parse_delete_only_from_source(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_only_from_source = _parse_delete_only_from_source(
            d.pop("delete_only_from_source", UNSET)
        )

        def _parse_delete_only_from_source_context(
            data: object,
        ) -> None | SourceContext | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                delete_only_from_source_context_type_1 = SourceContext.from_dict(data)

                return delete_only_from_source_context_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceContext | Unset, data)

        delete_only_from_source_context = _parse_delete_only_from_source_context(
            d.pop("delete_only_from_source_context", UNSET)
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

        def _parse_formats(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                formats_type_0 = cast(list[str], data)

                return formats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        formats = _parse_formats(d.pop("formats", UNSET))

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

        def _parse_version_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                version_ids_type_0 = []
                _version_ids_type_0 = data
                for version_ids_type_0_item_data in _version_ids_type_0:
                    version_ids_type_0_item = UUID(version_ids_type_0_item_data)

                    version_ids_type_0.append(version_ids_type_0_item)

                return version_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        version_ids = _parse_version_ids(d.pop("version_ids", UNSET))

        archive_asset_request_schema = cls(
            id=id,
            all_versions=all_versions,
            delete_only_from_source=delete_only_from_source,
            delete_only_from_source_context=delete_only_from_source_context,
            delete_original=delete_original,
            destination_directory_path=destination_directory_path,
            formats=formats,
            preferred_original_storage_id=preferred_original_storage_id,
            version_ids=version_ids,
        )

        archive_asset_request_schema.additional_properties = d
        return archive_asset_request_schema

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
