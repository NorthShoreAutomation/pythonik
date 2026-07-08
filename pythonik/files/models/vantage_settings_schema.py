from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VantageSettingsSchema")


@_attrs_define
class VantageSettingsSchema:
    """
    Attributes:
        host (str):
        port (int):
        share_name (str):
        temp_proxy_folder (str):
        workflow_id (str):
        exclude_patterns (list[str] | None | Unset):
        include_patterns (list[str] | None | Unset):
        local (bool | None | Unset):
        priority (int | None | Unset):
    """

    host: str
    port: int
    share_name: str
    temp_proxy_folder: str
    workflow_id: str
    exclude_patterns: list[str] | None | Unset = UNSET
    include_patterns: list[str] | None | Unset = UNSET
    local: bool | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        share_name = self.share_name

        temp_proxy_folder = self.temp_proxy_folder

        workflow_id = self.workflow_id

        exclude_patterns: list[str] | None | Unset
        if isinstance(self.exclude_patterns, Unset):
            exclude_patterns = UNSET
        elif isinstance(self.exclude_patterns, list):
            exclude_patterns = self.exclude_patterns

        else:
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | None | Unset
        if isinstance(self.include_patterns, Unset):
            include_patterns = UNSET
        elif isinstance(self.include_patterns, list):
            include_patterns = self.include_patterns

        else:
            include_patterns = self.include_patterns

        local: bool | None | Unset
        if isinstance(self.local, Unset):
            local = UNSET
        else:
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
                "host": host,
                "port": port,
                "share_name": share_name,
                "temp_proxy_folder": temp_proxy_folder,
                "workflow_id": workflow_id,
            }
        )
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
        host = d.pop("host")

        port = d.pop("port")

        share_name = d.pop("share_name")

        temp_proxy_folder = d.pop("temp_proxy_folder")

        workflow_id = d.pop("workflow_id")

        def _parse_exclude_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_patterns_type_0 = cast(list[str], data)

                return exclude_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_patterns = _parse_exclude_patterns(d.pop("exclude_patterns", UNSET))

        def _parse_include_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_patterns_type_0 = cast(list[str], data)

                return include_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_patterns = _parse_include_patterns(d.pop("include_patterns", UNSET))

        def _parse_local(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        local = _parse_local(d.pop("local", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        vantage_settings_schema = cls(
            host=host,
            port=port,
            share_name=share_name,
            temp_proxy_folder=temp_proxy_folder,
            workflow_id=workflow_id,
            exclude_patterns=exclude_patterns,
            include_patterns=include_patterns,
            local=local,
            priority=priority,
        )

        vantage_settings_schema.additional_properties = d
        return vantage_settings_schema

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
