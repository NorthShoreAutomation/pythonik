from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_usage_schema_storage_type_0 import (
        CurrentUsageSchemaStorageType0,
    )
    from ..models.current_usage_schema_users_type_0 import CurrentUsageSchemaUsersType0


T = TypeVar("T", bound="CurrentUsageSchema")


@_attrs_define
class CurrentUsageSchema:
    """
    Attributes:
        automation_runs (int | None | Unset):
        edge_transcoders (int | None | Unset):
        external_storage (int | None | Unset):
        images_analyzed (int | None | Unset):
        images_face_recognition (int | None | Unset):
        shield_enabled (bool | None | Unset):
        storage (CurrentUsageSchemaStorageType0 | None | Unset):
        storage_gateway_clusters (int | None | Unset):
        storage_gateway_nodes (int | None | Unset):
        transcription_hours (float | None | Unset):
        users (CurrentUsageSchemaUsersType0 | None | Unset):
        video_analyzed_hours (float | None | Unset):
        video_face_recognition_hours (float | None | Unset):
    """

    automation_runs: int | None | Unset = UNSET
    edge_transcoders: int | None | Unset = UNSET
    external_storage: int | None | Unset = UNSET
    images_analyzed: int | None | Unset = UNSET
    images_face_recognition: int | None | Unset = UNSET
    shield_enabled: bool | None | Unset = UNSET
    storage: CurrentUsageSchemaStorageType0 | None | Unset = UNSET
    storage_gateway_clusters: int | None | Unset = UNSET
    storage_gateway_nodes: int | None | Unset = UNSET
    transcription_hours: float | None | Unset = UNSET
    users: CurrentUsageSchemaUsersType0 | None | Unset = UNSET
    video_analyzed_hours: float | None | Unset = UNSET
    video_face_recognition_hours: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.current_usage_schema_storage_type_0 import (
            CurrentUsageSchemaStorageType0,
        )
        from ..models.current_usage_schema_users_type_0 import (
            CurrentUsageSchemaUsersType0,
        )

        automation_runs: int | None | Unset
        if isinstance(self.automation_runs, Unset):
            automation_runs = UNSET
        else:
            automation_runs = self.automation_runs

        edge_transcoders: int | None | Unset
        if isinstance(self.edge_transcoders, Unset):
            edge_transcoders = UNSET
        else:
            edge_transcoders = self.edge_transcoders

        external_storage: int | None | Unset
        if isinstance(self.external_storage, Unset):
            external_storage = UNSET
        else:
            external_storage = self.external_storage

        images_analyzed: int | None | Unset
        if isinstance(self.images_analyzed, Unset):
            images_analyzed = UNSET
        else:
            images_analyzed = self.images_analyzed

        images_face_recognition: int | None | Unset
        if isinstance(self.images_face_recognition, Unset):
            images_face_recognition = UNSET
        else:
            images_face_recognition = self.images_face_recognition

        shield_enabled: bool | None | Unset
        if isinstance(self.shield_enabled, Unset):
            shield_enabled = UNSET
        else:
            shield_enabled = self.shield_enabled

        storage: dict[str, Any] | None | Unset
        if isinstance(self.storage, Unset):
            storage = UNSET
        elif isinstance(self.storage, CurrentUsageSchemaStorageType0):
            storage = self.storage.to_dict()
        else:
            storage = self.storage

        storage_gateway_clusters: int | None | Unset
        if isinstance(self.storage_gateway_clusters, Unset):
            storage_gateway_clusters = UNSET
        else:
            storage_gateway_clusters = self.storage_gateway_clusters

        storage_gateway_nodes: int | None | Unset
        if isinstance(self.storage_gateway_nodes, Unset):
            storage_gateway_nodes = UNSET
        else:
            storage_gateway_nodes = self.storage_gateway_nodes

        transcription_hours: float | None | Unset
        if isinstance(self.transcription_hours, Unset):
            transcription_hours = UNSET
        else:
            transcription_hours = self.transcription_hours

        users: dict[str, Any] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, CurrentUsageSchemaUsersType0):
            users = self.users.to_dict()
        else:
            users = self.users

        video_analyzed_hours: float | None | Unset
        if isinstance(self.video_analyzed_hours, Unset):
            video_analyzed_hours = UNSET
        else:
            video_analyzed_hours = self.video_analyzed_hours

        video_face_recognition_hours: float | None | Unset
        if isinstance(self.video_face_recognition_hours, Unset):
            video_face_recognition_hours = UNSET
        else:
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
        from ..models.current_usage_schema_storage_type_0 import (
            CurrentUsageSchemaStorageType0,
        )
        from ..models.current_usage_schema_users_type_0 import (
            CurrentUsageSchemaUsersType0,
        )

        d = dict(src_dict)

        def _parse_automation_runs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        automation_runs = _parse_automation_runs(d.pop("automation_runs", UNSET))

        def _parse_edge_transcoders(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge_transcoders = _parse_edge_transcoders(d.pop("edge_transcoders", UNSET))

        def _parse_external_storage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        external_storage = _parse_external_storage(d.pop("external_storage", UNSET))

        def _parse_images_analyzed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        images_analyzed = _parse_images_analyzed(d.pop("images_analyzed", UNSET))

        def _parse_images_face_recognition(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        images_face_recognition = _parse_images_face_recognition(
            d.pop("images_face_recognition", UNSET)
        )

        def _parse_shield_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        shield_enabled = _parse_shield_enabled(d.pop("shield_enabled", UNSET))

        def _parse_storage(
            data: object,
        ) -> CurrentUsageSchemaStorageType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                storage_type_0 = CurrentUsageSchemaStorageType0.from_dict(data)

                return storage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CurrentUsageSchemaStorageType0 | None | Unset, data)

        storage = _parse_storage(d.pop("storage", UNSET))

        def _parse_storage_gateway_clusters(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_gateway_clusters = _parse_storage_gateway_clusters(
            d.pop("storage_gateway_clusters", UNSET)
        )

        def _parse_storage_gateway_nodes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_gateway_nodes = _parse_storage_gateway_nodes(
            d.pop("storage_gateway_nodes", UNSET)
        )

        def _parse_transcription_hours(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        transcription_hours = _parse_transcription_hours(
            d.pop("transcription_hours", UNSET)
        )

        def _parse_users(data: object) -> CurrentUsageSchemaUsersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                users_type_0 = CurrentUsageSchemaUsersType0.from_dict(data)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CurrentUsageSchemaUsersType0 | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        def _parse_video_analyzed_hours(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_analyzed_hours = _parse_video_analyzed_hours(
            d.pop("video_analyzed_hours", UNSET)
        )

        def _parse_video_face_recognition_hours(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_face_recognition_hours = _parse_video_face_recognition_hours(
            d.pop("video_face_recognition_hours", UNSET)
        )

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
