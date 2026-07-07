from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_filling_response_schema_metadata_values import (
        MetadataFillingResponseSchemaMetadataValues,
    )


T = TypeVar("T", bound="MetadataFillingResponseSchema")


@_attrs_define
class MetadataFillingResponseSchema:
    """
    Attributes:
        errors (list[str] | Unset):
        metadata_values (MetadataFillingResponseSchemaMetadataValues | Unset): Map of field names to generated values.
            Values can be a string, a list of strings, or an object with 'value' and optional 'label' keys.
        warnings (list[str] | Unset):
    """

    errors: list[str] | Unset = UNSET
    metadata_values: MetadataFillingResponseSchemaMetadataValues | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        metadata_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_values, Unset):
            metadata_values = self.metadata_values.to_dict()

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if metadata_values is not UNSET:
            field_dict["metadata_values"] = metadata_values
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_filling_response_schema_metadata_values import (
            MetadataFillingResponseSchemaMetadataValues,
        )

        d = dict(src_dict)
        errors = cast(list[str], d.pop("errors", UNSET))

        _metadata_values = d.pop("metadata_values", UNSET)
        metadata_values: MetadataFillingResponseSchemaMetadataValues | Unset
        if isinstance(_metadata_values, Unset):
            metadata_values = UNSET
        else:
            metadata_values = MetadataFillingResponseSchemaMetadataValues.from_dict(
                _metadata_values
            )

        warnings = cast(list[str], d.pop("warnings", UNSET))

        metadata_filling_response_schema = cls(
            errors=errors,
            metadata_values=metadata_values,
            warnings=warnings,
        )

        metadata_filling_response_schema.additional_properties = d
        return metadata_filling_response_schema

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
