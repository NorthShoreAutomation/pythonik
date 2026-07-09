from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automation_search_criteria_schema_doc_types_type_0_item import (
    AutomationSearchCriteriaSchemaDocTypesType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria_filter import CriteriaFilter


T = TypeVar("T", bound="AutomationSearchCriteriaSchema")


@_attrs_define
class AutomationSearchCriteriaSchema:
    """
    Attributes:
        automation_ids (list[UUID]):
        doc_types (list[AutomationSearchCriteriaSchemaDocTypesType0Item] | None | Unset):
        execution_time (datetime.datetime | None | Unset):
        filter_ (CriteriaFilter | None | Unset):
    """

    automation_ids: list[UUID]
    doc_types: list[AutomationSearchCriteriaSchemaDocTypesType0Item] | None | Unset = (
        UNSET
    )
    execution_time: datetime.datetime | None | Unset = UNSET
    filter_: CriteriaFilter | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.criteria_filter import CriteriaFilter

        automation_ids = []
        for automation_ids_item_data in self.automation_ids:
            automation_ids_item = str(automation_ids_item_data)
            automation_ids.append(automation_ids_item)

        doc_types: list[str] | None | Unset
        if isinstance(self.doc_types, Unset):
            doc_types = UNSET
        elif isinstance(self.doc_types, list):
            doc_types = []
            for doc_types_type_0_item_data in self.doc_types:
                doc_types_type_0_item = doc_types_type_0_item_data.value
                doc_types.append(doc_types_type_0_item)

        else:
            doc_types = self.doc_types

        execution_time: None | str | Unset
        if isinstance(self.execution_time, Unset):
            execution_time = UNSET
        elif isinstance(self.execution_time, datetime.datetime):
            execution_time = self.execution_time.isoformat()
        else:
            execution_time = self.execution_time

        filter_: dict[str, Any] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, CriteriaFilter):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "automation_ids": automation_ids,
            }
        )
        if doc_types is not UNSET:
            field_dict["doc_types"] = doc_types
        if execution_time is not UNSET:
            field_dict["execution_time"] = execution_time
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_filter import CriteriaFilter

        d = dict(src_dict)
        automation_ids = []
        _automation_ids = d.pop("automation_ids")
        for automation_ids_item_data in _automation_ids:
            automation_ids_item = UUID(automation_ids_item_data)

            automation_ids.append(automation_ids_item)

        def _parse_doc_types(
            data: object,
        ) -> list[AutomationSearchCriteriaSchemaDocTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                doc_types_type_0 = []
                _doc_types_type_0 = data
                for doc_types_type_0_item_data in _doc_types_type_0:
                    doc_types_type_0_item = (
                        AutomationSearchCriteriaSchemaDocTypesType0Item(
                            doc_types_type_0_item_data
                        )
                    )

                    doc_types_type_0.append(doc_types_type_0_item)

                return doc_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[AutomationSearchCriteriaSchemaDocTypesType0Item] | None | Unset,
                data,
            )

        doc_types = _parse_doc_types(d.pop("doc_types", UNSET))

        def _parse_execution_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_time_type_0 = datetime.datetime.fromisoformat(data)

                return execution_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        execution_time = _parse_execution_time(d.pop("execution_time", UNSET))

        def _parse_filter_(data: object) -> CriteriaFilter | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_1 = CriteriaFilter.from_dict(data)

                return filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CriteriaFilter | None | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        automation_search_criteria_schema = cls(
            automation_ids=automation_ids,
            doc_types=doc_types,
            execution_time=execution_time,
            filter_=filter_,
        )

        automation_search_criteria_schema.additional_properties = d
        return automation_search_criteria_schema

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
