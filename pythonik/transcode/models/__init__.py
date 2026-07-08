"""Contains all the data models used in inputs/outputs"""

from .abort_storage_transcode_jobs_schema import AbortStorageTranscodeJobsSchema
from .analyze_schema import AnalyzeSchema
from .analyze_schema_force_type import AnalyzeSchemaForceType
from .asset_link_data import AssetLinkData
from .asset_link_url_schema import AssetLinkURLSchema
from .bulk_action_schema import BulkActionSchema
from .bulk_action_schema_object_type import BulkActionSchemaObjectType
from .bulk_analyze_schema import BulkAnalyzeSchema
from .bulk_analyze_schema_force_type import BulkAnalyzeSchemaForceType
from .bulk_analyze_schema_object_type import BulkAnalyzeSchemaObjectType
from .bulk_metadata_filling_schema import BulkMetadataFillingSchema
from .bulk_metadata_filling_schema_object_type import (
    BulkMetadataFillingSchemaObjectType,
)
from .bulk_transcribe_schema import BulkTranscribeSchema
from .bulk_transcribe_schema_object_type import BulkTranscribeSchemaObjectType
from .delete_edge_transcode_workers_by_worker_id_response_default import (
    DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault,
)
from .delete_storages_by_storage_id_files_by_file_id_transcode_response_default import (
    DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault,
)
from .delete_storages_by_storage_id_response_default import (
    DeleteStoragesByStorageIdResponseDefault,
)
from .delete_storages_by_storage_id_transcode_by_record_id_response_default import (
    DeleteStoragesByStorageIdTranscodeByRecordIdResponseDefault,
)
from .delete_transcode_by_transcode_job_id_response_default import (
    DeleteTranscodeByTranscodeJobIdResponseDefault,
)
from .edge_thumbnail_job_field_schema import EdgeThumbnailJobFieldSchema
from .edge_transcode_endpoint_schema import EdgeTranscodeEndpointSchema
from .edge_transcode_endpoint_schema_data_type_0 import (
    EdgeTranscodeEndpointSchemaDataType0,
)
from .edge_transcode_input_schema import EdgeTranscodeInputSchema
from .edge_transcode_job_field_schema import EdgeTranscodeJobFieldSchema
from .edge_transcode_job_schema import EdgeTranscodeJobSchema
from .edge_transcode_jobs_schema import EdgeTranscodeJobsSchema
from .edge_transcode_worker_schema import EdgeTranscodeWorkerSchema
from .edge_transcode_worker_schema_status import EdgeTranscodeWorkerSchemaStatus
from .edge_transcode_workers_schema import EdgeTranscodeWorkersSchema
from .endpoint_schema import EndpointSchema
from .endpoint_schema_data_type_0 import EndpointSchemaDataType0
from .endpoint_schema_headers_type_0 import EndpointSchemaHeadersType0
from .facet_bucket_schema import FacetBucketSchema
from .facet_schema import FacetSchema
from .generate_collection_keyframe_schema import GenerateCollectionKeyframeSchema
from .get_edge_transcode_workers_by_worker_id_response_default import (
    GetEdgeTranscodeWorkersByWorkerIdResponseDefault,
)
from .get_edge_transcode_workers_response_default import (
    GetEdgeTranscodeWorkersResponseDefault,
)
from .get_metadata_filling_proposals_assets_by_asset_id_versions_by_version_id_response_default import (
    GetMetadataFillingProposalsAssetsByAssetIdVersionsByVersionIdResponseDefault,
)
from .get_metadata_filling_proposals_by_job_id_response_default import (
    GetMetadataFillingProposalsByJobIdResponseDefault,
)
from .get_storages_by_storage_id_edge_transcode_jobs_response_default import (
    GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault,
)
from .get_storages_by_storage_id_transcode_by_record_id_response_default import (
    GetStoragesByStorageIdTranscodeByRecordIdResponseDefault,
)
from .get_storages_by_storage_id_transcode_response_default import (
    GetStoragesByStorageIdTranscodeResponseDefault,
)
from .get_transcode_by_object_type_by_object_id_response_default import (
    GetTranscodeByObjectTypeByObjectIdResponseDefault,
)
from .get_transcode_by_object_type_by_object_id_versions_by_version_id_response_default import (
    GetTranscodeByObjectTypeByObjectIdVersionsByVersionIdResponseDefault,
)
from .get_transcode_by_transcode_job_id_response_default import (
    GetTranscodeByTranscodeJobIdResponseDefault,
)
from .get_transcode_queue_response_default import GetTranscodeQueueResponseDefault
from .get_transcode_queue_system_response_default import (
    GetTranscodeQueueSystemResponseDefault,
)
from .input_schema import InputSchema
from .job_base_schema import JobBaseSchema
from .job_schema import JobSchema
from .job_schema_analysis_data_type_0 import JobSchemaAnalysisDataType0
from .job_step import JobStep
from .job_step_schema import JobStepSchema
from .jobs_priority_schema import JobsPrioritySchema
from .jobs_state_schema import JobsStateSchema
from .jobs_state_schema_action import JobsStateSchemaAction
from .list_objects_schema import ListObjectsSchema
from .llm_metadata_job_schema import LLMMetadataJobSchema
from .llm_metadata_job_schema_analysis_data_type_0 import (
    LLMMetadataJobSchemaAnalysisDataType0,
)
from .local_storage_file_transcode_job_schema import LocalStorageFileTranscodeJobSchema
from .local_storage_file_transcode_jobs_schema import (
    LocalStorageFileTranscodeJobsSchema,
)
from .local_transcode_input_schema import LocalTranscodeInputSchema
from .local_transcode_job_schema import LocalTranscodeJobSchema
from .local_transcode_job_schema_analysis_data_type_0 import (
    LocalTranscodeJobSchemaAnalysisDataType0,
)
from .metadata_filling_proposal_by_asset_query_params_schema import (
    MetadataFillingProposalByAssetQueryParamsSchema,
)
from .metadata_filling_proposal_schema import MetadataFillingProposalSchema
from .metadata_filling_proposal_schema_review_status import (
    MetadataFillingProposalSchemaReviewStatus,
)
from .metadata_filling_response_schema import MetadataFillingResponseSchema
from .metadata_filling_response_schema_metadata_values_type_0 import (
    MetadataFillingResponseSchemaMetadataValuesType0,
)
from .metadata_filling_schema import MetadataFillingSchema
from .output_endpoint import OutputEndpoint
from .output_endpoint_headers_type_0 import OutputEndpointHeadersType0
from .output_endpoint_schema import OutputEndpointSchema
from .output_endpoint_schema_headers_type_0 import OutputEndpointSchemaHeadersType0
from .patch_edge_transcode_workers_by_worker_id_response_default import (
    PatchEdgeTranscodeWorkersByWorkerIdResponseDefault,
)
from .post_analyze_assets_by_asset_id_profiles_by_profile_id_response_default import (
    PostAnalyzeAssetsByAssetIdProfilesByProfileIdResponseDefault,
)
from .post_analyze_assets_by_asset_id_profiles_default_by_media_type_response_default import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault,
)
from .post_analyze_assets_by_asset_id_profiles_default_response_default import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultResponseDefault,
)
from .post_analyze_assets_by_asset_id_response_default import (
    PostAnalyzeAssetsByAssetIdResponseDefault,
)
from .post_analyze_bulk_response_default import PostAnalyzeBulkResponseDefault
from .post_edge_transcode_jobs_by_job_id_acknowledge_response_default import (
    PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefault,
)
from .post_edge_transcode_workers_response_default import (
    PostEdgeTranscodeWorkersResponseDefault,
)
from .post_keyframes_collections_by_collection_id_response_default import (
    PostKeyframesCollectionsByCollectionIdResponseDefault,
)
from .post_keyframes_playlists_by_playlist_id_response_default import (
    PostKeyframesPlaylistsByPlaylistIdResponseDefault,
)
from .post_metadata_filling_assets_by_asset_id_versions_by_version_id_response_default import (
    PostMetadataFillingAssetsByAssetIdVersionsByVersionIdResponseDefault,
)
from .post_metadata_filling_bulk_response_default import (
    PostMetadataFillingBulkResponseDefault,
)
from .post_metadata_filling_proposals_by_job_id_accept_response_default import (
    PostMetadataFillingProposalsByJobIdAcceptResponseDefault,
)
from .post_metadata_filling_proposals_by_job_id_discard_response_default import (
    PostMetadataFillingProposalsByJobIdDiscardResponseDefault,
)
from .post_metadata_filling_proposals_by_job_id_regenerate_response_default import (
    PostMetadataFillingProposalsByJobIdRegenerateResponseDefault,
)
from .post_transcode_by_transcode_job_id_position_by_position_response_default import (
    PostTranscodeByTranscodeJobIdPositionByPositionResponseDefault,
)
from .post_transcode_response_default import PostTranscodeResponseDefault
from .post_transcribe_assets_by_asset_id_profiles_default_response_default import (
    PostTranscribeAssetsByAssetIdProfilesDefaultResponseDefault,
)
from .post_transcribe_bulk_response_default import PostTranscribeBulkResponseDefault
from .put_edge_transcode_workers_by_worker_id_response_default import (
    PutEdgeTranscodeWorkersByWorkerIdResponseDefault,
)
from .put_transcode_by_transcode_job_id_priority_by_priority_response_default import (
    PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefault,
)
from .reindex_queue_record_schema import ReindexQueueRecordSchema
from .specified_keyframes import SpecifiedKeyframes
from .specified_keyframes_schema import SpecifiedKeyframesSchema
from .thumbnail_job import ThumbnailJob
from .thumbnail_job_schema import ThumbnailJobSchema
from .transcode_elastic_queue_record import TranscodeElasticQueueRecord
from .transcode_elastic_queue_record_schema import TranscodeElasticQueueRecordSchema
from .transcode_es_queue_records_schema import TranscodeESQueueRecordsSchema
from .transcode_job import TranscodeJob
from .transcode_job_schema import TranscodeJobSchema
from .transcode_queue_object_schema import TranscodeQueueObjectSchema
from .transcode_queue_record_schema import TranscodeQueueRecordSchema
from .transcode_queue_schema import TranscodeQueueSchema
from .transcode_queue_schema_facets_type_0 import TranscodeQueueSchemaFacetsType0
from .transcode_validate_media_info_schema import TranscodeValidateMediaInfoSchema
from .transcoders import Transcoders
from .transcoders_schema import TranscodersSchema
from .transcoders_schema_settings_type_0 import TranscodersSchemaSettingsType0
from .transcoders_settings_type_0 import TranscodersSettingsType0
from .transcribe_schema import TranscribeSchema
from .wildmoka_pipeline_transcode import WildmokaPipelineTranscode
from .wildmoka_pipeline_transcode_graph import WildmokaPipelineTranscodeGraph
from .wildmoka_pipeline_transcode_parameters import WildmokaPipelineTranscodeParameters
from .wildmoka_protect_transcode import WildmokaProtectTranscode
from .wildmoka_protect_transcode_callback_headers import (
    WildmokaProtectTranscodeCallbackHeaders,
)
from .wildmoka_protect_transcode_create_file_callback_payload import (
    WildmokaProtectTranscodeCreateFileCallbackPayload,
)

