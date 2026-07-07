"""Contains all the data models used in inputs/outputs"""

from .acl_update_schema import ACLUpdateSchema
from .acl_update_schema_mode import ACLUpdateSchemaMode
from .acl_update_schema_permissions_item import ACLUpdateSchemaPermissionsItem
from .action_schema_base import ActionSchemaBase
from .action_schema_base_parameters import ActionSchemaBaseParameters
from .add_to_collection_action_parameters import AddToCollectionActionParameters
from .add_to_collection_action_schema import AddToCollectionActionSchema
from .add_to_collection_action_schema_type import AddToCollectionActionSchemaType
from .analyze_action_parameters import AnalyzeActionParameters
from .analyze_action_parameters_force_type import AnalyzeActionParametersForceType
from .analyze_action_schema import AnalyzeActionSchema
from .analyze_action_schema_type import AnalyzeActionSchemaType
from .archive_action_parameters import ArchiveActionParameters
from .archive_action_schema import ArchiveActionSchema
from .archive_action_schema_type import ArchiveActionSchemaType
from .asset_archived_trigger_parameters import AssetArchivedTriggerParameters
from .asset_archived_trigger_schema import AssetArchivedTriggerSchema
from .asset_archived_trigger_schema_type import AssetArchivedTriggerSchemaType
from .asset_online_trigger_parameters import AssetOnlineTriggerParameters
from .asset_online_trigger_schema import AssetOnlineTriggerSchema
from .asset_online_trigger_schema_type import AssetOnlineTriggerSchemaType
from .asset_restored_trigger_parameters import AssetRestoredTriggerParameters
from .asset_restored_trigger_schema import AssetRestoredTriggerSchema
from .asset_restored_trigger_schema_type import AssetRestoredTriggerSchemaType
from .asset_shared_trigger_parameters import AssetSharedTriggerParameters
from .asset_shared_trigger_schema import AssetSharedTriggerSchema
from .asset_shared_trigger_schema_type import AssetSharedTriggerSchemaType
from .asset_transferred_to_storage_parameters import AssetTransferredToStorageParameters
from .asset_transferred_to_storage_trigger_schema import (
    AssetTransferredToStorageTriggerSchema,
)
from .asset_transferred_to_storage_trigger_schema_type import (
    AssetTransferredToStorageTriggerSchemaType,
)
from .automation_history_schema import AutomationHistorySchema
from .automation_history_schema_status import AutomationHistorySchemaStatus
from .automation_internal_schema import AutomationInternalSchema
from .automation_internal_schema_status import AutomationInternalSchemaStatus
from .automation_run_estimate_schema import AutomationRunEstimateSchema
from .automation_run_estimate_schema_facets import AutomationRunEstimateSchemaFacets
from .automation_schema import AutomationSchema
from .automation_schema_status import AutomationSchemaStatus
from .automation_stats_object_schema import AutomationStatsObjectSchema
from .automation_stats_object_schema_type import AutomationStatsObjectSchemaType
from .automation_stats_schema import AutomationStatsSchema
from .automations_internal_schema import AutomationsInternalSchema
from .automations_schema import AutomationsSchema
from .bucket_schema import BucketSchema
from .condition import Condition
from .condition_schema import ConditionSchema
from .create_publication_job_action import CreatePublicationJobAction
from .create_publication_job_action_schema import CreatePublicationJobActionSchema
from .create_publication_job_action_schema_type import (
    CreatePublicationJobActionSchemaType,
)
from .create_publication_job_action_type import CreatePublicationJobActionType
from .create_publication_job_parameters import CreatePublicationJobParameters
from .create_publication_job_parameters_metadata_overrides import (
    CreatePublicationJobParametersMetadataOverrides,
)
from .create_publication_job_thumbnail_keyframe import (
    CreatePublicationJobThumbnailKeyframe,
)
from .create_publication_job_thumbnail_keyframe_type import (
    CreatePublicationJobThumbnailKeyframeType,
)
from .create_publication_template import CreatePublicationTemplate
from .create_publication_template_data import CreatePublicationTemplateData
from .create_share_action import CreateShareAction
from .create_share_action_parameters import CreateShareActionParameters
from .create_share_action_parameters_schema import CreateShareActionParametersSchema
from .create_share_action_schema import CreateShareActionSchema
from .create_share_action_schema_type import CreateShareActionSchemaType
from .create_share_action_type import CreateShareActionType
from .created_at_transition_trigger import CreatedAtTransitionTrigger
from .created_at_transition_trigger_parameters import (
    CreatedAtTransitionTriggerParameters,
)
from .created_at_transition_trigger_schema import CreatedAtTransitionTriggerSchema
from .created_at_transition_trigger_schema_type import (
    CreatedAtTransitionTriggerSchemaType,
)
from .created_at_transition_trigger_type import CreatedAtTransitionTriggerType
from .delete_action import DeleteAction
from .delete_action_parameters import DeleteActionParameters
from .delete_action_schema import DeleteActionSchema
from .delete_action_schema_parameters import DeleteActionSchemaParameters
from .delete_action_schema_type import DeleteActionSchemaType
from .delete_action_type import DeleteActionType
from .delete_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default_type_0 import (
    DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0,
)
from .delete_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default_type_1 import (
    DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1,
)
from .delete_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default_type_1_errors import (
    DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1Errors,
)
from .delete_automations_by_automation_id_response_default_type_0 import (
    DeleteAutomationsByAutomationIdResponseDefaultType0,
)
from .delete_automations_by_automation_id_response_default_type_1 import (
    DeleteAutomationsByAutomationIdResponseDefaultType1,
)
from .delete_automations_by_automation_id_response_default_type_1_errors import (
    DeleteAutomationsByAutomationIdResponseDefaultType1Errors,
)
from .delete_file_set_action import DeleteFileSetAction
from .delete_file_set_action_parameters import DeleteFileSetActionParameters
from .delete_file_set_action_schema import DeleteFileSetActionSchema
from .delete_file_set_action_schema_type import DeleteFileSetActionSchemaType
from .delete_file_set_action_type import DeleteFileSetActionType
from .export_action import ExportAction
from .export_action_parameters import ExportActionParameters
from .export_action_parameters_metadata_format import (
    ExportActionParametersMetadataFormat,
)
from .export_action_schema import ExportActionSchema
from .export_action_schema_type import ExportActionSchemaType
from .export_action_type import ExportActionType
from .extract_faces_action import ExtractFacesAction
from .extract_faces_action_schema import ExtractFacesActionSchema
from .extract_faces_action_schema_type import ExtractFacesActionSchemaType
from .extract_faces_action_type import ExtractFacesActionType
from .extract_faces_parameters import ExtractFacesParameters
from .facet_schema import FacetSchema
from .get_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default_type_0 import (
    GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0,
)
from .get_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default_type_1 import (
    GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1,
)
from .get_automations_by_automation_id_history_by_object_type_by_object_id_by_version_id_response_default_type_1_errors import (
    GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1Errors,
)
from .get_automations_by_automation_id_response_default_type_0 import (
    GetAutomationsByAutomationIdResponseDefaultType0,
)
from .get_automations_by_automation_id_response_default_type_1 import (
    GetAutomationsByAutomationIdResponseDefaultType1,
)
from .get_automations_by_automation_id_response_default_type_1_errors import (
    GetAutomationsByAutomationIdResponseDefaultType1Errors,
)
from .get_automations_by_automation_id_runs_estimate_response_default_type_0 import (
    GetAutomationsByAutomationIdRunsEstimateResponseDefaultType0,
)
from .get_automations_by_automation_id_runs_estimate_response_default_type_1 import (
    GetAutomationsByAutomationIdRunsEstimateResponseDefaultType1,
)
from .get_automations_by_automation_id_runs_estimate_response_default_type_1_errors import (
    GetAutomationsByAutomationIdRunsEstimateResponseDefaultType1Errors,
)
from .get_automations_response_default_type_0 import GetAutomationsResponseDefaultType0
from .get_automations_response_default_type_1 import GetAutomationsResponseDefaultType1
from .get_automations_response_default_type_1_errors import (
    GetAutomationsResponseDefaultType1Errors,
)
from .list_objects_schema import ListObjectsSchema
from .metadata_field_value_schema import MetadataFieldValueSchema
from .metadata_field_value_schema_field_values_item import (
    MetadataFieldValueSchemaFieldValuesItem,
)
from .metadata_field_value_update_schema import MetadataFieldValueUpdateSchema
from .metadata_field_value_update_schema_field_values_item import (
    MetadataFieldValueUpdateSchemaFieldValuesItem,
)
from .metadata_field_value_update_schema_mode import MetadataFieldValueUpdateSchemaMode
from .metadata_update_action import MetadataUpdateAction
from .metadata_update_action_parameters import MetadataUpdateActionParameters
from .metadata_update_action_parameters_metadata_values import (
    MetadataUpdateActionParametersMetadataValues,
)
from .metadata_update_action_schema import MetadataUpdateActionSchema
from .metadata_update_action_schema_type import MetadataUpdateActionSchemaType
from .metadata_update_action_type import MetadataUpdateActionType
from .metadata_update_trigger import MetadataUpdateTrigger
from .metadata_update_trigger_parameters import MetadataUpdateTriggerParameters
from .metadata_update_trigger_parameters_event_type import (
    MetadataUpdateTriggerParametersEventType,
)
from .metadata_update_trigger_parameters_metadata_values import (
    MetadataUpdateTriggerParametersMetadataValues,
)
from .metadata_update_trigger_schema import MetadataUpdateTriggerSchema
from .metadata_update_trigger_schema_type import MetadataUpdateTriggerSchemaType
from .metadata_update_trigger_type import MetadataUpdateTriggerType
from .modified_at_transition_trigger import ModifiedAtTransitionTrigger
from .modified_at_transition_trigger_parameters import (
    ModifiedAtTransitionTriggerParameters,
)
from .modified_at_transition_trigger_schema import ModifiedAtTransitionTriggerSchema
from .modified_at_transition_trigger_schema_type import (
    ModifiedAtTransitionTriggerSchemaType,
)
from .modified_at_transition_trigger_type import ModifiedAtTransitionTriggerType
from .object_added_to_collection_trigger import ObjectAddedToCollectionTrigger
from .object_added_to_collection_trigger_schema import (
    ObjectAddedToCollectionTriggerSchema,
)
from .object_added_to_collection_trigger_schema_type import (
    ObjectAddedToCollectionTriggerSchemaType,
)
from .object_added_to_collection_trigger_type import ObjectAddedToCollectionTriggerType
from .object_collection_trigger_parameters import ObjectCollectionTriggerParameters
from .object_collection_trigger_parameters_schema import (
    ObjectCollectionTriggerParametersSchema,
)
from .object_removed_from_collection_trigger import ObjectRemovedFromCollectionTrigger
from .object_removed_from_collection_trigger_schema import (
    ObjectRemovedFromCollectionTriggerSchema,
)
from .object_removed_from_collection_trigger_schema_type import (
    ObjectRemovedFromCollectionTriggerSchemaType,
)
from .object_removed_from_collection_trigger_type import (
    ObjectRemovedFromCollectionTriggerType,
)
from .patch_automations_by_automation_id_response_default_type_0 import (
    PatchAutomationsByAutomationIdResponseDefaultType0,
)
from .patch_automations_by_automation_id_response_default_type_1 import (
    PatchAutomationsByAutomationIdResponseDefaultType1,
)
from .patch_automations_by_automation_id_response_default_type_1_errors import (
    PatchAutomationsByAutomationIdResponseDefaultType1Errors,
)
from .post_automations_by_automation_id_history_response_default_type_0 import (
    PostAutomationsByAutomationIdHistoryResponseDefaultType0,
)
from .post_automations_by_automation_id_history_response_default_type_1 import (
    PostAutomationsByAutomationIdHistoryResponseDefaultType1,
)
from .post_automations_by_automation_id_history_response_default_type_1_errors import (
    PostAutomationsByAutomationIdHistoryResponseDefaultType1Errors,
)
from .post_automations_by_automation_id_runs_response_default_type_0 import (
    PostAutomationsByAutomationIdRunsResponseDefaultType0,
)
from .post_automations_by_automation_id_runs_response_default_type_1 import (
    PostAutomationsByAutomationIdRunsResponseDefaultType1,
)
from .post_automations_by_automation_id_runs_response_default_type_1_errors import (
    PostAutomationsByAutomationIdRunsResponseDefaultType1Errors,
)
from .post_automations_response_default_type_0 import (
    PostAutomationsResponseDefaultType0,
)
from .post_automations_response_default_type_1 import (
    PostAutomationsResponseDefaultType1,
)
from .post_automations_response_default_type_1_errors import (
    PostAutomationsResponseDefaultType1Errors,
)
from .put_automations_by_automation_id_response_default_type_0 import (
    PutAutomationsByAutomationIdResponseDefaultType0,
)
from .put_automations_by_automation_id_response_default_type_1 import (
    PutAutomationsByAutomationIdResponseDefaultType1,
)
from .put_automations_by_automation_id_response_default_type_1_errors import (
    PutAutomationsByAutomationIdResponseDefaultType1Errors,
)
from .range_filter import RangeFilter
from .range_filter_schema import RangeFilterSchema
from .remove_asset_restriction_action import RemoveAssetRestrictionAction
from .remove_asset_restriction_action_parameters import (
    RemoveAssetRestrictionActionParameters,
)
from .remove_asset_restriction_action_schema import RemoveAssetRestrictionActionSchema
from .remove_asset_restriction_action_schema_type import (
    RemoveAssetRestrictionActionSchemaType,
)
from .remove_asset_restriction_action_type import RemoveAssetRestrictionActionType
from .request_original_action import RequestOriginalAction
from .request_original_action_schema import RequestOriginalActionSchema
from .request_original_action_schema_type import RequestOriginalActionSchemaType
from .request_original_action_type import RequestOriginalActionType
from .request_review_action import RequestReviewAction
from .request_review_action_parameters import RequestReviewActionParameters
from .request_review_action_parameters_status import RequestReviewActionParametersStatus
from .request_review_action_schema import RequestReviewActionSchema
from .request_review_action_schema_type import RequestReviewActionSchemaType
from .request_review_action_type import RequestReviewActionType
from .restore_action import RestoreAction
from .restore_action_parameters import RestoreActionParameters
from .restore_action_schema import RestoreActionSchema
from .restore_action_schema_type import RestoreActionSchemaType
from .restore_action_type import RestoreActionType
from .restrict_asset_action import RestrictAssetAction
from .restrict_asset_action_parameters import RestrictAssetActionParameters
from .restrict_asset_action_schema import RestrictAssetActionSchema
from .restrict_asset_action_schema_type import RestrictAssetActionSchemaType
from .restrict_asset_action_type import RestrictAssetActionType
from .review_status_changed_trigger import ReviewStatusChangedTrigger
from .review_status_changed_trigger_parameters import (
    ReviewStatusChangedTriggerParameters,
)
from .review_status_changed_trigger_parameters_statuses_item import (
    ReviewStatusChangedTriggerParametersStatusesItem,
)
from .review_status_changed_trigger_schema import ReviewStatusChangedTriggerSchema
from .review_status_changed_trigger_schema_type import (
    ReviewStatusChangedTriggerSchemaType,
)
from .review_status_changed_trigger_type import ReviewStatusChangedTriggerType
from .subtitle_added_trigger import SubtitleAddedTrigger
from .subtitle_added_trigger_parameters import SubtitleAddedTriggerParameters
from .subtitle_added_trigger_schema import SubtitleAddedTriggerSchema
from .subtitle_added_trigger_schema_type import SubtitleAddedTriggerSchemaType
from .subtitle_added_trigger_type import SubtitleAddedTriggerType
from .term import Term
from .term_external import TermExternal
from .term_schema import TermSchema
from .term_schema_external import TermSchemaExternal
from .transcode_action import TranscodeAction
from .transcode_action_parameters import TranscodeActionParameters
from .transcode_action_parameters_preferred_storage_method import (
    TranscodeActionParametersPreferredStorageMethod,
)
from .transcode_action_parameters_schema import TranscodeActionParametersSchema
from .transcode_action_parameters_schema_preferred_storage_method import (
    TranscodeActionParametersSchemaPreferredStorageMethod,
)
from .transcode_action_schema import TranscodeActionSchema
from .transcode_action_schema_type import TranscodeActionSchemaType
from .transcode_action_type import TranscodeActionType
from .transcribe_action import TranscribeAction
from .transcribe_action_parameters import TranscribeActionParameters
from .transcribe_action_schema import TranscribeActionSchema
from .transcribe_action_schema_type import TranscribeActionSchemaType
from .transcribe_action_type import TranscribeActionType
from .transfer_action import TransferAction
from .transfer_action_parameters import TransferActionParameters
from .transfer_action_parameters_schema import TransferActionParametersSchema
from .transfer_action_schema import TransferActionSchema
from .transfer_action_schema_type import TransferActionSchemaType
from .transfer_action_type import TransferActionType
from .trigger import Trigger
from .trigger_custom_action import TriggerCustomAction
from .trigger_custom_action_parameters import TriggerCustomActionParameters
from .trigger_custom_action_parameters_context import (
    TriggerCustomActionParametersContext,
)
from .trigger_custom_action_parameters_metadata_values import (
    TriggerCustomActionParametersMetadataValues,
)
from .trigger_custom_action_schema import TriggerCustomActionSchema
from .trigger_custom_action_schema_type import TriggerCustomActionSchemaType
from .trigger_custom_action_type import TriggerCustomActionType
from .trigger_event_type import TriggerEventType
from .trigger_operations_item import TriggerOperationsItem
from .trigger_realm import TriggerRealm
from .trigger_schema import TriggerSchema
from .trigger_schema_base import TriggerSchemaBase
from .trigger_schema_base_parameters import TriggerSchemaBaseParameters
from .trigger_schema_event_type import TriggerSchemaEventType
from .trigger_schema_operations_item import TriggerSchemaOperationsItem
from .trigger_schema_realm import TriggerSchemaRealm
from .trigger_schema_type import TriggerSchemaType
from .trigger_type import TriggerType
from .triggers_schema import TriggersSchema
from .update_acl_action import UpdateACLAction
from .update_acl_action_parameters import UpdateACLActionParameters
from .update_acl_action_schema import UpdateACLActionSchema
from .update_acl_action_schema_type import UpdateACLActionSchemaType
from .update_acl_action_type import UpdateACLActionType
from .version_online_trigger import VersionOnlineTrigger
from .version_online_trigger_parameters import VersionOnlineTriggerParameters
from .version_online_trigger_schema import VersionOnlineTriggerSchema
from .version_online_trigger_schema_type import VersionOnlineTriggerSchemaType
from .version_online_trigger_type import VersionOnlineTriggerType

