from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_field_value_update_schema import (
        MetadataFieldValueUpdateSchema,
    )


T = TypeVar("T", bound="MetadataUpdateActionParametersMetadataValues")


@_attrs_define
class MetadataUpdateActionParametersMetadataValues:
    """ """

    additional_properties: dict[str, MetadataFieldValueUpdateSchema] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field_value_update_schema import (
            MetadataFieldValueUpdateSchema,
        )

        d = dict(src_dict)
        metadata_update_action_parameters_metadata_values = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = MetadataFieldValueUpdateSchema.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        metadata_update_action_parameters_metadata_values.additional_properties = (
            additional_properties
        )
        return metadata_update_action_parameters_metadata_values

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> MetadataFieldValueUpdateSchema:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: MetadataFieldValueUpdateSchema) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
