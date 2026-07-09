from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.acl_update_schema import ACLUpdateSchema


T = TypeVar("T", bound="UpdateACLActionParameters")


@_attrs_define
class UpdateACLActionParameters:
    """
    Attributes:
        objects (list[ACLUpdateSchema]):
    """

    objects: list[ACLUpdateSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objects": objects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acl_update_schema import ACLUpdateSchema

        d = dict(src_dict)
        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = ACLUpdateSchema.from_dict(objects_item_data)

            objects.append(objects_item)

        update_acl_action_parameters = cls(
            objects=objects,
        )

        update_acl_action_parameters.additional_properties = d
        return update_acl_action_parameters

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
