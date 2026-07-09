from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_ac_ls_schema_multiple import CreateACLsSchemaMultiple


T = TypeVar("T", bound="CreateMultipleACLsSchema")


@_attrs_define
class CreateMultipleACLsSchema:
    """
    Attributes:
        objects (list[CreateACLsSchemaMultiple]): The number of objects in the list is limited to a minimum of 1 and a
            maximum of 100
    """

    objects: list[CreateACLsSchemaMultiple]
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
        from ..models.create_ac_ls_schema_multiple import CreateACLsSchemaMultiple

        d = dict(src_dict)
        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = CreateACLsSchemaMultiple.from_dict(objects_item_data)

            objects.append(objects_item)

        create_multiple_ac_ls_schema = cls(
            objects=objects,
        )

        create_multiple_ac_ls_schema.additional_properties = d
        return create_multiple_ac_ls_schema

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
