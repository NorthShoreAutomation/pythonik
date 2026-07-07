from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_update_action_parameters_metadata_values import (
        MetadataUpdateActionParametersMetadataValues,
    )


T = TypeVar("T", bound="MetadataUpdateActionParameters")


@_attrs_define
class MetadataUpdateActionParameters:
    """
    Attributes:
        metadata_values (MetadataUpdateActionParametersMetadataValues):
        metadata_view_id (UUID):
    """

    metadata_values: MetadataUpdateActionParametersMetadataValues
    metadata_view_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_values = self.metadata_values.to_dict()

        metadata_view_id = str(self.metadata_view_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata_values": metadata_values,
                "metadata_view_id": metadata_view_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_update_action_parameters_metadata_values import (
            MetadataUpdateActionParametersMetadataValues,
        )

        d = dict(src_dict)
        metadata_values = MetadataUpdateActionParametersMetadataValues.from_dict(
            d.pop("metadata_values")
        )

        metadata_view_id = UUID(d.pop("metadata_view_id"))

        metadata_update_action_parameters = cls(
            metadata_values=metadata_values,
            metadata_view_id=metadata_view_id,
        )

        metadata_update_action_parameters.additional_properties = d
        return metadata_update_action_parameters

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
