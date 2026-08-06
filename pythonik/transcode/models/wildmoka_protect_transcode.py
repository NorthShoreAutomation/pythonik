from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wildmoka_protect_transcode_callback_headers import (
        WildmokaProtectTranscodeCallbackHeaders,
    )
    from ..models.wildmoka_protect_transcode_create_file_callback_payload import (
        WildmokaProtectTranscodeCreateFileCallbackPayload,
    )


T = TypeVar("T", bound="WildmokaProtectTranscode")


@_attrs_define
class WildmokaProtectTranscode:
    """
    Attributes:
        asset_id (str):
        callback_headers (WildmokaProtectTranscodeCallbackHeaders):
        component_type (str):
        container_id (str):
        create_file_callback_payload (WildmokaProtectTranscodeCreateFileCallbackPayload):
        create_file_callback_url (str):
        drm (str):
        drm_asset_id (str):
        frame_count (int):
        frame_rate (float):
        has_audio (bool):
        height (int):
        input_url (str):
        monitor_job_id (str):
        proxy_id (str):
        segment_duration (int):
        update_file_status_callback_url (str):
        watermark (str):
        watermark_id (None | str):
        width (int):
    """

    asset_id: str
    callback_headers: WildmokaProtectTranscodeCallbackHeaders
    component_type: str
    container_id: str
    create_file_callback_payload: WildmokaProtectTranscodeCreateFileCallbackPayload
    create_file_callback_url: str
    drm: str
    drm_asset_id: str
    frame_count: int
    frame_rate: float
    has_audio: bool
    height: int
    input_url: str
    monitor_job_id: str
    proxy_id: str
    segment_duration: int
    update_file_status_callback_url: str
    watermark: str
    watermark_id: None | str
    width: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        callback_headers = self.callback_headers.to_dict()

        component_type = self.component_type

        container_id = self.container_id

        create_file_callback_payload = self.create_file_callback_payload.to_dict()

        create_file_callback_url = self.create_file_callback_url

        drm = self.drm

        drm_asset_id = self.drm_asset_id

        frame_count = self.frame_count

        frame_rate = self.frame_rate

        has_audio = self.has_audio

        height = self.height

        input_url = self.input_url

        monitor_job_id = self.monitor_job_id

        proxy_id = self.proxy_id

        segment_duration = self.segment_duration

        update_file_status_callback_url = self.update_file_status_callback_url

        watermark = self.watermark

        watermark_id: None | str
        watermark_id = self.watermark_id

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "callback_headers": callback_headers,
                "component_type": component_type,
                "container_id": container_id,
                "create_file_callback_payload": create_file_callback_payload,
                "create_file_callback_url": create_file_callback_url,
                "drm": drm,
                "drm_asset_id": drm_asset_id,
                "frame_count": frame_count,
                "frame_rate": frame_rate,
                "has_audio": has_audio,
                "height": height,
                "input_url": input_url,
                "monitor_job_id": monitor_job_id,
                "proxy_id": proxy_id,
                "segment_duration": segment_duration,
                "update_file_status_callback_url": update_file_status_callback_url,
                "watermark": watermark,
                "watermark_id": watermark_id,
                "width": width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wildmoka_protect_transcode_callback_headers import (
            WildmokaProtectTranscodeCallbackHeaders,
        )
        from ..models.wildmoka_protect_transcode_create_file_callback_payload import (
            WildmokaProtectTranscodeCreateFileCallbackPayload,
        )

        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        callback_headers = WildmokaProtectTranscodeCallbackHeaders.from_dict(
            d.pop("callback_headers")
        )

        component_type = d.pop("component_type")

        container_id = d.pop("container_id")

        create_file_callback_payload = (
            WildmokaProtectTranscodeCreateFileCallbackPayload.from_dict(
                d.pop("create_file_callback_payload")
            )
        )

        create_file_callback_url = d.pop("create_file_callback_url")

        drm = d.pop("drm")

        drm_asset_id = d.pop("drm_asset_id")

        frame_count = d.pop("frame_count")

        frame_rate = d.pop("frame_rate")

        has_audio = d.pop("has_audio")

        height = d.pop("height")

        input_url = d.pop("input_url")

        monitor_job_id = d.pop("monitor_job_id")

        proxy_id = d.pop("proxy_id")

        segment_duration = d.pop("segment_duration")

        update_file_status_callback_url = d.pop("update_file_status_callback_url")

        watermark = d.pop("watermark")

        def _parse_watermark_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        watermark_id = _parse_watermark_id(d.pop("watermark_id"))

        width = d.pop("width")

        wildmoka_protect_transcode = cls(
            asset_id=asset_id,
            callback_headers=callback_headers,
            component_type=component_type,
            container_id=container_id,
            create_file_callback_payload=create_file_callback_payload,
            create_file_callback_url=create_file_callback_url,
            drm=drm,
            drm_asset_id=drm_asset_id,
            frame_count=frame_count,
            frame_rate=frame_rate,
            has_audio=has_audio,
            height=height,
            input_url=input_url,
            monitor_job_id=monitor_job_id,
            proxy_id=proxy_id,
            segment_duration=segment_duration,
            update_file_status_callback_url=update_file_status_callback_url,
            watermark=watermark,
            watermark_id=watermark_id,
            width=width,
        )

        wildmoka_protect_transcode.additional_properties = d
        return wildmoka_protect_transcode

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
