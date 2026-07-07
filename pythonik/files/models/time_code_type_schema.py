from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        frames_number (int | Unset):
        is_drop_frame (bool | Unset):
        time_base (TimeBaseTypeSchema | Unset):
    """

    frames_number: int | Unset = UNSET
    is_drop_frame: bool | Unset = UNSET
    time_base: TimeBaseTypeSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frames_number = self.frames_number

        is_drop_frame = self.is_drop_frame

        time_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_base, Unset):
            time_base = self.time_base.to_dict()

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
        frames_number = d.pop("frames_number", UNSET)

        is_drop_frame = d.pop("is_drop_frame", UNSET)

        _time_base = d.pop("time_base", UNSET)
        time_base: TimeBaseTypeSchema | Unset
        if isinstance(_time_base, Unset):
            time_base = UNSET
        else:
            time_base = TimeBaseTypeSchema.from_dict(_time_base)

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
