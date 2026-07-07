from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingLimitsSchema")


@_attrs_define
class BillingLimitsSchema:
    """
    Attributes:
        ai_credits (int | None | Unset):
        ai_object_detection_hours (int | None | Unset):
        automation_tasks (int | None | Unset):
        browse_users (int | None | Unset):
        edge_transcoders (int | None | Unset):
        egress_gb (int | None | Unset):
        face_recognition_hours (int | None | Unset):
        face_recognition_images (int | None | Unset):
        image_recognition (int | None | Unset):
        max_storage_gateway_clusters (int | None | Unset):
        max_storage_gateway_nodes (int | None | Unset):
        multiregion_storage_gb (int | None | Unset):
        power_users (int | None | Unset):
        proxy_storage_gb (int | None | Unset):
        regional_storage_gb (int | None | Unset):
        shield_enabled (bool | None | Unset):
        standard_users (int | None | Unset):
        sync_session_max_clients (int | None | Unset):
        transcription_hours (int | None | Unset):
    """

    ai_credits: int | None | Unset = UNSET
    ai_object_detection_hours: int | None | Unset = UNSET
    automation_tasks: int | None | Unset = UNSET
    browse_users: int | None | Unset = UNSET
    edge_transcoders: int | None | Unset = UNSET
    egress_gb: int | None | Unset = UNSET
    face_recognition_hours: int | None | Unset = UNSET
    face_recognition_images: int | None | Unset = UNSET
    image_recognition: int | None | Unset = UNSET
    max_storage_gateway_clusters: int | None | Unset = UNSET
    max_storage_gateway_nodes: int | None | Unset = UNSET
    multiregion_storage_gb: int | None | Unset = UNSET
    power_users: int | None | Unset = UNSET
    proxy_storage_gb: int | None | Unset = UNSET
    regional_storage_gb: int | None | Unset = UNSET
    shield_enabled: bool | None | Unset = UNSET
    standard_users: int | None | Unset = UNSET
    sync_session_max_clients: int | None | Unset = UNSET
    transcription_hours: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ai_credits: int | None | Unset
        if isinstance(self.ai_credits, Unset):
            ai_credits = UNSET
        else:
            ai_credits = self.ai_credits

        ai_object_detection_hours: int | None | Unset
        if isinstance(self.ai_object_detection_hours, Unset):
            ai_object_detection_hours = UNSET
        else:
            ai_object_detection_hours = self.ai_object_detection_hours

        automation_tasks: int | None | Unset
        if isinstance(self.automation_tasks, Unset):
            automation_tasks = UNSET
        else:
            automation_tasks = self.automation_tasks

        browse_users: int | None | Unset
        if isinstance(self.browse_users, Unset):
            browse_users = UNSET
        else:
            browse_users = self.browse_users

        edge_transcoders: int | None | Unset
        if isinstance(self.edge_transcoders, Unset):
            edge_transcoders = UNSET
        else:
            edge_transcoders = self.edge_transcoders

        egress_gb: int | None | Unset
        if isinstance(self.egress_gb, Unset):
            egress_gb = UNSET
        else:
            egress_gb = self.egress_gb

        face_recognition_hours: int | None | Unset
        if isinstance(self.face_recognition_hours, Unset):
            face_recognition_hours = UNSET
        else:
            face_recognition_hours = self.face_recognition_hours

        face_recognition_images: int | None | Unset
        if isinstance(self.face_recognition_images, Unset):
            face_recognition_images = UNSET
        else:
            face_recognition_images = self.face_recognition_images

        image_recognition: int | None | Unset
        if isinstance(self.image_recognition, Unset):
            image_recognition = UNSET
        else:
            image_recognition = self.image_recognition

        max_storage_gateway_clusters: int | None | Unset
        if isinstance(self.max_storage_gateway_clusters, Unset):
            max_storage_gateway_clusters = UNSET
        else:
            max_storage_gateway_clusters = self.max_storage_gateway_clusters

        max_storage_gateway_nodes: int | None | Unset
        if isinstance(self.max_storage_gateway_nodes, Unset):
            max_storage_gateway_nodes = UNSET
        else:
            max_storage_gateway_nodes = self.max_storage_gateway_nodes

        multiregion_storage_gb: int | None | Unset
        if isinstance(self.multiregion_storage_gb, Unset):
            multiregion_storage_gb = UNSET
        else:
            multiregion_storage_gb = self.multiregion_storage_gb

        power_users: int | None | Unset
        if isinstance(self.power_users, Unset):
            power_users = UNSET
        else:
            power_users = self.power_users

        proxy_storage_gb: int | None | Unset
        if isinstance(self.proxy_storage_gb, Unset):
            proxy_storage_gb = UNSET
        else:
            proxy_storage_gb = self.proxy_storage_gb

        regional_storage_gb: int | None | Unset
        if isinstance(self.regional_storage_gb, Unset):
            regional_storage_gb = UNSET
        else:
            regional_storage_gb = self.regional_storage_gb

        shield_enabled: bool | None | Unset
        if isinstance(self.shield_enabled, Unset):
            shield_enabled = UNSET
        else:
            shield_enabled = self.shield_enabled

        standard_users: int | None | Unset
        if isinstance(self.standard_users, Unset):
            standard_users = UNSET
        else:
            standard_users = self.standard_users

        sync_session_max_clients: int | None | Unset
        if isinstance(self.sync_session_max_clients, Unset):
            sync_session_max_clients = UNSET
        else:
            sync_session_max_clients = self.sync_session_max_clients

        transcription_hours: int | None | Unset
        if isinstance(self.transcription_hours, Unset):
            transcription_hours = UNSET
        else:
            transcription_hours = self.transcription_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ai_credits is not UNSET:
            field_dict["ai_credits"] = ai_credits
        if ai_object_detection_hours is not UNSET:
            field_dict["ai_object_detection_hours"] = ai_object_detection_hours
        if automation_tasks is not UNSET:
            field_dict["automation_tasks"] = automation_tasks
        if browse_users is not UNSET:
            field_dict["browse_users"] = browse_users
        if edge_transcoders is not UNSET:
            field_dict["edge_transcoders"] = edge_transcoders
        if egress_gb is not UNSET:
            field_dict["egress_gb"] = egress_gb
        if face_recognition_hours is not UNSET:
            field_dict["face_recognition_hours"] = face_recognition_hours
        if face_recognition_images is not UNSET:
            field_dict["face_recognition_images"] = face_recognition_images
        if image_recognition is not UNSET:
            field_dict["image_recognition"] = image_recognition
        if max_storage_gateway_clusters is not UNSET:
            field_dict["max_storage_gateway_clusters"] = max_storage_gateway_clusters
        if max_storage_gateway_nodes is not UNSET:
            field_dict["max_storage_gateway_nodes"] = max_storage_gateway_nodes
        if multiregion_storage_gb is not UNSET:
            field_dict["multiregion_storage_gb"] = multiregion_storage_gb
        if power_users is not UNSET:
            field_dict["power_users"] = power_users
        if proxy_storage_gb is not UNSET:
            field_dict["proxy_storage_gb"] = proxy_storage_gb
        if regional_storage_gb is not UNSET:
            field_dict["regional_storage_gb"] = regional_storage_gb
        if shield_enabled is not UNSET:
            field_dict["shield_enabled"] = shield_enabled
        if standard_users is not UNSET:
            field_dict["standard_users"] = standard_users
        if sync_session_max_clients is not UNSET:
            field_dict["sync_session_max_clients"] = sync_session_max_clients
        if transcription_hours is not UNSET:
            field_dict["transcription_hours"] = transcription_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ai_credits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ai_credits = _parse_ai_credits(d.pop("ai_credits", UNSET))

        def _parse_ai_object_detection_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ai_object_detection_hours = _parse_ai_object_detection_hours(
            d.pop("ai_object_detection_hours", UNSET)
        )

        def _parse_automation_tasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        automation_tasks = _parse_automation_tasks(d.pop("automation_tasks", UNSET))

        def _parse_browse_users(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        browse_users = _parse_browse_users(d.pop("browse_users", UNSET))

        def _parse_edge_transcoders(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge_transcoders = _parse_edge_transcoders(d.pop("edge_transcoders", UNSET))

        def _parse_egress_gb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        egress_gb = _parse_egress_gb(d.pop("egress_gb", UNSET))

        def _parse_face_recognition_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        face_recognition_hours = _parse_face_recognition_hours(
            d.pop("face_recognition_hours", UNSET)
        )

        def _parse_face_recognition_images(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        face_recognition_images = _parse_face_recognition_images(
            d.pop("face_recognition_images", UNSET)
        )

        def _parse_image_recognition(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_recognition = _parse_image_recognition(d.pop("image_recognition", UNSET))

        def _parse_max_storage_gateway_clusters(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_storage_gateway_clusters = _parse_max_storage_gateway_clusters(
            d.pop("max_storage_gateway_clusters", UNSET)
        )

        def _parse_max_storage_gateway_nodes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_storage_gateway_nodes = _parse_max_storage_gateway_nodes(
            d.pop("max_storage_gateway_nodes", UNSET)
        )

        def _parse_multiregion_storage_gb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        multiregion_storage_gb = _parse_multiregion_storage_gb(
            d.pop("multiregion_storage_gb", UNSET)
        )

        def _parse_power_users(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        power_users = _parse_power_users(d.pop("power_users", UNSET))

        def _parse_proxy_storage_gb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proxy_storage_gb = _parse_proxy_storage_gb(d.pop("proxy_storage_gb", UNSET))

        def _parse_regional_storage_gb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        regional_storage_gb = _parse_regional_storage_gb(
            d.pop("regional_storage_gb", UNSET)
        )

        def _parse_shield_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        shield_enabled = _parse_shield_enabled(d.pop("shield_enabled", UNSET))

        def _parse_standard_users(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        standard_users = _parse_standard_users(d.pop("standard_users", UNSET))

        def _parse_sync_session_max_clients(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sync_session_max_clients = _parse_sync_session_max_clients(
            d.pop("sync_session_max_clients", UNSET)
        )

        def _parse_transcription_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        transcription_hours = _parse_transcription_hours(
            d.pop("transcription_hours", UNSET)
        )

        billing_limits_schema = cls(
            ai_credits=ai_credits,
            ai_object_detection_hours=ai_object_detection_hours,
            automation_tasks=automation_tasks,
            browse_users=browse_users,
            edge_transcoders=edge_transcoders,
            egress_gb=egress_gb,
            face_recognition_hours=face_recognition_hours,
            face_recognition_images=face_recognition_images,
            image_recognition=image_recognition,
            max_storage_gateway_clusters=max_storage_gateway_clusters,
            max_storage_gateway_nodes=max_storage_gateway_nodes,
            multiregion_storage_gb=multiregion_storage_gb,
            power_users=power_users,
            proxy_storage_gb=proxy_storage_gb,
            regional_storage_gb=regional_storage_gb,
            shield_enabled=shield_enabled,
            standard_users=standard_users,
            sync_session_max_clients=sync_session_max_clients,
            transcription_hours=transcription_hours,
        )

        billing_limits_schema.additional_properties = d
        return billing_limits_schema

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
