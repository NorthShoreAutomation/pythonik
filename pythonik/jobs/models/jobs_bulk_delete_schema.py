from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsBulkDeleteSchema")


@_attrs_define
class JobsBulkDeleteSchema:
    """
    Attributes:
        job_ids (list[UUID] | None | Unset):
    """

    job_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_ids: list[str] | None | Unset
        if isinstance(self.job_ids, Unset):
            job_ids = UNSET
        elif isinstance(self.job_ids, list):
            job_ids = []
            for job_ids_type_0_item_data in self.job_ids:
                job_ids_type_0_item = str(job_ids_type_0_item_data)
                job_ids.append(job_ids_type_0_item)

        else:
            job_ids = self.job_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_ids is not UNSET:
            field_dict["job_ids"] = job_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_job_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_ids_type_0 = []
                _job_ids_type_0 = data
                for job_ids_type_0_item_data in _job_ids_type_0:
                    job_ids_type_0_item = UUID(job_ids_type_0_item_data)

                    job_ids_type_0.append(job_ids_type_0_item)

                return job_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        job_ids = _parse_job_ids(d.pop("job_ids", UNSET))

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
