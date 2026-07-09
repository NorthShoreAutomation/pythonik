from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_action_schema_type import DeleteActionSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_action_schema_parameters_type_0 import (
        DeleteActionSchemaParametersType0,
    )


T = TypeVar("T", bound="DeleteActionSchema")


@_attrs_define
class DeleteActionSchema:
    """
    Attributes:
        type_ (DeleteActionSchemaType):  Default: DeleteActionSchemaType.DELETE_ASSET.
        parameters (DeleteActionSchemaParametersType0 | None | Unset):
    """

    type_: DeleteActionSchemaType = DeleteActionSchemaType.DELETE_ASSET
    parameters: DeleteActionSchemaParametersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.delete_action_schema_parameters_type_0 import (
            DeleteActionSchemaParametersType0,
        )

        type_ = self.type_.value

        parameters: dict[str, Any] | None | Unset
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, DeleteActionSchemaParametersType0):
            parameters = self.parameters.to_dict()
        else:
            parameters = self.parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_action_schema_parameters_type_0 import (
            DeleteActionSchemaParametersType0,
        )

        d = dict(src_dict)
        type_ = DeleteActionSchemaType(d.pop("type"))

        def _parse_parameters(
            data: object,
        ) -> DeleteActionSchemaParametersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0 = DeleteActionSchemaParametersType0.from_dict(data)

                return parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeleteActionSchemaParametersType0 | None | Unset, data)

        parameters = _parse_parameters(d.pop("parameters", UNSET))

        delete_action_schema = cls(
            type_=type_,
            parameters=parameters,
        )

        delete_action_schema.additional_properties = d
        return delete_action_schema

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
