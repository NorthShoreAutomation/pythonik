from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drawing_primitive import DrawingPrimitive


T = TypeVar("T", bound="Drawing")


@_attrs_define
class Drawing:
    """
    Attributes:
        primitives (list[DrawingPrimitive] | None | Unset):
        version (int | None | Unset):
    """

    primitives: list[DrawingPrimitive] | None | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primitives: list[dict[str, Any]] | None | Unset
        if isinstance(self.primitives, Unset):
            primitives = UNSET
        elif isinstance(self.primitives, list):
            primitives = []
            for primitives_type_0_item_data in self.primitives:
                primitives_type_0_item = primitives_type_0_item_data.to_dict()
                primitives.append(primitives_type_0_item)

        else:
            primitives = self.primitives

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
        from ..models.drawing_primitive import DrawingPrimitive

        d = dict(src_dict)

        def _parse_primitives(data: object) -> list[DrawingPrimitive] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                primitives_type_0 = []
                _primitives_type_0 = data
                for primitives_type_0_item_data in _primitives_type_0:
                    primitives_type_0_item = DrawingPrimitive.from_dict(
                        primitives_type_0_item_data
                    )

                    primitives_type_0.append(primitives_type_0_item)

                return primitives_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DrawingPrimitive] | None | Unset, data)

        primitives = _parse_primitives(d.pop("primitives", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        drawing = cls(
            primitives=primitives,
            version=version,
        )

        drawing.additional_properties = d
        return drawing

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
