from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.global_settings_schema_log_level import GlobalSettingsSchemaLogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalSettingsSchema")


@_attrs_define
class GlobalSettingsSchema:
    """
    Attributes:
        debug (bool | None | Unset):
        log_level (GlobalSettingsSchemaLogLevel | None | Unset):
    """

    debug: bool | None | Unset = UNSET
    log_level: GlobalSettingsSchemaLogLevel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debug: bool | None | Unset
        if isinstance(self.debug, Unset):
            debug = UNSET
        else:
            debug = self.debug

        log_level: None | str | Unset
        if isinstance(self.log_level, Unset):
            log_level = UNSET
        elif isinstance(self.log_level, GlobalSettingsSchemaLogLevel):
            log_level = self.log_level.value
        else:
            log_level = self.log_level

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

        def _parse_debug(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        debug = _parse_debug(d.pop("debug", UNSET))

        def _parse_log_level(
            data: object,
        ) -> GlobalSettingsSchemaLogLevel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                log_level_type_1 = GlobalSettingsSchemaLogLevel(data)

                return log_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GlobalSettingsSchemaLogLevel | None | Unset, data)

        log_level = _parse_log_level(d.pop("log_level", UNSET))

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
