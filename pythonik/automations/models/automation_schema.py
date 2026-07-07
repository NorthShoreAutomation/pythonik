from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automation_schema_status import AutomationSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_to_collection_action_schema import AddToCollectionActionSchema
    from ..models.analyze_action_schema import AnalyzeActionSchema
    from ..models.archive_action_schema import ArchiveActionSchema
    from ..models.asset_archived_trigger_schema import AssetArchivedTriggerSchema
    from ..models.asset_online_trigger_schema import AssetOnlineTriggerSchema
    from ..models.asset_restored_trigger_schema import AssetRestoredTriggerSchema
    from ..models.asset_shared_trigger_schema import AssetSharedTriggerSchema
    from ..models.asset_transferred_to_storage_trigger_schema import (
        AssetTransferredToStorageTriggerSchema,
    )
    from ..models.condition import Condition
    from ..models.create_publication_job_action import CreatePublicationJobAction
    from ..models.create_share_action import CreateShareAction
    from ..models.created_at_transition_trigger import CreatedAtTransitionTrigger
    from ..models.delete_action import DeleteAction
    from ..models.delete_file_set_action import DeleteFileSetAction
    from ..models.export_action import ExportAction
    from ..models.extract_faces_action import ExtractFacesAction
    from ..models.metadata_update_action import MetadataUpdateAction
    from ..models.metadata_update_trigger import MetadataUpdateTrigger
    from ..models.modified_at_transition_trigger import ModifiedAtTransitionTrigger
    from ..models.object_added_to_collection_trigger import (
        ObjectAddedToCollectionTrigger,
    )
    from ..models.object_removed_from_collection_trigger import (
        ObjectRemovedFromCollectionTrigger,
    )
    from ..models.remove_asset_restriction_action import RemoveAssetRestrictionAction
    from ..models.request_original_action import RequestOriginalAction
    from ..models.request_review_action import RequestReviewAction
    from ..models.restore_action import RestoreAction
    from ..models.restrict_asset_action import RestrictAssetAction
    from ..models.review_status_changed_trigger import ReviewStatusChangedTrigger
    from ..models.subtitle_added_trigger import SubtitleAddedTrigger
    from ..models.transcode_action import TranscodeAction
    from ..models.transcribe_action import TranscribeAction
    from ..models.transfer_action import TransferAction
    from ..models.trigger_custom_action import TriggerCustomAction
    from ..models.update_acl_action import UpdateACLAction
    from ..models.version_online_trigger import VersionOnlineTrigger


T = TypeVar("T", bound="AutomationSchema")


