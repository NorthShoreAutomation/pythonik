from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyframe import Keyframe


T = TypeVar("T", bound="AssetVersionKeyframesSchema")


@_attrs_define
class AssetVersionKeyframesSchema:
    """
    Attributes:
        asset_id (UUID):
        version_id (str):
        keyframes (list[Keyframe] | None | Unset):
    """

    asset_id: UUID
    version_id: str
    keyframes: list[Keyframe] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        version_id = self.version_id

        keyframes: list[dict[str, Any]] | None | Unset
        if isinstance(self.keyframes, Unset):
            keyframes = UNSET
        elif isinstance(self.keyframes, list):
            keyframes = []
            for keyframes_type_0_item_data in self.keyframes:
                keyframes_type_0_item = keyframes_type_0_item_data.to_dict()
                keyframes.append(keyframes_type_0_item)

        else:
            keyframes = self.keyframes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "version_id": version_id,
            }
        )
        if keyframes is not UNSET:
            field_dict["keyframes"] = keyframes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.keyframe import Keyframe

        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        version_id = d.pop("version_id")

        def _parse_keyframes(data: object) -> list[Keyframe] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyframes_type_0 = []
                _keyframes_type_0 = data
                for keyframes_type_0_item_data in _keyframes_type_0:
                    keyframes_type_0_item = Keyframe.from_dict(
                        keyframes_type_0_item_data
                    )

                    keyframes_type_0.append(keyframes_type_0_item)

                return keyframes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Keyframe] | None | Unset, data)

        keyframes = _parse_keyframes(d.pop("keyframes", UNSET))

        asset_version_keyframes_schema = cls(
            asset_id=asset_id,
            version_id=version_id,
            keyframes=keyframes,
        )

        asset_version_keyframes_schema.additional_properties = d
        return asset_version_keyframes_schema

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
