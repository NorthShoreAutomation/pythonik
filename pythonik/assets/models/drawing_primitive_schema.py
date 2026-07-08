from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        color (None | str | Unset):
        opacity (float | None | Unset):
        points (list[DrawingPointSchema] | None | Unset):
        text (None | str | Unset):
        width (float | None | Unset):
    """

    type_: DrawingPrimitiveSchemaType
    color: None | str | Unset = UNSET
    opacity: float | None | Unset = UNSET
    points: list[DrawingPointSchema] | None | Unset = UNSET
    text: None | str | Unset = UNSET
    width: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        opacity: float | None | Unset
        if isinstance(self.opacity, Unset):
            opacity = UNSET
        else:
            opacity = self.opacity

        points: list[dict[str, Any]] | None | Unset
        if isinstance(self.points, Unset):
            points = UNSET
        elif isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)

        else:
            points = self.points

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        width: float | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
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

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_opacity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        opacity = _parse_opacity(d.pop("opacity", UNSET))

        def _parse_points(data: object) -> list[DrawingPointSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = DrawingPointSchema.from_dict(
                        points_type_0_item_data
                    )

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DrawingPointSchema] | None | Unset, data)

        points = _parse_points(d.pop("points", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

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
