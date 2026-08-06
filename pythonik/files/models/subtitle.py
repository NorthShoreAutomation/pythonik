from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Subtitle")


@_attrs_define
class Subtitle:
    """
    Attributes:
        asset_id (UUID):
        closed_captions (bool):
        format_id (UUID):
        id (UUID):
        language (str):
        name (None | str | Unset):
        version_id (None | Unset | UUID):
    """

    asset_id: UUID
    closed_captions: bool
    format_id: UUID
    id: UUID
    language: str
    name: None | str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        closed_captions = self.closed_captions

        format_id = str(self.format_id)

        id = str(self.id)

        language = self.language

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        subtitle = cls(
            asset_id=asset_id,
            closed_captions=closed_captions,
            format_id=format_id,
            id=id,
            language=language,
            name=name,
            version_id=version_id,
        )

        subtitle.additional_properties = d
        return subtitle

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
