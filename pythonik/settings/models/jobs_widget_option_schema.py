from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_widget_option_schema_filters import JobsWidgetOptionSchemaFilters
    from ..models.sort import Sort


T = TypeVar("T", bound="JobsWidgetOptionSchema")


@_attrs_define
class JobsWidgetOptionSchema:
    """
    Attributes:
        columns (list[str] | Unset):
        filters (JobsWidgetOptionSchemaFilters | Unset):
        limit (int | Unset):
        sort (list[Sort] | Unset):
    """

    columns: list[str] | Unset = UNSET
    filters: JobsWidgetOptionSchemaFilters | Unset = UNSET
    limit: int | Unset = UNSET
    sort: list[Sort] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns: list[str] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        limit = self.limit

        sort: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = []
            for sort_item_data in self.sort:
                sort_item = sort_item_data.to_dict()
                sort.append(sort_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if filters is not UNSET:
            field_dict["filters"] = filters
        if limit is not UNSET:
            field_dict["limit"] = limit
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jobs_widget_option_schema_filters import (
            JobsWidgetOptionSchemaFilters,
        )
        from ..models.sort import Sort

        d = dict(src_dict)
        columns = cast(list[str], d.pop("columns", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: JobsWidgetOptionSchemaFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = JobsWidgetOptionSchemaFilters.from_dict(_filters)

        limit = d.pop("limit", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: list[Sort] | Unset = UNSET
        if _sort is not UNSET:
            sort = []
            for sort_item_data in _sort:
                sort_item = Sort.from_dict(sort_item_data)

                sort.append(sort_item)

        jobs_widget_option_schema = cls(
            columns=columns,
            filters=filters,
            limit=limit,
            sort=sort,
        )

        jobs_widget_option_schema.additional_properties = d
        return jobs_widget_option_schema

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
