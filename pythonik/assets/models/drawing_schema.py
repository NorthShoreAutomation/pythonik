from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drawing_primitive_schema import DrawingPrimitiveSchema


T = TypeVar("T", bound="DrawingSchema")


@_attrs_define
class DrawingSchema:
    """
    Attributes:
        primitives (list[DrawingPrimitiveSchema] | Unset):
        version (int | None | Unset):
    """

    primitives: list[DrawingPrimitiveSchema] | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primitives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.primitives, Unset):
            primitives = []
            for primitives_item_data in self.primitives:
                primitives_item = primitives_item_data.to_dict()
                primitives.append(primitives_item)

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primitives is not UNSET:
            field_dict["primitives"] = primitives
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drawing_primitive_schema import DrawingPrimitiveSchema

        d = dict(src_dict)
        _primitives = d.pop("primitives", UNSET)
        primitives: list[DrawingPrimitiveSchema] | Unset = UNSET
        if _primitives is not UNSET:
            primitives = []
            for primitives_item_data in _primitives:
                primitives_item = DrawingPrimitiveSchema.from_dict(primitives_item_data)

                primitives.append(primitives_item)

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        drawing_schema = cls(
            primitives=primitives,
            version=version,
        )

        drawing_schema.additional_properties = d
        return drawing_schema

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
