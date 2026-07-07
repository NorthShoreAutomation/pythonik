from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edge_thumbnail_job_field_schema import EdgeThumbnailJobFieldSchema
    from ..models.edge_transcode_input_schema import EdgeTranscodeInputSchema
    from ..models.edge_transcode_job_field_schema import EdgeTranscodeJobFieldSchema
    from ..models.job_step import JobStep


T = TypeVar("T", bound="EdgeTranscodeJobSchema")


@_attrs_define
class EdgeTranscodeJobSchema:
    """
    Attributes:
        input_ (EdgeTranscodeInputSchema):
        asset_id (str | Unset):
        collection_id (str | Unset):
        job_id (str | Unset):
        job_steps (list[JobStep] | Unset):
        media_info (None | str | Unset):
        thumbnail (list[EdgeThumbnailJobFieldSchema] | Unset):
        transcode (list[EdgeTranscodeJobFieldSchema] | Unset):
    """

    input_: EdgeTranscodeInputSchema
    asset_id: str | Unset = UNSET
    collection_id: str | Unset = UNSET
    job_id: str | Unset = UNSET
    job_steps: list[JobStep] | Unset = UNSET
    media_info: None | str | Unset = UNSET
    thumbnail: list[EdgeThumbnailJobFieldSchema] | Unset = UNSET
    transcode: list[EdgeTranscodeJobFieldSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_.to_dict()

        asset_id = self.asset_id

        collection_id = self.collection_id

        job_id = self.job_id

        job_steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job_steps, Unset):
            job_steps = []
            for job_steps_item_data in self.job_steps:
                job_steps_item = job_steps_item_data.to_dict()
                job_steps.append(job_steps_item)

        media_info: None | str | Unset
        if isinstance(self.media_info, Unset):
            media_info = UNSET
        else:
            media_info = self.media_info

        thumbnail: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = []
            for thumbnail_item_data in self.thumbnail:
                thumbnail_item = thumbnail_item_data.to_dict()
                thumbnail.append(thumbnail_item)

        transcode: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transcode, Unset):
            transcode = []
            for transcode_item_data in self.transcode:
                transcode_item = transcode_item_data.to_dict()
                transcode.append(transcode_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
            }
        )
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
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
        from ..models.edge_thumbnail_job_field_schema import EdgeThumbnailJobFieldSchema
        from ..models.edge_transcode_input_schema import EdgeTranscodeInputSchema
        from ..models.edge_transcode_job_field_schema import EdgeTranscodeJobFieldSchema
        from ..models.job_step import JobStep

        d = dict(src_dict)
        input_ = EdgeTranscodeInputSchema.from_dict(d.pop("input"))

        asset_id = d.pop("asset_id", UNSET)

        collection_id = d.pop("collection_id", UNSET)

        job_id = d.pop("job_id", UNSET)

        _job_steps = d.pop("job_steps", UNSET)
        job_steps: list[JobStep] | Unset = UNSET
        if _job_steps is not UNSET:
            job_steps = []
            for job_steps_item_data in _job_steps:
                job_steps_item = JobStep.from_dict(job_steps_item_data)

                job_steps.append(job_steps_item)

        def _parse_media_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_info = _parse_media_info(d.pop("media_info", UNSET))

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: list[EdgeThumbnailJobFieldSchema] | Unset = UNSET
        if _thumbnail is not UNSET:
            thumbnail = []
            for thumbnail_item_data in _thumbnail:
                thumbnail_item = EdgeThumbnailJobFieldSchema.from_dict(
                    thumbnail_item_data
                )

                thumbnail.append(thumbnail_item)

        _transcode = d.pop("transcode", UNSET)
        transcode: list[EdgeTranscodeJobFieldSchema] | Unset = UNSET
        if _transcode is not UNSET:
            transcode = []
            for transcode_item_data in _transcode:
                transcode_item = EdgeTranscodeJobFieldSchema.from_dict(
                    transcode_item_data
                )

                transcode.append(transcode_item)

        edge_transcode_job_schema = cls(
            input_=input_,
            asset_id=asset_id,
            collection_id=collection_id,
            job_id=job_id,
            job_steps=job_steps,
            media_info=media_info,
            thumbnail=thumbnail,
            transcode=transcode,
        )

        edge_transcode_job_schema.additional_properties = d
        return edge_transcode_job_schema

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