__all__ = (
    "AbortStorageTranscodeJobsSchema",
    "AnalyzeSchema",
    "AnalyzeSchemaForceType",
    "AssetLinkData",
    "AssetLinkURLSchema",
    "BulkActionSchema",
    "BulkActionSchemaObjectType",
    "BulkAnalyzeSchema",
    "BulkAnalyzeSchemaForceType",
    "BulkAnalyzeSchemaObjectType",
    "BulkMetadataFillingSchema",
    "BulkMetadataFillingSchemaObjectType",
    "BulkTranscribeSchema",
    "BulkTranscribeSchemaObjectType",
    "DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault",
    "DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault",
    "DeleteStoragesByStorageIdResponseDefault",
    "DeleteStoragesByStorageIdTranscodeByRecordIdResponseDefault",
    "DeleteTranscodeByTranscodeJobIdResponseDefault",
    "EdgeThumbnailJobFieldSchema",
    "EdgeTranscodeEndpointSchema",
    "EdgeTranscodeEndpointSchemaDataType0",
    "EdgeTranscodeInputSchema",
    "EdgeTranscodeJobFieldSchema",
    "EdgeTranscodeJobSchema",
    "EdgeTranscodeJobsSchema",
    "EdgeTranscodeWorkerSchema",
    "EdgeTranscodeWorkerSchemaStatus",
    "EdgeTranscodeWorkersSchema",
    "EndpointSchema",
    "EndpointSchemaDataType0",
    "EndpointSchemaHeadersType0",
    "FacetBucketSchema",
    "FacetSchema",
    "GenerateCollectionKeyframeSchema",
    "GetEdgeTranscodeWorkersByWorkerIdResponseDefault",
    "GetEdgeTranscodeWorkersResponseDefault",
    "GetMetadataFillingProposalsAssetsByAssetIdVersionsByVersionIdResponseDefault",
    "GetMetadataFillingProposalsByJobIdResponseDefault",
    "GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault",
    "GetStoragesByStorageIdTranscodeByRecordIdResponseDefault",
    "GetStoragesByStorageIdTranscodeResponseDefault",
    "GetTranscodeByObjectTypeByObjectIdResponseDefault",
    "GetTranscodeByObjectTypeByObjectIdVersionsByVersionIdResponseDefault",
    "GetTranscodeByTranscodeJobIdResponseDefault",
    "GetTranscodeQueueResponseDefault",
    "GetTranscodeQueueSystemResponseDefault",
    "InputSchema",
    "JobBaseSchema",
    "JobSchema",
    "JobSchemaAnalysisDataType0",
    "JobsPrioritySchema",
    "JobsStateSchema",
    "JobsStateSchemaAction",
    "JobStep",
    "JobStepSchema",
    "ListObjectsSchema",
    "LLMMetadataJobSchema",
    "LLMMetadataJobSchemaAnalysisDataType0",
    "LocalStorageFileTranscodeJobSchema",
    "LocalStorageFileTranscodeJobsSchema",
    "LocalTranscodeInputSchema",
    "LocalTranscodeJobSchema",
    "LocalTranscodeJobSchemaAnalysisDataType0",
    "MetadataFillingProposalByAssetQueryParamsSchema",
    "MetadataFillingProposalSchema",
    "MetadataFillingProposalSchemaReviewStatus",
    "MetadataFillingResponseSchema",
    "MetadataFillingResponseSchemaMetadataValuesType0",
    "MetadataFillingSchema",
    "OutputEndpoint",
    "OutputEndpointHeadersType0",
    "OutputEndpointSchema",
    "OutputEndpointSchemaHeadersType0",
    "PatchEdgeTranscodeWorkersByWorkerIdResponseDefault",
    "PostAnalyzeAssetsByAssetIdProfilesByProfileIdResponseDefault",
    "PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefault",
    "PostAnalyzeAssetsByAssetIdProfilesDefaultResponseDefault",
    "PostAnalyzeAssetsByAssetIdResponseDefault",
    "PostAnalyzeBulkResponseDefault",
    "PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefault",
    "PostEdgeTranscodeWorkersResponseDefault",
    "PostKeyframesCollectionsByCollectionIdResponseDefault",
    "PostKeyframesPlaylistsByPlaylistIdResponseDefault",
    "PostMetadataFillingAssetsByAssetIdVersionsByVersionIdResponseDefault",
    "PostMetadataFillingBulkResponseDefault",
    "PostMetadataFillingProposalsByJobIdAcceptResponseDefault",
    "PostMetadataFillingProposalsByJobIdDiscardResponseDefault",
    "PostMetadataFillingProposalsByJobIdRegenerateResponseDefault",
    "PostTranscodeByTranscodeJobIdPositionByPositionResponseDefault",
    "PostTranscodeResponseDefault",
    "PostTranscribeAssetsByAssetIdProfilesDefaultResponseDefault",
    "PostTranscribeBulkResponseDefault",
    "PutEdgeTranscodeWorkersByWorkerIdResponseDefault",
    "PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefault",
    "ReindexQueueRecordSchema",
    "SpecifiedKeyframes",
    "SpecifiedKeyframesSchema",
    "ThumbnailJob",
    "ThumbnailJobSchema",
    "TranscodeElasticQueueRecord",
    "TranscodeElasticQueueRecordSchema",
    "TranscodeESQueueRecordsSchema",
    "TranscodeJob",
    "TranscodeJobSchema",
    "TranscodeQueueObjectSchema",
    "TranscodeQueueRecordSchema",
    "TranscodeQueueSchema",
    "TranscodeQueueSchemaFacetsType0",
    "Transcoders",
    "TranscodersSchema",
    "TranscodersSchemaSettingsType0",
    "TranscodersSettingsType0",
    "TranscodeValidateMediaInfoSchema",
    "TranscribeSchema",
    "WildmokaPipelineTranscode",
    "WildmokaPipelineTranscodeGraph",
    "WildmokaPipelineTranscodeParameters",
    "WildmokaProtectTranscode",
    "WildmokaProtectTranscodeCallbackHeaders",
    "WildmokaProtectTranscodeCreateFileCallbackPayload",
)