__all__ = (
    "ACLUpdateSchema",
    "ACLUpdateSchemaMode",
    "ACLUpdateSchemaPermissionsItem",
    "ActionSchemaBase",
    "ActionSchemaBaseParameters",
    "AddToCollectionActionParameters",
    "AddToCollectionActionSchema",
    "AddToCollectionActionSchemaType",
    "AnalyzeActionParameters",
    "AnalyzeActionParametersForceType",
    "AnalyzeActionSchema",
    "AnalyzeActionSchemaType",
    "ArchiveActionParameters",
    "ArchiveActionSchema",
    "ArchiveActionSchemaType",
    "AssetArchivedTriggerParameters",
    "AssetArchivedTriggerSchema",
    "AssetArchivedTriggerSchemaType",
    "AssetOnlineTriggerParameters",
    "AssetOnlineTriggerSchema",
    "AssetOnlineTriggerSchemaType",
    "AssetRestoredTriggerParameters",
    "AssetRestoredTriggerSchema",
    "AssetRestoredTriggerSchemaType",
    "AssetSharedTriggerParameters",
    "AssetSharedTriggerSchema",
    "AssetSharedTriggerSchemaType",
    "AssetTransferredToStorageParameters",
    "AssetTransferredToStorageTriggerSchema",
    "AssetTransferredToStorageTriggerSchemaType",
    "AutomationHistorySchema",
    "AutomationHistorySchemaStatus",
    "AutomationInternalSchema",
    "AutomationInternalSchemaStatus",
    "AutomationRunEstimateSchema",
    "AutomationRunEstimateSchemaFacets",
    "AutomationSchema",
    "AutomationSchemaStatus",
    "AutomationsInternalSchema",
    "AutomationsSchema",
    "AutomationStatsObjectSchema",
    "AutomationStatsObjectSchemaType",
    "AutomationStatsSchema",
    "BucketSchema",
    "Condition",
    "ConditionSchema",
    "CreatedAtTransitionTrigger",
    "CreatedAtTransitionTriggerParameters",
    "CreatedAtTransitionTriggerSchema",
    "CreatedAtTransitionTriggerSchemaType",
    "CreatedAtTransitionTriggerType",
    "CreatePublicationJobAction",
    "CreatePublicationJobActionSchema",
    "CreatePublicationJobActionSchemaType",
    "CreatePublicationJobActionType",
    "CreatePublicationJobParameters",
    "CreatePublicationJobParametersMetadataOverrides",
    "CreatePublicationJobThumbnailKeyframe",
    "CreatePublicationJobThumbnailKeyframeType",
    "CreatePublicationTemplate",
    "CreatePublicationTemplateData",
    "CreateShareAction",
    "CreateShareActionParameters",
    "CreateShareActionParametersSchema",
    "CreateShareActionSchema",
    "CreateShareActionSchemaType",
    "CreateShareActionType",
    "DeleteAction",
    "DeleteActionParameters",
    "DeleteActionSchema",
    "DeleteActionSchemaParameters",
    "DeleteActionSchemaType",
    "DeleteActionType",
    "DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0",
    "DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1",
    "DeleteAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1Errors",
    "DeleteAutomationsByAutomationIdResponseDefaultType0",
    "DeleteAutomationsByAutomationIdResponseDefaultType1",
    "DeleteAutomationsByAutomationIdResponseDefaultType1Errors",
    "DeleteFileSetAction",
    "DeleteFileSetActionParameters",
    "DeleteFileSetActionSchema",
    "DeleteFileSetActionSchemaType",
    "DeleteFileSetActionType",
    "ExportAction",
    "ExportActionParameters",
    "ExportActionParametersMetadataFormat",
    "ExportActionSchema",
    "ExportActionSchemaType",
    "ExportActionType",
    "ExtractFacesAction",
    "ExtractFacesActionSchema",
    "ExtractFacesActionSchemaType",
    "ExtractFacesActionType",
    "ExtractFacesParameters",
    "FacetSchema",
    "GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType0",
    "GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1",
    "GetAutomationsByAutomationIdHistoryByObjectTypeByObjectIdByVersionIdResponseDefaultType1Errors",
    "GetAutomationsByAutomationIdResponseDefaultType0",
    "GetAutomationsByAutomationIdResponseDefaultType1",
    "GetAutomationsByAutomationIdResponseDefaultType1Errors",
    "GetAutomationsByAutomationIdRunsEstimateResponseDefaultType0",
    "GetAutomationsByAutomationIdRunsEstimateResponseDefaultType1",
    "GetAutomationsByAutomationIdRunsEstimateResponseDefaultType1Errors",
    "GetAutomationsResponseDefaultType0",
    "GetAutomationsResponseDefaultType1",
    "GetAutomationsResponseDefaultType1Errors",
    "ListObjectsSchema",
    "MetadataFieldValueSchema",
    "MetadataFieldValueSchemaFieldValuesItem",
    "MetadataFieldValueUpdateSchema",
    "MetadataFieldValueUpdateSchemaFieldValuesItem",
    "MetadataFieldValueUpdateSchemaMode",
    "MetadataUpdateAction",
    "MetadataUpdateActionParameters",
    "MetadataUpdateActionParametersMetadataValues",
    "MetadataUpdateActionSchema",
    "MetadataUpdateActionSchemaType",
    "MetadataUpdateActionType",
    "MetadataUpdateTrigger",
    "MetadataUpdateTriggerParameters",
    "MetadataUpdateTriggerParametersEventType",
    "MetadataUpdateTriggerParametersMetadataValues",
    "MetadataUpdateTriggerSchema",
    "MetadataUpdateTriggerSchemaType",
    "MetadataUpdateTriggerType",
    "ModifiedAtTransitionTrigger",
    "ModifiedAtTransitionTriggerParameters",
    "ModifiedAtTransitionTriggerSchema",
    "ModifiedAtTransitionTriggerSchemaType",
    "ModifiedAtTransitionTriggerType",
    "ObjectAddedToCollectionTrigger",
    "ObjectAddedToCollectionTriggerSchema",
    "ObjectAddedToCollectionTriggerSchemaType",
    "ObjectAddedToCollectionTriggerType",
    "ObjectCollectionTriggerParameters",
    "ObjectCollectionTriggerParametersSchema",
    "ObjectRemovedFromCollectionTrigger",
    "ObjectRemovedFromCollectionTriggerSchema",
    "ObjectRemovedFromCollectionTriggerSchemaType",
    "ObjectRemovedFromCollectionTriggerType",
    "PatchAutomationsByAutomationIdResponseDefaultType0",
    "PatchAutomationsByAutomationIdResponseDefaultType1",
    "PatchAutomationsByAutomationIdResponseDefaultType1Errors",
    "PostAutomationsByAutomationIdHistoryResponseDefaultType0",
    "PostAutomationsByAutomationIdHistoryResponseDefaultType1",
    "PostAutomationsByAutomationIdHistoryResponseDefaultType1Errors",
    "PostAutomationsByAutomationIdRunsResponseDefaultType0",
    "PostAutomationsByAutomationIdRunsResponseDefaultType1",
    "PostAutomationsByAutomationIdRunsResponseDefaultType1Errors",
    "PostAutomationsResponseDefaultType0",
    "PostAutomationsResponseDefaultType1",
    "PostAutomationsResponseDefaultType1Errors",
    "PutAutomationsByAutomationIdResponseDefaultType0",
    "PutAutomationsByAutomationIdResponseDefaultType1",
    "PutAutomationsByAutomationIdResponseDefaultType1Errors",
    "RangeFilter",
    "RangeFilterSchema",
    "RemoveAssetRestrictionAction",
    "RemoveAssetRestrictionActionParameters",
    "RemoveAssetRestrictionActionSchema",
    "RemoveAssetRestrictionActionSchemaType",
    "RemoveAssetRestrictionActionType",
    "RequestOriginalAction",
    "RequestOriginalActionSchema",
    "RequestOriginalActionSchemaType",
    "RequestOriginalActionType",
    "RequestReviewAction",
    "RequestReviewActionParameters",
    "RequestReviewActionParametersStatus",
    "RequestReviewActionSchema",
    "RequestReviewActionSchemaType",
    "RequestReviewActionType",
    "RestoreAction",
    "RestoreActionParameters",
    "RestoreActionSchema",
    "RestoreActionSchemaType",
    "RestoreActionType",
    "RestrictAssetAction",
    "RestrictAssetActionParameters",
    "RestrictAssetActionSchema",
    "RestrictAssetActionSchemaType",
    "RestrictAssetActionType",
    "ReviewStatusChangedTrigger",
    "ReviewStatusChangedTriggerParameters",
    "ReviewStatusChangedTriggerParametersStatusesItem",
    "ReviewStatusChangedTriggerSchema",
    "ReviewStatusChangedTriggerSchemaType",
    "ReviewStatusChangedTriggerType",
    "SubtitleAddedTrigger",
    "SubtitleAddedTriggerParameters",
    "SubtitleAddedTriggerSchema",
    "SubtitleAddedTriggerSchemaType",
    "SubtitleAddedTriggerType",
    "Term",
    "TermExternal",
    "TermSchema",
    "TermSchemaExternal",
    "TranscodeAction",
    "TranscodeActionParameters",
    "TranscodeActionParametersPreferredStorageMethod",
    "TranscodeActionParametersSchema",
    "TranscodeActionParametersSchemaPreferredStorageMethod",
    "TranscodeActionSchema",
    "TranscodeActionSchemaType",
    "TranscodeActionType",
    "TranscribeAction",
    "TranscribeActionParameters",
    "TranscribeActionSchema",
    "TranscribeActionSchemaType",
    "TranscribeActionType",
    "TransferAction",
    "TransferActionParameters",
    "TransferActionParametersSchema",
    "TransferActionSchema",
    "TransferActionSchemaType",
    "TransferActionType",
    "Trigger",
    "TriggerCustomAction",
    "TriggerCustomActionParameters",
    "TriggerCustomActionParametersContext",
    "TriggerCustomActionParametersMetadataValues",
    "TriggerCustomActionSchema",
    "TriggerCustomActionSchemaType",
    "TriggerCustomActionType",
    "TriggerEventType",
    "TriggerOperationsItem",
    "TriggerRealm",
    "TriggerSchema",
    "TriggerSchemaBase",
    "TriggerSchemaBaseParameters",
    "TriggerSchemaEventType",
    "TriggerSchemaOperationsItem",
    "TriggerSchemaRealm",
    "TriggerSchemaType",
    "TriggersSchema",
    "TriggerType",
    "UpdateACLAction",
    "UpdateACLActionParameters",
    "UpdateACLActionSchema",
    "UpdateACLActionSchemaType",
    "UpdateACLActionType",
    "VersionOnlineTrigger",
    "VersionOnlineTriggerParameters",
    "VersionOnlineTriggerSchema",
    "VersionOnlineTriggerSchemaType",
    "VersionOnlineTriggerType",
)
