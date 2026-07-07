from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_schema_base_parameters import TriggerSchemaBaseParameters


T = TypeVar("T", bound="TriggerSchemaBase")


@_attrs_define
class TriggerSchemaBase:
    """
    Attributes:
        parameters (TriggerSchemaBaseParameters | Unset):
    """

    parameters: TriggerSchemaBaseParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_schema_base_parameters import TriggerSchemaBaseParameters

        d = dict(src_dict)
        _parameters = d.pop("parameters", UNSET)
        parameters: TriggerSchemaBaseParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = TriggerSchemaBaseParameters.from_dict(_parameters)

        trigger_schema_base = cls(
            parameters=parameters,
        )

        trigger_schema_base.additional_properties = d
        return trigger_schema_base

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
