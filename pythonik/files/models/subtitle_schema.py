from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubtitleSchema")


@_attrs_define
class SubtitleSchema:
    """
    Attributes:
        asset_id (UUID):
        closed_captions (bool):
        format_id (UUID):
        id (UUID):
        language (str):
        content (str | Unset):
        name (str | Unset):
        version_id (UUID | Unset):
    """

    asset_id: UUID
    closed_captions: bool
    format_id: UUID
    id: UUID
    language: str
    content: str | Unset = UNSET
    name: str | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        closed_captions = self.closed_captions

        format_id = str(self.format_id)

        id = str(self.id)

        language = self.language

        content = self.content

        name = self.name

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "closed_captions": closed_captions,
                "format_id": format_id,
                "id": id,
                "language": language,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if name is not UNSET:
            field_dict["name"] = name
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        closed_captions = d.pop("closed_captions")

        format_id = UUID(d.pop("format_id"))

        id = UUID(d.pop("id"))

        language = d.pop("language")

        content = d.pop("content", UNSET)

        name = d.pop("name", UNSET)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        subtitle_schema = cls(
            asset_id=asset_id,
            closed_captions=closed_captions,
            format_id=format_id,
            id=id,
            language=language,
            content=content,
            name=name,
            version_id=version_id,
        )

        subtitle_schema.additional_properties = d
        return subtitle_schema

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
