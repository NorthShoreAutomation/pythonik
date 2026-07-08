"""Contains all the data models used in inputs/outputs"""

from .asset_version_schema import AssetVersionSchema
from .base_query_params_schema import BaseQueryParamsSchema
from .bulk_confirm_person_schema import BulkConfirmPersonSchema
from .bulk_delete_persons_by_ids_schema import BulkDeletePersonsByIdsSchema
from .bulk_delete_persons_by_versions_schema import BulkDeletePersonsByVersionsSchema
from .bulk_delete_persons_schema import BulkDeletePersonsSchema
from .bulk_face_extract_schema import BulkFaceExtractSchema
from .bulk_face_extract_schema_object_type import BulkFaceExtractSchemaObjectType
from .bulk_person_by_asset_and_version import BulkPersonByAssetAndVersion
from .bulk_person_by_asset_and_version_list_schema import (
    BulkPersonByAssetAndVersionListSchema,
)
from .bulk_person_by_asset_and_version_schema import BulkPersonByAssetAndVersionSchema
from .bulk_reindex_persons_schema import BulkReindexPersonsSchema
from .change_person_instance_schema import ChangePersonInstanceSchema
from .check_persons_status_schema import CheckPersonsStatusSchema
from .copy_persons_schema import CopyPersonsSchema
from .create_person_schema import CreatePersonSchema
from .delete_face_recognition_assets_by_asset_id_persons_bulk_response_default_type_0 import (
    DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefaultType0,
)
from .delete_face_recognition_assets_by_asset_id_persons_bulk_response_default_type_1 import (
    DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefaultType1,
)
from .delete_face_recognition_assets_by_asset_id_persons_bulk_response_default_type_1_errors import (
    DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefaultType1Errors,
)
from .delete_face_recognition_persons_bulk_delete_response_default_type_0 import (
    DeleteFaceRecognitionPersonsBulkDeleteResponseDefaultType0,
)
from .delete_face_recognition_persons_bulk_delete_response_default_type_1 import (
    DeleteFaceRecognitionPersonsBulkDeleteResponseDefaultType1,
)
from .delete_face_recognition_persons_bulk_delete_response_default_type_1_errors import (
    DeleteFaceRecognitionPersonsBulkDeleteResponseDefaultType1Errors,
)
from .delete_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_response_default_type_0 import (
    DeleteFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdResponseDefaultType0,
)
from .delete_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_response_default_type_1 import (
    DeleteFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdResponseDefaultType1,
)
from .delete_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_response_default_type_1_errors import (
    DeleteFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdResponseDefaultType1Errors,
)
from .delete_face_recognition_persons_by_person_id_bulk_response_default_type_0 import (
    DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0,
)
from .delete_face_recognition_persons_by_person_id_bulk_response_default_type_1 import (
    DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1,
)
from .delete_face_recognition_persons_by_person_id_bulk_response_default_type_1_errors import (
    DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1Errors,
)
from .delete_face_recognition_persons_by_person_id_response_default_type_0 import (
    DeleteFaceRecognitionPersonsByPersonIdResponseDefaultType0,
)
from .delete_face_recognition_persons_by_person_id_response_default_type_1 import (
    DeleteFaceRecognitionPersonsByPersonIdResponseDefaultType1,
)
from .delete_face_recognition_persons_by_person_id_response_default_type_1_errors import (
    DeleteFaceRecognitionPersonsByPersonIdResponseDefaultType1Errors,
)
from .delete_person import DeletePerson
from .delete_person_by_version import DeletePersonByVersion
from .delete_person_by_version_schema import DeletePersonByVersionSchema
from .delete_person_schema import DeletePersonSchema
from .embedding_base_schema import EmbeddingBaseSchema
from .embedding_base_schema_type_type_1 import EmbeddingBaseSchemaTypeType1
from .embedding_by_face_schema import EmbeddingByFaceSchema
from .embedding_by_face_schema_type_type_1 import EmbeddingByFaceSchemaTypeType1
from .embedding_by_person_schema import EmbeddingByPersonSchema
from .embedding_by_person_schema_type_type_1 import EmbeddingByPersonSchemaTypeType1
from .embedding_by_status_schema import EmbeddingByStatusSchema
from .embedding_by_status_schema_status_type_1 import EmbeddingByStatusSchemaStatusType1
from .embedding_by_status_schema_type_type_1 import EmbeddingByStatusSchemaTypeType1
from .embedding_schema import EmbeddingSchema
from .embedding_schema_status_type_1 import EmbeddingSchemaStatusType1
from .embedding_schema_type_type_1 import EmbeddingSchemaTypeType1
from .face import Face
from .face_base_schema import FaceBaseSchema
from .face_base_schema_status_type_1 import FaceBaseSchemaStatusType1
from .face_by_asset_and_version_schema import FaceByAssetAndVersionSchema
from .face_by_asset_and_version_schema_status_type_1 import (
    FaceByAssetAndVersionSchemaStatusType1,
)
from .face_by_person_schema import FaceByPersonSchema
from .face_by_person_schema_status_type_1 import FaceByPersonSchemaStatusType1
from .face_landmark_schema import FaceLandmarkSchema
from .face_list_schema import FaceListSchema
from .face_schema import FaceSchema
from .face_schema_status_type_1 import FaceSchemaStatusType1
from .face_status_type_1 import FaceStatusType1
from .get_face_recognition_assets_by_asset_id_versions_by_version_id_persons_response_default_type_0 import (
    GetFaceRecognitionAssetsByAssetIdVersionsByVersionIdPersonsResponseDefaultType0,
)
from .get_face_recognition_assets_by_asset_id_versions_by_version_id_persons_response_default_type_1 import (
    GetFaceRecognitionAssetsByAssetIdVersionsByVersionIdPersonsResponseDefaultType1,
)
from .get_face_recognition_assets_by_asset_id_versions_by_version_id_persons_response_default_type_1_errors import (
    GetFaceRecognitionAssetsByAssetIdVersionsByVersionIdPersonsResponseDefaultType1Errors,
)
from .get_face_recognition_persons_by_person_id_faces_by_face_id_image_url_response_default_type_0 import (
    GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0,
)
from .get_face_recognition_persons_by_person_id_faces_by_face_id_image_url_response_default_type_1 import (
    GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1,
)
from .get_face_recognition_persons_by_person_id_faces_by_face_id_image_url_response_default_type_1_errors import (
    GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1Errors,
)
from .get_face_recognition_persons_by_person_id_response_default_type_0 import (
    GetFaceRecognitionPersonsByPersonIdResponseDefaultType0,
)
from .get_face_recognition_persons_by_person_id_response_default_type_1 import (
    GetFaceRecognitionPersonsByPersonIdResponseDefaultType1,
)
from .get_face_recognition_persons_by_person_id_response_default_type_1_errors import (
    GetFaceRecognitionPersonsByPersonIdResponseDefaultType1Errors,
)
from .get_face_recognition_persons_by_person_id_versions_response_default_type_0 import (
    GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0,
)
from .get_face_recognition_persons_by_person_id_versions_response_default_type_1 import (
    GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1,
)
from .get_face_recognition_persons_by_person_id_versions_response_default_type_1_errors import (
    GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1Errors,
)
from .get_face_recognition_persons_response_default_type_0 import (
    GetFaceRecognitionPersonsResponseDefaultType0,
)
from .get_face_recognition_persons_response_default_type_1 import (
    GetFaceRecognitionPersonsResponseDefaultType1,
)
from .get_face_recognition_persons_response_default_type_1_errors import (
    GetFaceRecognitionPersonsResponseDefaultType1Errors,
)
from .jobs_priority_schema import JobsPrioritySchema
from .jobs_state_schema import JobsStateSchema
from .jobs_state_schema_action import JobsStateSchemaAction
from .list_objects_schema import ListObjectsSchema
from .ml_detection_queue_record_schema import MLDetectionQueueRecordSchema
from .patch_face_recognition_persons_by_person_id_response_default_type_0 import (
    PatchFaceRecognitionPersonsByPersonIdResponseDefaultType0,
)
from .patch_face_recognition_persons_by_person_id_response_default_type_1 import (
    PatchFaceRecognitionPersonsByPersonIdResponseDefaultType1,
)
from .patch_face_recognition_persons_by_person_id_response_default_type_1_errors import (
    PatchFaceRecognitionPersonsByPersonIdResponseDefaultType1Errors,
)
from .person import Person
from .person_assets_versions_list_schema import PersonAssetsVersionsListSchema
from .person_by_asset_and_version import PersonByAssetAndVersion
from .person_by_asset_and_version_in_admin import PersonByAssetAndVersionInAdmin
from .person_by_asset_and_version_in_admin_schema import (
    PersonByAssetAndVersionInAdminSchema,
)
from .person_by_asset_and_version_in_admin_schema_status import (
    PersonByAssetAndVersionInAdminSchemaStatus,
)
from .person_by_asset_and_version_in_admin_status import (
    PersonByAssetAndVersionInAdminStatus,
)
from .person_by_asset_and_version_list_schema import PersonByAssetAndVersionListSchema
from .person_by_asset_and_version_schema import PersonByAssetAndVersionSchema
from .person_by_asset_and_version_schema_status import (
    PersonByAssetAndVersionSchemaStatus,
)
from .person_by_asset_and_version_status import PersonByAssetAndVersionStatus
from .person_instances_query_params_schema import PersonInstancesQueryParamsSchema
from .person_list_schema import PersonListSchema
from .person_list_schema_facets_type_0 import PersonListSchemaFacetsType0
from .person_schema import PersonSchema
from .person_schema_status import PersonSchemaStatus
from .person_status import PersonStatus
from .persons_query_params_schema import PersonsQueryParamsSchema
from .post_face_recognition_bulk_extract_response_default_type_0 import (
    PostFaceRecognitionBulkExtractResponseDefaultType0,
)
from .post_face_recognition_bulk_extract_response_default_type_1 import (
    PostFaceRecognitionBulkExtractResponseDefaultType1,
)
from .post_face_recognition_bulk_extract_response_default_type_1_errors import (
    PostFaceRecognitionBulkExtractResponseDefaultType1Errors,
)
from .post_face_recognition_embeddings_by_embedding_id_reindex_response_default_type_0 import (
    PostFaceRecognitionEmbeddingsByEmbeddingIdReindexResponseDefaultType0,
)
from .post_face_recognition_embeddings_by_embedding_id_reindex_response_default_type_1 import (
    PostFaceRecognitionEmbeddingsByEmbeddingIdReindexResponseDefaultType1,
)
from .post_face_recognition_embeddings_by_embedding_id_reindex_response_default_type_1_errors import (
    PostFaceRecognitionEmbeddingsByEmbeddingIdReindexResponseDefaultType1Errors,
)
from .post_face_recognition_embeddings_reindex_response_default_type_0 import (
    PostFaceRecognitionEmbeddingsReindexResponseDefaultType0,
)
from .post_face_recognition_embeddings_reindex_response_default_type_1 import (
    PostFaceRecognitionEmbeddingsReindexResponseDefaultType1,
)
from .post_face_recognition_embeddings_reindex_response_default_type_1_errors import (
    PostFaceRecognitionEmbeddingsReindexResponseDefaultType1Errors,
)
from .post_face_recognition_extract_assets_by_asset_id_versions_by_version_id_response_default_type_0 import (
    PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefaultType0,
)
from .post_face_recognition_extract_assets_by_asset_id_versions_by_version_id_response_default_type_1 import (
    PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefaultType1,
)
from .post_face_recognition_extract_assets_by_asset_id_versions_by_version_id_response_default_type_1_errors import (
    PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefaultType1Errors,
)
from .post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_change_person_response_default_type_0 import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdChangePersonResponseDefaultType0,
)
from .post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_change_person_response_default_type_1 import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdChangePersonResponseDefaultType1,
)
from .post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_change_person_response_default_type_1_errors import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdChangePersonResponseDefaultType1Errors,
)
from .post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_confirm_person_response_default_type_0 import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0,
)
from .post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_confirm_person_response_default_type_1 import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1,
)
from .post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_confirm_person_response_default_type_1_errors import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1Errors,
)
from .post_face_recognition_persons_by_person_id_confirm_person_response_default_type_0 import (
    PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefaultType0,
)
from .post_face_recognition_persons_by_person_id_confirm_person_response_default_type_1 import (
    PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefaultType1,
)
from .post_face_recognition_persons_by_person_id_confirm_person_response_default_type_1_errors import (
    PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefaultType1Errors,
)
from .post_face_recognition_persons_by_person_id_merge_by_new_person_id_response_default_type_0 import (
    PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefaultType0,
)
from .post_face_recognition_persons_by_person_id_merge_by_new_person_id_response_default_type_1 import (
    PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefaultType1,
)
from .post_face_recognition_persons_by_person_id_merge_by_new_person_id_response_default_type_1_errors import (
    PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefaultType1Errors,
)
from .post_face_recognition_persons_by_person_id_reindex_response_default_type_0 import (
    PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0,
)
from .post_face_recognition_persons_by_person_id_reindex_response_default_type_1 import (
    PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1,
)
from .post_face_recognition_persons_by_person_id_reindex_response_default_type_1_errors import (
    PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1Errors,
)
from .post_face_recognition_persons_by_person_id_update_and_confirm_response_default_type_0 import (
    PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefaultType0,
)
from .post_face_recognition_persons_by_person_id_update_and_confirm_response_default_type_1 import (
    PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefaultType1,
)
from .post_face_recognition_persons_by_person_id_update_and_confirm_response_default_type_1_errors import (
    PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefaultType1Errors,
)
from .post_face_recognition_persons_reindex_response_default_type_0 import (
    PostFaceRecognitionPersonsReindexResponseDefaultType0,
)
from .post_face_recognition_persons_reindex_response_default_type_1 import (
    PostFaceRecognitionPersonsReindexResponseDefaultType1,
)
from .post_face_recognition_persons_reindex_response_default_type_1_errors import (
    PostFaceRecognitionPersonsReindexResponseDefaultType1Errors,
)
from .put_face_recognition_change_person_jobs_state_response_default_type_0 import (
    PutFaceRecognitionChangePersonJobsStateResponseDefaultType0,
)
from .put_face_recognition_change_person_jobs_state_response_default_type_1 import (
    PutFaceRecognitionChangePersonJobsStateResponseDefaultType1,
)
from .put_face_recognition_change_person_jobs_state_response_default_type_1_errors import (
    PutFaceRecognitionChangePersonJobsStateResponseDefaultType1Errors,
)
from .put_face_recognition_jobs_priority_response_default_type_0 import (
    PutFaceRecognitionJobsPriorityResponseDefaultType0,
)
from .put_face_recognition_jobs_priority_response_default_type_1 import (
    PutFaceRecognitionJobsPriorityResponseDefaultType1,
)
from .put_face_recognition_jobs_priority_response_default_type_1_errors import (
    PutFaceRecognitionJobsPriorityResponseDefaultType1Errors,
)
from .put_face_recognition_jobs_state_response_default_type_0 import (
    PutFaceRecognitionJobsStateResponseDefaultType0,
)
from .put_face_recognition_jobs_state_response_default_type_1 import (
    PutFaceRecognitionJobsStateResponseDefaultType1,
)
from .put_face_recognition_jobs_state_response_default_type_1_errors import (
    PutFaceRecognitionJobsStateResponseDefaultType1Errors,
)
from .put_face_recognition_persons_by_person_id_response_default_type_0 import (
    PutFaceRecognitionPersonsByPersonIdResponseDefaultType0,
)
from .put_face_recognition_persons_by_person_id_response_default_type_1 import (
    PutFaceRecognitionPersonsByPersonIdResponseDefaultType1,
)
from .put_face_recognition_persons_by_person_id_response_default_type_1_errors import (
    PutFaceRecognitionPersonsByPersonIdResponseDefaultType1Errors,
)
from .reindex_all_embeddings_schema import ReindexAllEmbeddingsSchema
from .reindex_embedding_schema import ReindexEmbeddingSchema
from .reindex_person_schema import ReindexPersonSchema
from .reindex_queue_record_schema import ReindexQueueRecordSchema
from .update_confirm_person_schema import UpdateConfirmPersonSchema
from .update_person_schema import UpdatePersonSchema
from .url_schema import URLSchema
from .versions_schema import VersionsSchema

