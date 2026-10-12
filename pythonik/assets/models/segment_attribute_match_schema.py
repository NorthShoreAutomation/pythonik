from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.segment_attribute_match_schema_operator import (
    SegmentAttributeMatchSchemaOperator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SegmentAttributeMatchSchema")


@_attrs_define
class SegmentAttributeMatchSchema:
    """
    Attributes:
        name (str):
        value (Any):
        operator (None | SegmentAttributeMatchSchemaOperator | Unset):
    """

    name: str
    value: Any
    operator: None | SegmentAttributeMatchSchemaOperator | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        operator: None | str | Unset
        if isinstance(self.operator, Unset):
            operator = UNSET
        elif isinstance(self.operator, SegmentAttributeMatchSchemaOperator):
            operator = self.operator.value
        else:
            operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        def _parse_operator(
            data: object,
        ) -> None | SegmentAttributeMatchSchemaOperator | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operator_type_1 = SegmentAttributeMatchSchemaOperator(data)

                return operator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentAttributeMatchSchemaOperator | Unset, data)

        operator = _parse_operator(d.pop("operator", UNSET))

        segment_attribute_match_schema = cls(
            name=name,
            value=value,
            operator=operator,
        )

        segment_attribute_match_schema.additional_properties = d
        return segment_attribute_match_schema

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
