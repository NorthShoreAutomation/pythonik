from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.video_base_schema_scaling_method import VideoBaseSchemaScalingMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoBaseSchema")


@_attrs_define
class VideoBaseSchema:
    """
    Attributes:
        audio_bitrate (int | Unset):
        bitrate (int | Unset):
        edit_proxy_folder (None | str | Unset):
        enable_multi_channel_audio (bool | Unset):
        exclude_patterns (list[str] | Unset):
        hdr_brightness (float | None | Unset):
        hdr_contrast (float | None | Unset):
        hdr_gamma (float | None | Unset):
        hdr_saturation (float | None | Unset):
        hdr_tonemap_desat (float | None | Unset):
        hdr_tonemap_peak (float | None | Unset):
        include_patterns (list[str] | Unset):
        local (bool | Unset):
        merge_multichannel_audio_tracks (bool | Unset):
        priority (int | None | Unset):
        scaling_method (VideoBaseSchemaScalingMethod | Unset):
        width (int | Unset):
    """

    audio_bitrate: int | Unset = UNSET
    bitrate: int | Unset = UNSET
    edit_proxy_folder: None | str | Unset = UNSET
    enable_multi_channel_audio: bool | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    hdr_brightness: float | None | Unset = UNSET
    hdr_contrast: float | None | Unset = UNSET
    hdr_gamma: float | None | Unset = UNSET
    hdr_saturation: float | None | Unset = UNSET
    hdr_tonemap_desat: float | None | Unset = UNSET
    hdr_tonemap_peak: float | None | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    local: bool | Unset = UNSET
    merge_multichannel_audio_tracks: bool | Unset = UNSET
    priority: int | None | Unset = UNSET
    scaling_method: VideoBaseSchemaScalingMethod | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio_bitrate = self.audio_bitrate

        bitrate = self.bitrate

        edit_proxy_folder: None | str | Unset
        if isinstance(self.edit_proxy_folder, Unset):
            edit_proxy_folder = UNSET
        else:
            edit_proxy_folder = self.edit_proxy_folder

        enable_multi_channel_audio = self.enable_multi_channel_audio

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        hdr_brightness: float | None | Unset
        if isinstance(self.hdr_brightness, Unset):
            hdr_brightness = UNSET
        else:
            hdr_brightness = self.hdr_brightness

        hdr_contrast: float | None | Unset
        if isinstance(self.hdr_contrast, Unset):
            hdr_contrast = UNSET
        else:
            hdr_contrast = self.hdr_contrast

        hdr_gamma: float | None | Unset
        if isinstance(self.hdr_gamma, Unset):
            hdr_gamma = UNSET
        else:
            hdr_gamma = self.hdr_gamma

        hdr_saturation: float | None | Unset
        if isinstance(self.hdr_saturation, Unset):
            hdr_saturation = UNSET
        else:
            hdr_saturation = self.hdr_saturation

        hdr_tonemap_desat: float | None | Unset
        if isinstance(self.hdr_tonemap_desat, Unset):
            hdr_tonemap_desat = UNSET
        else:
            hdr_tonemap_desat = self.hdr_tonemap_desat

        hdr_tonemap_peak: float | None | Unset
        if isinstance(self.hdr_tonemap_peak, Unset):
            hdr_tonemap_peak = UNSET
        else:
            hdr_tonemap_peak = self.hdr_tonemap_peak

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        local = self.local

        merge_multichannel_audio_tracks = self.merge_multichannel_audio_tracks

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        scaling_method: str | Unset = UNSET
        if not isinstance(self.scaling_method, Unset):
            scaling_method = self.scaling_method.value

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audio_bitrate is not UNSET:
            field_dict["audio_bitrate"] = audio_bitrate
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if edit_proxy_folder is not UNSET:
            field_dict["edit_proxy_folder"] = edit_proxy_folder
        if enable_multi_channel_audio is not UNSET:
            field_dict["enable_multi_channel_audio"] = enable_multi_channel_audio
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if hdr_brightness is not UNSET:
            field_dict["hdr_brightness"] = hdr_brightness
        if hdr_contrast is not UNSET:
            field_dict["hdr_contrast"] = hdr_contrast
        if hdr_gamma is not UNSET:
            field_dict["hdr_gamma"] = hdr_gamma
        if hdr_saturation is not UNSET:
            field_dict["hdr_saturation"] = hdr_saturation
        if hdr_tonemap_desat is not UNSET:
            field_dict["hdr_tonemap_desat"] = hdr_tonemap_desat
        if hdr_tonemap_peak is not UNSET:
            field_dict["hdr_tonemap_peak"] = hdr_tonemap_peak
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if local is not UNSET:
            field_dict["local"] = local
        if merge_multichannel_audio_tracks is not UNSET:
            field_dict["merge_multichannel_audio_tracks"] = (
                merge_multichannel_audio_tracks
            )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if scaling_method is not UNSET:
            field_dict["scaling_method"] = scaling_method
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audio_bitrate = d.pop("audio_bitrate", UNSET)

        bitrate = d.pop("bitrate", UNSET)

        def _parse_edit_proxy_folder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_proxy_folder = _parse_edit_proxy_folder(d.pop("edit_proxy_folder", UNSET))

        enable_multi_channel_audio = d.pop("enable_multi_channel_audio", UNSET)

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        def _parse_hdr_brightness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hdr_brightness = _parse_hdr_brightness(d.pop("hdr_brightness", UNSET))

        def _parse_hdr_contrast(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hdr_contrast = _parse_hdr_contrast(d.pop("hdr_contrast", UNSET))

        def _parse_hdr_gamma(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hdr_gamma = _parse_hdr_gamma(d.pop("hdr_gamma", UNSET))

        def _parse_hdr_saturation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hdr_saturation = _parse_hdr_saturation(d.pop("hdr_saturation", UNSET))

        def _parse_hdr_tonemap_desat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hdr_tonemap_desat = _parse_hdr_tonemap_desat(d.pop("hdr_tonemap_desat", UNSET))

        def _parse_hdr_tonemap_peak(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hdr_tonemap_peak = _parse_hdr_tonemap_peak(d.pop("hdr_tonemap_peak", UNSET))

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        local = d.pop("local", UNSET)

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

        _scaling_method = d.pop("scaling_method", UNSET)
        scaling_method: VideoBaseSchemaScalingMethod | Unset
        if isinstance(_scaling_method, Unset):
            scaling_method = UNSET
        else:
            scaling_method = VideoBaseSchemaScalingMethod(_scaling_method)

        width = d.pop("width", UNSET)

        video_base_schema = cls(
            audio_bitrate=audio_bitrate,
            bitrate=bitrate,
            edit_proxy_folder=edit_proxy_folder,
            enable_multi_channel_audio=enable_multi_channel_audio,
            exclude_patterns=exclude_patterns,
            hdr_brightness=hdr_brightness,
            hdr_contrast=hdr_contrast,
            hdr_gamma=hdr_gamma,
            hdr_saturation=hdr_saturation,
            hdr_tonemap_desat=hdr_tonemap_desat,
            hdr_tonemap_peak=hdr_tonemap_peak,
            include_patterns=include_patterns,
            local=local,
            merge_multichannel_audio_tracks=merge_multichannel_audio_tracks,
            priority=priority,
            scaling_method=scaling_method,
            width=width,
        )

        video_base_schema.additional_properties = d
        return video_base_schema

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
