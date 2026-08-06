from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetBatchExportItemSchema")


@_attrs_define
class AssetBatchExportItemSchema:
    """
    Attributes:
        asset_id (UUID):
        file_name (None | str | Unset):
        format_id (None | Unset | UUID):
    """

    asset_id: UUID
    file_name: None | str | Unset = UNSET
    format_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        format_id: None | str | Unset
        if isinstance(self.format_id, Unset):
            format_id = UNSET
        elif isinstance(self.format_id, UUID):
            format_id = str(self.format_id)
        else:
            format_id = self.format_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
            }
        )
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if format_id is not UNSET:
            field_dict["format_id"] = format_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_format_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_id_type_0 = UUID(data)

                return format_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        format_id = _parse_format_id(d.pop("format_id", UNSET))

        asset_batch_export_item_schema = cls(
            asset_id=asset_id,
            file_name=file_name,
            format_id=format_id,
        )

        asset_batch_export_item_schema.additional_properties = d
        return asset_batch_export_item_schema

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
