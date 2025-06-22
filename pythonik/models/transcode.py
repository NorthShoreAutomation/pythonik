"""
Iconik Transcode Models
This module contains Pydantic models for the Iconik Transcode API.
"""

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Literal,
    Optional,
    Union,
)

from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
)


class TranscribeSchema(BaseModel):
    """Represents a TranscribeSchema in the Iconik system."""

    engine: Optional[str] = None
    force: Optional[bool] = None
    language: Optional[str] = None
    profile_id: Optional[str] = None
    speakers: Optional[int] = Field(None, ge=1, le=100)
    summary: Optional[bool] = None
    topics_extraction: Optional[bool] = None
    translate_languages: Optional[List[str]] = Field(default_factory=list)


class TranscodersSchema(BaseModel):
    """Represents a TranscodersSchema in the Iconik system."""

    id: Optional[str] = None
    name: Optional[str] = None
    settings: Optional[Dict[str, Any]] = Field(default_factory=dict)
    type: Optional[str] = None


class TranscodeValidateMediaInfoSchema(BaseModel):
    """Represents a TranscodeValidateMediaInfoSchema in the Iconik system."""

    filename: Optional[str] = None
    media_info: str


class TranscodeQueueSchema(BaseModel):
    """Represents a TranscodeQueueSchema in the Iconik system."""

    facets: Optional[Dict[str, "FacetSchema"]] = Field(default_factory=dict)
    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List["TranscodeQueueObjectSchema"]] = Field(
        default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class TranscodeQueueRecordSchema(BaseModel):
    """Represents a TranscodeQueueRecordSchema in the Iconik system."""

    bytes_params: Optional[Any] = None
    date_created: Optional[str] = None
    date_updated: Optional[str] = None
    id: Optional[str] = None
    job_id: Optional[str] = None
    media_info: Optional[str] = None
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    params: Optional[str] = None
    priority: Optional[int] = None
    retry_count: Optional[int] = None
    spec: Optional[str] = None
    status: Optional[str] = None
    system_domain_id: Optional[str] = None
    system_name: Optional[str] = None
    type: Optional[str] = None
    user_id: Optional[str] = None
    version_id: Optional[str] = None


class TranscodeQueueObjectSchema(BaseModel):
    """Represents a TranscodeQueueObjectSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_updated: Optional[datetime] = None
    id: Optional[str] = None
    job_id: Optional[str] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    retry_count: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    status: Optional[str] = None
    system_domain: Optional[str] = None
    system_domain_id: Optional[str] = None
    system_domain_timestamp: Optional[float] = None
    system_name: Optional[str] = None
    type: Optional[str] = None
    user_id: Optional[str] = None


class TranscodeElasticQueueRecordSchema(BaseModel):
    """Represents a TranscodeElasticQueueRecordSchema in the Iconik system."""

    date_created: Optional[str] = None
    date_updated: Optional[str] = None
    id: Optional[str] = None
    job_id: Optional[str] = None
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    priority: Optional[str] = None
    queue: Optional[str] = None
    retry_count: Optional[str] = None
    status: Optional[str] = None
    storage_id: Optional[str] = None
    system_domain_id: Optional[str] = None
    system_domain_timestamp: Optional[str] = None
    system_name: Optional[str] = None
    type: Optional[str] = None
    user_id: Optional[str] = None
    version_id: Optional[str] = None


class TranscodeESQueueRecordsSchema(BaseModel):
    """Represents a TranscodeESQueueRecordsSchema in the Iconik system."""

    objects: Optional[List["TranscodeElasticQueueRecord"]] = Field(
        default_factory=list)


class TranscodeElasticQueueRecord(BaseModel):
    """Represents a TranscodeElasticQueueRecord in the Iconik system."""

    date_created: Optional[str] = None
    date_updated: Optional[str] = None
    id: Optional[str] = None
    job_id: Optional[str] = None
    object_id: Optional[str] = None
    object_type: Optional[str] = None
    priority: Optional[str] = None
    queue: Optional[str] = None
    retry_count: Optional[str] = None
    status: Optional[str] = None
    storage_id: Optional[str] = None
    system_domain_id: Optional[str] = None
    system_domain_timestamp: Optional[str] = None
    system_name: Optional[str] = None
    type: Optional[str] = None
    user_id: Optional[str] = None
    version_id: Optional[str] = None


class ThumbnailJobSchema(BaseModel):
    """Represents a ThumbnailJobSchema in the Iconik system."""

    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    id: Optional[str] = None
    max_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    min_interval: Optional[int] = Field(None,
                                        ge=-9223372036854775808,
                                        le=9223372036854775807)
    output_endpoint: "OutputEndpointSchema"
    set_as_custom_keyframe: Optional[bool] = None
    time_end_milliseconds: Optional[int] = Field(None,
                                                 ge=-9223372036854775808,
                                                 le=9223372036854775807)
    time_start_milliseconds: Optional[int] = Field(None,
                                                   ge=-9223372036854775808,
                                                   le=9223372036854775807)
    timestamp: Optional[int] = Field(None,
                                     ge=-9223372036854775808,
                                     le=9223372036854775807)
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class SpecifiedKeyframesSchema(BaseModel):
    """Represents a SpecifiedKeyframesSchema in the Iconik system."""

    url: str


class ReindexQueueRecordSchema(BaseModel):
    """Represents a ReindexQueueRecordSchema in the Iconik system."""

    sync_to_another_dc: Optional[bool] = None


class LocalTranscodeJobSchema(BaseModel):
    """Represents a LocalTranscodeJobSchema in the Iconik system."""

    amazon_rekognition: Optional[bool] = None
    analysis_data: Optional[Dict[str, Any]] = Field(default_factory=dict)
    analysis_query_default_service_account: Optional[bool] = None
    analyzed_before: Optional[bool] = None
    asset_id: Optional[str] = None
    asset_link: Optional[str] = None
    collection_id: Optional[str] = None
    create_transcription: Optional[bool] = None
    delete_old_transcriptions: Optional[bool] = None
    force_transcoder: Optional[str] = None
    google_cloud_video_intelligence: Optional[bool] = None
    input: "LocalTranscodeInputSchema"
    job_id: Optional[str] = None
    job_steps: Optional[List["JobStepSchema"]] = Field(default_factory=list)
    language: Optional[str] = None
    media_info: Optional[str] = None
    overwrite: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    speakers: Optional[int] = Field(None, ge=2, le=100)
    thumbnail: Optional[List["ThumbnailJob"]] = Field(default_factory=list)
    transcode: Optional[List["TranscodeJob"]] = Field(default_factory=list)
    valid_transcoders: Optional[List["Transcoders"]] = Field(
        default_factory=list)
    version_id: Optional[str] = None


class LocalTranscodeInputSchema(BaseModel):
    """Represents a LocalTranscodeInputSchema in the Iconik system."""

    asset_id: str
    checksum: Optional[str] = None
    closed_captions: Optional[bool] = None
    collection_id: Optional[str] = None
    component_ids: Optional[List[str]] = Field(default_factory=list)
    directory_path: str
    endpoint: "EndpointSchema"
    engine: Optional[str] = None
    file_id: str
    file_set_id: str
    filename: str
    format_id: str
    language: Optional[str] = None
    original_name: Optional[str] = None
    proxy_id: Optional[str] = None
    size: int = Field(..., ge=-9223372036854775808, le=9223372036854775807)
    storage_id: str
    update_proxy_mediainfo: Optional[bool] = None
    version_id: str


class LocalStorageFileTranscodeJobsSchema(BaseModel):
    """Represents a LocalStorageFileTranscodeJobsSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    objects: Optional[List["LocalStorageFileTranscodeJobSchema"]] = Field(
        default_factory=list)
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class LocalStorageFileTranscodeJobSchema(BaseModel):
    """Represents a LocalStorageFileTranscodeJobSchema in the Iconik system."""

    asset_id: str
    checksum: Optional[str] = None
    collection_id: Optional[str] = None
    component_ids: Optional[List[str]] = Field(default_factory=list)
    directory_path: str
    file_id: str
    file_set_id: str
    filename: str
    format_id: str
    id: Optional[str] = None
    job_id: str
    priority: Optional[int] = Field(None, ge=1, le=10)
    size: int = Field(..., ge=-9223372036854775808, le=9223372036854775807)
    version_id: str


class ListObjectsSchema(BaseModel):
    """Represents a ListObjectsSchema in the Iconik system."""

    first_url: Optional[str] = None
    last_url: Optional[str] = None
    next_url: Optional[str] = None
    page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    pages: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    per_page: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    prev_url: Optional[str] = None
    total: Optional[int] = Field(None,
                                 ge=-9223372036854775808,
                                 le=9223372036854775807)


class JobsStateSchema(BaseModel):
    """Represents a JobsStateSchema in the Iconik system."""

    action: Literal["ABORT", "RESTART"]
    job_ids: List[str]


class JobsPrioritySchema(BaseModel):
    """Represents a JobsPrioritySchema in the Iconik system."""

    job_ids: List[str]
    priority: int = Field(..., ge=1, le=10)


class JobStepSchema(BaseModel):
    """Represents a JobStepSchema in the Iconik system."""

    date_created: Optional[datetime] = None
    date_updated: Optional[datetime] = None
    id: Optional[str] = None
    label: Optional[str] = None
    message: Optional[str] = None
    status: Optional[str] = None


class JobBaseSchema(BaseModel):
    """Represents a JobBaseSchema in the Iconik system."""

    asset_id: Optional[str] = None
    collection_id: Optional[str] = None
    input: Optional["InputSchema"] = None
    job_id: Optional[str] = None
    job_steps: Optional[List["JobStep"]] = Field(default_factory=list)
    media_info: Optional[str] = None
    thumbnail: Optional[List["ThumbnailJob"]] = Field(default_factory=list)
    transcode: Optional[List["TranscodeJob"]] = Field(default_factory=list)


class GenerateCollectionKeyframeSchema(BaseModel):
    """Represents a GenerateCollectionKeyframeSchema in the Iconik system."""

    deleted_asset_id: Optional[str] = None
    force: Optional[bool] = None
    specified_asset_ids: Optional[List[str]] = Field(default_factory=list)
    specified_keyframes: Optional[List["SpecifiedKeyframes"]] = Field(
        default_factory=list)


class SpecifiedKeyframes(BaseModel):
    """Represents a SpecifiedKeyframes in the Iconik system."""

    url: str


class FacetSchema(BaseModel):
    """Represents a FacetSchema in the Iconik system."""

    buckets: Optional[List["FacetBucketSchema"]] = Field(default_factory=list)
    doc_count_error_upper_bound: Optional[int] = Field(None,
                                                       ge=-9223372036854775808,
                                                       le=9223372036854775807)
    sum_other_doc_count: Optional[int] = Field(None,
                                               ge=-9223372036854775808,
                                               le=9223372036854775807)


class FacetBucketSchema(BaseModel):
    """Represents a FacetBucketSchema in the Iconik system."""

    doc_count: Optional[int] = Field(None,
                                     ge=-9223372036854775808,
                                     le=9223372036854775807)
    key: Optional[str] = None


class EdgeTranscodeWorkersSchema(BaseModel):
    """Represents a EdgeTranscodeWorkersSchema in the Iconik system."""

    objects: Optional[List["EdgeTranscodeWorkerSchema"]] = Field(
        default_factory=list)


class EdgeTranscodeWorkerSchema(BaseModel):
    """Represents a EdgeTranscodeWorkerSchema in the Iconik system."""

    id: Optional[str] = None
    last_update_date: Optional[datetime] = None
    status: Literal["ACTIVE", "INACTIVE"]
    storage_id: str


class EdgeTranscodeJobsSchema(BaseModel):
    """Represents a EdgeTranscodeJobsSchema in the Iconik system."""

    objects: Optional[List["EdgeTranscodeJobSchema"]] = Field(
        default_factory=list)


class TranscodeJobSchema(BaseModel):
    """Represents a TranscodeJobSchema in the Iconik system."""

    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    id: Optional[str] = None
    output_endpoint: "OutputEndpointSchema"
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class OutputEndpointSchema(BaseModel):
    """Represents a OutputEndpointSchema in the Iconik system."""

    headers: Optional[Dict[str, Any]] = Field(default_factory=dict)
    key: str


class JobSchema(BaseModel):
    """Represents a JobSchema in the Iconik system."""

    amazon_rekognition: Optional[bool] = None
    analysis_data: Optional[Dict[str, Any]] = Field(default_factory=dict)
    analysis_query_default_service_account: Optional[bool] = None
    analyzed_before: Optional[bool] = None
    asset_id: Optional[str] = None
    asset_link: Optional[str] = None
    collection_id: Optional[str] = None
    create_transcription: Optional[bool] = None
    delete_old_transcriptions: Optional[bool] = None
    force_transcoder: Optional[str] = None
    google_cloud_video_intelligence: Optional[bool] = None
    input: Optional["InputSchema"] = None
    job_id: Optional[str] = None
    job_steps: Optional[List["JobStep"]] = Field(default_factory=list)
    language: Optional[str] = None
    media_info: Optional[str] = None
    overwrite: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=10)
    speakers: Optional[int] = Field(None, ge=2, le=100)
    thumbnail: Optional[List["ThumbnailJob"]] = Field(default_factory=list)
    transcode: Optional[List["TranscodeJob"]] = Field(default_factory=list)
    valid_transcoders: Optional[List["Transcoders"]] = Field(
        default_factory=list)
    version_id: Optional[str] = None


