from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_field_value_schema_mode import MetadataFieldValueSchemaMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_field_value_schema_field_values_item import (
        MetadataFieldValueSchemaFieldValuesItem,
    )


T = TypeVar("T", bound="MetadataFieldValueSchema")


@_attrs_define
class MetadataFieldValueSchema:
    """
    Attributes:
        date_created (datetime.datetime | None | Unset):
        field_values (list[MetadataFieldValueSchemaFieldValuesItem] | Unset):
        mode (MetadataFieldValueSchemaMode | Unset):  Default: MetadataFieldValueSchemaMode.OVERWRITE.
    """

    date_created: datetime.datetime | None | Unset = UNSET
    field_values: list[MetadataFieldValueSchemaFieldValuesItem] | Unset = UNSET
    mode: MetadataFieldValueSchemaMode | Unset = MetadataFieldValueSchemaMode.OVERWRITE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

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
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if field_values is not UNSET:
            field_dict["field_values"] = field_values
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field_value_schema_field_values_item import (
            MetadataFieldValueSchemaFieldValuesItem,
        )

        d = dict(src_dict)

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        _field_values = d.pop("field_values", UNSET)
        field_values: list[MetadataFieldValueSchemaFieldValuesItem] | Unset = UNSET
        if _field_values is not UNSET:
            field_values = []
            for field_values_item_data in _field_values:
                field_values_item = MetadataFieldValueSchemaFieldValuesItem.from_dict(
                    field_values_item_data
                )

                field_values.append(field_values_item)

        _mode = d.pop("mode", UNSET)
        mode: MetadataFieldValueSchemaMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = MetadataFieldValueSchemaMode(_mode)

        metadata_field_value_schema = cls(
            date_created=date_created,
            field_values=field_values,
            mode=mode,
        )

        metadata_field_value_schema.additional_properties = d
        return metadata_field_value_schema

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
