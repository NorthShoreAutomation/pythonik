from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IconikEdgeTranscoderSchema")


@_attrs_define
class IconikEdgeTranscoderSchema:
    """
    Attributes:
        enable_multi_channel_audio (bool | Unset):
        exclude_patterns (list[str] | Unset):
        include_patterns (list[str] | Unset):
        local (bool | Unset):
        max_transcoding_jobs (int | Unset):
        merge_multichannel_audio_tracks (bool | Unset):
        priority (int | None | Unset):
    """

    enable_multi_channel_audio: bool | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    local: bool | Unset = UNSET
    max_transcoding_jobs: int | Unset = UNSET
    merge_multichannel_audio_tracks: bool | Unset = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_multi_channel_audio = self.enable_multi_channel_audio

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        local = self.local

        max_transcoding_jobs = self.max_transcoding_jobs

        merge_multichannel_audio_tracks = self.merge_multichannel_audio_tracks

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_multi_channel_audio is not UNSET:
            field_dict["enable_multi_channel_audio"] = enable_multi_channel_audio
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if local is not UNSET:
            field_dict["local"] = local
        if max_transcoding_jobs is not UNSET:
            field_dict["max_transcoding_jobs"] = max_transcoding_jobs
        if merge_multichannel_audio_tracks is not UNSET:
            field_dict["merge_multichannel_audio_tracks"] = (
                merge_multichannel_audio_tracks
            )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_multi_channel_audio = d.pop("enable_multi_channel_audio", UNSET)

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        local = d.pop("local", UNSET)

        max_transcoding_jobs = d.pop("max_transcoding_jobs", UNSET)

        merge_multichannel_audio_tracks = d.pop(
            "merge_multichannel_audio_tracks", UNSET
        )

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        iconik_edge_transcoder_schema = cls(
            enable_multi_channel_audio=enable_multi_channel_audio,
            exclude_patterns=exclude_patterns,
            include_patterns=include_patterns,
            local=local,
            max_transcoding_jobs=max_transcoding_jobs,
            merge_multichannel_audio_tracks=merge_multichannel_audio_tracks,
            priority=priority,
        )

        iconik_edge_transcoder_schema.additional_properties = d
        return iconik_edge_transcoder_schema

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
