from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcode_action_parameters_preferred_storage_method import (
    TranscodeActionParametersPreferredStorageMethod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscodeActionParameters")


@_attrs_define
class TranscodeActionParameters:
    """
    Attributes:
        format_name (None | str | Unset):  Default: 'ORIGINAL'.
        prefer_any_cloud (bool | None | Unset):
        preferred_storage_id (None | Unset | UUID):
        preferred_storage_method (None | TranscodeActionParametersPreferredStorageMethod | Unset):
        priority (int | None | Unset):
    """

    format_name: None | str | Unset = "ORIGINAL"
    prefer_any_cloud: bool | None | Unset = UNSET
    preferred_storage_id: None | Unset | UUID = UNSET
    preferred_storage_method: (
        None | TranscodeActionParametersPreferredStorageMethod | Unset
    ) = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_name: None | str | Unset
        if isinstance(self.format_name, Unset):
            format_name = UNSET
        else:
            format_name = self.format_name

        prefer_any_cloud: bool | None | Unset
        if isinstance(self.prefer_any_cloud, Unset):
            prefer_any_cloud = UNSET
        else:
            prefer_any_cloud = self.prefer_any_cloud

        preferred_storage_id: None | str | Unset
        if isinstance(self.preferred_storage_id, Unset):
            preferred_storage_id = UNSET
        elif isinstance(self.preferred_storage_id, UUID):
            preferred_storage_id = str(self.preferred_storage_id)
        else:
            preferred_storage_id = self.preferred_storage_id

        preferred_storage_method: None | str | Unset
        if isinstance(self.preferred_storage_method, Unset):
            preferred_storage_method = UNSET
        elif isinstance(
            self.preferred_storage_method,
            TranscodeActionParametersPreferredStorageMethod,
        ):
            preferred_storage_method = self.preferred_storage_method.value
        else:
            preferred_storage_method = self.preferred_storage_method

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_name is not UNSET:
            field_dict["format_name"] = format_name
        if prefer_any_cloud is not UNSET:
            field_dict["prefer_any_cloud"] = prefer_any_cloud
        if preferred_storage_id is not UNSET:
            field_dict["preferred_storage_id"] = preferred_storage_id
        if preferred_storage_method is not UNSET:
            field_dict["preferred_storage_method"] = preferred_storage_method
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_format_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_name = _parse_format_name(d.pop("format_name", UNSET))

        def _parse_prefer_any_cloud(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        prefer_any_cloud = _parse_prefer_any_cloud(d.pop("prefer_any_cloud", UNSET))

        def _parse_preferred_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_storage_id_type_0 = UUID(data)

                return preferred_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        preferred_storage_id = _parse_preferred_storage_id(
            d.pop("preferred_storage_id", UNSET)
        )

        def _parse_preferred_storage_method(
            data: object,
        ) -> None | TranscodeActionParametersPreferredStorageMethod | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_storage_method_type_1 = (
                    TranscodeActionParametersPreferredStorageMethod(data)
                )

                return preferred_storage_method_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TranscodeActionParametersPreferredStorageMethod | Unset, data
            )

        preferred_storage_method = _parse_preferred_storage_method(
            d.pop("preferred_storage_method", UNSET)
        )

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        transcode_action_parameters = cls(
            format_name=format_name,
            prefer_any_cloud=prefer_any_cloud,
            preferred_storage_id=preferred_storage_id,
            preferred_storage_method=preferred_storage_method,
            priority=priority,
        )

        transcode_action_parameters.additional_properties = d
        return transcode_action_parameters

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
