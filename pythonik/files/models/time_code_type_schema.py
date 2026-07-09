from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_base_type_schema import TimeBaseTypeSchema


T = TypeVar("T", bound="TimeCodeTypeSchema")


@_attrs_define
class TimeCodeTypeSchema:
    """
    Attributes:
        frames_number (int | None | Unset):
        is_drop_frame (bool | None | Unset):
        time_base (None | TimeBaseTypeSchema | Unset):
    """

    frames_number: int | None | Unset = UNSET
    is_drop_frame: bool | None | Unset = UNSET
    time_base: None | TimeBaseTypeSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.time_base_type_schema import TimeBaseTypeSchema

        frames_number: int | None | Unset
        if isinstance(self.frames_number, Unset):
            frames_number = UNSET
        else:
            frames_number = self.frames_number

        is_drop_frame: bool | None | Unset
        if isinstance(self.is_drop_frame, Unset):
            is_drop_frame = UNSET
        else:
            is_drop_frame = self.is_drop_frame

        time_base: dict[str, Any] | None | Unset
        if isinstance(self.time_base, Unset):
            time_base = UNSET
        elif isinstance(self.time_base, TimeBaseTypeSchema):
            time_base = self.time_base.to_dict()
        else:
            time_base = self.time_base

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if frames_number is not UNSET:
            field_dict["frames_number"] = frames_number
        if is_drop_frame is not UNSET:
            field_dict["is_drop_frame"] = is_drop_frame
        if time_base is not UNSET:
            field_dict["time_base"] = time_base

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_base_type_schema import TimeBaseTypeSchema

        d = dict(src_dict)

        def _parse_frames_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        frames_number = _parse_frames_number(d.pop("frames_number", UNSET))

        def _parse_is_drop_frame(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_drop_frame = _parse_is_drop_frame(d.pop("is_drop_frame", UNSET))

        def _parse_time_base(data: object) -> None | TimeBaseTypeSchema | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_base_type_1 = TimeBaseTypeSchema.from_dict(data)

                return time_base_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TimeBaseTypeSchema | Unset, data)

        time_base = _parse_time_base(d.pop("time_base", UNSET))

        time_code_type_schema = cls(
            frames_number=frames_number,
            is_drop_frame=is_drop_frame,
            time_base=time_base,
        )

        time_code_type_schema.additional_properties = d
        return time_code_type_schema

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
