from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_field_value_update_schema_mode import (
    MetadataFieldValueUpdateSchemaMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_field_value_update_schema_field_values_item import (
        MetadataFieldValueUpdateSchemaFieldValuesItem,
    )


T = TypeVar("T", bound="MetadataFieldValueUpdateSchema")


@_attrs_define
class MetadataFieldValueUpdateSchema:
    """
    Attributes:
        field_values (list[MetadataFieldValueUpdateSchemaFieldValuesItem] | Unset):
        mode (MetadataFieldValueUpdateSchemaMode | Unset):  Default: MetadataFieldValueUpdateSchemaMode.OVERWRITE.
    """

    field_values: list[MetadataFieldValueUpdateSchemaFieldValuesItem] | Unset = UNSET
    mode: MetadataFieldValueUpdateSchemaMode | Unset = (
        MetadataFieldValueUpdateSchemaMode.OVERWRITE
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_values, Unset):
            field_values = []
            for field_values_item_data in self.field_values:
                field_values_item = field_values_item_data.to_dict()
                field_values.append(field_values_item)

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_values is not UNSET:
            field_dict["field_values"] = field_values
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field_value_update_schema_field_values_item import (
            MetadataFieldValueUpdateSchemaFieldValuesItem,
        )

        d = dict(src_dict)
        _field_values = d.pop("field_values", UNSET)
        field_values: list[MetadataFieldValueUpdateSchemaFieldValuesItem] | Unset = (
            UNSET
        )
        if _field_values is not UNSET:
            field_values = []
            for field_values_item_data in _field_values:
                field_values_item = (
                    MetadataFieldValueUpdateSchemaFieldValuesItem.from_dict(
                        field_values_item_data
                    )
                )

                field_values.append(field_values_item)

        _mode = d.pop("mode", UNSET)
        mode: MetadataFieldValueUpdateSchemaMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = MetadataFieldValueUpdateSchemaMode(_mode)

        metadata_field_value_update_schema = cls(
            field_values=field_values,
            mode=mode,
        )

        metadata_field_value_update_schema.additional_properties = d
        return metadata_field_value_update_schema

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
