from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetSubclipKeyframesSchema")


@_attrs_define
class AssetSubclipKeyframesSchema:
    """
    Attributes:
        asset_id (UUID):
        original_asset_id (UUID):
        original_version_id (UUID):
        time_end_milliseconds (int):
        time_start_milliseconds (int):
        version_id (UUID):
        filename (str | Unset):
        name (str | Unset):
        original_segment_id (UUID | Unset):
    """

    asset_id: UUID
    original_asset_id: UUID
    original_version_id: UUID
    time_end_milliseconds: int
    time_start_milliseconds: int
    version_id: UUID
    filename: str | Unset = UNSET
    name: str | Unset = UNSET
    original_segment_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        original_asset_id = str(self.original_asset_id)

        original_version_id = str(self.original_version_id)

        time_end_milliseconds = self.time_end_milliseconds

        time_start_milliseconds = self.time_start_milliseconds

        version_id = str(self.version_id)

        filename = self.filename

        name = self.name

        original_segment_id: str | Unset = UNSET
        if not isinstance(self.original_segment_id, Unset):
            original_segment_id = str(self.original_segment_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "original_asset_id": original_asset_id,
                "original_version_id": original_version_id,
                "time_end_milliseconds": time_end_milliseconds,
                "time_start_milliseconds": time_start_milliseconds,
                "version_id": version_id,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename
        if name is not UNSET:
            field_dict["name"] = name
        if original_segment_id is not UNSET:
            field_dict["original_segment_id"] = original_segment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        original_asset_id = UUID(d.pop("original_asset_id"))

        original_version_id = UUID(d.pop("original_version_id"))

        time_end_milliseconds = d.pop("time_end_milliseconds")

        time_start_milliseconds = d.pop("time_start_milliseconds")

        version_id = UUID(d.pop("version_id"))

        filename = d.pop("filename", UNSET)

        name = d.pop("name", UNSET)

        _original_segment_id = d.pop("original_segment_id", UNSET)
        original_segment_id: UUID | Unset
        if isinstance(_original_segment_id, Unset):
            original_segment_id = UNSET
        else:
            original_segment_id = UUID(_original_segment_id)

        asset_subclip_keyframes_schema = cls(
            asset_id=asset_id,
            original_asset_id=original_asset_id,
            original_version_id=original_version_id,
            time_end_milliseconds=time_end_milliseconds,
            time_start_milliseconds=time_start_milliseconds,
            version_id=version_id,
            filename=filename,
            name=name,
            original_segment_id=original_segment_id,
        )

        asset_subclip_keyframes_schema.additional_properties = d
        return asset_subclip_keyframes_schema

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
