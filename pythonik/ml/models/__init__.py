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
from .delete_face_recognition_assets_by_asset_id_persons_bulk_response_default import (
    DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault,
)
from .delete_face_recognition_persons_bulk_delete_response_default import (
    DeleteFaceRecognitionPersonsBulkDeleteResponseDefault,
)
from .delete_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_response_default import (
    DeleteFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdResponseDefault,
)
from .delete_face_recognition_persons_by_person_id_bulk_response_default import (
    DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefault,
)
from .delete_face_recognition_persons_by_person_id_response_default import (
    DeleteFaceRecognitionPersonsByPersonIdResponseDefault,
)
from .delete_person import DeletePerson
from .delete_person_by_version import DeletePersonByVersion
from .delete_person_by_version_schema import DeletePersonByVersionSchema
from .delete_person_schema import DeletePersonSchema
from .embedding_base_schema import EmbeddingBaseSchema
from .embedding_base_schema_type import EmbeddingBaseSchemaType
from .embedding_by_face_schema import EmbeddingByFaceSchema
from .embedding_by_face_schema_type import EmbeddingByFaceSchemaType
from .embedding_by_person_schema import EmbeddingByPersonSchema
from .embedding_by_person_schema_type import EmbeddingByPersonSchemaType
from .embedding_by_status_schema import EmbeddingByStatusSchema
from .embedding_by_status_schema_status import EmbeddingByStatusSchemaStatus
from .embedding_by_status_schema_type import EmbeddingByStatusSchemaType
from .embedding_schema import EmbeddingSchema
from .embedding_schema_status import EmbeddingSchemaStatus
from .embedding_schema_type import EmbeddingSchemaType
from .face import Face
from .face_base_schema import FaceBaseSchema
from .face_base_schema_status import FaceBaseSchemaStatus
from .face_by_asset_and_version_schema import FaceByAssetAndVersionSchema
from .face_by_asset_and_version_schema_status import FaceByAssetAndVersionSchemaStatus
from .face_by_person_schema import FaceByPersonSchema
from .face_by_person_schema_status import FaceByPersonSchemaStatus
from .face_landmark_schema import FaceLandmarkSchema
from .face_list_schema import FaceListSchema
from .face_schema import FaceSchema
from .face_schema_status import FaceSchemaStatus
from .face_status import FaceStatus
from .get_face_recognition_assets_by_asset_id_versions_by_version_id_persons_response_default import (
    GetFaceRecognitionAssetsByAssetIdVersionsByVersionIdPersonsResponseDefault,
)
from .get_face_recognition_persons_by_person_id_faces_by_face_id_image_url_response_default import (
    GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefault,
)
from .get_face_recognition_persons_by_person_id_response_default import (
    GetFaceRecognitionPersonsByPersonIdResponseDefault,
)
from .get_face_recognition_persons_by_person_id_versions_response_default import (
    GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault,
)
from .get_face_recognition_persons_response_default import (
    GetFaceRecognitionPersonsResponseDefault,
)
from .jobs_priority_schema import JobsPrioritySchema
from .jobs_state_schema import JobsStateSchema
from .jobs_state_schema_action import JobsStateSchemaAction
from .list_objects_schema import ListObjectsSchema
from .ml_detection_queue_record_schema import MLDetectionQueueRecordSchema
from .patch_face_recognition_persons_by_person_id_response_default import (
    PatchFaceRecognitionPersonsByPersonIdResponseDefault,
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
from .post_face_recognition_bulk_extract_response_default import (
    PostFaceRecognitionBulkExtractResponseDefault,
)
from .post_face_recognition_embeddings_by_embedding_id_reindex_response_default import (
    PostFaceRecognitionEmbeddingsByEmbeddingIdReindexResponseDefault,
)
from .post_face_recognition_embeddings_reindex_response_default import (
    PostFaceRecognitionEmbeddingsReindexResponseDefault,
)
from .post_face_recognition_extract_assets_by_asset_id_versions_by_version_id_response_default import (
    PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault,
)
from .post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_change_person_response_default import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdChangePersonResponseDefault,
)
from .post_face_recognition_persons_by_person_id_assets_by_asset_id_versions_by_version_id_confirm_person_response_default import (
    PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefault,
)
from .post_face_recognition_persons_by_person_id_confirm_person_response_default import (
    PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault,
)
from .post_face_recognition_persons_by_person_id_merge_by_new_person_id_response_default import (
    PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault,
)
from .post_face_recognition_persons_by_person_id_reindex_response_default import (
    PostFaceRecognitionPersonsByPersonIdReindexResponseDefault,
)
from .post_face_recognition_persons_by_person_id_update_and_confirm_response_default import (
    PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault,
)
from .post_face_recognition_persons_reindex_response_default import (
    PostFaceRecognitionPersonsReindexResponseDefault,
)
from .put_face_recognition_change_person_jobs_state_response_default import (
    PutFaceRecognitionChangePersonJobsStateResponseDefault,
)
from .put_face_recognition_jobs_priority_response_default import (
    PutFaceRecognitionJobsPriorityResponseDefault,
)
from .put_face_recognition_jobs_state_response_default import (
    PutFaceRecognitionJobsStateResponseDefault,
)
from .put_face_recognition_persons_by_person_id_response_default import (
    PutFaceRecognitionPersonsByPersonIdResponseDefault,
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
    "DeleteFaceRecognitionAssetsByAssetIdPersonsBulkResponseDefault",
    "DeleteFaceRecognitionPersonsBulkDeleteResponseDefault",
    "DeleteFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdResponseDefault",
    "DeleteFaceRecognitionPersonsByPersonIdBulkResponseDefault",
    "DeleteFaceRecognitionPersonsByPersonIdResponseDefault",
    "DeletePerson",
    "DeletePersonByVersion",
    "DeletePersonByVersionSchema",
    "DeletePersonSchema",
    "EmbeddingBaseSchema",
    "EmbeddingBaseSchemaType",
    "EmbeddingByFaceSchema",
    "EmbeddingByFaceSchemaType",
    "EmbeddingByPersonSchema",
    "EmbeddingByPersonSchemaType",
    "EmbeddingByStatusSchema",
    "EmbeddingByStatusSchemaStatus",
    "EmbeddingByStatusSchemaType",
    "EmbeddingSchema",
    "EmbeddingSchemaStatus",
    "EmbeddingSchemaType",
    "Face",
    "FaceBaseSchema",
    "FaceBaseSchemaStatus",
    "FaceByAssetAndVersionSchema",
    "FaceByAssetAndVersionSchemaStatus",
    "FaceByPersonSchema",
    "FaceByPersonSchemaStatus",
    "FaceLandmarkSchema",
    "FaceListSchema",
    "FaceSchema",
    "FaceSchemaStatus",
    "FaceStatus",
    "GetFaceRecognitionAssetsByAssetIdVersionsByVersionIdPersonsResponseDefault",
    "GetFaceRecognitionPersonsByPersonIdFacesByFaceIdImageUrlResponseDefault",
    "GetFaceRecognitionPersonsByPersonIdResponseDefault",
    "GetFaceRecognitionPersonsByPersonIdVersionsResponseDefault",
    "GetFaceRecognitionPersonsResponseDefault",
    "JobsPrioritySchema",
    "JobsStateSchema",
    "JobsStateSchemaAction",
    "ListObjectsSchema",
    "MLDetectionQueueRecordSchema",
    "PatchFaceRecognitionPersonsByPersonIdResponseDefault",
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
    "PostFaceRecognitionBulkExtractResponseDefault",
    "PostFaceRecognitionEmbeddingsByEmbeddingIdReindexResponseDefault",
    "PostFaceRecognitionEmbeddingsReindexResponseDefault",
    "PostFaceRecognitionExtractAssetsByAssetIdVersionsByVersionIdResponseDefault",
    "PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdChangePersonResponseDefault",
    "PostFaceRecognitionPersonsByPersonIdAssetsByAssetIdVersionsByVersionIdConfirmPersonResponseDefault",
    "PostFaceRecognitionPersonsByPersonIdConfirmPersonResponseDefault",
    "PostFaceRecognitionPersonsByPersonIdMergeByNewPersonIdResponseDefault",
    "PostFaceRecognitionPersonsByPersonIdReindexResponseDefault",
    "PostFaceRecognitionPersonsByPersonIdUpdateAndConfirmResponseDefault",
    "PostFaceRecognitionPersonsReindexResponseDefault",
    "PutFaceRecognitionChangePersonJobsStateResponseDefault",
    "PutFaceRecognitionJobsPriorityResponseDefault",
    "PutFaceRecognitionJobsStateResponseDefault",
    "PutFaceRecognitionPersonsByPersonIdResponseDefault",
    "ReindexAllEmbeddingsSchema",
    "ReindexEmbeddingSchema",
    "ReindexPersonSchema",
    "ReindexQueueRecordSchema",
    "UpdateConfirmPersonSchema",
    "UpdatePersonSchema",
    "URLSchema",
    "VersionsSchema",
)
