from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_field_value_update_schema_mode import (
    MetadataFieldValueUpdateSchemaMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_field_value_update_schema_field_values_type_0_item import (
        MetadataFieldValueUpdateSchemaFieldValuesType0Item,
    )


T = TypeVar("T", bound="MetadataFieldValueUpdateSchema")


@_attrs_define
class MetadataFieldValueUpdateSchema:
    """
    Attributes:
        field_values (list[MetadataFieldValueUpdateSchemaFieldValuesType0Item] | None | Unset):
        mode (MetadataFieldValueUpdateSchemaMode | None | Unset):
    """

    field_values: (
        list[MetadataFieldValueUpdateSchemaFieldValuesType0Item] | None | Unset
    ) = UNSET
    mode: MetadataFieldValueUpdateSchemaMode | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.field_values, Unset):
            field_values = UNSET
        elif isinstance(self.field_values, list):
            field_values = []
            for field_values_type_0_item_data in self.field_values:
                field_values_type_0_item = field_values_type_0_item_data.to_dict()
                field_values.append(field_values_type_0_item)

        else:
            field_values = self.field_values

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, MetadataFieldValueUpdateSchemaMode):
            mode = self.mode.value
        else:
            mode = self.mode

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
        from ..models.metadata_field_value_update_schema_field_values_type_0_item import (
            MetadataFieldValueUpdateSchemaFieldValuesType0Item,
        )

        d = dict(src_dict)

        def _parse_field_values(
            data: object,
        ) -> list[MetadataFieldValueUpdateSchemaFieldValuesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_values_type_0 = []
                _field_values_type_0 = data
                for field_values_type_0_item_data in _field_values_type_0:
                    field_values_type_0_item = (
                        MetadataFieldValueUpdateSchemaFieldValuesType0Item.from_dict(
                            field_values_type_0_item_data
                        )
                    )

                    field_values_type_0.append(field_values_type_0_item)

                return field_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[MetadataFieldValueUpdateSchemaFieldValuesType0Item] | None | Unset,
                data,
            )

        field_values = _parse_field_values(d.pop("field_values", UNSET))

        def _parse_mode(
            data: object,
        ) -> MetadataFieldValueUpdateSchemaMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = MetadataFieldValueUpdateSchemaMode(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetadataFieldValueUpdateSchemaMode | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

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
