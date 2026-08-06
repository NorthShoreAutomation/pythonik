from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_schema import InputSchema
    from ..models.job_step import JobStep
    from ..models.thumbnail_job import ThumbnailJob
    from ..models.transcode_job import TranscodeJob


T = TypeVar("T", bound="JobBaseSchema")


@_attrs_define
class JobBaseSchema:
    """
    Attributes:
        asset_id (None | str | Unset):
        collection_id (None | str | Unset):
        input_ (InputSchema | None | Unset):
        job_id (None | str | Unset):
        job_steps (list[JobStep] | None | Unset):
        media_info (None | str | Unset):
        thumbnail (list[ThumbnailJob] | None | Unset):
        transcode (list[TranscodeJob] | None | Unset):
    """

    asset_id: None | str | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    input_: InputSchema | None | Unset = UNSET
    job_id: None | str | Unset = UNSET
    job_steps: list[JobStep] | None | Unset = UNSET
    media_info: None | str | Unset = UNSET
    thumbnail: list[ThumbnailJob] | None | Unset = UNSET
    transcode: list[TranscodeJob] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_schema import InputSchema

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        input_: dict[str, Any] | None | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        elif isinstance(self.input_, InputSchema):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        job_steps: list[dict[str, Any]] | None | Unset
        if isinstance(self.job_steps, Unset):
            job_steps = UNSET
        elif isinstance(self.job_steps, list):
            job_steps = []
            for job_steps_type_0_item_data in self.job_steps:
                job_steps_type_0_item = job_steps_type_0_item_data.to_dict()
                job_steps.append(job_steps_type_0_item)

        else:
            job_steps = self.job_steps

        media_info: None | str | Unset
        if isinstance(self.media_info, Unset):
            media_info = UNSET
        else:
            media_info = self.media_info

        thumbnail: list[dict[str, Any]] | None | Unset
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        elif isinstance(self.thumbnail, list):
            thumbnail = []
            for thumbnail_type_0_item_data in self.thumbnail:
                thumbnail_type_0_item = thumbnail_type_0_item_data.to_dict()
                thumbnail.append(thumbnail_type_0_item)

        else:
            thumbnail = self.thumbnail

        transcode: list[dict[str, Any]] | None | Unset
        if isinstance(self.transcode, Unset):
            transcode = UNSET
        elif isinstance(self.transcode, list):
            transcode = []
            for transcode_type_0_item_data in self.transcode:
                transcode_type_0_item = transcode_type_0_item_data.to_dict()
                transcode.append(transcode_type_0_item)

        else:
            transcode = self.transcode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if input_ is not UNSET:
            field_dict["input"] = input_
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job_steps is not UNSET:
            field_dict["job_steps"] = job_steps
        if media_info is not UNSET:
            field_dict["media_info"] = media_info
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if transcode is not UNSET:
            field_dict["transcode"] = transcode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_schema import InputSchema
        from ..models.job_step import JobStep
        from ..models.thumbnail_job import ThumbnailJob
        from ..models.transcode_job import TranscodeJob

        d = dict(src_dict)

        def _parse_asset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_input_(data: object) -> InputSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_1 = InputSchema.from_dict(data)

                return input_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InputSchema | None | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_job_steps(data: object) -> list[JobStep] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_steps_type_0 = []
                _job_steps_type_0 = data
                for job_steps_type_0_item_data in _job_steps_type_0:
                    job_steps_type_0_item = JobStep.from_dict(
                        job_steps_type_0_item_data
                    )

                    job_steps_type_0.append(job_steps_type_0_item)

                return job_steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobStep] | None | Unset, data)

        job_steps = _parse_job_steps(d.pop("job_steps", UNSET))

        def _parse_media_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_info = _parse_media_info(d.pop("media_info", UNSET))

        def _parse_thumbnail(data: object) -> list[ThumbnailJob] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                thumbnail_type_0 = []
                _thumbnail_type_0 = data
                for thumbnail_type_0_item_data in _thumbnail_type_0:
                    thumbnail_type_0_item = ThumbnailJob.from_dict(
                        thumbnail_type_0_item_data
                    )

                    thumbnail_type_0.append(thumbnail_type_0_item)

                return thumbnail_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ThumbnailJob] | None | Unset, data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))

        def _parse_transcode(data: object) -> list[TranscodeJob] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transcode_type_0 = []
                _transcode_type_0 = data
                for transcode_type_0_item_data in _transcode_type_0:
                    transcode_type_0_item = TranscodeJob.from_dict(
                        transcode_type_0_item_data
                    )

                    transcode_type_0.append(transcode_type_0_item)

                return transcode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TranscodeJob] | None | Unset, data)

        transcode = _parse_transcode(d.pop("transcode", UNSET))

        job_base_schema = cls(
            asset_id=asset_id,
            collection_id=collection_id,
            input_=input_,
            job_id=job_id,
            job_steps=job_steps,
            media_info=media_info,
            thumbnail=thumbnail,
            transcode=transcode,
        )

        job_base_schema.additional_properties = d
        return job_base_schema

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
