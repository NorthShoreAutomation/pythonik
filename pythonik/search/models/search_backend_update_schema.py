from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_backend_update_schema_options_type_0 import (
        SearchBackendUpdateSchemaOptionsType0,
    )


T = TypeVar("T", bound="SearchBackendUpdateSchema")


@_attrs_define
class SearchBackendUpdateSchema:
    """PUT/PATCH body. ``kind`` is immutable: it may be echoed back unchanged
    (clients often resend what they read) but never altered.

        Attributes:
            enabled (bool | None | Unset):
            kind (None | str | Unset):
            name (None | str | Unset):
            options (None | SearchBackendUpdateSchemaOptionsType0 | Unset):
    """

    enabled: bool | None | Unset = UNSET
    kind: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    options: None | SearchBackendUpdateSchemaOptionsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_backend_update_schema_options_type_0 import (
            SearchBackendUpdateSchemaOptionsType0,
        )

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, SearchBackendUpdateSchemaOptionsType0):
            options = self.options.to_dict()
        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_backend_update_schema_options_type_0 import (
            SearchBackendUpdateSchemaOptionsType0,
        )

        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_options(
            data: object,
        ) -> None | SearchBackendUpdateSchemaOptionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = SearchBackendUpdateSchemaOptionsType0.from_dict(data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchBackendUpdateSchemaOptionsType0 | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        search_backend_update_schema = cls(
            enabled=enabled,
            kind=kind,
            name=name,
            options=options,
        )

        search_backend_update_schema.additional_properties = d
        return search_backend_update_schema

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
