from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferStatsSchema")


@_attrs_define
class TransferStatsSchema:
    """
    Attributes:
        bytes_sent (int):
        ip (None | str | Unset):
        object_info (None | str | Unset):
        object_name (None | str | Unset):
        time_taken_us (int | None | Unset):
    """

    bytes_sent: int
    ip: None | str | Unset = UNSET
    object_info: None | str | Unset = UNSET
    object_name: None | str | Unset = UNSET
    time_taken_us: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_sent = self.bytes_sent

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        object_info: None | str | Unset
        if isinstance(self.object_info, Unset):
            object_info = UNSET
        else:
            object_info = self.object_info

        object_name: None | str | Unset
        if isinstance(self.object_name, Unset):
            object_name = UNSET
        else:
            object_name = self.object_name

        time_taken_us: int | None | Unset
        if isinstance(self.time_taken_us, Unset):
            time_taken_us = UNSET
        else:
            time_taken_us = self.time_taken_us

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bytes_sent": bytes_sent,
            }
        )
        if ip is not UNSET:
            field_dict["ip"] = ip
        if object_info is not UNSET:
            field_dict["object_info"] = object_info
        if object_name is not UNSET:
            field_dict["object_name"] = object_name
        if time_taken_us is not UNSET:
            field_dict["time_taken_us"] = time_taken_us

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_sent = d.pop("bytes_sent")

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        def _parse_object_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_info = _parse_object_info(d.pop("object_info", UNSET))

        def _parse_object_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_name = _parse_object_name(d.pop("object_name", UNSET))

        def _parse_time_taken_us(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_taken_us = _parse_time_taken_us(d.pop("time_taken_us", UNSET))

        transfer_stats_schema = cls(
            bytes_sent=bytes_sent,
            ip=ip,
            object_info=object_info,
            object_name=object_name,
            time_taken_us=time_taken_us,
        )

        transfer_stats_schema.additional_properties = d
        return transfer_stats_schema

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
