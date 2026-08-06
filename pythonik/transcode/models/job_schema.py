from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_schema import InputSchema
    from ..models.job_schema_analysis_data_type_0 import JobSchemaAnalysisDataType0
    from ..models.job_step import JobStep
    from ..models.thumbnail_job import ThumbnailJob
    from ..models.transcode_job import TranscodeJob
    from ..models.transcoders import Transcoders


T = TypeVar("T", bound="JobSchema")


@_attrs_define
class JobSchema:
    """
    Attributes:
        amazon_rekognition (bool | None | Unset):
        analysis_data (JobSchemaAnalysisDataType0 | None | Unset):
        analysis_query_default_service_account (bool | None | Unset):
        analyzed_before (bool | None | Unset):
        asset_id (None | str | Unset):
        asset_link (None | str | Unset):
        collection_id (None | str | Unset):
        create_transcription (bool | None | Unset):
        delete_old_transcriptions (bool | None | Unset):
        force_transcoder (None | str | Unset):
        google_cloud_video_intelligence (bool | None | Unset):
        input_ (InputSchema | None | Unset):
        job_id (None | str | Unset):
        job_steps (list[JobStep] | None | Unset):
        language (None | str | Unset):
        media_info (None | str | Unset):
        overwrite (bool | None | Unset):
        priority (int | None | Unset):
        speakers (int | None | Unset):
        thumbnail (list[ThumbnailJob] | None | Unset):
        transcode (list[TranscodeJob] | None | Unset):
        valid_transcoders (list[Transcoders] | None | Unset):
        version_id (None | str | Unset):
    """

    amazon_rekognition: bool | None | Unset = UNSET
    analysis_data: JobSchemaAnalysisDataType0 | None | Unset = UNSET
    analysis_query_default_service_account: bool | None | Unset = UNSET
    analyzed_before: bool | None | Unset = UNSET
    asset_id: None | str | Unset = UNSET
    asset_link: None | str | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    create_transcription: bool | None | Unset = UNSET
    delete_old_transcriptions: bool | None | Unset = UNSET
    force_transcoder: None | str | Unset = UNSET
    google_cloud_video_intelligence: bool | None | Unset = UNSET
    input_: InputSchema | None | Unset = UNSET
    job_id: None | str | Unset = UNSET
    job_steps: list[JobStep] | None | Unset = UNSET
    language: None | str | Unset = UNSET
    media_info: None | str | Unset = UNSET
    overwrite: bool | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    speakers: int | None | Unset = UNSET
    thumbnail: list[ThumbnailJob] | None | Unset = UNSET
    transcode: list[TranscodeJob] | None | Unset = UNSET
    valid_transcoders: list[Transcoders] | None | Unset = UNSET
    version_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_schema import InputSchema
        from ..models.job_schema_analysis_data_type_0 import JobSchemaAnalysisDataType0

        amazon_rekognition: bool | None | Unset
        if isinstance(self.amazon_rekognition, Unset):
            amazon_rekognition = UNSET
        else:
            amazon_rekognition = self.amazon_rekognition

        analysis_data: dict[str, Any] | None | Unset
        if isinstance(self.analysis_data, Unset):
            analysis_data = UNSET
        elif isinstance(self.analysis_data, JobSchemaAnalysisDataType0):
            analysis_data = self.analysis_data.to_dict()
        else:
            analysis_data = self.analysis_data

        analysis_query_default_service_account: bool | None | Unset
        if isinstance(self.analysis_query_default_service_account, Unset):
            analysis_query_default_service_account = UNSET
        else:
            analysis_query_default_service_account = (
                self.analysis_query_default_service_account
            )

        analyzed_before: bool | None | Unset
        if isinstance(self.analyzed_before, Unset):
            analyzed_before = UNSET
        else:
            analyzed_before = self.analyzed_before

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        asset_link: None | str | Unset
        if isinstance(self.asset_link, Unset):
            asset_link = UNSET
        else:
            asset_link = self.asset_link

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

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

        force_transcoder: None | str | Unset
        if isinstance(self.force_transcoder, Unset):
            force_transcoder = UNSET
        else:
            force_transcoder = self.force_transcoder

        google_cloud_video_intelligence: bool | None | Unset
        if isinstance(self.google_cloud_video_intelligence, Unset):
            google_cloud_video_intelligence = UNSET
        else:
            google_cloud_video_intelligence = self.google_cloud_video_intelligence

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

        overwrite: bool | None | Unset
        if isinstance(self.overwrite, Unset):
            overwrite = UNSET
        else:
            overwrite = self.overwrite

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        speakers: int | None | Unset
        if isinstance(self.speakers, Unset):
            speakers = UNSET
        else:
            speakers = self.speakers

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

        valid_transcoders: list[dict[str, Any]] | None | Unset
        if isinstance(self.valid_transcoders, Unset):
            valid_transcoders = UNSET
        elif isinstance(self.valid_transcoders, list):
            valid_transcoders = []
            for valid_transcoders_type_0_item_data in self.valid_transcoders:
                valid_transcoders_type_0_item = (
                    valid_transcoders_type_0_item_data.to_dict()
                )
                valid_transcoders.append(valid_transcoders_type_0_item)

        else:
            valid_transcoders = self.valid_transcoders

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        else:
            version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        from ..models.job_schema_analysis_data_type_0 import JobSchemaAnalysisDataType0
        from ..models.job_step import JobStep
        from ..models.thumbnail_job import ThumbnailJob
        from ..models.transcode_job import TranscodeJob
        from ..models.transcoders import Transcoders

        d = dict(src_dict)

        def _parse_amazon_rekognition(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        amazon_rekognition = _parse_amazon_rekognition(
            d.pop("amazon_rekognition", UNSET)
        )

        def _parse_analysis_data(
            data: object,
        ) -> JobSchemaAnalysisDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                analysis_data_type_0 = JobSchemaAnalysisDataType0.from_dict(data)

                return analysis_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobSchemaAnalysisDataType0 | None | Unset, data)

        analysis_data = _parse_analysis_data(d.pop("analysis_data", UNSET))

        def _parse_analysis_query_default_service_account(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        analysis_query_default_service_account = (
            _parse_analysis_query_default_service_account(
                d.pop("analysis_query_default_service_account", UNSET)
            )
        )

        def _parse_analyzed_before(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        analyzed_before = _parse_analyzed_before(d.pop("analyzed_before", UNSET))

        def _parse_asset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_asset_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_link = _parse_asset_link(d.pop("asset_link", UNSET))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

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

        def _parse_force_transcoder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        force_transcoder = _parse_force_transcoder(d.pop("force_transcoder", UNSET))

        def _parse_google_cloud_video_intelligence(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        google_cloud_video_intelligence = _parse_google_cloud_video_intelligence(
            d.pop("google_cloud_video_intelligence", UNSET)
        )

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

        def _parse_overwrite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overwrite = _parse_overwrite(d.pop("overwrite", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_speakers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        speakers = _parse_speakers(d.pop("speakers", UNSET))

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

        def _parse_valid_transcoders(data: object) -> list[Transcoders] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                valid_transcoders_type_0 = []
                _valid_transcoders_type_0 = data
                for valid_transcoders_type_0_item_data in _valid_transcoders_type_0:
                    valid_transcoders_type_0_item = Transcoders.from_dict(
                        valid_transcoders_type_0_item_data
                    )

                    valid_transcoders_type_0.append(valid_transcoders_type_0_item)

                return valid_transcoders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Transcoders] | None | Unset, data)

        valid_transcoders = _parse_valid_transcoders(d.pop("valid_transcoders", UNSET))

        def _parse_version_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        job_schema = cls(
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
            priority=priority,
            speakers=speakers,
            thumbnail=thumbnail,
            transcode=transcode,
            valid_transcoders=valid_transcoders,
            version_id=version_id,
        )

        job_schema.additional_properties = d
        return job_schema

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
