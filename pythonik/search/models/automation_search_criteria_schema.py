from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automation_search_criteria_schema_doc_types_item import (
    AutomationSearchCriteriaSchemaDocTypesItem,
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
        doc_types (list[AutomationSearchCriteriaSchemaDocTypesItem] | Unset):
        execution_time (datetime.datetime | Unset):
        filter_ (CriteriaFilter | Unset):
    """

    automation_ids: list[UUID]
    doc_types: list[AutomationSearchCriteriaSchemaDocTypesItem] | Unset = UNSET
    execution_time: datetime.datetime | Unset = UNSET
    filter_: CriteriaFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation_ids = []
        for automation_ids_item_data in self.automation_ids:
            automation_ids_item = str(automation_ids_item_data)
            automation_ids.append(automation_ids_item)

        doc_types: list[str] | Unset = UNSET
        if not isinstance(self.doc_types, Unset):
            doc_types = []
            for doc_types_item_data in self.doc_types:
                doc_types_item = doc_types_item_data.value
                doc_types.append(doc_types_item)

        execution_time: str | Unset = UNSET
        if not isinstance(self.execution_time, Unset):
            execution_time = self.execution_time.isoformat()

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

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

        _doc_types = d.pop("doc_types", UNSET)
        doc_types: list[AutomationSearchCriteriaSchemaDocTypesItem] | Unset = UNSET
        if _doc_types is not UNSET:
            doc_types = []
            for doc_types_item_data in _doc_types:
                doc_types_item = AutomationSearchCriteriaSchemaDocTypesItem(
                    doc_types_item_data
                )

                doc_types.append(doc_types_item)

        _execution_time = d.pop("execution_time", UNSET)
        execution_time: datetime.datetime | Unset
        if isinstance(_execution_time, Unset):
            execution_time = UNSET
        else:
            execution_time = datetime.datetime.fromisoformat(_execution_time)

        _filter_ = d.pop("filter", UNSET)
        filter_: CriteriaFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = CriteriaFilter.from_dict(_filter_)

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