class Transcoders(BaseModel):
    """Represents a Transcoders in the Iconik system."""

    id: Optional[str] = None
    name: Optional[str] = None
    settings: Optional[Dict[str, Any]] = Field(default_factory=dict)
    type: Optional[str] = None


class EdgeTranscodeJobSchema(BaseModel):
    """Represents a EdgeTranscodeJobSchema in the Iconik system."""

    asset_id: Optional[str] = None
    collection_id: Optional[str] = None
    input: "EdgeTranscodeInputSchema"
    job_id: Optional[str] = None
    job_steps: Optional[List["JobStep"]] = Field(default_factory=list)
    media_info: Optional[str] = None
    thumbnail: Optional[List["EdgeThumbnailJobFieldSchema"]] = Field(
        default_factory=list)
    transcode: Optional[List["EdgeTranscodeJobFieldSchema"]] = Field(
        default_factory=list)


class JobStep(BaseModel):
    """Represents a JobStep in the Iconik system."""

    date_created: Optional[datetime] = None
    date_updated: Optional[datetime] = None
    id: Optional[str] = None
    label: Optional[str] = None
    message: Optional[str] = None
    status: Optional[str] = None


class ThumbnailJob(BaseModel):
    """Represents a ThumbnailJob in the Iconik system."""

    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    id: Optional[str] = None
    max_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    min_interval: Optional[int] = Field(None,
                                        ge=-9223372036854775808,
                                        le=9223372036854775807)
    output_endpoint: "OutputEndpoint"
    set_as_custom_keyframe: Optional[bool] = None
    time_end_milliseconds: Optional[int] = Field(None,
                                                 ge=-9223372036854775808,
                                                 le=9223372036854775807)
    time_start_milliseconds: Optional[int] = Field(None,
                                                   ge=-9223372036854775808,
                                                   le=9223372036854775807)
    timestamp: Optional[int] = Field(None,
                                     ge=-9223372036854775808,
                                     le=9223372036854775807)
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class InputSchema(BaseModel):
    """Represents a InputSchema in the Iconik system."""

    asset_id: Optional[str] = None
    closed_captions: Optional[bool] = None
    collection_id: Optional[str] = None
    directory_path: Optional[str] = None
    endpoint: "EndpointSchema"
    engine: Optional[str] = None
    file_id: Optional[str] = None
    file_set_id: Optional[str] = None
    format_id: Optional[str] = None
    language: Optional[str] = None
    original_name: Optional[str] = None
    proxy_id: Optional[str] = None
    storage_id: Optional[str] = None
    update_proxy_mediainfo: Optional[bool] = None
    version_id: Optional[str] = None


