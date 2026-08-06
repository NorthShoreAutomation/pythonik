from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_publication_job_thumbnail_keyframe_type import (
    CreatePublicationJobThumbnailKeyframeType,
)

T = TypeVar("T", bound="CreatePublicationJobThumbnailKeyframe")


@_attrs_define
class CreatePublicationJobThumbnailKeyframe:
    """
    Attributes:
        asset_id (str):
        keyframe_id (str):
        type_ (CreatePublicationJobThumbnailKeyframeType):  Default: CreatePublicationJobThumbnailKeyframeType.KEYFRAME.
    """

    asset_id: str
    keyframe_id: str
    type_: CreatePublicationJobThumbnailKeyframeType = (
        CreatePublicationJobThumbnailKeyframeType.KEYFRAME
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        keyframe_id = self.keyframe_id

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "keyframe_id": keyframe_id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        keyframe_id = d.pop("keyframe_id")

        type_ = CreatePublicationJobThumbnailKeyframeType(d.pop("type"))

        create_publication_job_thumbnail_keyframe = cls(
            asset_id=asset_id,
            keyframe_id=keyframe_id,
            type_=type_,
        )

        create_publication_job_thumbnail_keyframe.additional_properties = d
        return create_publication_job_thumbnail_keyframe

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