@_attrs_define
class AutomationSchema:
    """
    Attributes:
        actions (list[AddToCollectionActionSchema | AnalyzeActionSchema | ArchiveActionSchema |
            CreatePublicationJobAction | CreateShareAction | DeleteAction | DeleteFileSetAction | ExportAction |
            ExtractFacesAction | MetadataUpdateAction | RemoveAssetRestrictionAction | RequestOriginalAction |
            RequestReviewAction | RestoreAction | RestrictAssetAction | TranscodeAction | TranscribeAction | TransferAction
            | TriggerCustomAction | UpdateACLAction]):
        name (str):
        triggers (list[AssetArchivedTriggerSchema | AssetOnlineTriggerSchema | AssetRestoredTriggerSchema |
            AssetSharedTriggerSchema | AssetTransferredToStorageTriggerSchema | CreatedAtTransitionTrigger |
            MetadataUpdateTrigger | ModifiedAtTransitionTrigger | ObjectAddedToCollectionTrigger |
            ObjectRemovedFromCollectionTrigger | ReviewStatusChangedTrigger | SubtitleAddedTrigger | VersionOnlineTrigger]):
        conditions (list[Condition] | Unset):
        created_by (UUID | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        id (UUID | Unset):
        modified_by (UUID | Unset):
        status (AutomationSchemaStatus | Unset):
        system_domain_id (UUID | Unset):
    """

    actions: list[
        AddToCollectionActionSchema
        | AnalyzeActionSchema
        | ArchiveActionSchema
        | CreatePublicationJobAction
        | CreateShareAction
        | DeleteAction
        | DeleteFileSetAction
        | ExportAction
        | ExtractFacesAction
        | MetadataUpdateAction
        | RemoveAssetRestrictionAction
        | RequestOriginalAction
        | RequestReviewAction
        | RestoreAction
        | RestrictAssetAction
        | TranscodeAction
        | TranscribeAction
        | TransferAction
        | TriggerCustomAction
        | UpdateACLAction
    ]
    name: str
    triggers: list[
        AssetArchivedTriggerSchema
        | AssetOnlineTriggerSchema
        | AssetRestoredTriggerSchema
        | AssetSharedTriggerSchema
        | AssetTransferredToStorageTriggerSchema
        | CreatedAtTransitionTrigger
        | MetadataUpdateTrigger
        | ModifiedAtTransitionTrigger
        | ObjectAddedToCollectionTrigger
        | ObjectRemovedFromCollectionTrigger
        | ReviewStatusChangedTrigger
        | SubtitleAddedTrigger
        | VersionOnlineTrigger
    ]
    conditions: list[Condition] | Unset = UNSET
    created_by: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    modified_by: UUID | Unset = UNSET
    status: AutomationSchemaStatus | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_to_collection_action_schema import AddToCollectionActionSchema
        from ..models.analyze_action_schema import AnalyzeActionSchema
        from ..models.archive_action_schema import ArchiveActionSchema
        from ..models.asset_archived_trigger_schema import AssetArchivedTriggerSchema
        from ..models.asset_online_trigger_schema import AssetOnlineTriggerSchema
        from ..models.asset_restored_trigger_schema import AssetRestoredTriggerSchema
        from ..models.asset_shared_trigger_schema import AssetSharedTriggerSchema
        from ..models.asset_transferred_to_storage_trigger_schema import (
            AssetTransferredToStorageTriggerSchema,
        )
        from ..models.create_publication_job_action import CreatePublicationJobAction
        from ..models.create_share_action import CreateShareAction
        from ..models.created_at_transition_trigger import CreatedAtTransitionTrigger
        from ..models.delete_action import DeleteAction
        from ..models.delete_file_set_action import DeleteFileSetAction
        from ..models.export_action import ExportAction
        from ..models.extract_faces_action import ExtractFacesAction
        from ..models.metadata_update_action import MetadataUpdateAction
        from ..models.metadata_update_trigger import MetadataUpdateTrigger
        from ..models.modified_at_transition_trigger import ModifiedAtTransitionTrigger
        from ..models.object_added_to_collection_trigger import (
            ObjectAddedToCollectionTrigger,
        )
        from ..models.remove_asset_restriction_action import (
            RemoveAssetRestrictionAction,
        )
        from ..models.request_original_action import RequestOriginalAction
        from ..models.request_review_action import RequestReviewAction
        from ..models.restore_action import RestoreAction
        from ..models.restrict_asset_action import RestrictAssetAction
        from ..models.review_status_changed_trigger import ReviewStatusChangedTrigger
        from ..models.subtitle_added_trigger import SubtitleAddedTrigger
        from ..models.transcode_action import TranscodeAction
        from ..models.transcribe_action import TranscribeAction
        from ..models.transfer_action import TransferAction
        from ..models.update_acl_action import UpdateACLAction
        from ..models.version_online_trigger import VersionOnlineTrigger

        actions = []
        for actions_item_data in self.actions:
            actions_item: dict[str, Any]
            if isinstance(actions_item_data, AnalyzeActionSchema):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ExtractFacesAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, CreatePublicationJobAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ArchiveActionSchema):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, RestoreAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ExportAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateACLAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, MetadataUpdateAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, TranscodeAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, TransferAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, RequestOriginalAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, AddToCollectionActionSchema):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, TranscribeAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, CreateShareAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, DeleteAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, DeleteFileSetAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, RestrictAssetAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, RemoveAssetRestrictionAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, RequestReviewAction):
                actions_item = actions_item_data.to_dict()
            else:
                actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        name = self.name

        triggers = []
        for triggers_item_data in self.triggers:
            triggers_item: dict[str, Any]
            if isinstance(triggers_item_data, MetadataUpdateTrigger):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, AssetSharedTriggerSchema):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, SubtitleAddedTrigger):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, ReviewStatusChangedTrigger):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, AssetOnlineTriggerSchema):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, VersionOnlineTrigger):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, AssetTransferredToStorageTriggerSchema):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, AssetArchivedTriggerSchema):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, AssetRestoredTriggerSchema):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, CreatedAtTransitionTrigger):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, ModifiedAtTransitionTrigger):
                triggers_item = triggers_item_data.to_dict()
            elif isinstance(triggers_item_data, ObjectAddedToCollectionTrigger):
                triggers_item = triggers_item_data.to_dict()
            else:
                triggers_item = triggers_item_data.to_dict()

            triggers.append(triggers_item)

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        modified_by: str | Unset = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = str(self.modified_by)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "name": name,
                "triggers": triggers,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if modified_by is not UNSET:
            field_dict["modified_by"] = modified_by
        if status is not UNSET:
            field_dict["status"] = status
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_to_collection_action_schema import AddToCollectionActionSchema
        from ..models.analyze_action_schema import AnalyzeActionSchema
        from ..models.archive_action_schema import ArchiveActionSchema
        from ..models.asset_archived_trigger_schema import AssetArchivedTriggerSchema
        from ..models.asset_online_trigger_schema import AssetOnlineTriggerSchema
        from ..models.asset_restored_trigger_schema import AssetRestoredTriggerSchema
        from ..models.asset_shared_trigger_schema import AssetSharedTriggerSchema
        from ..models.asset_transferred_to_storage_trigger_schema import (
            AssetTransferredToStorageTriggerSchema,
        )
        from ..models.condition import Condition
        from ..models.create_publication_job_action import CreatePublicationJobAction
        from ..models.create_share_action import CreateShareAction
        from ..models.created_at_transition_trigger import CreatedAtTransitionTrigger
        from ..models.delete_action import DeleteAction
        from ..models.delete_file_set_action import DeleteFileSetAction
        from ..models.export_action import ExportAction
        from ..models.extract_faces_action import ExtractFacesAction
        from ..models.metadata_update_action import MetadataUpdateAction
        from ..models.metadata_update_trigger import MetadataUpdateTrigger
        from ..models.modified_at_transition_trigger import ModifiedAtTransitionTrigger
        from ..models.object_added_to_collection_trigger import (
            ObjectAddedToCollectionTrigger,
        )
        from ..models.object_removed_from_collection_trigger import (
            ObjectRemovedFromCollectionTrigger,
        )
        from ..models.remove_asset_restriction_action import (
            RemoveAssetRestrictionAction,
        )
        from ..models.request_original_action import RequestOriginalAction
        from ..models.request_review_action import RequestReviewAction
        from ..models.restore_action import RestoreAction
        from ..models.restrict_asset_action import RestrictAssetAction
        from ..models.review_status_changed_trigger import ReviewStatusChangedTrigger
        from ..models.subtitle_added_trigger import SubtitleAddedTrigger
        from ..models.transcode_action import TranscodeAction
        from ..models.transcribe_action import TranscribeAction
        from ..models.transfer_action import TransferAction
        from ..models.trigger_custom_action import TriggerCustomAction
        from ..models.update_acl_action import UpdateACLAction
        from ..models.version_online_trigger import VersionOnlineTrigger

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:

            def _parse_actions_item(
                data: object,
            ) -> (
                AddToCollectionActionSchema
                | AnalyzeActionSchema
                | ArchiveActionSchema
                | CreatePublicationJobAction
                | CreateShareAction
                | DeleteAction
                | DeleteFileSetAction
                | ExportAction
                | ExtractFacesAction
                | MetadataUpdateAction
                | RemoveAssetRestrictionAction
                | RequestOriginalAction
                | RequestReviewAction
                | RestoreAction
                | RestrictAssetAction
                | TranscodeAction
                | TranscribeAction
                | TransferAction
                | TriggerCustomAction
                | UpdateACLAction
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_0 = AnalyzeActionSchema.from_dict(data)

                    return actions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_1 = ExtractFacesAction.from_dict(data)

                    return actions_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_2 = CreatePublicationJobAction.from_dict(data)

                    return actions_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_3 = ArchiveActionSchema.from_dict(data)

                    return actions_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_4 = RestoreAction.from_dict(data)

                    return actions_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_5 = ExportAction.from_dict(data)

                    return actions_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_6 = UpdateACLAction.from_dict(data)

                    return actions_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_7 = MetadataUpdateAction.from_dict(data)

                    return actions_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_8 = TranscodeAction.from_dict(data)

                    return actions_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_9 = TransferAction.from_dict(data)

                    return actions_item_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_10 = RequestOriginalAction.from_dict(data)

                    return actions_item_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_11 = AddToCollectionActionSchema.from_dict(data)

                    return actions_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_12 = TranscribeAction.from_dict(data)

                    return actions_item_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_13 = CreateShareAction.from_dict(data)

                    return actions_item_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_14 = DeleteAction.from_dict(data)

                    return actions_item_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_15 = DeleteFileSetAction.from_dict(data)

                    return actions_item_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_16 = RestrictAssetAction.from_dict(data)

                    return actions_item_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_17 = RemoveAssetRestrictionAction.from_dict(data)

                    return actions_item_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_18 = RequestReviewAction.from_dict(data)

                    return actions_item_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                actions_item_type_19 = TriggerCustomAction.from_dict(data)

                return actions_item_type_19

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        name = d.pop("name")

        triggers = []
        _triggers = d.pop("triggers")
        for triggers_item_data in _triggers:

            def _parse_triggers_item(
                data: object,
            ) -> (
                AssetArchivedTriggerSchema
                | AssetOnlineTriggerSchema
                | AssetRestoredTriggerSchema
                | AssetSharedTriggerSchema
                | AssetTransferredToStorageTriggerSchema
                | CreatedAtTransitionTrigger
                | MetadataUpdateTrigger
                | ModifiedAtTransitionTrigger
                | ObjectAddedToCollectionTrigger
                | ObjectRemovedFromCollectionTrigger
                | ReviewStatusChangedTrigger
                | SubtitleAddedTrigger
                | VersionOnlineTrigger
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_0 = MetadataUpdateTrigger.from_dict(data)

                    return triggers_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_1 = AssetSharedTriggerSchema.from_dict(data)

                    return triggers_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_2 = SubtitleAddedTrigger.from_dict(data)

                    return triggers_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_3 = ReviewStatusChangedTrigger.from_dict(data)

                    return triggers_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_4 = AssetOnlineTriggerSchema.from_dict(data)

                    return triggers_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_5 = VersionOnlineTrigger.from_dict(data)

                    return triggers_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_6 = (
                        AssetTransferredToStorageTriggerSchema.from_dict(data)
                    )

                    return triggers_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_7 = AssetArchivedTriggerSchema.from_dict(data)

                    return triggers_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_8 = AssetRestoredTriggerSchema.from_dict(data)

                    return triggers_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_9 = CreatedAtTransitionTrigger.from_dict(data)

                    return triggers_item_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_10 = ModifiedAtTransitionTrigger.from_dict(data)

                    return triggers_item_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    triggers_item_type_11 = ObjectAddedToCollectionTrigger.from_dict(
                        data
                    )

                    return triggers_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                triggers_item_type_12 = ObjectRemovedFromCollectionTrigger.from_dict(
                    data
                )

                return triggers_item_type_12

            triggers_item = _parse_triggers_item(triggers_item_data)

            triggers.append(triggers_item)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[Condition] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = Condition.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        _created_by = d.pop("created_by", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _modified_by = d.pop("modified_by", UNSET)
        modified_by: UUID | Unset
        if isinstance(_modified_by, Unset):
            modified_by = UNSET
        else:
            modified_by = UUID(_modified_by)

        _status = d.pop("status", UNSET)
        status: AutomationSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AutomationSchemaStatus(_status)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        automation_schema = cls(
            actions=actions,
            name=name,
            triggers=triggers,
            conditions=conditions,
            created_by=created_by,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            id=id,
            modified_by=modified_by,
            status=status,
            system_domain_id=system_domain_id,
        )

        automation_schema.additional_properties = d
        return automation_schema

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
