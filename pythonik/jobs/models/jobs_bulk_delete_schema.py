from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsBulkDeleteSchema")


@_attrs_define
class JobsBulkDeleteSchema:
    """
    Attributes:
        job_ids (list[UUID] | Unset):
    """

    job_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_ids: list[str] | Unset = UNSET
        if not isinstance(self.job_ids, Unset):
            job_ids = []
            for job_ids_item_data in self.job_ids:
                job_ids_item = str(job_ids_item_data)
                job_ids.append(job_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_ids is not UNSET:
            field_dict["job_ids"] = job_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _job_ids = d.pop("job_ids", UNSET)
        job_ids: list[UUID] | Unset = UNSET
        if _job_ids is not UNSET:
            job_ids = []
            for job_ids_item_data in _job_ids:
                job_ids_item = UUID(job_ids_item_data)

                job_ids.append(job_ids_item)

        jobs_bulk_delete_schema = cls(
            job_ids=job_ids,
        )

        jobs_bulk_delete_schema.additional_properties = d
        return jobs_bulk_delete_schema

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