class TranscodeJob(BaseModel):
    """Represents a TranscodeJob in the Iconik system."""

    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    id: Optional[str] = None
    output_endpoint: "OutputEndpoint"
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class OutputEndpoint(BaseModel):
    """Represents a OutputEndpoint in the Iconik system."""

    headers: Optional[Dict[str, Any]] = Field(default_factory=dict)
    key: str


class EdgeTranscodeJobFieldSchema(BaseModel):
    """Represents a EdgeTranscodeJobFieldSchema in the Iconik system."""

    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    id: Optional[str] = None
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class EdgeTranscodeInputSchema(BaseModel):
    """Represents a EdgeTranscodeInputSchema in the Iconik system."""

    asset_id: Optional[str] = None
    closed_captions: Optional[bool] = None
    directory_path: Optional[str] = None
    endpoint: "EdgeTranscodeEndpointSchema"
    file_id: Optional[str] = None
    file_set_id: Optional[str] = None
    format_id: Optional[str] = None
    language: Optional[str] = None
    original_name: Optional[str] = None
    proxy_id: Optional[str] = None
    storage_id: Optional[str] = None


class EndpointSchema(BaseModel):
    """Represents a EndpointSchema in the Iconik system."""

    data: Optional[Dict[str, Any]] = Field(default_factory=dict)
    headers: Optional[Dict[str, Any]] = Field(default_factory=dict)
    method: Optional[str] = None
    storage_method: Optional[str] = None
    type: Optional[str] = None
    url: str


