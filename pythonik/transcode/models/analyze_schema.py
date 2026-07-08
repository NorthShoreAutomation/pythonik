from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analyze_schema_force_type_type_1 import AnalyzeSchemaForceTypeType1


T = TypeVar("T", bound="AnalyzeSchema")


@_attrs_define
class AnalyzeSchema:
    """
    Attributes:
        force (bool | None | Unset):  Default: False.
        force_type (AnalyzeSchemaForceTypeType1 | None | Unset):
        service_name (None | str | Unset):
    """

    force: bool | None | Unset = False
    force_type: AnalyzeSchemaForceTypeType1 | None | Unset = UNSET
    service_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analyze_schema_force_type_type_1 import (
            AnalyzeSchemaForceTypeType1,
        )

        force: bool | None | Unset
        if isinstance(self.force, Unset):
            force = UNSET
        else:
            force = self.force

        force_type: dict[str, Any] | None | Unset
        if isinstance(self.force_type, Unset):
            force_type = UNSET
        elif isinstance(self.force_type, AnalyzeSchemaForceTypeType1):
            force_type = self.force_type.to_dict()
        else:
            force_type = self.force_type

        service_name: None | str | Unset
        if isinstance(self.service_name, Unset):
            service_name = UNSET
        else:
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
        from ..models.analyze_schema_force_type_type_1 import (
            AnalyzeSchemaForceTypeType1,
        )

        d = dict(src_dict)

        def _parse_force(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force = _parse_force(d.pop("force", UNSET))

        def _parse_force_type(
            data: object,
        ) -> AnalyzeSchemaForceTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                force_type_type_1 = AnalyzeSchemaForceTypeType1.from_dict(data)

                return force_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyzeSchemaForceTypeType1 | None | Unset, data)

        force_type = _parse_force_type(d.pop("force_type", UNSET))

        def _parse_service_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_name = _parse_service_name(d.pop("service_name", UNSET))

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
