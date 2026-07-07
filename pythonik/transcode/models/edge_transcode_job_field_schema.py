from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EdgeTranscodeJobFieldSchema")


@_attrs_define
class EdgeTranscodeJobFieldSchema:
    """
    Attributes:
        height (int | Unset):
        id (str | Unset):
        width (int | Unset):
    """

    height: int | Unset = UNSET
    id: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        id = self.id

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        width = d.pop("width", UNSET)

        edge_transcode_job_field_schema = cls(
            height=height,
            id=id,
            width=width,
        )

        edge_transcode_job_field_schema.additional_properties = d
        return edge_transcode_job_field_schema

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