class EdgeTranscodeEndpointSchema(BaseModel):
    """Represents a EdgeTranscodeEndpointSchema in the Iconik system."""

    data: Optional[Dict[str, Any]] = Field(default_factory=dict)
    method: Optional[str] = None
    storage_method: Optional[str] = None
    type: Optional[str] = None
    url: str


class EdgeThumbnailJobFieldSchema(BaseModel):
    """Represents a EdgeThumbnailJobFieldSchema in the Iconik system."""

    height: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    id: Optional[str] = None
    max_number: Optional[int] = Field(None, ge=-2147483648, le=2147483647)
    min_interval: Optional[int] = Field(None,
                                        ge=-9223372036854775808,
                                        le=9223372036854775807)
    timestamp: Optional[int] = Field(None,
                                     ge=-9223372036854775808,
                                     le=9223372036854775807)
    width: Optional[int] = Field(None, ge=-2147483648, le=2147483647)


class BulkTranscribeSchema(BaseModel):
    """Represents a BulkTranscribeSchema in the Iconik system."""

    engine: Optional[str] = None
    force: Optional[bool] = None
    language: Optional[str] = None
    object_ids: List[str]
    object_type: Literal["assets", "collections", "saved_searches"]
    profile_id: Optional[str] = None
    speakers: Optional[int] = Field(None, ge=1, le=100)
    summary: Optional[bool] = None
    topics_extraction: Optional[bool] = None
    translate_languages: Optional[List[str]] = Field(default_factory=list)


