from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.criteria_range_filter_schema import CriteriaRangeFilterSchema
    from ..models.multi_select_filter_group_schema import MultiSelectFilterGroupSchema


T = TypeVar("T", bound="NltfParseResultSchemaFilter")


@_attrs_define
class NltfParseResultSchemaFilter:
    """ """

    additional_properties: dict[
        str,
        CriteriaRangeFilterSchema
        | list[MultiSelectFilterGroupSchema]
        | list[str]
        | str,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.criteria_range_filter_schema import CriteriaRangeFilterSchema

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = prop

            elif isinstance(prop, list):
                field_dict[prop_name] = []
                for additional_property_type_2_item_data in prop:
                    additional_property_type_2_item = (
                        additional_property_type_2_item_data.to_dict()
                    )
                    field_dict[prop_name].append(additional_property_type_2_item)

            elif isinstance(prop, CriteriaRangeFilterSchema):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_range_filter_schema import CriteriaRangeFilterSchema
        from ..models.multi_select_filter_group_schema import (
            MultiSelectFilterGroupSchema,
        )

        d = dict(src_dict)
        nltf_parse_result_schema_filter = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> (
                CriteriaRangeFilterSchema
                | list[MultiSelectFilterGroupSchema]
                | list[str]
                | str
            ):
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_1 = cast(list[str], data)

                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_2 = []
                    _additional_property_type_2 = data
                    for (
                        additional_property_type_2_item_data
                    ) in _additional_property_type_2:
                        additional_property_type_2_item = (
                            MultiSelectFilterGroupSchema.from_dict(
                                additional_property_type_2_item_data
                            )
                        )

                        additional_property_type_2.append(
                            additional_property_type_2_item
                        )

                    return additional_property_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_3 = CriteriaRangeFilterSchema.from_dict(
                        data
                    )

                    return additional_property_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(
                    CriteriaRangeFilterSchema
                    | list[MultiSelectFilterGroupSchema]
                    | list[str]
                    | str,
                    data,
                )

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        nltf_parse_result_schema_filter.additional_properties = additional_properties
        return nltf_parse_result_schema_filter

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> (
        CriteriaRangeFilterSchema | list[MultiSelectFilterGroupSchema] | list[str] | str
    ):
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: CriteriaRangeFilterSchema
        | list[MultiSelectFilterGroupSchema]
        | list[str]
        | str,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
