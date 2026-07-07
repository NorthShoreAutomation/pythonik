from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analyze_schema_force_type import AnalyzeSchemaForceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyzeSchema")


@_attrs_define
class AnalyzeSchema:
    """
    Attributes:
        force (bool | Unset):  Default: False.
        force_type (AnalyzeSchemaForceType | Unset):  Default: AnalyzeSchemaForceType.APPEND.
        service_name (str | Unset):
    """

    force: bool | Unset = False
    force_type: AnalyzeSchemaForceType | Unset = AnalyzeSchemaForceType.APPEND
    service_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        force = self.force

        force_type: str | Unset = UNSET
        if not isinstance(self.force_type, Unset):
            force_type = self.force_type.value

        service_name = self.service_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force is not UNSET:
            field_dict["force"] = force
        if force_type is not UNSET:
            field_dict["force_type"] = force_type
        if service_name is not UNSET:
            field_dict["service_name"] = service_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        force = d.pop("force", UNSET)

        _force_type = d.pop("force_type", UNSET)
        force_type: AnalyzeSchemaForceType | Unset
        if isinstance(_force_type, Unset):
            force_type = UNSET
        else:
            force_type = AnalyzeSchemaForceType(_force_type)

        service_name = d.pop("service_name", UNSET)

        analyze_schema = cls(
            force=force,
            force_type=force_type,
            service_name=service_name,
        )

        analyze_schema.additional_properties = d
        return analyze_schema

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
