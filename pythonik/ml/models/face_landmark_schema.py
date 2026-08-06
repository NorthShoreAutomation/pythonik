from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FaceLandmarkSchema")


@_attrs_define
class FaceLandmarkSchema:
    """
    Attributes:
        x (float | None | Unset):
        y (float | None | Unset):
    """

    x: float | None | Unset = UNSET
    y: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x: float | None | Unset
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        y: float | None | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x = _parse_x(d.pop("x", UNSET))

        def _parse_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y = _parse_y(d.pop("y", UNSET))

        face_landmark_schema = cls(
            x=x,
            y=y,
        )

        face_landmark_schema.additional_properties = d
        return face_landmark_schema

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
