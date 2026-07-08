from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
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
        deleted_asset_id (None | Unset | UUID):
        force (bool | None | Unset):
        specified_asset_ids (list[UUID] | None | Unset):
        specified_keyframes (list[SpecifiedKeyframes] | None | Unset):
    """

    deleted_asset_id: None | Unset | UUID = UNSET
    force: bool | None | Unset = UNSET
    specified_asset_ids: list[UUID] | None | Unset = UNSET
    specified_keyframes: list[SpecifiedKeyframes] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted_asset_id: None | str | Unset
        if isinstance(self.deleted_asset_id, Unset):
            deleted_asset_id = UNSET
        elif isinstance(self.deleted_asset_id, UUID):
            deleted_asset_id = str(self.deleted_asset_id)
        else:
            deleted_asset_id = self.deleted_asset_id

        force: bool | None | Unset
        if isinstance(self.force, Unset):
            force = UNSET
        else:
            force = self.force

        specified_asset_ids: list[str] | None | Unset
        if isinstance(self.specified_asset_ids, Unset):
            specified_asset_ids = UNSET
        elif isinstance(self.specified_asset_ids, list):
            specified_asset_ids = []
            for specified_asset_ids_type_0_item_data in self.specified_asset_ids:
                specified_asset_ids_type_0_item = str(
                    specified_asset_ids_type_0_item_data
                )
                specified_asset_ids.append(specified_asset_ids_type_0_item)

        else:
            specified_asset_ids = self.specified_asset_ids

        specified_keyframes: list[dict[str, Any]] | None | Unset
        if isinstance(self.specified_keyframes, Unset):
            specified_keyframes = UNSET
        elif isinstance(self.specified_keyframes, list):
            specified_keyframes = []
            for specified_keyframes_type_0_item_data in self.specified_keyframes:
                specified_keyframes_type_0_item = (
                    specified_keyframes_type_0_item_data.to_dict()
                )
                specified_keyframes.append(specified_keyframes_type_0_item)

        else:
            specified_keyframes = self.specified_keyframes

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

        def _parse_deleted_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_asset_id_type_0 = UUID(data)

                return deleted_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deleted_asset_id = _parse_deleted_asset_id(d.pop("deleted_asset_id", UNSET))

        def _parse_force(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force = _parse_force(d.pop("force", UNSET))

        def _parse_specified_asset_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                specified_asset_ids_type_0 = []
                _specified_asset_ids_type_0 = data
                for specified_asset_ids_type_0_item_data in _specified_asset_ids_type_0:
                    specified_asset_ids_type_0_item = UUID(
                        specified_asset_ids_type_0_item_data
                    )

                    specified_asset_ids_type_0.append(specified_asset_ids_type_0_item)

                return specified_asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        specified_asset_ids = _parse_specified_asset_ids(
            d.pop("specified_asset_ids", UNSET)
        )

        def _parse_specified_keyframes(
            data: object,
        ) -> list[SpecifiedKeyframes] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                specified_keyframes_type_0 = []
                _specified_keyframes_type_0 = data
                for specified_keyframes_type_0_item_data in _specified_keyframes_type_0:
                    specified_keyframes_type_0_item = SpecifiedKeyframes.from_dict(
                        specified_keyframes_type_0_item_data
                    )

                    specified_keyframes_type_0.append(specified_keyframes_type_0_item)

                return specified_keyframes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SpecifiedKeyframes] | None | Unset, data)

        specified_keyframes = _parse_specified_keyframes(
            d.pop("specified_keyframes", UNSET)
        )

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
