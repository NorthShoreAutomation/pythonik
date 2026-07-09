from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_field_value_schema_field_values_type_0_item import (
        MetadataFieldValueSchemaFieldValuesType0Item,
    )


T = TypeVar("T", bound="MetadataFieldValueSchema")


@_attrs_define
class MetadataFieldValueSchema:
    """
    Attributes:
        date_created (datetime.datetime | None | Unset):
        field_values (list[MetadataFieldValueSchemaFieldValuesType0Item] | None | Unset):
    """

    date_created: datetime.datetime | None | Unset = UNSET
    field_values: list[MetadataFieldValueSchemaFieldValuesType0Item] | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if field_values is not UNSET:
            field_dict["field_values"] = field_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field_value_schema_field_values_type_0_item import (
            MetadataFieldValueSchemaFieldValuesType0Item,
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

        def _parse_field_values(
            data: object,
        ) -> list[MetadataFieldValueSchemaFieldValuesType0Item] | None | Unset:
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
                        MetadataFieldValueSchemaFieldValuesType0Item.from_dict(
                            field_values_type_0_item_data
                        )
                    )

                    field_values_type_0.append(field_values_type_0_item)

                return field_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[MetadataFieldValueSchemaFieldValuesType0Item] | None | Unset, data
            )

        field_values = _parse_field_values(d.pop("field_values", UNSET))

        metadata_field_value_schema = cls(
            date_created=date_created,
            field_values=field_values,
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
