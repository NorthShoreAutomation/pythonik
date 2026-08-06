from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopySourceQueryParamsSchema")


@_attrs_define
class CopySourceQueryParamsSchema:
    """
    Attributes:
        source_object_id (None | Unset | UUID):
        source_object_type (None | str | Unset):
        source_version_id (None | Unset | UUID):
    """

    source_object_id: None | Unset | UUID = UNSET
    source_object_type: None | str | Unset = UNSET
    source_version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_object_id: None | str | Unset
        if isinstance(self.source_object_id, Unset):
            source_object_id = UNSET
        elif isinstance(self.source_object_id, UUID):
            source_object_id = str(self.source_object_id)
        else:
            source_object_id = self.source_object_id

        source_object_type: None | str | Unset
        if isinstance(self.source_object_type, Unset):
            source_object_type = UNSET
        else:
            source_object_type = self.source_object_type

        source_version_id: None | str | Unset
        if isinstance(self.source_version_id, Unset):
            source_version_id = UNSET
        elif isinstance(self.source_version_id, UUID):
            source_version_id = str(self.source_version_id)
        else:
            source_version_id = self.source_version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_object_id is not UNSET:
            field_dict["source_object_id"] = source_object_id
        if source_object_type is not UNSET:
            field_dict["source_object_type"] = source_object_type
        if source_version_id is not UNSET:
            field_dict["source_version_id"] = source_version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_source_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_object_id_type_0 = UUID(data)

                return source_object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_object_id = _parse_source_object_id(d.pop("source_object_id", UNSET))

        def _parse_source_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_object_type = _parse_source_object_type(
            d.pop("source_object_type", UNSET)
        )

        def _parse_source_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_version_id_type_0 = UUID(data)

                return source_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_version_id = _parse_source_version_id(d.pop("source_version_id", UNSET))

        copy_source_query_params_schema = cls(
            source_object_id=source_object_id,
            source_object_type=source_object_type,
            source_version_id=source_version_id,
        )

        copy_source_query_params_schema.additional_properties = d
        return copy_source_query_params_schema

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
