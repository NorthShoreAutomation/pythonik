from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestrictAssetActionParameters")


@_attrs_define
class RestrictAssetActionParameters:
    """
    Attributes:
        restrict_metadata_field (str):
        warning (str | Unset):
        warning_metadata_field (str | Unset):
    """

    restrict_metadata_field: str
    warning: str | Unset = UNSET
    warning_metadata_field: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restrict_metadata_field = self.restrict_metadata_field

        warning = self.warning

        warning_metadata_field = self.warning_metadata_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restrict_metadata_field": restrict_metadata_field,
            }
        )
        if warning is not UNSET:
            field_dict["warning"] = warning
        if warning_metadata_field is not UNSET:
            field_dict["warning_metadata_field"] = warning_metadata_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restrict_metadata_field = d.pop("restrict_metadata_field")

        warning = d.pop("warning", UNSET)

        warning_metadata_field = d.pop("warning_metadata_field", UNSET)

        restrict_asset_action_parameters = cls(
            restrict_metadata_field=restrict_metadata_field,
            warning=warning,
            warning_metadata_field=warning_metadata_field,
        )

        restrict_asset_action_parameters.additional_properties = d
        return restrict_asset_action_parameters

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
