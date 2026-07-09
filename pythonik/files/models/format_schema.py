from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.format_schema_archive_status import FormatSchemaArchiveStatus
from ..models.format_schema_status import FormatSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_schema import ComponentSchema
    from ..models.external_references import ExternalReferences
    from ..models.format_schema_metadata_type_0_item import (
        FormatSchemaMetadataType0Item,
    )


T = TypeVar("T", bound="FormatSchema")


@_attrs_define
class FormatSchema:
    """
    Attributes:
        name (str):
        archive_status (FormatSchemaArchiveStatus | None | Unset):
        asset_id (None | Unset | UUID):
        components (list[ComponentSchema] | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_deleted (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        deleted_by_user (None | Unset | UUID):
        external_references (list[ExternalReferences] | None | Unset):
        id (None | Unset | UUID):
        is_online (bool | None | Unset):
        metadata (list[FormatSchemaMetadataType0Item] | None | Unset): Sequence cannot have more than 10000. Excess
            values will be stripped
        status (FormatSchemaStatus | None | Unset):
        storage_methods (list[str] | None | Unset):
        user_id (None | Unset | UUID):
        version_id (None | Unset | UUID):
        warnings (list[str] | None | Unset):
    """

    name: str
    archive_status: FormatSchemaArchiveStatus | None | Unset = UNSET
    asset_id: None | Unset | UUID = UNSET
    components: list[ComponentSchema] | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_deleted: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    deleted_by_user: None | Unset | UUID = UNSET
    external_references: list[ExternalReferences] | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_online: bool | None | Unset = UNSET
    metadata: list[FormatSchemaMetadataType0Item] | None | Unset = UNSET
    status: FormatSchemaStatus | None | Unset = UNSET
    storage_methods: list[str] | None | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    version_id: None | Unset | UUID = UNSET
    warnings: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        archive_status: None | str | Unset
        if isinstance(self.archive_status, Unset):
            archive_status = UNSET
        elif isinstance(self.archive_status, FormatSchemaArchiveStatus):
            archive_status = self.archive_status.value
        else:
            archive_status = self.archive_status

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        components: list[dict[str, Any]] | None | Unset
        if isinstance(self.components, Unset):
            components = UNSET
        elif isinstance(self.components, list):
            components = []
            for components_type_0_item_data in self.components:
                components_type_0_item = components_type_0_item_data.to_dict()
                components.append(components_type_0_item)

        else:
            components = self.components

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_deleted: None | str | Unset
        if isinstance(self.date_deleted, Unset):
            date_deleted = UNSET
        elif isinstance(self.date_deleted, datetime.datetime):
            date_deleted = self.date_deleted.isoformat()
        else:
            date_deleted = self.date_deleted

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        deleted_by_user: None | str | Unset
        if isinstance(self.deleted_by_user, Unset):
            deleted_by_user = UNSET
        elif isinstance(self.deleted_by_user, UUID):
            deleted_by_user = str(self.deleted_by_user)
        else:
            deleted_by_user = self.deleted_by_user

        external_references: list[dict[str, Any]] | None | Unset
        if isinstance(self.external_references, Unset):
            external_references = UNSET
        elif isinstance(self.external_references, list):
            external_references = []
            for external_references_type_0_item_data in self.external_references:
                external_references_type_0_item = (
                    external_references_type_0_item_data.to_dict()
                )
                external_references.append(external_references_type_0_item)

        else:
            external_references = self.external_references

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_online: bool | None | Unset
        if isinstance(self.is_online, Unset):
            is_online = UNSET
        else:
            is_online = self.is_online

        metadata: list[dict[str, Any]] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, list):
            metadata = []
            for metadata_type_0_item_data in self.metadata:
                metadata_type_0_item = metadata_type_0_item_data.to_dict()
                metadata.append(metadata_type_0_item)

        else:
            metadata = self.metadata

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, FormatSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        storage_methods: list[str] | None | Unset
        if isinstance(self.storage_methods, Unset):
            storage_methods = UNSET
        elif isinstance(self.storage_methods, list):
            storage_methods = self.storage_methods

        else:
            storage_methods = self.storage_methods

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if archive_status is not UNSET:
            field_dict["archive_status"] = archive_status
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if components is not UNSET:
            field_dict["components"] = components
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_deleted is not UNSET:
            field_dict["date_deleted"] = date_deleted
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if deleted_by_user is not UNSET:
            field_dict["deleted_by_user"] = deleted_by_user
        if external_references is not UNSET:
            field_dict["external_references"] = external_references
        if id is not UNSET:
            field_dict["id"] = id
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status is not UNSET:
            field_dict["status"] = status
        if storage_methods is not UNSET:
            field_dict["storage_methods"] = storage_methods
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if version_id is not UNSET:
            field_dict["version_id"] = version_id
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.component_schema import ComponentSchema
        from ..models.external_references import ExternalReferences
        from ..models.format_schema_metadata_type_0_item import (
            FormatSchemaMetadataType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_archive_status(
            data: object,
        ) -> FormatSchemaArchiveStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archive_status_type_1 = FormatSchemaArchiveStatus(data)

                return archive_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormatSchemaArchiveStatus | None | Unset, data)

        archive_status = _parse_archive_status(d.pop("archive_status", UNSET))

        def _parse_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_id_type_0 = UUID(data)

                return asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_components(data: object) -> list[ComponentSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                components_type_0 = []
                _components_type_0 = data
                for components_type_0_item_data in _components_type_0:
                    components_type_0_item = ComponentSchema.from_dict(
                        components_type_0_item_data
                    )

                    components_type_0.append(components_type_0_item)

                return components_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComponentSchema] | None | Unset, data)

        components = _parse_components(d.pop("components", UNSET))

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

        def _parse_date_deleted(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_deleted_type_0 = datetime.datetime.fromisoformat(data)

                return date_deleted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_deleted = _parse_date_deleted(d.pop("date_deleted", UNSET))

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

        def _parse_external_references(
            data: object,
        ) -> list[ExternalReferences] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_references_type_0 = []
                _external_references_type_0 = data
                for external_references_type_0_item_data in _external_references_type_0:
                    external_references_type_0_item = ExternalReferences.from_dict(
                        external_references_type_0_item_data
                    )

                    external_references_type_0.append(external_references_type_0_item)

                return external_references_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalReferences] | None | Unset, data)

        external_references = _parse_external_references(
            d.pop("external_references", UNSET)
        )

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

        def _parse_is_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_online = _parse_is_online(d.pop("is_online", UNSET))

        def _parse_metadata(
            data: object,
        ) -> list[FormatSchemaMetadataType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_type_0 = []
                _metadata_type_0 = data
                for metadata_type_0_item_data in _metadata_type_0:
                    metadata_type_0_item = FormatSchemaMetadataType0Item.from_dict(
                        metadata_type_0_item_data
                    )

                    metadata_type_0.append(metadata_type_0_item)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FormatSchemaMetadataType0Item] | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_status(data: object) -> FormatSchemaStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = FormatSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormatSchemaStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_storage_methods(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                storage_methods_type_0 = cast(list[str], data)

                return storage_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        storage_methods = _parse_storage_methods(d.pop("storage_methods", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        format_schema = cls(
            name=name,
            archive_status=archive_status,
            asset_id=asset_id,
            components=components,
            date_created=date_created,
            date_deleted=date_deleted,
            date_modified=date_modified,
            deleted_by_user=deleted_by_user,
            external_references=external_references,
            id=id,
            is_online=is_online,
            metadata=metadata,
            status=status,
            storage_methods=storage_methods,
            user_id=user_id,
            version_id=version_id,
            warnings=warnings,
        )

        format_schema.additional_properties = d
        return format_schema

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
