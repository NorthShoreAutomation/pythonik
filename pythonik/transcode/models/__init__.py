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
from .delete_edge_transcode_workers_by_worker_id_response_default_type_0 import (
    DeleteEdgeTranscodeWorkersByWorkerIdResponseDefaultType0,
)
from .delete_edge_transcode_workers_by_worker_id_response_default_type_1 import (
    DeleteEdgeTranscodeWorkersByWorkerIdResponseDefaultType1,
)
from .delete_edge_transcode_workers_by_worker_id_response_default_type_1_errors import (
    DeleteEdgeTranscodeWorkersByWorkerIdResponseDefaultType1Errors,
)
from .delete_storages_by_storage_id_files_by_file_id_transcode_response_default_type_0 import (
    DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefaultType0,
)
from .delete_storages_by_storage_id_files_by_file_id_transcode_response_default_type_1 import (
    DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefaultType1,
)
from .delete_storages_by_storage_id_files_by_file_id_transcode_response_default_type_1_errors import (
    DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefaultType1Errors,
)
from .delete_storages_by_storage_id_response_default_type_0 import (
    DeleteStoragesByStorageIdResponseDefaultType0,
)
from .delete_storages_by_storage_id_response_default_type_1 import (
    DeleteStoragesByStorageIdResponseDefaultType1,
)
from .delete_storages_by_storage_id_response_default_type_1_errors import (
    DeleteStoragesByStorageIdResponseDefaultType1Errors,
)
from .delete_storages_by_storage_id_transcode_by_record_id_response_default_type_0 import (
    DeleteStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0,
)
from .delete_storages_by_storage_id_transcode_by_record_id_response_default_type_1 import (
    DeleteStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1,
)
from .delete_storages_by_storage_id_transcode_by_record_id_response_default_type_1_errors import (
    DeleteStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1Errors,
)
from .delete_transcode_by_transcode_job_id_response_default_type_0 import (
    DeleteTranscodeByTranscodeJobIdResponseDefaultType0,
)
from .delete_transcode_by_transcode_job_id_response_default_type_1 import (
    DeleteTranscodeByTranscodeJobIdResponseDefaultType1,
)
from .delete_transcode_by_transcode_job_id_response_default_type_1_errors import (
    DeleteTranscodeByTranscodeJobIdResponseDefaultType1Errors,
)
from .edge_thumbnail_job_field_schema import EdgeThumbnailJobFieldSchema
from .edge_transcode_endpoint_schema import EdgeTranscodeEndpointSchema
from .edge_transcode_endpoint_schema_data import EdgeTranscodeEndpointSchemaData
from .edge_transcode_input_schema import EdgeTranscodeInputSchema
from .edge_transcode_job_field_schema import EdgeTranscodeJobFieldSchema
from .edge_transcode_job_schema import EdgeTranscodeJobSchema
from .edge_transcode_jobs_schema import EdgeTranscodeJobsSchema
from .edge_transcode_worker_schema import EdgeTranscodeWorkerSchema
from .edge_transcode_worker_schema_status import EdgeTranscodeWorkerSchemaStatus
from .edge_transcode_workers_schema import EdgeTranscodeWorkersSchema
from .endpoint_schema import EndpointSchema
from .endpoint_schema_data import EndpointSchemaData
from .endpoint_schema_headers import EndpointSchemaHeaders
from .facet_bucket_schema import FacetBucketSchema
from .facet_schema import FacetSchema
from .generate_collection_keyframe_schema import GenerateCollectionKeyframeSchema
from .get_edge_transcode_workers_by_worker_id_response_default_type_0 import (
    GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0,
)
from .get_edge_transcode_workers_by_worker_id_response_default_type_1 import (
    GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1,
)
from .get_edge_transcode_workers_by_worker_id_response_default_type_1_errors import (
    GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1Errors,
)
from .get_edge_transcode_workers_response_default_type_0 import (
    GetEdgeTranscodeWorkersResponseDefaultType0,
)
from .get_edge_transcode_workers_response_default_type_1 import (
    GetEdgeTranscodeWorkersResponseDefaultType1,
)
from .get_edge_transcode_workers_response_default_type_1_errors import (
    GetEdgeTranscodeWorkersResponseDefaultType1Errors,
)
from .get_metadata_filling_proposals_assets_by_asset_id_versions_by_version_id_response_default_type_0 import (
    GetMetadataFillingProposalsAssetsByAssetIdVersionsByVersionIdResponseDefaultType0,
)
from .get_metadata_filling_proposals_assets_by_asset_id_versions_by_version_id_response_default_type_1 import (
    GetMetadataFillingProposalsAssetsByAssetIdVersionsByVersionIdResponseDefaultType1,
)
from .get_metadata_filling_proposals_assets_by_asset_id_versions_by_version_id_response_default_type_1_errors import (
    GetMetadataFillingProposalsAssetsByAssetIdVersionsByVersionIdResponseDefaultType1Errors,
)
from .get_metadata_filling_proposals_by_job_id_response_default_type_0 import (
    GetMetadataFillingProposalsByJobIdResponseDefaultType0,
)
from .get_metadata_filling_proposals_by_job_id_response_default_type_1 import (
    GetMetadataFillingProposalsByJobIdResponseDefaultType1,
)
from .get_metadata_filling_proposals_by_job_id_response_default_type_1_errors import (
    GetMetadataFillingProposalsByJobIdResponseDefaultType1Errors,
)
from .get_storages_by_storage_id_edge_transcode_jobs_response_default_type_0 import (
    GetStoragesByStorageIdEdgeTranscodeJobsResponseDefaultType0,
)
from .get_storages_by_storage_id_edge_transcode_jobs_response_default_type_1 import (
    GetStoragesByStorageIdEdgeTranscodeJobsResponseDefaultType1,
)
from .get_storages_by_storage_id_edge_transcode_jobs_response_default_type_1_errors import (
    GetStoragesByStorageIdEdgeTranscodeJobsResponseDefaultType1Errors,
)
from .get_storages_by_storage_id_transcode_by_record_id_response_default_type_0 import (
    GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0,
)
from .get_storages_by_storage_id_transcode_by_record_id_response_default_type_1 import (
    GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1,
)
from .get_storages_by_storage_id_transcode_by_record_id_response_default_type_1_errors import (
    GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1Errors,
)
from .get_storages_by_storage_id_transcode_response_default_type_0 import (
    GetStoragesByStorageIdTranscodeResponseDefaultType0,
)
from .get_storages_by_storage_id_transcode_response_default_type_1 import (
    GetStoragesByStorageIdTranscodeResponseDefaultType1,
)
from .get_storages_by_storage_id_transcode_response_default_type_1_errors import (
    GetStoragesByStorageIdTranscodeResponseDefaultType1Errors,
)
from .get_transcode_by_object_type_by_object_id_response_default_type_0 import (
    GetTranscodeByObjectTypeByObjectIdResponseDefaultType0,
)
from .get_transcode_by_object_type_by_object_id_response_default_type_1 import (
    GetTranscodeByObjectTypeByObjectIdResponseDefaultType1,
)
from .get_transcode_by_object_type_by_object_id_response_default_type_1_errors import (
    GetTranscodeByObjectTypeByObjectIdResponseDefaultType1Errors,
)
from .get_transcode_by_object_type_by_object_id_versions_by_version_id_response_default_type_0 import (
    GetTranscodeByObjectTypeByObjectIdVersionsByVersionIdResponseDefaultType0,
)
from .get_transcode_by_object_type_by_object_id_versions_by_version_id_response_default_type_1 import (
    GetTranscodeByObjectTypeByObjectIdVersionsByVersionIdResponseDefaultType1,
)
from .get_transcode_by_object_type_by_object_id_versions_by_version_id_response_default_type_1_errors import (
    GetTranscodeByObjectTypeByObjectIdVersionsByVersionIdResponseDefaultType1Errors,
)
from .get_transcode_by_transcode_job_id_response_default_type_0 import (
    GetTranscodeByTranscodeJobIdResponseDefaultType0,
)
from .get_transcode_by_transcode_job_id_response_default_type_1 import (
    GetTranscodeByTranscodeJobIdResponseDefaultType1,
)
from .get_transcode_by_transcode_job_id_response_default_type_1_errors import (
    GetTranscodeByTranscodeJobIdResponseDefaultType1Errors,
)
from .get_transcode_queue_response_default_type_0 import (
    GetTranscodeQueueResponseDefaultType0,
)
from .get_transcode_queue_response_default_type_1 import (
    GetTranscodeQueueResponseDefaultType1,
)
from .get_transcode_queue_response_default_type_1_errors import (
    GetTranscodeQueueResponseDefaultType1Errors,
)
from .get_transcode_queue_system_response_default_type_0 import (
    GetTranscodeQueueSystemResponseDefaultType0,
)
from .get_transcode_queue_system_response_default_type_1 import (
    GetTranscodeQueueSystemResponseDefaultType1,
)
from .get_transcode_queue_system_response_default_type_1_errors import (
    GetTranscodeQueueSystemResponseDefaultType1Errors,
)
from .input_schema import InputSchema
from .job_base_schema import JobBaseSchema
from .job_schema import JobSchema
from .job_schema_analysis_data import JobSchemaAnalysisData
from .job_step import JobStep
from .job_step_schema import JobStepSchema
from .jobs_priority_schema import JobsPrioritySchema
from .jobs_state_schema import JobsStateSchema
from .jobs_state_schema_action import JobsStateSchemaAction
from .list_objects_schema import ListObjectsSchema
from .llm_metadata_job_schema import LLMMetadataJobSchema
from .llm_metadata_job_schema_analysis_data import LLMMetadataJobSchemaAnalysisData
from .local_storage_file_transcode_job_schema import LocalStorageFileTranscodeJobSchema
from .local_storage_file_transcode_jobs_schema import (
    LocalStorageFileTranscodeJobsSchema,
)
from .local_transcode_input_schema import LocalTranscodeInputSchema
from .local_transcode_job_schema import LocalTranscodeJobSchema
from .local_transcode_job_schema_analysis_data import (
    LocalTranscodeJobSchemaAnalysisData,
)
from .metadata_filling_proposal_by_asset_query_params_schema import (
    MetadataFillingProposalByAssetQueryParamsSchema,
)
from .metadata_filling_proposal_schema import MetadataFillingProposalSchema
from .metadata_filling_proposal_schema_review_status import (
    MetadataFillingProposalSchemaReviewStatus,
)
from .metadata_filling_response_schema import MetadataFillingResponseSchema
from .metadata_filling_response_schema_metadata_values import (
    MetadataFillingResponseSchemaMetadataValues,
)
from .metadata_filling_schema import MetadataFillingSchema
from .output_endpoint import OutputEndpoint
from .output_endpoint_headers import OutputEndpointHeaders
from .output_endpoint_schema import OutputEndpointSchema
from .output_endpoint_schema_headers import OutputEndpointSchemaHeaders
from .patch_edge_transcode_workers_by_worker_id_response_default_type_0 import (
    PatchEdgeTranscodeWorkersByWorkerIdResponseDefaultType0,
)
from .patch_edge_transcode_workers_by_worker_id_response_default_type_1 import (
    PatchEdgeTranscodeWorkersByWorkerIdResponseDefaultType1,
)
from .patch_edge_transcode_workers_by_worker_id_response_default_type_1_errors import (
    PatchEdgeTranscodeWorkersByWorkerIdResponseDefaultType1Errors,
)
from .post_analyze_assets_by_asset_id_profiles_by_profile_id_response_default_type_0 import (
    PostAnalyzeAssetsByAssetIdProfilesByProfileIdResponseDefaultType0,
)
from .post_analyze_assets_by_asset_id_profiles_by_profile_id_response_default_type_1 import (
    PostAnalyzeAssetsByAssetIdProfilesByProfileIdResponseDefaultType1,
)
from .post_analyze_assets_by_asset_id_profiles_by_profile_id_response_default_type_1_errors import (
    PostAnalyzeAssetsByAssetIdProfilesByProfileIdResponseDefaultType1Errors,
)
from .post_analyze_assets_by_asset_id_profiles_default_by_media_type_response_default_type_0 import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefaultType0,
)
from .post_analyze_assets_by_asset_id_profiles_default_by_media_type_response_default_type_1 import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefaultType1,
)
from .post_analyze_assets_by_asset_id_profiles_default_by_media_type_response_default_type_1_errors import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefaultType1Errors,
)
from .post_analyze_assets_by_asset_id_profiles_default_response_default_type_0 import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultResponseDefaultType0,
)
from .post_analyze_assets_by_asset_id_profiles_default_response_default_type_1 import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultResponseDefaultType1,
)
from .post_analyze_assets_by_asset_id_profiles_default_response_default_type_1_errors import (
    PostAnalyzeAssetsByAssetIdProfilesDefaultResponseDefaultType1Errors,
)
from .post_analyze_assets_by_asset_id_response_default_type_0 import (
    PostAnalyzeAssetsByAssetIdResponseDefaultType0,
)
from .post_analyze_assets_by_asset_id_response_default_type_1 import (
    PostAnalyzeAssetsByAssetIdResponseDefaultType1,
)
from .post_analyze_assets_by_asset_id_response_default_type_1_errors import (
    PostAnalyzeAssetsByAssetIdResponseDefaultType1Errors,
)
from .post_analyze_bulk_response_default_type_0 import (
    PostAnalyzeBulkResponseDefaultType0,
)
from .post_analyze_bulk_response_default_type_1 import (
    PostAnalyzeBulkResponseDefaultType1,
)
from .post_analyze_bulk_response_default_type_1_errors import (
    PostAnalyzeBulkResponseDefaultType1Errors,
)
from .post_edge_transcode_jobs_by_job_id_acknowledge_response_default_type_0 import (
    PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0,
)
from .post_edge_transcode_jobs_by_job_id_acknowledge_response_default_type_1 import (
    PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1,
)
from .post_edge_transcode_jobs_by_job_id_acknowledge_response_default_type_1_errors import (
    PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1Errors,
)
from .post_edge_transcode_workers_response_default_type_0 import (
    PostEdgeTranscodeWorkersResponseDefaultType0,
)
from .post_edge_transcode_workers_response_default_type_1 import (
    PostEdgeTranscodeWorkersResponseDefaultType1,
)
from .post_edge_transcode_workers_response_default_type_1_errors import (
    PostEdgeTranscodeWorkersResponseDefaultType1Errors,
)
from .post_keyframes_collections_by_collection_id_response_default_type_0 import (
    PostKeyframesCollectionsByCollectionIdResponseDefaultType0,
)
from .post_keyframes_collections_by_collection_id_response_default_type_1 import (
    PostKeyframesCollectionsByCollectionIdResponseDefaultType1,
)
from .post_keyframes_collections_by_collection_id_response_default_type_1_errors import (
    PostKeyframesCollectionsByCollectionIdResponseDefaultType1Errors,
)
from .post_keyframes_playlists_by_playlist_id_response_default_type_0 import (
    PostKeyframesPlaylistsByPlaylistIdResponseDefaultType0,
)
from .post_keyframes_playlists_by_playlist_id_response_default_type_1 import (
    PostKeyframesPlaylistsByPlaylistIdResponseDefaultType1,
)
from .post_keyframes_playlists_by_playlist_id_response_default_type_1_errors import (
    PostKeyframesPlaylistsByPlaylistIdResponseDefaultType1Errors,
)
from .post_metadata_filling_assets_by_asset_id_versions_by_version_id_response_default_type_0 import (
    PostMetadataFillingAssetsByAssetIdVersionsByVersionIdResponseDefaultType0,
)
from .post_metadata_filling_assets_by_asset_id_versions_by_version_id_response_default_type_1 import (
    PostMetadataFillingAssetsByAssetIdVersionsByVersionIdResponseDefaultType1,
)
from .post_metadata_filling_assets_by_asset_id_versions_by_version_id_response_default_type_1_errors import (
    PostMetadataFillingAssetsByAssetIdVersionsByVersionIdResponseDefaultType1Errors,
)
from .post_metadata_filling_bulk_response_default_type_0 import (
    PostMetadataFillingBulkResponseDefaultType0,
)
from .post_metadata_filling_bulk_response_default_type_1 import (
    PostMetadataFillingBulkResponseDefaultType1,
)
from .post_metadata_filling_bulk_response_default_type_1_errors import (
    PostMetadataFillingBulkResponseDefaultType1Errors,
)
from .post_metadata_filling_proposals_by_job_id_accept_response_default_type_0 import (
    PostMetadataFillingProposalsByJobIdAcceptResponseDefaultType0,
)
from .post_metadata_filling_proposals_by_job_id_accept_response_default_type_1 import (
    PostMetadataFillingProposalsByJobIdAcceptResponseDefaultType1,
)
from .post_metadata_filling_proposals_by_job_id_accept_response_default_type_1_errors import (
    PostMetadataFillingProposalsByJobIdAcceptResponseDefaultType1Errors,
)
from .post_metadata_filling_proposals_by_job_id_discard_response_default_type_0 import (
    PostMetadataFillingProposalsByJobIdDiscardResponseDefaultType0,
)
from .post_metadata_filling_proposals_by_job_id_discard_response_default_type_1 import (
    PostMetadataFillingProposalsByJobIdDiscardResponseDefaultType1,
)
from .post_metadata_filling_proposals_by_job_id_discard_response_default_type_1_errors import (
    PostMetadataFillingProposalsByJobIdDiscardResponseDefaultType1Errors,
)
from .post_metadata_filling_proposals_by_job_id_regenerate_response_default_type_0 import (
    PostMetadataFillingProposalsByJobIdRegenerateResponseDefaultType0,
)
from .post_metadata_filling_proposals_by_job_id_regenerate_response_default_type_1 import (
    PostMetadataFillingProposalsByJobIdRegenerateResponseDefaultType1,
)
from .post_metadata_filling_proposals_by_job_id_regenerate_response_default_type_1_errors import (
    PostMetadataFillingProposalsByJobIdRegenerateResponseDefaultType1Errors,
)
from .post_transcode_by_transcode_job_id_position_by_position_response_default_type_0 import (
    PostTranscodeByTranscodeJobIdPositionByPositionResponseDefaultType0,
)
from .post_transcode_by_transcode_job_id_position_by_position_response_default_type_1 import (
    PostTranscodeByTranscodeJobIdPositionByPositionResponseDefaultType1,
)
from .post_transcode_by_transcode_job_id_position_by_position_response_default_type_1_errors import (
    PostTranscodeByTranscodeJobIdPositionByPositionResponseDefaultType1Errors,
)
from .post_transcode_response_default_type_0 import PostTranscodeResponseDefaultType0
from .post_transcode_response_default_type_1 import PostTranscodeResponseDefaultType1
from .post_transcode_response_default_type_1_errors import (
    PostTranscodeResponseDefaultType1Errors,
)
from .post_transcribe_assets_by_asset_id_profiles_default_response_default_type_0 import (
    PostTranscribeAssetsByAssetIdProfilesDefaultResponseDefaultType0,
)
from .post_transcribe_assets_by_asset_id_profiles_default_response_default_type_1 import (
    PostTranscribeAssetsByAssetIdProfilesDefaultResponseDefaultType1,
)
from .post_transcribe_assets_by_asset_id_profiles_default_response_default_type_1_errors import (
    PostTranscribeAssetsByAssetIdProfilesDefaultResponseDefaultType1Errors,
)
from .post_transcribe_bulk_response_default_type_0 import (
    PostTranscribeBulkResponseDefaultType0,
)
from .post_transcribe_bulk_response_default_type_1 import (
    PostTranscribeBulkResponseDefaultType1,
)
from .post_transcribe_bulk_response_default_type_1_errors import (
    PostTranscribeBulkResponseDefaultType1Errors,
)
from .put_edge_transcode_workers_by_worker_id_response_default_type_0 import (
    PutEdgeTranscodeWorkersByWorkerIdResponseDefaultType0,
)
from .put_edge_transcode_workers_by_worker_id_response_default_type_1 import (
    PutEdgeTranscodeWorkersByWorkerIdResponseDefaultType1,
)
from .put_edge_transcode_workers_by_worker_id_response_default_type_1_errors import (
    PutEdgeTranscodeWorkersByWorkerIdResponseDefaultType1Errors,
)
from .put_transcode_by_transcode_job_id_priority_by_priority_response_default_type_0 import (
    PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0,
)
from .put_transcode_by_transcode_job_id_priority_by_priority_response_default_type_1 import (
    PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1,
)
from .put_transcode_by_transcode_job_id_priority_by_priority_response_default_type_1_errors import (
    PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1Errors,
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
from .transcode_queue_schema_facets import TranscodeQueueSchemaFacets
from .transcode_validate_media_info_schema import TranscodeValidateMediaInfoSchema
from .transcoders import Transcoders
from .transcoders_schema import TranscodersSchema
from .transcoders_schema_settings import TranscodersSchemaSettings
from .transcoders_settings import TranscodersSettings
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
    "DeleteEdgeTranscodeWorkersByWorkerIdResponseDefaultType0",
    "DeleteEdgeTranscodeWorkersByWorkerIdResponseDefaultType1",
    "DeleteEdgeTranscodeWorkersByWorkerIdResponseDefaultType1Errors",
    "DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefaultType0",
    "DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefaultType1",
    "DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefaultType1Errors",
    "DeleteStoragesByStorageIdResponseDefaultType0",
    "DeleteStoragesByStorageIdResponseDefaultType1",
    "DeleteStoragesByStorageIdResponseDefaultType1Errors",
    "DeleteStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0",
    "DeleteStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1",
    "DeleteStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1Errors",
    "DeleteTranscodeByTranscodeJobIdResponseDefaultType0",
    "DeleteTranscodeByTranscodeJobIdResponseDefaultType1",
    "DeleteTranscodeByTranscodeJobIdResponseDefaultType1Errors",
    "EdgeThumbnailJobFieldSchema",
    "EdgeTranscodeEndpointSchema",
    "EdgeTranscodeEndpointSchemaData",
    "EdgeTranscodeInputSchema",
    "EdgeTranscodeJobFieldSchema",
    "EdgeTranscodeJobSchema",
    "EdgeTranscodeJobsSchema",
    "EdgeTranscodeWorkerSchema",
    "EdgeTranscodeWorkerSchemaStatus",
    "EdgeTranscodeWorkersSchema",
    "EndpointSchema",
    "EndpointSchemaData",
    "EndpointSchemaHeaders",
    "FacetBucketSchema",
    "FacetSchema",
    "GenerateCollectionKeyframeSchema",
    "GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0",
    "GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1",
    "GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1Errors",
    "GetEdgeTranscodeWorkersResponseDefaultType0",
    "GetEdgeTranscodeWorkersResponseDefaultType1",
    "GetEdgeTranscodeWorkersResponseDefaultType1Errors",
    "GetMetadataFillingProposalsAssetsByAssetIdVersionsByVersionIdResponseDefaultType0",
    "GetMetadataFillingProposalsAssetsByAssetIdVersionsByVersionIdResponseDefaultType1",
    "GetMetadataFillingProposalsAssetsByAssetIdVersionsByVersionIdResponseDefaultType1Errors",
    "GetMetadataFillingProposalsByJobIdResponseDefaultType0",
    "GetMetadataFillingProposalsByJobIdResponseDefaultType1",
    "GetMetadataFillingProposalsByJobIdResponseDefaultType1Errors",
    "GetStoragesByStorageIdEdgeTranscodeJobsResponseDefaultType0",
    "GetStoragesByStorageIdEdgeTranscodeJobsResponseDefaultType1",
    "GetStoragesByStorageIdEdgeTranscodeJobsResponseDefaultType1Errors",
    "GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0",
    "GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1",
    "GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1Errors",
    "GetStoragesByStorageIdTranscodeResponseDefaultType0",
    "GetStoragesByStorageIdTranscodeResponseDefaultType1",
    "GetStoragesByStorageIdTranscodeResponseDefaultType1Errors",
    "GetTranscodeByObjectTypeByObjectIdResponseDefaultType0",
    "GetTranscodeByObjectTypeByObjectIdResponseDefaultType1",
    "GetTranscodeByObjectTypeByObjectIdResponseDefaultType1Errors",
    "GetTranscodeByObjectTypeByObjectIdVersionsByVersionIdResponseDefaultType0",
    "GetTranscodeByObjectTypeByObjectIdVersionsByVersionIdResponseDefaultType1",
    "GetTranscodeByObjectTypeByObjectIdVersionsByVersionIdResponseDefaultType1Errors",
    "GetTranscodeByTranscodeJobIdResponseDefaultType0",
    "GetTranscodeByTranscodeJobIdResponseDefaultType1",
    "GetTranscodeByTranscodeJobIdResponseDefaultType1Errors",
    "GetTranscodeQueueResponseDefaultType0",
    "GetTranscodeQueueResponseDefaultType1",
    "GetTranscodeQueueResponseDefaultType1Errors",
    "GetTranscodeQueueSystemResponseDefaultType0",
    "GetTranscodeQueueSystemResponseDefaultType1",
    "GetTranscodeQueueSystemResponseDefaultType1Errors",
    "InputSchema",
    "JobBaseSchema",
    "JobSchema",
    "JobSchemaAnalysisData",
    "JobsPrioritySchema",
    "JobsStateSchema",
    "JobsStateSchemaAction",
    "JobStep",
    "JobStepSchema",
    "ListObjectsSchema",
    "LLMMetadataJobSchema",
    "LLMMetadataJobSchemaAnalysisData",
    "LocalStorageFileTranscodeJobSchema",
    "LocalStorageFileTranscodeJobsSchema",
    "LocalTranscodeInputSchema",
    "LocalTranscodeJobSchema",
    "LocalTranscodeJobSchemaAnalysisData",
    "MetadataFillingProposalByAssetQueryParamsSchema",
    "MetadataFillingProposalSchema",
    "MetadataFillingProposalSchemaReviewStatus",
    "MetadataFillingResponseSchema",
    "MetadataFillingResponseSchemaMetadataValues",
    "MetadataFillingSchema",
    "OutputEndpoint",
    "OutputEndpointHeaders",
    "OutputEndpointSchema",
    "OutputEndpointSchemaHeaders",
    "PatchEdgeTranscodeWorkersByWorkerIdResponseDefaultType0",
    "PatchEdgeTranscodeWorkersByWorkerIdResponseDefaultType1",
    "PatchEdgeTranscodeWorkersByWorkerIdResponseDefaultType1Errors",
    "PostAnalyzeAssetsByAssetIdProfilesByProfileIdResponseDefaultType0",
    "PostAnalyzeAssetsByAssetIdProfilesByProfileIdResponseDefaultType1",
    "PostAnalyzeAssetsByAssetIdProfilesByProfileIdResponseDefaultType1Errors",
    "PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefaultType0",
    "PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefaultType1",
    "PostAnalyzeAssetsByAssetIdProfilesDefaultByMediaTypeResponseDefaultType1Errors",
    "PostAnalyzeAssetsByAssetIdProfilesDefaultResponseDefaultType0",
    "PostAnalyzeAssetsByAssetIdProfilesDefaultResponseDefaultType1",
    "PostAnalyzeAssetsByAssetIdProfilesDefaultResponseDefaultType1Errors",
    "PostAnalyzeAssetsByAssetIdResponseDefaultType0",
    "PostAnalyzeAssetsByAssetIdResponseDefaultType1",
    "PostAnalyzeAssetsByAssetIdResponseDefaultType1Errors",
    "PostAnalyzeBulkResponseDefaultType0",
    "PostAnalyzeBulkResponseDefaultType1",
    "PostAnalyzeBulkResponseDefaultType1Errors",
    "PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0",
    "PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1",
    "PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1Errors",
    "PostEdgeTranscodeWorkersResponseDefaultType0",
    "PostEdgeTranscodeWorkersResponseDefaultType1",
    "PostEdgeTranscodeWorkersResponseDefaultType1Errors",
    "PostKeyframesCollectionsByCollectionIdResponseDefaultType0",
    "PostKeyframesCollectionsByCollectionIdResponseDefaultType1",
    "PostKeyframesCollectionsByCollectionIdResponseDefaultType1Errors",
    "PostKeyframesPlaylistsByPlaylistIdResponseDefaultType0",
    "PostKeyframesPlaylistsByPlaylistIdResponseDefaultType1",
    "PostKeyframesPlaylistsByPlaylistIdResponseDefaultType1Errors",
    "PostMetadataFillingAssetsByAssetIdVersionsByVersionIdResponseDefaultType0",
    "PostMetadataFillingAssetsByAssetIdVersionsByVersionIdResponseDefaultType1",
    "PostMetadataFillingAssetsByAssetIdVersionsByVersionIdResponseDefaultType1Errors",
    "PostMetadataFillingBulkResponseDefaultType0",
    "PostMetadataFillingBulkResponseDefaultType1",
    "PostMetadataFillingBulkResponseDefaultType1Errors",
    "PostMetadataFillingProposalsByJobIdAcceptResponseDefaultType0",
    "PostMetadataFillingProposalsByJobIdAcceptResponseDefaultType1",
    "PostMetadataFillingProposalsByJobIdAcceptResponseDefaultType1Errors",
    "PostMetadataFillingProposalsByJobIdDiscardResponseDefaultType0",
    "PostMetadataFillingProposalsByJobIdDiscardResponseDefaultType1",
    "PostMetadataFillingProposalsByJobIdDiscardResponseDefaultType1Errors",
    "PostMetadataFillingProposalsByJobIdRegenerateResponseDefaultType0",
    "PostMetadataFillingProposalsByJobIdRegenerateResponseDefaultType1",
    "PostMetadataFillingProposalsByJobIdRegenerateResponseDefaultType1Errors",
    "PostTranscodeByTranscodeJobIdPositionByPositionResponseDefaultType0",
    "PostTranscodeByTranscodeJobIdPositionByPositionResponseDefaultType1",
    "PostTranscodeByTranscodeJobIdPositionByPositionResponseDefaultType1Errors",
    "PostTranscodeResponseDefaultType0",
    "PostTranscodeResponseDefaultType1",
    "PostTranscodeResponseDefaultType1Errors",
    "PostTranscribeAssetsByAssetIdProfilesDefaultResponseDefaultType0",
    "PostTranscribeAssetsByAssetIdProfilesDefaultResponseDefaultType1",
    "PostTranscribeAssetsByAssetIdProfilesDefaultResponseDefaultType1Errors",
    "PostTranscribeBulkResponseDefaultType0",
    "PostTranscribeBulkResponseDefaultType1",
    "PostTranscribeBulkResponseDefaultType1Errors",
    "PutEdgeTranscodeWorkersByWorkerIdResponseDefaultType0",
    "PutEdgeTranscodeWorkersByWorkerIdResponseDefaultType1",
    "PutEdgeTranscodeWorkersByWorkerIdResponseDefaultType1Errors",
    "PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0",
    "PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1",
    "PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1Errors",
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
    "TranscodeQueueSchemaFacets",
    "Transcoders",
    "TranscodersSchema",
    "TranscodersSchemaSettings",
    "TranscodersSettings",
    "TranscodeValidateMediaInfoSchema",
    "TranscribeSchema",
    "WildmokaPipelineTranscode",
    "WildmokaPipelineTranscodeGraph",
    "WildmokaPipelineTranscodeParameters",
    "WildmokaProtectTranscode",
    "WildmokaProtectTranscodeCallbackHeaders",
    "WildmokaProtectTranscodeCreateFileCallbackPayload",
)
