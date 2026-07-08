from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iconik_storage_gateway_cluster_read_schema_status_type_1 import (
        IconikStorageGatewayClusterReadSchemaStatusType1,
    )
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
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        description (None | str | Unset):
        id (None | Unset | UUID):
        leader_changed_at (datetime.datetime | None | Unset):
        leader_id (None | Unset | UUID): Last reported leader ID.
        nodes (list[IconikStorageGatewayRead] | None | Unset):
        settings (ISGConfigClusterSettingsSchema | None | Unset): Application configuration settings as key-value pairs
        status (IconikStorageGatewayClusterReadSchemaStatusType1 | None | Unset):
        total_files_number (int | None | Unset): Total number of files
        transcode_queue_total (int | None | Unset): Total number of scheduled transcode jobs
        uploads_queue_total (int | None | Unset): Total number of scheduled auto-uploads
        visibility_timeout (int | None | Unset): The number of seconds jobs should remain invisible to other nodes
            Default: 3600.
    """

    db_connection_uri: str
    enabled: bool
    name: str
    storage_ids: list[UUID]
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    leader_changed_at: datetime.datetime | None | Unset = UNSET
    leader_id: None | Unset | UUID = UNSET
    nodes: list[IconikStorageGatewayRead] | None | Unset = UNSET
    settings: ISGConfigClusterSettingsSchema | None | Unset = UNSET
    status: IconikStorageGatewayClusterReadSchemaStatusType1 | None | Unset = UNSET
    total_files_number: int | None | Unset = UNSET
    transcode_queue_total: int | None | Unset = UNSET
    uploads_queue_total: int | None | Unset = UNSET
    visibility_timeout: int | None | Unset = 3600
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.iconik_storage_gateway_cluster_read_schema_status_type_1 import (
            IconikStorageGatewayClusterReadSchemaStatusType1,
        )
        from ..models.isg_config_cluster_settings_schema import (
            ISGConfigClusterSettingsSchema,
        )

        db_connection_uri = self.db_connection_uri

        enabled = self.enabled

        name = self.name

        storage_ids = []
        for storage_ids_item_data in self.storage_ids:
            storage_ids_item = str(storage_ids_item_data)
            storage_ids.append(storage_ids_item)

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        leader_changed_at: None | str | Unset
        if isinstance(self.leader_changed_at, Unset):
            leader_changed_at = UNSET
        elif isinstance(self.leader_changed_at, datetime.datetime):
            leader_changed_at = self.leader_changed_at.isoformat()
        else:
            leader_changed_at = self.leader_changed_at

        leader_id: None | str | Unset
        if isinstance(self.leader_id, Unset):
            leader_id = UNSET
        elif isinstance(self.leader_id, UUID):
            leader_id = str(self.leader_id)
        else:
            leader_id = self.leader_id

        nodes: list[dict[str, Any]] | None | Unset
        if isinstance(self.nodes, Unset):
            nodes = UNSET
        elif isinstance(self.nodes, list):
            nodes = []
            for nodes_type_0_item_data in self.nodes:
                nodes_type_0_item = nodes_type_0_item_data.to_dict()
                nodes.append(nodes_type_0_item)

        else:
            nodes = self.nodes

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, ISGConfigClusterSettingsSchema):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, IconikStorageGatewayClusterReadSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        total_files_number: int | None | Unset
        if isinstance(self.total_files_number, Unset):
            total_files_number = UNSET
        else:
            total_files_number = self.total_files_number

        transcode_queue_total: int | None | Unset
        if isinstance(self.transcode_queue_total, Unset):
            transcode_queue_total = UNSET
        else:
            transcode_queue_total = self.transcode_queue_total

        uploads_queue_total: int | None | Unset
        if isinstance(self.uploads_queue_total, Unset):
            uploads_queue_total = UNSET
        else:
            uploads_queue_total = self.uploads_queue_total

        visibility_timeout: int | None | Unset
        if isinstance(self.visibility_timeout, Unset):
            visibility_timeout = UNSET
        else:
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
        from ..models.iconik_storage_gateway_cluster_read_schema_status_type_1 import (
            IconikStorageGatewayClusterReadSchemaStatusType1,
        )
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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_leader_changed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                leader_changed_at_type_0 = datetime.datetime.fromisoformat(data)

                return leader_changed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        leader_changed_at = _parse_leader_changed_at(d.pop("leader_changed_at", UNSET))

        def _parse_leader_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                leader_id_type_0 = UUID(data)

                return leader_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        leader_id = _parse_leader_id(d.pop("leader_id", UNSET))

        def _parse_nodes(data: object) -> list[IconikStorageGatewayRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nodes_type_0 = []
                _nodes_type_0 = data
                for nodes_type_0_item_data in _nodes_type_0:
                    nodes_type_0_item = IconikStorageGatewayRead.from_dict(
                        nodes_type_0_item_data
                    )

                    nodes_type_0.append(nodes_type_0_item)

                return nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IconikStorageGatewayRead] | None | Unset, data)

        nodes = _parse_nodes(d.pop("nodes", UNSET))

        def _parse_settings(
            data: object,
        ) -> ISGConfigClusterSettingsSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_1 = ISGConfigClusterSettingsSchema.from_dict(data)

                return settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ISGConfigClusterSettingsSchema | None | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        def _parse_status(
            data: object,
        ) -> IconikStorageGatewayClusterReadSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = (
                    IconikStorageGatewayClusterReadSchemaStatusType1.from_dict(data)
                )

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                IconikStorageGatewayClusterReadSchemaStatusType1 | None | Unset, data
            )

        status = _parse_status(d.pop("status", UNSET))

        def _parse_total_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_files_number = _parse_total_files_number(
            d.pop("total_files_number", UNSET)
        )

        def _parse_transcode_queue_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        transcode_queue_total = _parse_transcode_queue_total(
            d.pop("transcode_queue_total", UNSET)
        )

        def _parse_uploads_queue_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        uploads_queue_total = _parse_uploads_queue_total(
            d.pop("uploads_queue_total", UNSET)
        )

        def _parse_visibility_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        visibility_timeout = _parse_visibility_timeout(
            d.pop("visibility_timeout", UNSET)
        )

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
