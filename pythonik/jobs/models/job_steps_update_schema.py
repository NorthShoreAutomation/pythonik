from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_step_update_bulk_schema import JobStepUpdateBulkSchema


T = TypeVar("T", bound="JobStepsUpdateSchema")


@_attrs_define
class JobStepsUpdateSchema:
    """
    Attributes:
        steps (list[JobStepUpdateBulkSchema]):
    """

    steps: list[JobStepUpdateBulkSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_step_update_bulk_schema import JobStepUpdateBulkSchema

        d = dict(src_dict)
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = JobStepUpdateBulkSchema.from_dict(steps_item_data)

            steps.append(steps_item)

        job_steps_update_schema = cls(
            steps=steps,
        )

        job_steps_update_schema.additional_properties = d
        return job_steps_update_schema

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