__all__ = (
    "AssetVersionSchema",
    "BaseQueryParamsSchema",
    "BulkConfirmPersonSchema",
    "BulkDeletePersonsByIdsSchema",
    "BulkDeletePersonsByVersionsSchema",
    "BulkDeletePersonsSchema",
    "BulkFaceExtractSchema",
    "BulkFaceExtractSchemaObjectType",
    "BulkPersonByAssetAndVersion",
    "BulkPersonByAssetAndVersionListSchema",
    "BulkPersonByAssetAndVersionSchema",
    "BulkReindexPersonsSchema",
    "ChangePersonInstanceSchema",
    "CheckPersonsStatusSchema",
    "CopyPersonsSchema",
    "CreatePersonSchema",
    "DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefaultType0",
    "DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefaultType1",
    "DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefaultType1Errors",
    "DeleteFaceRecognitionPersonsBulkDeleteResponseDefaultType0",
    "DeleteFaceRecognitionPersonsBulkDeleteResponseDefaultType1",
    "DeleteFaceRecognitionPersonsBulkDeleteResponseDefaultType1Errors",
    "DeleteFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdResponseDefaultType0",
    "DeleteFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdResponseDefaultType1",
    "DeleteFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdResponseDefaultType1Errors",
    "DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType0",
    "DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1",
    "DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefaultType1Errors",
    "DeleteFaceRecognitionPersonsByPersonIdResponseDefaultType0",
    "DeleteFaceRecognitionPersonsByPersonIdResponseDefaultType1",
    "DeleteFaceRecognitionPersonsByPersonIdResponseDefaultType1Errors",
    "DeletePerson",
    "DeletePersonByVersion",
    "DeletePersonByVersionSchema",
    "DeletePersonSchema",
    "EmbeddingBaseSchema",
    "EmbeddingBaseSchemaTypeType1",
    "EmbeddingByFaceSchema",
    "EmbeddingByFaceSchemaTypeType1",
    "EmbeddingByPersonSchema",
    "EmbeddingByPersonSchemaTypeType1",
    "EmbeddingByStatusSchema",
    "EmbeddingByStatusSchemaStatusType1",
    "EmbeddingByStatusSchemaTypeType1",
    "EmbeddingSchema",
    "EmbeddingSchemaStatusType1",
    "EmbeddingSchemaTypeType1",
    "Face",
    "FaceBaseSchema",
    "FaceBaseSchemaStatusType1",
    "FaceByAssetAndVersionSchema",
    "FaceByAssetAndVersionSchemaStatusType1",
    "FaceByPersonSchema",
    "FaceByPersonSchemaStatusType1",
    "FaceLandmarkSchema",
    "FaceListSchema",
    "FaceSchema",
    "FaceSchemaStatusType1",
    "FaceStatusType1",
    "GetFaceRecognitionAssetsByAssetIdVersionsByVersionIdPersonsResponseDefaultType0",
    "GetFaceRecognitionAssetsByAssetIdVersionsByVersionIdPersonsResponseDefaultType1",
    "GetFaceRecognitionAssetsByAssetIdVersionsByVersionIdPersonsResponseDefaultType1Errors",
    "GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType0",
    "GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1",
    "GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefaultType1Errors",
    "GetFaceRecognitionPersonsByPersonIdResponseDefaultType0",
    "GetFaceRecognitionPersonsByPersonIdResponseDefaultType1",
    "GetFaceRecognitionPersonsByPersonIdResponseDefaultType1Errors",
    "GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType0",
    "GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1",
    "GetFaceRecognitionPersonsByPersonIdVersionsResponseDefaultType1Errors",
    "GetFaceRecognitionPersonsResponseDefaultType0",
    "GetFaceRecognitionPersonsResponseDefaultType1",
    "GetFaceRecognitionPersonsResponseDefaultType1Errors",
    "JobsPrioritySchema",
    "JobsStateSchema",
    "JobsStateSchemaAction",
    "ListObjectsSchema",
    "MLDetectionQueueRecordSchema",
    "PatchFaceRecognitionPersonsByPersonIdResponseDefaultType0",
    "PatchFaceRecognitionPersonsByPersonIdResponseDefaultType1",
    "PatchFaceRecognitionPersonsByPersonIdResponseDefaultType1Errors",
    "Person",
    "PersonAssetsVersionsListSchema",
    "PersonByAssetAndVersion",
    "PersonByAssetAndVersionInAdmin",
    "PersonByAssetAndVersionInAdminSchema",
    "PersonByAssetAndVersionInAdminSchemaStatus",
    "PersonByAssetAndVersionInAdminStatus",
    "PersonByAssetAndVersionListSchema",
    "PersonByAssetAndVersionSchema",
    "PersonByAssetAndVersionSchemaStatus",
    "PersonByAssetAndVersionStatus",
    "PersonInstancesQueryParamsSchema",
    "PersonListSchema",
    "PersonListSchemaFacetsType0",
    "PersonSchema",
    "PersonSchemaStatus",
    "PersonsQueryParamsSchema",
    "PersonStatus",
    "PostFaceRecognitionBulkExtractResponseDefaultType0",
    "PostFaceRecognitionBulkExtractResponseDefaultType1",
    "PostFaceRecognitionBulkExtractResponseDefaultType1Errors",
    "PostFaceRecognitionEmbeddingsByEmbeddingIdReindexResponseDefaultType0",
    "PostFaceRecognitionEmbeddingsByEmbeddingIdReindexResponseDefaultType1",
    "PostFaceRecognitionEmbeddingsByEmbeddingIdReindexResponseDefaultType1Errors",
    "PostFaceRecognitionEmbeddingsReindexResponseDefaultType0",
    "PostFaceRecognitionEmbeddingsReindexResponseDefaultType1",
    "PostFaceRecognitionEmbeddingsReindexResponseDefaultType1Errors",
    "PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefaultType0",
    "PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefaultType1",
    "PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefaultType1Errors",
    "PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdChangePersonResponseDefaultType0",
    "PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdChangePersonResponseDefaultType1",
    "PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdChangePersonResponseDefaultType1Errors",
    "PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType0",
    "PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1",
    "PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefaultType1Errors",
    "PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefaultType0",
    "PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefaultType1",
    "PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefaultType1Errors",
    "PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefaultType0",
    "PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefaultType1",
    "PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefaultType1Errors",
    "PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType0",
    "PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1",
    "PostFaceRecognitionPersonsByPersonIdReindexResponseDefaultType1Errors",
    "PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefaultType0",
    "PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefaultType1",
    "PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefaultType1Errors",
    "PostFaceRecognitionPersonsReindexResponseDefaultType0",
    "PostFaceRecognitionPersonsReindexResponseDefaultType1",
    "PostFaceRecognitionPersonsReindexResponseDefaultType1Errors",
    "PutFaceRecognitionChangePersonJobsStateResponseDefaultType0",
    "PutFaceRecognitionChangePersonJobsStateResponseDefaultType1",
    "PutFaceRecognitionChangePersonJobsStateResponseDefaultType1Errors",
    "PutFaceRecognitionJobsPriorityResponseDefaultType0",
    "PutFaceRecognitionJobsPriorityResponseDefaultType1",
    "PutFaceRecognitionJobsPriorityResponseDefaultType1Errors",
    "PutFaceRecognitionJobsStateResponseDefaultType0",
    "PutFaceRecognitionJobsStateResponseDefaultType1",
    "PutFaceRecognitionJobsStateResponseDefaultType1Errors",
    "PutFaceRecognitionPersonsByPersonIdResponseDefaultType0",
    "PutFaceRecognitionPersonsByPersonIdResponseDefaultType1",
    "PutFaceRecognitionPersonsByPersonIdResponseDefaultType1Errors",
    "ReindexAllEmbeddingsSchema",
    "ReindexEmbeddingSchema",
    "ReindexPersonSchema",
    "ReindexQueueRecordSchema",
    "UpdateConfirmPersonSchema",
    "UpdatePersonSchema",
    "URLSchema",
    "VersionsSchema",
)
