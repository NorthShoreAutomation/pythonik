from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.drawing_primitive_schema_type import DrawingPrimitiveSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drawing_point_schema import DrawingPointSchema


T = TypeVar("T", bound="DrawingPrimitiveSchema")


@_attrs_define
class DrawingPrimitiveSchema:
    """
    Attributes:
        type_ (DrawingPrimitiveSchemaType):
        color (str | Unset):
        opacity (float | Unset):
        points (list[DrawingPointSchema] | Unset):
        text (str | Unset):
        width (float | Unset):
    """

    type_: DrawingPrimitiveSchemaType
    color: str | Unset = UNSET
    opacity: float | Unset = UNSET
    points: list[DrawingPointSchema] | Unset = UNSET
    text: str | Unset = UNSET
    width: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        color = self.color

        opacity = self.opacity

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        text = self.text

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if opacity is not UNSET:
            field_dict["opacity"] = opacity
        if points is not UNSET:
            field_dict["points"] = points
        if text is not UNSET:
            field_dict["text"] = text
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drawing_point_schema import DrawingPointSchema

        d = dict(src_dict)
        type_ = DrawingPrimitiveSchemaType(d.pop("type"))

        color = d.pop("color", UNSET)

        opacity = d.pop("opacity", UNSET)

        _points = d.pop("points", UNSET)
        points: list[DrawingPointSchema] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = DrawingPointSchema.from_dict(points_item_data)

                points.append(points_item)

        text = d.pop("text", UNSET)

        width = d.pop("width", UNSET)

        drawing_primitive_schema = cls(
            type_=type_,
            color=color,
            opacity=opacity,
            points=points,
            text=text,
            width=width,
        )

        drawing_primitive_schema.additional_properties = d
        return drawing_primitive_schema

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
