from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_filling_response_schema_metadata_values_type_0 import (
        MetadataFillingResponseSchemaMetadataValuesType0,
    )


T = TypeVar("T", bound="MetadataFillingResponseSchema")


@_attrs_define
class MetadataFillingResponseSchema:
    """
    Attributes:
        errors (list[str] | None | Unset):
        metadata_values (MetadataFillingResponseSchemaMetadataValuesType0 | None | Unset): Map of field names to
            generated values. Values can be a string, a list of strings, or an object with 'value' and optional 'label'
            keys.
        warnings (list[str] | None | Unset):
    """

    errors: list[str] | None | Unset = UNSET
    metadata_values: MetadataFillingResponseSchemaMetadataValuesType0 | None | Unset = (
        UNSET
    )
    warnings: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.metadata_filling_response_schema_metadata_values_type_0 import (
            MetadataFillingResponseSchemaMetadataValuesType0,
        )

        errors: list[str] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        else:
            errors = self.errors

        metadata_values: dict[str, Any] | None | Unset
        if isinstance(self.metadata_values, Unset):
            metadata_values = UNSET
        elif isinstance(
            self.metadata_values, MetadataFillingResponseSchemaMetadataValuesType0
        ):
            metadata_values = self.metadata_values.to_dict()
        else:
            metadata_values = self.metadata_values

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings

        else:
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
        from ..models.metadata_filling_response_schema_metadata_values_type_0 import (
            MetadataFillingResponseSchemaMetadataValuesType0,
        )

        d = dict(src_dict)

        def _parse_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(list[str], data)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_metadata_values(
            data: object,
        ) -> MetadataFillingResponseSchemaMetadataValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_values_type_0 = (
                    MetadataFillingResponseSchemaMetadataValuesType0.from_dict(data)
                )

                return metadata_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MetadataFillingResponseSchemaMetadataValuesType0 | None | Unset, data
            )

        metadata_values = _parse_metadata_values(d.pop("metadata_values", UNSET))

        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

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
