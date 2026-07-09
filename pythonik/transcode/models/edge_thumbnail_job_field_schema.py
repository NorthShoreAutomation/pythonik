from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EdgeThumbnailJobFieldSchema")


@_attrs_define
class EdgeThumbnailJobFieldSchema:
    """
    Attributes:
        height (int | None | Unset):
        id (None | str | Unset):
        max_number (int | None | Unset):
        min_interval (int | None | Unset):
        time_end_milliseconds (int | None | Unset):
        time_start_milliseconds (int | None | Unset):
        timestamp (int | None | Unset):
        width (int | None | Unset):
    """

    height: int | None | Unset = UNSET
    id: None | str | Unset = UNSET
    max_number: int | None | Unset = UNSET
    min_interval: int | None | Unset = UNSET
    time_end_milliseconds: int | None | Unset = UNSET
    time_start_milliseconds: int | None | Unset = UNSET
    timestamp: int | None | Unset = UNSET
    width: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        max_number: int | None | Unset
        if isinstance(self.max_number, Unset):
            max_number = UNSET
        else:
            max_number = self.max_number

        min_interval: int | None | Unset
        if isinstance(self.min_interval, Unset):
            min_interval = UNSET
        else:
            min_interval = self.min_interval

        time_end_milliseconds: int | None | Unset
        if isinstance(self.time_end_milliseconds, Unset):
            time_end_milliseconds = UNSET
        else:
            time_end_milliseconds = self.time_end_milliseconds

        time_start_milliseconds: int | None | Unset
        if isinstance(self.time_start_milliseconds, Unset):
            time_start_milliseconds = UNSET
        else:
            time_start_milliseconds = self.time_start_milliseconds

        timestamp: int | None | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if max_number is not UNSET:
            field_dict["max_number"] = max_number
        if min_interval is not UNSET:
            field_dict["min_interval"] = min_interval
        if time_end_milliseconds is not UNSET:
            field_dict["time_end_milliseconds"] = time_end_milliseconds
        if time_start_milliseconds is not UNSET:
            field_dict["time_start_milliseconds"] = time_start_milliseconds
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_max_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_number = _parse_max_number(d.pop("max_number", UNSET))

        def _parse_min_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_interval = _parse_min_interval(d.pop("min_interval", UNSET))

        def _parse_time_end_milliseconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_end_milliseconds = _parse_time_end_milliseconds(
            d.pop("time_end_milliseconds", UNSET)
        )

        def _parse_time_start_milliseconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_start_milliseconds = _parse_time_start_milliseconds(
            d.pop("time_start_milliseconds", UNSET)
        )

        def _parse_timestamp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

        edge_thumbnail_job_field_schema = cls(
            height=height,
            id=id,
            max_number=max_number,
            min_interval=min_interval,
            time_end_milliseconds=time_end_milliseconds,
            time_start_milliseconds=time_start_milliseconds,
            timestamp=timestamp,
            width=width,
        )

        edge_thumbnail_job_field_schema.additional_properties = d
        return edge_thumbnail_job_field_schema

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
