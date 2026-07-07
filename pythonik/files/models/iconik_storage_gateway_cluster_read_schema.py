from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iconik_storage_gateway_cluster_read_schema_status import (
    IconikStorageGatewayClusterReadSchemaStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iconik_storage_gateway_read import IconikStorageGatewayRead
    from ..models.isg_config_cluster_settings_schema import (
        ISGConfigClusterSettingsSchema,
    )


T = TypeVar("T", bound="IconikStorageGatewayClusterReadSchema")


@_attrs_define
class IconikStorageGatewayClusterReadSchema:
    """
    Attributes:
        db_connection_uri (str): Database connection URI
        enabled (bool): Application toggle. If turned off ISG will enter idle state waiting to get enabled again.
        name (str):
        storage_ids (list[UUID]):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        id (UUID | Unset):
        leader_changed_at (datetime.datetime | Unset):
        leader_id (UUID | Unset): Last reported leader ID.
        nodes (list[IconikStorageGatewayRead] | Unset):
        settings (ISGConfigClusterSettingsSchema | Unset):
        status (IconikStorageGatewayClusterReadSchemaStatus | Unset):
        total_files_number (int | Unset): Total number of files
        transcode_queue_total (int | Unset): Total number of scheduled transcode jobs
        uploads_queue_total (int | Unset): Total number of scheduled auto-uploads
        visibility_timeout (int | Unset): The number of seconds jobs should remain invisible to other nodes Default:
            3600.
    """

    db_connection_uri: str
    enabled: bool
    name: str
    storage_ids: list[UUID]
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    leader_changed_at: datetime.datetime | Unset = UNSET
    leader_id: UUID | Unset = UNSET
    nodes: list[IconikStorageGatewayRead] | Unset = UNSET
    settings: ISGConfigClusterSettingsSchema | Unset = UNSET
    status: IconikStorageGatewayClusterReadSchemaStatus | Unset = UNSET
    total_files_number: int | Unset = UNSET
    transcode_queue_total: int | Unset = UNSET
    uploads_queue_total: int | Unset = UNSET
    visibility_timeout: int | Unset = 3600
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        db_connection_uri = self.db_connection_uri

        enabled = self.enabled

        name = self.name

        storage_ids = []
        for storage_ids_item_data in self.storage_ids:
            storage_ids_item = str(storage_ids_item_data)
            storage_ids.append(storage_ids_item)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        leader_changed_at: str | Unset = UNSET
        if not isinstance(self.leader_changed_at, Unset):
            leader_changed_at = self.leader_changed_at.isoformat()

        leader_id: str | Unset = UNSET
        if not isinstance(self.leader_id, Unset):
            leader_id = str(self.leader_id)

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        total_files_number = self.total_files_number

        transcode_queue_total = self.transcode_queue_total

        uploads_queue_total = self.uploads_queue_total

        visibility_timeout = self.visibility_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "db_connection_uri": db_connection_uri,
                "enabled": enabled,
                "name": name,
                "storage_ids": storage_ids,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if leader_changed_at is not UNSET:
            field_dict["leader_changed_at"] = leader_changed_at
        if leader_id is not UNSET:
            field_dict["leader_id"] = leader_id
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if settings is not UNSET:
            field_dict["settings"] = settings
        if status is not UNSET:
            field_dict["status"] = status
        if total_files_number is not UNSET:
            field_dict["total_files_number"] = total_files_number
        if transcode_queue_total is not UNSET:
            field_dict["transcode_queue_total"] = transcode_queue_total
        if uploads_queue_total is not UNSET:
            field_dict["uploads_queue_total"] = uploads_queue_total
        if visibility_timeout is not UNSET:
            field_dict["visibility_timeout"] = visibility_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iconik_storage_gateway_read import IconikStorageGatewayRead
        from ..models.isg_config_cluster_settings_schema import (
            ISGConfigClusterSettingsSchema,
        )

        d = dict(src_dict)
        db_connection_uri = d.pop("db_connection_uri")

        enabled = d.pop("enabled")

        name = d.pop("name")

        storage_ids = []
        _storage_ids = d.pop("storage_ids")
        for storage_ids_item_data in _storage_ids:
            storage_ids_item = UUID(storage_ids_item_data)

            storage_ids.append(storage_ids_item)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _leader_changed_at = d.pop("leader_changed_at", UNSET)
        leader_changed_at: datetime.datetime | Unset
        if isinstance(_leader_changed_at, Unset):
            leader_changed_at = UNSET
        else:
            leader_changed_at = datetime.datetime.fromisoformat(_leader_changed_at)

        _leader_id = d.pop("leader_id", UNSET)
        leader_id: UUID | Unset
        if isinstance(_leader_id, Unset):
            leader_id = UNSET
        else:
            leader_id = UUID(_leader_id)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[IconikStorageGatewayRead] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = IconikStorageGatewayRead.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        _settings = d.pop("settings", UNSET)
        settings: ISGConfigClusterSettingsSchema | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ISGConfigClusterSettingsSchema.from_dict(_settings)

        _status = d.pop("status", UNSET)
        status: IconikStorageGatewayClusterReadSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IconikStorageGatewayClusterReadSchemaStatus(_status)

        total_files_number = d.pop("total_files_number", UNSET)

        transcode_queue_total = d.pop("transcode_queue_total", UNSET)

        uploads_queue_total = d.pop("uploads_queue_total", UNSET)

        visibility_timeout = d.pop("visibility_timeout", UNSET)

        iconik_storage_gateway_cluster_read_schema = cls(
            db_connection_uri=db_connection_uri,
            enabled=enabled,
            name=name,
            storage_ids=storage_ids,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            id=id,
            leader_changed_at=leader_changed_at,
            leader_id=leader_id,
            nodes=nodes,
            settings=settings,
            status=status,
            total_files_number=total_files_number,
            transcode_queue_total=transcode_queue_total,
            uploads_queue_total=uploads_queue_total,
            visibility_timeout=visibility_timeout,
        )

        iconik_storage_gateway_cluster_read_schema.additional_properties = d
        return iconik_storage_gateway_cluster_read_schema

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
