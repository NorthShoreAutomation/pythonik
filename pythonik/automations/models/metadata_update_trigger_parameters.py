from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_update_trigger_parameters_event_type import (
    MetadataUpdateTriggerParametersEventType,
)

if TYPE_CHECKING:
    from ..models.metadata_update_trigger_parameters_metadata_values import (
        MetadataUpdateTriggerParametersMetadataValues,
    )


T = TypeVar("T", bound="MetadataUpdateTriggerParameters")


@_attrs_define
class MetadataUpdateTriggerParameters:
    """
    Attributes:
        event_type (MetadataUpdateTriggerParametersEventType):
        metadata_values (MetadataUpdateTriggerParametersMetadataValues):
    """

    event_type: MetadataUpdateTriggerParametersEventType
    metadata_values: MetadataUpdateTriggerParametersMetadataValues
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        metadata_values = self.metadata_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "metadata_values": metadata_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_update_trigger_parameters_metadata_values import (
            MetadataUpdateTriggerParametersMetadataValues,
        )

        d = dict(src_dict)
        event_type = MetadataUpdateTriggerParametersEventType(d.pop("event_type"))

        metadata_values = MetadataUpdateTriggerParametersMetadataValues.from_dict(
            d.pop("metadata_values")
        )

        metadata_update_trigger_parameters = cls(
            event_type=event_type,
            metadata_values=metadata_values,
        )

        metadata_update_trigger_parameters.additional_properties = d
        return metadata_update_trigger_parameters

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
