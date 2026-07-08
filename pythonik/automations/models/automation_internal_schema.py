from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_to_collection_action_schema import AddToCollectionActionSchema
    from ..models.analyze_action_schema import AnalyzeActionSchema
    from ..models.archive_action_schema import ArchiveActionSchema
    from ..models.automation_internal_schema_status_type_1 import (
        AutomationInternalSchemaStatusType1,
    )
    from ..models.condition import Condition
    from ..models.create_publication_job_action import CreatePublicationJobAction
    from ..models.create_share_action import CreateShareAction
    from ..models.delete_action import DeleteAction
    from ..models.delete_file_set_action import DeleteFileSetAction
    from ..models.export_action import ExportAction
    from ..models.extract_faces_action import ExtractFacesAction
    from ..models.metadata_update_action import MetadataUpdateAction
    from ..models.remove_asset_restriction_action import RemoveAssetRestrictionAction
    from ..models.request_original_action import RequestOriginalAction
    from ..models.request_review_action import RequestReviewAction
    from ..models.restore_action import RestoreAction
    from ..models.restrict_asset_action import RestrictAssetAction
    from ..models.transcode_action import TranscodeAction
    from ..models.transcribe_action import TranscribeAction
    from ..models.transfer_action import TransferAction
    from ..models.trigger import Trigger
    from ..models.trigger_custom_action import TriggerCustomAction
    from ..models.update_acl_action import UpdateACLAction


T = TypeVar("T", bound="AutomationInternalSchema")


@_attrs_define
class AutomationInternalSchema:
    """
    Attributes:
        actions (list[AddToCollectionActionSchema | AnalyzeActionSchema | ArchiveActionSchema |
            CreatePublicationJobAction | CreateShareAction | DeleteAction | DeleteFileSetAction | ExportAction |
            ExtractFacesAction | MetadataUpdateAction | RemoveAssetRestrictionAction | RequestOriginalAction |
            RequestReviewAction | RestoreAction | RestrictAssetAction | TranscodeAction | TranscribeAction | TransferAction
            | TriggerCustomAction | UpdateACLAction]):
        name (str):
        triggers (list[Trigger]):
        conditions (list[Condition] | None | Unset):
        created_by (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        description (None | str | Unset):
        id (None | Unset | UUID):
        modified_by (None | Unset | UUID):
        status (AutomationInternalSchemaStatusType1 | None | Unset):
        system_domain_id (None | Unset | UUID):
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
    triggers: list[Trigger]
    conditions: list[Condition] | None | Unset = UNSET
    created_by: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    modified_by: None | Unset | UUID = UNSET
    status: AutomationInternalSchemaStatusType1 | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_to_collection_action_schema import AddToCollectionActionSchema
        from ..models.analyze_action_schema import AnalyzeActionSchema
        from ..models.archive_action_schema import ArchiveActionSchema
        from ..models.automation_internal_schema_status_type_1 import (
            AutomationInternalSchemaStatusType1,
        )
        from ..models.create_publication_job_action import CreatePublicationJobAction
        from ..models.create_share_action import CreateShareAction
        from ..models.delete_action import DeleteAction
        from ..models.delete_file_set_action import DeleteFileSetAction
        from ..models.export_action import ExportAction
        from ..models.extract_faces_action import ExtractFacesAction
        from ..models.metadata_update_action import MetadataUpdateAction
        from ..models.remove_asset_restriction_action import (
            RemoveAssetRestrictionAction,
        )
        from ..models.request_original_action import RequestOriginalAction
        from ..models.request_review_action import RequestReviewAction
        from ..models.restore_action import RestoreAction
        from ..models.restrict_asset_action import RestrictAssetAction
        from ..models.transcode_action import TranscodeAction
        from ..models.transcribe_action import TranscribeAction
        from ..models.transfer_action import TransferAction
        from ..models.update_acl_action import UpdateACLAction

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
            triggers_item = triggers_item_data.to_dict()
            triggers.append(triggers_item)

        conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        modified_by: None | str | Unset
        if isinstance(self.modified_by, Unset):
            modified_by = UNSET
        elif isinstance(self.modified_by, UUID):
            modified_by = str(self.modified_by)
        else:
            modified_by = self.modified_by

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, AutomationInternalSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

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
        from ..models.automation_internal_schema_status_type_1 import (
            AutomationInternalSchemaStatusType1,
        )
        from ..models.condition import Condition
        from ..models.create_publication_job_action import CreatePublicationJobAction
        from ..models.create_share_action import CreateShareAction
        from ..models.delete_action import DeleteAction
        from ..models.delete_file_set_action import DeleteFileSetAction
        from ..models.export_action import ExportAction
        from ..models.extract_faces_action import ExtractFacesAction
        from ..models.metadata_update_action import MetadataUpdateAction
        from ..models.remove_asset_restriction_action import (
            RemoveAssetRestrictionAction,
        )
        from ..models.request_original_action import RequestOriginalAction
        from ..models.request_review_action import RequestReviewAction
        from ..models.restore_action import RestoreAction
        from ..models.restrict_asset_action import RestrictAssetAction
        from ..models.transcode_action import TranscodeAction
        from ..models.transcribe_action import TranscribeAction
        from ..models.transfer_action import TransferAction
        from ..models.trigger import Trigger
        from ..models.trigger_custom_action import TriggerCustomAction
        from ..models.update_acl_action import UpdateACLAction

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
            triggers_item = Trigger.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        def _parse_conditions(data: object) -> list[Condition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:
                    conditions_type_0_item = Condition.from_dict(
                        conditions_type_0_item_data
                    )

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Condition] | None | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_modified_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_by_type_0 = UUID(data)

                return modified_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        modified_by = _parse_modified_by(d.pop("modified_by", UNSET))

        def _parse_status(
            data: object,
        ) -> AutomationInternalSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = AutomationInternalSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutomationInternalSchemaStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        automation_internal_schema = cls(
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

        automation_internal_schema.additional_properties = d
        return automation_internal_schema

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
