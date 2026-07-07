from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelestreamCloudSchema")


@_attrs_define
class TelestreamCloudSchema:
    """
    Attributes:
        access_key (str):
        factory_id (str):
        keyframes_profile_id (str):
        proxy_profile_id (str):
        secret_key (str):
        storage_id (str):
        api_host (str | Unset):
        api_port (int | Unset):
        exclude_patterns (list[str] | Unset):
        include_patterns (list[str] | Unset):
        local (bool | Unset):
        priority (int | None | Unset):
    """

    access_key: str
    factory_id: str
    keyframes_profile_id: str
    proxy_profile_id: str
    secret_key: str
    storage_id: str
    api_host: str | Unset = UNSET
    api_port: int | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    local: bool | Unset = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        factory_id = self.factory_id

        keyframes_profile_id = self.keyframes_profile_id

        proxy_profile_id = self.proxy_profile_id

        secret_key = self.secret_key

        storage_id = self.storage_id

        api_host = self.api_host

        api_port = self.api_port

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        local = self.local

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_key": access_key,
                "factory_id": factory_id,
                "keyframes_profile_id": keyframes_profile_id,
                "proxy_profile_id": proxy_profile_id,
                "secret_key": secret_key,
                "storage_id": storage_id,
            }
        )
        if api_host is not UNSET:
            field_dict["api_host"] = api_host
        if api_port is not UNSET:
            field_dict["api_port"] = api_port
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if local is not UNSET:
            field_dict["local"] = local
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("access_key")

        factory_id = d.pop("factory_id")

        keyframes_profile_id = d.pop("keyframes_profile_id")

        proxy_profile_id = d.pop("proxy_profile_id")

        secret_key = d.pop("secret_key")

        storage_id = d.pop("storage_id")

        api_host = d.pop("api_host", UNSET)

        api_port = d.pop("api_port", UNSET)

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        local = d.pop("local", UNSET)

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        telestream_cloud_schema = cls(
            access_key=access_key,
            factory_id=factory_id,
            keyframes_profile_id=keyframes_profile_id,
            proxy_profile_id=proxy_profile_id,
            secret_key=secret_key,
            storage_id=storage_id,
            api_host=api_host,
            api_port=api_port,
            exclude_patterns=exclude_patterns,
            include_patterns=include_patterns,
            local=local,
            priority=priority,
        )

        telestream_cloud_schema.additional_properties = d
        return telestream_cloud_schema

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
