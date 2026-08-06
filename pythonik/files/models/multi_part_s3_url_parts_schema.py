from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.multi_part_s3_url_part_schema import MultiPartS3UrlPartSchema


T = TypeVar("T", bound="MultiPartS3UrlPartsSchema")


@_attrs_define
class MultiPartS3UrlPartsSchema:
    """
    Attributes:
        parts (list[MultiPartS3UrlPartSchema]):
        upload_id (str):
    """

    parts: list[MultiPartS3UrlPartSchema]
    upload_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()
            parts.append(parts_item)

        upload_id = self.upload_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parts": parts,
                "upload_id": upload_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_part_s3_url_part_schema import MultiPartS3UrlPartSchema

        d = dict(src_dict)
        parts = []
        _parts = d.pop("parts")
        for parts_item_data in _parts:
            parts_item = MultiPartS3UrlPartSchema.from_dict(parts_item_data)

            parts.append(parts_item)

        upload_id = d.pop("upload_id")

        multi_part_s3_url_parts_schema = cls(
            parts=parts,
            upload_id=upload_id,
        )

        multi_part_s3_url_parts_schema.additional_properties = d
        return multi_part_s3_url_parts_schema

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
