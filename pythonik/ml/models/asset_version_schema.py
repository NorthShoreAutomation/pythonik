from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetVersionSchema")


@_attrs_define
class AssetVersionSchema:
    """
    Attributes:
        asset_id (None | Unset | UUID):
        face_ids (list[UUID] | None | Unset):
        segment_count (int | None | Unset):
        version_id (None | Unset | UUID):
    """

    asset_id: None | Unset | UUID = UNSET
    face_ids: list[UUID] | None | Unset = UNSET
    segment_count: int | None | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        face_ids: list[str] | None | Unset
        if isinstance(self.face_ids, Unset):
            face_ids = UNSET
        elif isinstance(self.face_ids, list):
            face_ids = []
            for face_ids_type_0_item_data in self.face_ids:
                face_ids_type_0_item = str(face_ids_type_0_item_data)
                face_ids.append(face_ids_type_0_item)

        else:
            face_ids = self.face_ids

        segment_count: int | None | Unset
        if isinstance(self.segment_count, Unset):
            segment_count = UNSET
        else:
            segment_count = self.segment_count

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

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

        def _parse_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_id_type_0 = UUID(data)

                return asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_face_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                face_ids_type_0 = []
                _face_ids_type_0 = data
                for face_ids_type_0_item_data in _face_ids_type_0:
                    face_ids_type_0_item = UUID(face_ids_type_0_item_data)

                    face_ids_type_0.append(face_ids_type_0_item)

                return face_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        face_ids = _parse_face_ids(d.pop("face_ids", UNSET))

        def _parse_segment_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        segment_count = _parse_segment_count(d.pop("segment_count", UNSET))

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

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
