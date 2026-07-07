from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.specified_keyframes import SpecifiedKeyframes


T = TypeVar("T", bound="GenerateCollectionKeyframeSchema")


@_attrs_define
class GenerateCollectionKeyframeSchema:
    """
    Attributes:
        deleted_asset_id (UUID | Unset):
        force (bool | Unset):
        specified_asset_ids (list[UUID] | Unset):
        specified_keyframes (list[SpecifiedKeyframes] | Unset):
    """

    deleted_asset_id: UUID | Unset = UNSET
    force: bool | Unset = UNSET
    specified_asset_ids: list[UUID] | Unset = UNSET
    specified_keyframes: list[SpecifiedKeyframes] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted_asset_id: str | Unset = UNSET
        if not isinstance(self.deleted_asset_id, Unset):
            deleted_asset_id = str(self.deleted_asset_id)

        force = self.force

        specified_asset_ids: list[str] | Unset = UNSET
        if not isinstance(self.specified_asset_ids, Unset):
            specified_asset_ids = []
            for specified_asset_ids_item_data in self.specified_asset_ids:
                specified_asset_ids_item = str(specified_asset_ids_item_data)
                specified_asset_ids.append(specified_asset_ids_item)

        specified_keyframes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.specified_keyframes, Unset):
            specified_keyframes = []
            for specified_keyframes_item_data in self.specified_keyframes:
                specified_keyframes_item = specified_keyframes_item_data.to_dict()
                specified_keyframes.append(specified_keyframes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted_asset_id is not UNSET:
            field_dict["deleted_asset_id"] = deleted_asset_id
        if force is not UNSET:
            field_dict["force"] = force
        if specified_asset_ids is not UNSET:
            field_dict["specified_asset_ids"] = specified_asset_ids
        if specified_keyframes is not UNSET:
            field_dict["specified_keyframes"] = specified_keyframes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.specified_keyframes import SpecifiedKeyframes

        d = dict(src_dict)
        _deleted_asset_id = d.pop("deleted_asset_id", UNSET)
        deleted_asset_id: UUID | Unset
        if isinstance(_deleted_asset_id, Unset):
            deleted_asset_id = UNSET
        else:
            deleted_asset_id = UUID(_deleted_asset_id)

        force = d.pop("force", UNSET)

        _specified_asset_ids = d.pop("specified_asset_ids", UNSET)
        specified_asset_ids: list[UUID] | Unset = UNSET
        if _specified_asset_ids is not UNSET:
            specified_asset_ids = []
            for specified_asset_ids_item_data in _specified_asset_ids:
                specified_asset_ids_item = UUID(specified_asset_ids_item_data)

                specified_asset_ids.append(specified_asset_ids_item)

        _specified_keyframes = d.pop("specified_keyframes", UNSET)
        specified_keyframes: list[SpecifiedKeyframes] | Unset = UNSET
        if _specified_keyframes is not UNSET:
            specified_keyframes = []
            for specified_keyframes_item_data in _specified_keyframes:
                specified_keyframes_item = SpecifiedKeyframes.from_dict(
                    specified_keyframes_item_data
                )

                specified_keyframes.append(specified_keyframes_item)

        generate_collection_keyframe_schema = cls(
            deleted_asset_id=deleted_asset_id,
            force=force,
            specified_asset_ids=specified_asset_ids,
            specified_keyframes=specified_keyframes,
        )

        generate_collection_keyframe_schema.additional_properties = d
        return generate_collection_keyframe_schema

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
