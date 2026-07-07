from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_version_keyframes_schema import AssetVersionKeyframesSchema


T = TypeVar("T", bound="AssetVersionsKeyframesSchema")


@_attrs_define
class AssetVersionsKeyframesSchema:
    """
    Attributes:
        objects (list[AssetVersionKeyframesSchema] | Unset):
    """

    objects: list[AssetVersionKeyframesSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()
                objects.append(objects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objects is not UNSET:
            field_dict["objects"] = objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_version_keyframes_schema import AssetVersionKeyframesSchema

        d = dict(src_dict)
        _objects = d.pop("objects", UNSET)
        objects: list[AssetVersionKeyframesSchema] | Unset = UNSET
        if _objects is not UNSET:
            objects = []
            for objects_item_data in _objects:
                objects_item = AssetVersionKeyframesSchema.from_dict(objects_item_data)

                objects.append(objects_item)

        asset_versions_keyframes_schema = cls(
            objects=objects,
        )

        asset_versions_keyframes_schema.additional_properties = d
        return asset_versions_keyframes_schema

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
