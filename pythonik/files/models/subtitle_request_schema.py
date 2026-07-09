from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubtitleRequestSchema")


@_attrs_define
class SubtitleRequestSchema:
    """
    Attributes:
        create_transcription (bool | None | Unset):
        delete_old_transcriptions (bool | None | Unset):
        priority (int | None | Unset):
    """

    create_transcription: bool | None | Unset = UNSET
    delete_old_transcriptions: bool | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_transcription: bool | None | Unset
        if isinstance(self.create_transcription, Unset):
            create_transcription = UNSET
        else:
            create_transcription = self.create_transcription

        delete_old_transcriptions: bool | None | Unset
        if isinstance(self.delete_old_transcriptions, Unset):
            delete_old_transcriptions = UNSET
        else:
            delete_old_transcriptions = self.delete_old_transcriptions

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_transcription is not UNSET:
            field_dict["create_transcription"] = create_transcription
        if delete_old_transcriptions is not UNSET:
            field_dict["delete_old_transcriptions"] = delete_old_transcriptions
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_create_transcription(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        create_transcription = _parse_create_transcription(
            d.pop("create_transcription", UNSET)
        )

        def _parse_delete_old_transcriptions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_old_transcriptions = _parse_delete_old_transcriptions(
            d.pop("delete_old_transcriptions", UNSET)
        )

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        subtitle_request_schema = cls(
            create_transcription=create_transcription,
            delete_old_transcriptions=delete_old_transcriptions,
            priority=priority,
        )

        subtitle_request_schema.additional_properties = d
        return subtitle_request_schema

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
