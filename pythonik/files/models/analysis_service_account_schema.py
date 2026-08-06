from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_service_account_schema_method import (
    AnalysisServiceAccountSchemaMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_service_account_schema_settings import (
        AnalysisServiceAccountSchemaSettings,
    )


T = TypeVar("T", bound="AnalysisServiceAccountSchema")


@_attrs_define
class AnalysisServiceAccountSchema:
    """
    Attributes:
        method (AnalysisServiceAccountSchemaMethod):
        name (str):
        settings (AnalysisServiceAccountSchemaSettings):
        id (None | Unset | UUID):
    """

    method: AnalysisServiceAccountSchemaMethod
    name: str
    settings: AnalysisServiceAccountSchemaSettings
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        name = self.name

        settings = self.settings.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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
        from ..models.analysis_service_account_schema_settings import (
            AnalysisServiceAccountSchemaSettings,
        )

        d = dict(src_dict)
        method = AnalysisServiceAccountSchemaMethod(d.pop("method"))

        name = d.pop("name")

        settings = AnalysisServiceAccountSchemaSettings.from_dict(d.pop("settings"))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        analysis_service_account_schema = cls(
            method=method,
            name=name,
            settings=settings,
            id=id,
        )

        analysis_service_account_schema.additional_properties = d
        return analysis_service_account_schema

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