class BulkAnalyzeSchema(BaseModel):
    """Represents a BulkAnalyzeSchema in the Iconik system."""

    force: Optional[bool] = None
    force_type: Optional[Literal["OVERWRITE", "APPEND"]] = None
    object_ids: List[str]
    object_type: Literal["assets", "collections", "saved_searches"]
    profile_id: Optional[str] = None


class BulkActionSchema(BaseModel):
    """Represents a BulkActionSchema in the Iconik system."""

    object_ids: List[str]
    object_type: Literal["assets", "collections", "saved_searches"]


class AssetLinkURLSchema(BaseModel):
    """Represents a AssetLinkURLSchema in the Iconik system."""

    url: Union[str, HttpUrl]


class AssetLinkData(BaseModel):
    """Represents a AssetLinkData in the Iconik system."""

    site_name: Optional[str] = None
    title: Optional[str] = None


class AnalyzeSchema(BaseModel):
    """Represents a AnalyzeSchema in the Iconik system."""

    force: Optional[bool] = None
    force_type: Optional[Literal["OVERWRITE", "APPEND"]] = None
    service_name: Optional[str] = None


class AbortStorageTranscodeJobsSchema(BaseModel):
    """Represents a AbortStorageTranscodeJobsSchema in the Iconik system."""

    error_message: Optional[str] = None


