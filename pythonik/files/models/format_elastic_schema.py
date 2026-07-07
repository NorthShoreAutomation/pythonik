from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.format_elastic_schema_archive_status import (
    FormatElasticSchemaArchiveStatus,
)
from ..models.format_elastic_schema_status import FormatElasticSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_schema import ComponentSchema
    from ..models.external_references import ExternalReferences
    from ..models.format_elastic_schema_metadata_item import (
        FormatElasticSchemaMetadataItem,
    )


T = TypeVar("T", bound="FormatElasticSchema")


@_attrs_define
class FormatElasticSchema:
    """
    Attributes:
        name (str):
        archive_status (FormatElasticSchemaArchiveStatus | Unset):
        asset_id (UUID | Unset):
        components (list[ComponentSchema] | Unset):
        date_created (datetime.datetime | Unset):
        date_deleted (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        deleted_by_user (UUID | Unset):
        external_references (list[ExternalReferences] | Unset):
        id (UUID | Unset):
        is_online (bool | Unset):
        metadata (list[FormatElasticSchemaMetadataItem] | Unset): Sequence cannot have more than 10000. Excess values
            will be stripped
        status (FormatElasticSchemaStatus | Unset):
        storage_methods (list[str] | Unset):
        user_id (UUID | Unset):
        version_id (UUID | Unset):
        warnings (list[str] | Unset):
    """

    name: str
    archive_status: FormatElasticSchemaArchiveStatus | Unset = UNSET
    asset_id: UUID | Unset = UNSET
    components: list[ComponentSchema] | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_deleted: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    deleted_by_user: UUID | Unset = UNSET
    external_references: list[ExternalReferences] | Unset = UNSET
    id: UUID | Unset = UNSET
    is_online: bool | Unset = UNSET
    metadata: list[FormatElasticSchemaMetadataItem] | Unset = UNSET
    status: FormatElasticSchemaStatus | Unset = UNSET
    storage_methods: list[str] | Unset = UNSET
    user_id: UUID | Unset = UNSET
    version_id: UUID | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        archive_status: str | Unset = UNSET
        if not isinstance(self.archive_status, Unset):
            archive_status = self.archive_status.value

        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_deleted: str | Unset = UNSET
        if not isinstance(self.date_deleted, Unset):
            date_deleted = self.date_deleted.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        deleted_by_user: str | Unset = UNSET
        if not isinstance(self.deleted_by_user, Unset):
            deleted_by_user = str(self.deleted_by_user)

        external_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_references, Unset):
            external_references = []
            for external_references_item_data in self.external_references:
                external_references_item = external_references_item_data.to_dict()
                external_references.append(external_references_item)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_online = self.is_online

        metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()
                metadata.append(metadata_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_methods: list[str] | Unset = UNSET
        if not isinstance(self.storage_methods, Unset):
            storage_methods = self.storage_methods

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
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
        from ..models.format_elastic_schema_metadata_item import (
            FormatElasticSchemaMetadataItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _archive_status = d.pop("archive_status", UNSET)
        archive_status: FormatElasticSchemaArchiveStatus | Unset
        if isinstance(_archive_status, Unset):
            archive_status = UNSET
        else:
            archive_status = FormatElasticSchemaArchiveStatus(_archive_status)

        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        _components = d.pop("components", UNSET)
        components: list[ComponentSchema] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = ComponentSchema.from_dict(components_item_data)

                components.append(components_item)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_deleted = d.pop("date_deleted", UNSET)
        date_deleted: datetime.datetime | Unset
        if isinstance(_date_deleted, Unset):
            date_deleted = UNSET
        else:
            date_deleted = datetime.datetime.fromisoformat(_date_deleted)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        _deleted_by_user = d.pop("deleted_by_user", UNSET)
        deleted_by_user: UUID | Unset
        if isinstance(_deleted_by_user, Unset):
            deleted_by_user = UNSET
        else:
            deleted_by_user = UUID(_deleted_by_user)

        _external_references = d.pop("external_references", UNSET)
        external_references: list[ExternalReferences] | Unset = UNSET
        if _external_references is not UNSET:
            external_references = []
            for external_references_item_data in _external_references:
                external_references_item = ExternalReferences.from_dict(
                    external_references_item_data
                )

                external_references.append(external_references_item)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_online = d.pop("is_online", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: list[FormatElasticSchemaMetadataItem] | Unset = UNSET
        if _metadata is not UNSET:
            metadata = []
            for metadata_item_data in _metadata:
                metadata_item = FormatElasticSchemaMetadataItem.from_dict(
                    metadata_item_data
                )

                metadata.append(metadata_item)

        _status = d.pop("status", UNSET)
        status: FormatElasticSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FormatElasticSchemaStatus(_status)

        storage_methods = cast(list[str], d.pop("storage_methods", UNSET))

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        format_elastic_schema = cls(
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

        format_elastic_schema.additional_properties = d
        return format_elastic_schema

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
