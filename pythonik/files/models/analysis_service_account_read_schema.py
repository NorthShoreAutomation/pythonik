from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_service_account_read_schema_method import (
    AnalysisServiceAccountReadSchemaMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_service_account_read_schema_settings import (
        AnalysisServiceAccountReadSchemaSettings,
    )


T = TypeVar("T", bound="AnalysisServiceAccountReadSchema")


@_attrs_define
class AnalysisServiceAccountReadSchema:
    """
    Attributes:
        method (AnalysisServiceAccountReadSchemaMethod):
        name (str):
        settings (AnalysisServiceAccountReadSchemaSettings):
        id (UUID | Unset):
    """

    method: AnalysisServiceAccountReadSchemaMethod
    name: str
    settings: AnalysisServiceAccountReadSchemaSettings
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        name = self.name

        settings = self.settings.to_dict()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "name": name,
                "settings": settings,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analysis_service_account_read_schema_settings import (
            AnalysisServiceAccountReadSchemaSettings,
        )

        d = dict(src_dict)
        method = AnalysisServiceAccountReadSchemaMethod(d.pop("method"))

        name = d.pop("name")

        settings = AnalysisServiceAccountReadSchemaSettings.from_dict(d.pop("settings"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        analysis_service_account_read_schema = cls(
            method=method,
            name=name,
            settings=settings,
            id=id,
        )

        analysis_service_account_read_schema.additional_properties = d
        return analysis_service_account_read_schema

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
