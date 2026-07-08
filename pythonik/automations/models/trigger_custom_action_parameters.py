from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_custom_action_parameters_context import (
    TriggerCustomActionParametersContext,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_custom_action_parameters_metadata_values_type_0 import (
        TriggerCustomActionParametersMetadataValuesType0,
    )


T = TypeVar("T", bound="TriggerCustomActionParameters")


@_attrs_define
class TriggerCustomActionParameters:
    """
    Attributes:
        action_id (UUID):
        context (TriggerCustomActionParametersContext):
        metadata_values (None | TriggerCustomActionParametersMetadataValuesType0 | Unset):
    """

    action_id: UUID
    context: TriggerCustomActionParametersContext
    metadata_values: None | TriggerCustomActionParametersMetadataValuesType0 | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trigger_custom_action_parameters_metadata_values_type_0 import (
            TriggerCustomActionParametersMetadataValuesType0,
        )

        action_id = str(self.action_id)

        context = self.context.value

        metadata_values: dict[str, Any] | None | Unset
        if isinstance(self.metadata_values, Unset):
            metadata_values = UNSET
        elif isinstance(
            self.metadata_values, TriggerCustomActionParametersMetadataValuesType0
        ):
            metadata_values = self.metadata_values.to_dict()
        else:
            metadata_values = self.metadata_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_id": action_id,
                "context": context,
            }
        )
        if metadata_values is not UNSET:
            field_dict["metadata_values"] = metadata_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_custom_action_parameters_metadata_values_type_0 import (
            TriggerCustomActionParametersMetadataValuesType0,
        )

        d = dict(src_dict)
        action_id = UUID(d.pop("action_id"))

        context = TriggerCustomActionParametersContext(d.pop("context"))

        def _parse_metadata_values(
            data: object,
        ) -> None | TriggerCustomActionParametersMetadataValuesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_values_type_0 = (
                    TriggerCustomActionParametersMetadataValuesType0.from_dict(data)
                )

                return metadata_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TriggerCustomActionParametersMetadataValuesType0 | Unset, data
            )

        metadata_values = _parse_metadata_values(d.pop("metadata_values", UNSET))

        trigger_custom_action_parameters = cls(
            action_id=action_id,
            context=context,
            metadata_values=metadata_values,
        )

        trigger_custom_action_parameters.additional_properties = d
        return trigger_custom_action_parameters

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
