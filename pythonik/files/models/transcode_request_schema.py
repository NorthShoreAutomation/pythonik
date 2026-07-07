from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscodeRequestSchema")


@_attrs_define
class TranscodeRequestSchema:
    """
    Attributes:
        job_id (None | Unset | UUID):
        priority (int | None | Unset):
        set_as_custom_keyframe (bool | None | Unset):
        update_proxy_mediainfo (bool | Unset):
        use_storage_transcode_ignore_pattern (bool | None | Unset):
    """

    job_id: None | Unset | UUID = UNSET
    priority: int | None | Unset = UNSET
    set_as_custom_keyframe: bool | None | Unset = UNSET
    update_proxy_mediainfo: bool | Unset = UNSET
    use_storage_transcode_ignore_pattern: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        set_as_custom_keyframe: bool | None | Unset
        if isinstance(self.set_as_custom_keyframe, Unset):
            set_as_custom_keyframe = UNSET
        else:
            set_as_custom_keyframe = self.set_as_custom_keyframe

        update_proxy_mediainfo = self.update_proxy_mediainfo

        use_storage_transcode_ignore_pattern: bool | None | Unset
        if isinstance(self.use_storage_transcode_ignore_pattern, Unset):
            use_storage_transcode_ignore_pattern = UNSET
        else:
            use_storage_transcode_ignore_pattern = (
                self.use_storage_transcode_ignore_pattern
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if set_as_custom_keyframe is not UNSET:
            field_dict["set_as_custom_keyframe"] = set_as_custom_keyframe
        if update_proxy_mediainfo is not UNSET:
            field_dict["update_proxy_mediainfo"] = update_proxy_mediainfo
        if use_storage_transcode_ignore_pattern is not UNSET:
            field_dict["use_storage_transcode_ignore_pattern"] = (
                use_storage_transcode_ignore_pattern
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_set_as_custom_keyframe(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        set_as_custom_keyframe = _parse_set_as_custom_keyframe(
            d.pop("set_as_custom_keyframe", UNSET)
        )

        update_proxy_mediainfo = d.pop("update_proxy_mediainfo", UNSET)

        def _parse_use_storage_transcode_ignore_pattern(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_storage_transcode_ignore_pattern = (
            _parse_use_storage_transcode_ignore_pattern(
                d.pop("use_storage_transcode_ignore_pattern", UNSET)
            )
        )

        transcode_request_schema = cls(
            job_id=job_id,
            priority=priority,
            set_as_custom_keyframe=set_as_custom_keyframe,
            update_proxy_mediainfo=update_proxy_mediainfo,
            use_storage_transcode_ignore_pattern=use_storage_transcode_ignore_pattern,
        )

        transcode_request_schema.additional_properties = d
        return transcode_request_schema

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
