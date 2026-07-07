from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_usage_schema_storage import CurrentUsageSchemaStorage
    from ..models.current_usage_schema_users import CurrentUsageSchemaUsers


T = TypeVar("T", bound="CurrentUsageSchema")


@_attrs_define
class CurrentUsageSchema:
    """
    Attributes:
        automation_runs (int | Unset):
        edge_transcoders (int | Unset):
        external_storage (int | Unset):
        images_analyzed (int | Unset):
        images_face_recognition (int | Unset):
        shield_enabled (bool | Unset):
        storage (CurrentUsageSchemaStorage | Unset):
        storage_gateway_clusters (int | Unset):
        storage_gateway_nodes (int | Unset):
        transcription_hours (float | Unset):
        users (CurrentUsageSchemaUsers | Unset):
        video_analyzed_hours (float | Unset):
        video_face_recognition_hours (float | Unset):
    """

    automation_runs: int | Unset = UNSET
    edge_transcoders: int | Unset = UNSET
    external_storage: int | Unset = UNSET
    images_analyzed: int | Unset = UNSET
    images_face_recognition: int | Unset = UNSET
    shield_enabled: bool | Unset = UNSET
    storage: CurrentUsageSchemaStorage | Unset = UNSET
    storage_gateway_clusters: int | Unset = UNSET
    storage_gateway_nodes: int | Unset = UNSET
    transcription_hours: float | Unset = UNSET
    users: CurrentUsageSchemaUsers | Unset = UNSET
    video_analyzed_hours: float | Unset = UNSET
    video_face_recognition_hours: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation_runs = self.automation_runs

        edge_transcoders = self.edge_transcoders

        external_storage = self.external_storage

        images_analyzed = self.images_analyzed

        images_face_recognition = self.images_face_recognition

        shield_enabled = self.shield_enabled

        storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage.to_dict()

        storage_gateway_clusters = self.storage_gateway_clusters

        storage_gateway_nodes = self.storage_gateway_nodes

        transcription_hours = self.transcription_hours

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        video_analyzed_hours = self.video_analyzed_hours

        video_face_recognition_hours = self.video_face_recognition_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automation_runs is not UNSET:
            field_dict["automation_runs"] = automation_runs
        if edge_transcoders is not UNSET:
            field_dict["edge_transcoders"] = edge_transcoders
        if external_storage is not UNSET:
            field_dict["external_storage"] = external_storage
        if images_analyzed is not UNSET:
            field_dict["images_analyzed"] = images_analyzed
        if images_face_recognition is not UNSET:
            field_dict["images_face_recognition"] = images_face_recognition
        if shield_enabled is not UNSET:
            field_dict["shield_enabled"] = shield_enabled
        if storage is not UNSET:
            field_dict["storage"] = storage
        if storage_gateway_clusters is not UNSET:
            field_dict["storage_gateway_clusters"] = storage_gateway_clusters
        if storage_gateway_nodes is not UNSET:
            field_dict["storage_gateway_nodes"] = storage_gateway_nodes
        if transcription_hours is not UNSET:
            field_dict["transcription_hours"] = transcription_hours
        if users is not UNSET:
            field_dict["users"] = users
        if video_analyzed_hours is not UNSET:
            field_dict["video_analyzed_hours"] = video_analyzed_hours
        if video_face_recognition_hours is not UNSET:
            field_dict["video_face_recognition_hours"] = video_face_recognition_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_usage_schema_storage import CurrentUsageSchemaStorage
        from ..models.current_usage_schema_users import CurrentUsageSchemaUsers

        d = dict(src_dict)
        automation_runs = d.pop("automation_runs", UNSET)

        edge_transcoders = d.pop("edge_transcoders", UNSET)

        external_storage = d.pop("external_storage", UNSET)

        images_analyzed = d.pop("images_analyzed", UNSET)

        images_face_recognition = d.pop("images_face_recognition", UNSET)

        shield_enabled = d.pop("shield_enabled", UNSET)

        _storage = d.pop("storage", UNSET)
        storage: CurrentUsageSchemaStorage | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = CurrentUsageSchemaStorage.from_dict(_storage)

        storage_gateway_clusters = d.pop("storage_gateway_clusters", UNSET)

        storage_gateway_nodes = d.pop("storage_gateway_nodes", UNSET)

        transcription_hours = d.pop("transcription_hours", UNSET)

        _users = d.pop("users", UNSET)
        users: CurrentUsageSchemaUsers | Unset
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = CurrentUsageSchemaUsers.from_dict(_users)

        video_analyzed_hours = d.pop("video_analyzed_hours", UNSET)

        video_face_recognition_hours = d.pop("video_face_recognition_hours", UNSET)

        current_usage_schema = cls(
            automation_runs=automation_runs,
            edge_transcoders=edge_transcoders,
            external_storage=external_storage,
            images_analyzed=images_analyzed,
            images_face_recognition=images_face_recognition,
            shield_enabled=shield_enabled,
            storage=storage,
            storage_gateway_clusters=storage_gateway_clusters,
            storage_gateway_nodes=storage_gateway_nodes,
            transcription_hours=transcription_hours,
            users=users,
            video_analyzed_hours=video_analyzed_hours,
            video_face_recognition_hours=video_face_recognition_hours,
        )

        current_usage_schema.additional_properties = d
        return current_usage_schema

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
