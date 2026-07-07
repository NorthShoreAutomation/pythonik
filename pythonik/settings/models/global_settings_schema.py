from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.global_settings_schema_log_level import GlobalSettingsSchemaLogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalSettingsSchema")


@_attrs_define
class GlobalSettingsSchema:
    """
    Attributes:
        debug (bool | Unset):
        log_level (GlobalSettingsSchemaLogLevel | Unset):
    """

    debug: bool | Unset = UNSET
    log_level: GlobalSettingsSchemaLogLevel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debug = self.debug

        log_level: str | Unset = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if debug is not UNSET:
            field_dict["debug"] = debug
        if log_level is not UNSET:
            field_dict["log_level"] = log_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        debug = d.pop("debug", UNSET)

        _log_level = d.pop("log_level", UNSET)
        log_level: GlobalSettingsSchemaLogLevel | Unset
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = GlobalSettingsSchemaLogLevel(_log_level)

        global_settings_schema = cls(
            debug=debug,
            log_level=log_level,
        )

        global_settings_schema.additional_properties = d
        return global_settings_schema

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
