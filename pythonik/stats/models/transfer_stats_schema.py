from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferStatsSchema")


@_attrs_define
class TransferStatsSchema:
    """
    Attributes:
        bytes_sent (int):
        ip (str | Unset):
        object_info (str | Unset):
        object_name (str | Unset):
        time_taken_us (int | Unset):
    """

    bytes_sent: int
    ip: str | Unset = UNSET
    object_info: str | Unset = UNSET
    object_name: str | Unset = UNSET
    time_taken_us: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_sent = self.bytes_sent

        ip = self.ip

        object_info = self.object_info

        object_name = self.object_name

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

        ip = d.pop("ip", UNSET)

        object_info = d.pop("object_info", UNSET)

        object_name = d.pop("object_name", UNSET)

        time_taken_us = d.pop("time_taken_us", UNSET)

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
