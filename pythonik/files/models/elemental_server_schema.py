from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElementalServerSchema")


@_attrs_define
class ElementalServerSchema:
    """
    Attributes:
        api_key (str):
        base_url (str):
        mount_point (str):
        profile (int):
        username (str):
        exclude_patterns (list[str] | Unset):
        include_patterns (list[str] | Unset):
        keyframe_map_output_group_order (int | Unset):
        keyframe_output_group_order (int | Unset):
        local (bool | Unset):
        priority (int | None | Unset):
        proxy_output_group_order (int | Unset):
    """

    api_key: str
    base_url: str
    mount_point: str
    profile: int
    username: str
    exclude_patterns: list[str] | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    keyframe_map_output_group_order: int | Unset = UNSET
    keyframe_output_group_order: int | Unset = UNSET
    local: bool | Unset = UNSET
    priority: int | None | Unset = UNSET
    proxy_output_group_order: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        base_url = self.base_url

        mount_point = self.mount_point

        profile = self.profile

        username = self.username

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        keyframe_map_output_group_order = self.keyframe_map_output_group_order

        keyframe_output_group_order = self.keyframe_output_group_order

        local = self.local

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        proxy_output_group_order = self.proxy_output_group_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key": api_key,
                "base_url": base_url,
                "mount_point": mount_point,
                "profile": profile,
                "username": username,
            }
        )
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if keyframe_map_output_group_order is not UNSET:
            field_dict["keyframe_map_output_group_order"] = (
                keyframe_map_output_group_order
            )
        if keyframe_output_group_order is not UNSET:
            field_dict["keyframe_output_group_order"] = keyframe_output_group_order
        if local is not UNSET:
            field_dict["local"] = local
        if priority is not UNSET:
            field_dict["priority"] = priority
        if proxy_output_group_order is not UNSET:
            field_dict["proxy_output_group_order"] = proxy_output_group_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("api_key")

        base_url = d.pop("base_url")

        mount_point = d.pop("mount_point")

        profile = d.pop("profile")

        username = d.pop("username")

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        keyframe_map_output_group_order = d.pop(
            "keyframe_map_output_group_order", UNSET
        )

        keyframe_output_group_order = d.pop("keyframe_output_group_order", UNSET)

        local = d.pop("local", UNSET)

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        proxy_output_group_order = d.pop("proxy_output_group_order", UNSET)

        elemental_server_schema = cls(
            api_key=api_key,
            base_url=base_url,
            mount_point=mount_point,
            profile=profile,
            username=username,
            exclude_patterns=exclude_patterns,
            include_patterns=include_patterns,
            keyframe_map_output_group_order=keyframe_map_output_group_order,
            keyframe_output_group_order=keyframe_output_group_order,
            local=local,
            priority=priority,
            proxy_output_group_order=proxy_output_group_order,
        )

        elemental_server_schema.additional_properties = d
        return elemental_server_schema

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
