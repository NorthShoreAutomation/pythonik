from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetVersionSchema")


@_attrs_define
class AssetVersionSchema:
    """
    Attributes:
        asset_id (UUID | Unset):
        face_ids (list[UUID] | Unset):
        segment_count (int | Unset):
        version_id (UUID | Unset):
    """

    asset_id: UUID | Unset = UNSET
    face_ids: list[UUID] | Unset = UNSET
    segment_count: int | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        face_ids: list[str] | Unset = UNSET
        if not isinstance(self.face_ids, Unset):
            face_ids = []
            for face_ids_item_data in self.face_ids:
                face_ids_item = str(face_ids_item_data)
                face_ids.append(face_ids_item)

        segment_count = self.segment_count

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if face_ids is not UNSET:
            field_dict["face_ids"] = face_ids
        if segment_count is not UNSET:
            field_dict["segment_count"] = segment_count
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        _face_ids = d.pop("face_ids", UNSET)
        face_ids: list[UUID] | Unset = UNSET
        if _face_ids is not UNSET:
            face_ids = []
            for face_ids_item_data in _face_ids:
                face_ids_item = UUID(face_ids_item_data)

                face_ids.append(face_ids_item)

        segment_count = d.pop("segment_count", UNSET)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        asset_version_schema = cls(
            asset_id=asset_id,
            face_ids=face_ids,
            segment_count=segment_count,
            version_id=version_id,
        )

        asset_version_schema.additional_properties = d
        return asset_version_schema

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
