from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalysisProfileServiceIdSchema")


@_attrs_define
class AnalysisProfileServiceIdSchema:
    """
    Attributes:
        analysis_service_account_id (UUID):
    """

    analysis_service_account_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis_service_account_id = str(self.analysis_service_account_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysis_service_account_id": analysis_service_account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        analysis_service_account_id = UUID(d.pop("analysis_service_account_id"))

        analysis_profile_service_id_schema = cls(
            analysis_service_account_id=analysis_service_account_id,
        )

        analysis_profile_service_id_schema.additional_properties = d
        return analysis_profile_service_id_schema

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
