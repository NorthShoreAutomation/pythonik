from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_endpoint import OutputEndpoint


T = TypeVar("T", bound="ThumbnailJob")


@_attrs_define
class ThumbnailJob:
    """
    Attributes:
        output_endpoint (OutputEndpoint):
        height (int | Unset):
        id (str | Unset):
        max_number (int | Unset):
        min_interval (int | Unset):
        set_as_custom_keyframe (bool | Unset):
        time_end_milliseconds (int | None | Unset):
        time_start_milliseconds (int | None | Unset):
        timestamp (int | Unset):
        width (int | Unset):
    """

    output_endpoint: OutputEndpoint
    height: int | Unset = UNSET
    id: str | Unset = UNSET
    max_number: int | Unset = UNSET
    min_interval: int | Unset = UNSET
    set_as_custom_keyframe: bool | Unset = UNSET
    time_end_milliseconds: int | None | Unset = UNSET
    time_start_milliseconds: int | None | Unset = UNSET
    timestamp: int | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        output_endpoint = self.output_endpoint.to_dict()

        height = self.height

        id = self.id

        max_number = self.max_number

        min_interval = self.min_interval

        set_as_custom_keyframe = self.set_as_custom_keyframe

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

        timestamp = self.timestamp

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "output_endpoint": output_endpoint,
            }
        )
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if max_number is not UNSET:
            field_dict["max_number"] = max_number
        if min_interval is not UNSET:
            field_dict["min_interval"] = min_interval
        if set_as_custom_keyframe is not UNSET:
            field_dict["set_as_custom_keyframe"] = set_as_custom_keyframe
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
        from ..models.output_endpoint import OutputEndpoint

        d = dict(src_dict)
        output_endpoint = OutputEndpoint.from_dict(d.pop("output_endpoint"))

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        max_number = d.pop("max_number", UNSET)

        min_interval = d.pop("min_interval", UNSET)

        set_as_custom_keyframe = d.pop("set_as_custom_keyframe", UNSET)

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

        timestamp = d.pop("timestamp", UNSET)

        width = d.pop("width", UNSET)

        thumbnail_job = cls(
            output_endpoint=output_endpoint,
            height=height,
            id=id,
            max_number=max_number,
            min_interval=min_interval,
            set_as_custom_keyframe=set_as_custom_keyframe,
            time_end_milliseconds=time_end_milliseconds,
            time_start_milliseconds=time_start_milliseconds,
            timestamp=timestamp,
            width=width,
        )

        thumbnail_job.additional_properties = d
        return thumbnail_job

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