# Update forward references
TranscribeSchema.model_rebuild()
TranscodersSchema.model_rebuild()
TranscodeValidateMediaInfoSchema.model_rebuild()
TranscodeQueueSchema.model_rebuild()
TranscodeQueueRecordSchema.model_rebuild()
TranscodeQueueObjectSchema.model_rebuild()
TranscodeElasticQueueRecordSchema.model_rebuild()
TranscodeESQueueRecordsSchema.model_rebuild()
TranscodeElasticQueueRecord.model_rebuild()
ThumbnailJobSchema.model_rebuild()
SpecifiedKeyframesSchema.model_rebuild()
ReindexQueueRecordSchema.model_rebuild()
LocalTranscodeJobSchema.model_rebuild()
LocalTranscodeInputSchema.model_rebuild()
LocalStorageFileTranscodeJobsSchema.model_rebuild()
LocalStorageFileTranscodeJobSchema.model_rebuild()
ListObjectsSchema.model_rebuild()
JobsStateSchema.model_rebuild()
JobsPrioritySchema.model_rebuild()
JobStepSchema.model_rebuild()
JobBaseSchema.model_rebuild()
GenerateCollectionKeyframeSchema.model_rebuild()
SpecifiedKeyframes.model_rebuild()
FacetSchema.model_rebuild()
FacetBucketSchema.model_rebuild()
EdgeTranscodeWorkersSchema.model_rebuild()
EdgeTranscodeWorkerSchema.model_rebuild()
EdgeTranscodeJobsSchema.model_rebuild()
TranscodeJobSchema.model_rebuild()
OutputEndpointSchema.model_rebuild()
JobSchema.model_rebuild()
Transcoders.model_rebuild()
EdgeTranscodeJobSchema.model_rebuild()
JobStep.model_rebuild()
ThumbnailJob.model_rebuild()
InputSchema.model_rebuild()
TranscodeJob.model_rebuild()
OutputEndpoint.model_rebuild()
EdgeTranscodeJobFieldSchema.model_rebuild()
EdgeTranscodeInputSchema.model_rebuild()
EndpointSchema.model_rebuild()
EdgeTranscodeEndpointSchema.model_rebuild()
EdgeThumbnailJobFieldSchema.model_rebuild()
BulkTranscribeSchema.model_rebuild()
BulkAnalyzeSchema.model_rebuild()
BulkActionSchema.model_rebuild()
AssetLinkURLSchema.model_rebuild()
AssetLinkData.model_rebuild()
AnalyzeSchema.model_rebuild()
AbortStorageTranscodeJobsSchema.model_rebuild()
