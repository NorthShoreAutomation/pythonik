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
        enable_multi_channel_audio (bool | None | Unset):
        exclude_patterns (list[str] | None | Unset):
        include_patterns (list[str] | None | Unset):
        local (bool | None | Unset):
        max_transcoding_jobs (int | None | Unset):
        merge_multichannel_audio_tracks (bool | None | Unset):
        priority (int | None | Unset):
    """

    enable_multi_channel_audio: bool | None | Unset = UNSET
    exclude_patterns: list[str] | None | Unset = UNSET
    include_patterns: list[str] | None | Unset = UNSET
    local: bool | None | Unset = UNSET
    max_transcoding_jobs: int | None | Unset = UNSET
    merge_multichannel_audio_tracks: bool | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_multi_channel_audio: bool | None | Unset
        if isinstance(self.enable_multi_channel_audio, Unset):
            enable_multi_channel_audio = UNSET
        else:
            enable_multi_channel_audio = self.enable_multi_channel_audio

        exclude_patterns: list[str] | None | Unset
        if isinstance(self.exclude_patterns, Unset):
            exclude_patterns = UNSET
        elif isinstance(self.exclude_patterns, list):
            exclude_patterns = self.exclude_patterns

        else:
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | None | Unset
        if isinstance(self.include_patterns, Unset):
            include_patterns = UNSET
        elif isinstance(self.include_patterns, list):
            include_patterns = self.include_patterns

        else:
            include_patterns = self.include_patterns

        local: bool | None | Unset
        if isinstance(self.local, Unset):
            local = UNSET
        else:
            local = self.local

        max_transcoding_jobs: int | None | Unset
        if isinstance(self.max_transcoding_jobs, Unset):
            max_transcoding_jobs = UNSET
        else:
            max_transcoding_jobs = self.max_transcoding_jobs

        merge_multichannel_audio_tracks: bool | None | Unset
        if isinstance(self.merge_multichannel_audio_tracks, Unset):
            merge_multichannel_audio_tracks = UNSET
        else:
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

        def _parse_enable_multi_channel_audio(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_multi_channel_audio = _parse_enable_multi_channel_audio(
            d.pop("enable_multi_channel_audio", UNSET)
        )

        def _parse_exclude_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_patterns_type_0 = cast(list[str], data)

                return exclude_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_patterns = _parse_exclude_patterns(d.pop("exclude_patterns", UNSET))

        def _parse_include_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_patterns_type_0 = cast(list[str], data)

                return include_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_patterns = _parse_include_patterns(d.pop("include_patterns", UNSET))

        def _parse_local(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        local = _parse_local(d.pop("local", UNSET))

        def _parse_max_transcoding_jobs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_transcoding_jobs = _parse_max_transcoding_jobs(
            d.pop("max_transcoding_jobs", UNSET)
        )

        def _parse_merge_multichannel_audio_tracks(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        merge_multichannel_audio_tracks = _parse_merge_multichannel_audio_tracks(
            d.pop("merge_multichannel_audio_tracks", UNSET)
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
