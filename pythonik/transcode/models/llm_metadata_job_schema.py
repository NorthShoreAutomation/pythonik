from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_schema import InputSchema
    from ..models.job_step_schema import JobStepSchema
    from ..models.llm_metadata_job_schema_analysis_data import (
        LLMMetadataJobSchemaAnalysisData,
    )
    from ..models.thumbnail_job import ThumbnailJob
    from ..models.transcode_job import TranscodeJob
    from ..models.transcoders import Transcoders


T = TypeVar("T", bound="LLMMetadataJobSchema")


@_attrs_define
class LLMMetadataJobSchema:
    """
    Attributes:
        field_names (list[str]):
        view_id (UUID):
        amazon_rekognition (bool | Unset):
        analysis_data (LLMMetadataJobSchemaAnalysisData | Unset):
        analysis_query_default_service_account (bool | Unset):
        analyzed_before (bool | Unset):
        asset_id (str | Unset):
        asset_link (str | Unset):
        collection_id (str | Unset):
        create_transcription (bool | Unset):
        delete_old_transcriptions (bool | Unset):
        force_transcoder (str | Unset):
        google_cloud_video_intelligence (bool | Unset):
        input_ (InputSchema | Unset):
        job_id (str | Unset):
        job_steps (list[JobStepSchema] | Unset):
        language (None | str | Unset):
        media_info (None | str | Unset):
        overwrite (bool | Unset):
        parent_job_id (None | str | Unset):
        priority (int | Unset):
        speakers (int | None | Unset):
        thumbnail (list[ThumbnailJob] | Unset):
        transcode (list[TranscodeJob] | Unset):
        valid_transcoders (list[Transcoders] | Unset):
        version_id (str | Unset):
    """

    field_names: list[str]
    view_id: UUID
    amazon_rekognition: bool | Unset = UNSET
    analysis_data: LLMMetadataJobSchemaAnalysisData | Unset = UNSET
    analysis_query_default_service_account: bool | Unset = UNSET
    analyzed_before: bool | Unset = UNSET
    asset_id: str | Unset = UNSET
    asset_link: str | Unset = UNSET
    collection_id: str | Unset = UNSET
    create_transcription: bool | Unset = UNSET
    delete_old_transcriptions: bool | Unset = UNSET
    force_transcoder: str | Unset = UNSET
    google_cloud_video_intelligence: bool | Unset = UNSET
    input_: InputSchema | Unset = UNSET
    job_id: str | Unset = UNSET
    job_steps: list[JobStepSchema] | Unset = UNSET
    language: None | str | Unset = UNSET
    media_info: None | str | Unset = UNSET
    overwrite: bool | Unset = UNSET
    parent_job_id: None | str | Unset = UNSET
    priority: int | Unset = UNSET
    speakers: int | None | Unset = UNSET
    thumbnail: list[ThumbnailJob] | Unset = UNSET
    transcode: list[TranscodeJob] | Unset = UNSET
    valid_transcoders: list[Transcoders] | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_names = self.field_names

        view_id = str(self.view_id)

        amazon_rekognition = self.amazon_rekognition

        analysis_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analysis_data, Unset):
            analysis_data = self.analysis_data.to_dict()

        analysis_query_default_service_account = (
            self.analysis_query_default_service_account
        )

        analyzed_before = self.analyzed_before

        asset_id = self.asset_id

        asset_link = self.asset_link

        collection_id = self.collection_id

        create_transcription = self.create_transcription

        delete_old_transcriptions = self.delete_old_transcriptions

        force_transcoder = self.force_transcoder

        google_cloud_video_intelligence = self.google_cloud_video_intelligence

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        job_id = self.job_id

        job_steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job_steps, Unset):
            job_steps = []
            for job_steps_item_data in self.job_steps:
                job_steps_item = job_steps_item_data.to_dict()
                job_steps.append(job_steps_item)

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        media_info: None | str | Unset
        if isinstance(self.media_info, Unset):
            media_info = UNSET
        else:
            media_info = self.media_info

        overwrite = self.overwrite

        parent_job_id: None | str | Unset
        if isinstance(self.parent_job_id, Unset):
            parent_job_id = UNSET
        else:
            parent_job_id = self.parent_job_id

        priority = self.priority

        speakers: int | None | Unset
        if isinstance(self.speakers, Unset):
            speakers = UNSET
        else:
            speakers = self.speakers

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

        valid_transcoders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.valid_transcoders, Unset):
            valid_transcoders = []
            for valid_transcoders_item_data in self.valid_transcoders:
                valid_transcoders_item = valid_transcoders_item_data.to_dict()
                valid_transcoders.append(valid_transcoders_item)

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_names": field_names,
                "view_id": view_id,
            }
        )
        if amazon_rekognition is not UNSET:
            field_dict["amazon_rekognition"] = amazon_rekognition
        if analysis_data is not UNSET:
            field_dict["analysis_data"] = analysis_data
        if analysis_query_default_service_account is not UNSET:
            field_dict["analysis_query_default_service_account"] = (
                analysis_query_default_service_account
            )
        if analyzed_before is not UNSET:
            field_dict["analyzed_before"] = analyzed_before
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_link is not UNSET:
            field_dict["asset_link"] = asset_link
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if create_transcription is not UNSET:
            field_dict["create_transcription"] = create_transcription
        if delete_old_transcriptions is not UNSET:
            field_dict["delete_old_transcriptions"] = delete_old_transcriptions
        if force_transcoder is not UNSET:
            field_dict["force_transcoder"] = force_transcoder
        if google_cloud_video_intelligence is not UNSET:
            field_dict["google_cloud_video_intelligence"] = (
                google_cloud_video_intelligence
            )
        if input_ is not UNSET:
            field_dict["input"] = input_
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job_steps is not UNSET:
            field_dict["job_steps"] = job_steps
        if language is not UNSET:
            field_dict["language"] = language
        if media_info is not UNSET:
            field_dict["media_info"] = media_info
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if parent_job_id is not UNSET:
            field_dict["parent_job_id"] = parent_job_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if speakers is not UNSET:
            field_dict["speakers"] = speakers
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if transcode is not UNSET:
            field_dict["transcode"] = transcode
        if valid_transcoders is not UNSET:
            field_dict["valid_transcoders"] = valid_transcoders
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_schema import InputSchema
        from ..models.job_step_schema import JobStepSchema
        from ..models.llm_metadata_job_schema_analysis_data import (
            LLMMetadataJobSchemaAnalysisData,
        )
        from ..models.thumbnail_job import ThumbnailJob
        from ..models.transcode_job import TranscodeJob
        from ..models.transcoders import Transcoders

        d = dict(src_dict)
        field_names = cast(list[str], d.pop("field_names"))

        view_id = UUID(d.pop("view_id"))

        amazon_rekognition = d.pop("amazon_rekognition", UNSET)

        _analysis_data = d.pop("analysis_data", UNSET)
        analysis_data: LLMMetadataJobSchemaAnalysisData | Unset
        if isinstance(_analysis_data, Unset):
            analysis_data = UNSET
        else:
            analysis_data = LLMMetadataJobSchemaAnalysisData.from_dict(_analysis_data)

        analysis_query_default_service_account = d.pop(
            "analysis_query_default_service_account", UNSET
        )

        analyzed_before = d.pop("analyzed_before", UNSET)

        asset_id = d.pop("asset_id", UNSET)

        asset_link = d.pop("asset_link", UNSET)

        collection_id = d.pop("collection_id", UNSET)

        create_transcription = d.pop("create_transcription", UNSET)

        delete_old_transcriptions = d.pop("delete_old_transcriptions", UNSET)

        force_transcoder = d.pop("force_transcoder", UNSET)

        google_cloud_video_intelligence = d.pop(
            "google_cloud_video_intelligence", UNSET
        )

        _input_ = d.pop("input", UNSET)
        input_: InputSchema | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = InputSchema.from_dict(_input_)

        job_id = d.pop("job_id", UNSET)

        _job_steps = d.pop("job_steps", UNSET)
        job_steps: list[JobStepSchema] | Unset = UNSET
        if _job_steps is not UNSET:
            job_steps = []
            for job_steps_item_data in _job_steps:
                job_steps_item = JobStepSchema.from_dict(job_steps_item_data)

                job_steps.append(job_steps_item)

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_media_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_info = _parse_media_info(d.pop("media_info", UNSET))

        overwrite = d.pop("overwrite", UNSET)

        def _parse_parent_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_job_id = _parse_parent_job_id(d.pop("parent_job_id", UNSET))

        priority = d.pop("priority", UNSET)

        def _parse_speakers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        speakers = _parse_speakers(d.pop("speakers", UNSET))

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: list[ThumbnailJob] | Unset = UNSET
        if _thumbnail is not UNSET:
            thumbnail = []
            for thumbnail_item_data in _thumbnail:
                thumbnail_item = ThumbnailJob.from_dict(thumbnail_item_data)

                thumbnail.append(thumbnail_item)

        _transcode = d.pop("transcode", UNSET)
        transcode: list[TranscodeJob] | Unset = UNSET
        if _transcode is not UNSET:
            transcode = []
            for transcode_item_data in _transcode:
                transcode_item = TranscodeJob.from_dict(transcode_item_data)

                transcode.append(transcode_item)

        _valid_transcoders = d.pop("valid_transcoders", UNSET)
        valid_transcoders: list[Transcoders] | Unset = UNSET
        if _valid_transcoders is not UNSET:
            valid_transcoders = []
            for valid_transcoders_item_data in _valid_transcoders:
                valid_transcoders_item = Transcoders.from_dict(
                    valid_transcoders_item_data
                )

                valid_transcoders.append(valid_transcoders_item)

        version_id = d.pop("version_id", UNSET)

        llm_metadata_job_schema = cls(
            field_names=field_names,
            view_id=view_id,
            amazon_rekognition=amazon_rekognition,
            analysis_data=analysis_data,
            analysis_query_default_service_account=analysis_query_default_service_account,
            analyzed_before=analyzed_before,
            asset_id=asset_id,
            asset_link=asset_link,
            collection_id=collection_id,
            create_transcription=create_transcription,
            delete_old_transcriptions=delete_old_transcriptions,
            force_transcoder=force_transcoder,
            google_cloud_video_intelligence=google_cloud_video_intelligence,
            input_=input_,
            job_id=job_id,
            job_steps=job_steps,
            language=language,
            media_info=media_info,
            overwrite=overwrite,
            parent_job_id=parent_job_id,
            priority=priority,
            speakers=speakers,
            thumbnail=thumbnail,
            transcode=transcode,
            valid_transcoders=valid_transcoders,
            version_id=version_id,
        )

        llm_metadata_job_schema.additional_properties = d
        return llm_metadata_job_schema

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
