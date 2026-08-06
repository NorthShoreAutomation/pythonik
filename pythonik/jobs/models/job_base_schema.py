from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_base_schema_status import JobBaseSchemaStatus
from ..models.job_base_schema_type import JobBaseSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_context_schema import ActionContextSchema
    from ..models.job_base_schema_children_progress_type_0 import (
        JobBaseSchemaChildrenProgressType0,
    )
    from ..models.job_base_schema_job_context_type_0 import JobBaseSchemaJobContextType0
    from ..models.job_base_schema_metadata_type_0 import JobBaseSchemaMetadataType0
    from ..models.related_object import RelatedObject


T = TypeVar("T", bound="JobBaseSchema")


@_attrs_define
class JobBaseSchema:
    """
    Attributes:
        status (JobBaseSchemaStatus):
        title (str):
        type_ (JobBaseSchemaType):
        action_context (ActionContextSchema | None | Unset):
        children_progress (JobBaseSchemaChildrenProgressType0 | None | Unset):
        completed_at (datetime.datetime | None | Unset):
        custom_type (None | str | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        error_message (None | str | Unset):
        has_children (bool | None | Unset):
        id (None | Unset | UUID):
        job_context (JobBaseSchemaJobContextType0 | None | Unset):
        message (None | str | Unset):
        metadata (JobBaseSchemaMetadataType0 | None | Unset):
        object_id (None | Unset | UUID):
        object_type (None | str | Unset):
        parent_id (None | Unset | UUID):
        priority (int | None | Unset):
        progress (int | None | Unset):
        progress_processed (int | None | Unset):
        progress_total (int | None | Unset):
        related_objects (list[RelatedObject] | None | Unset):
        started_at (datetime.datetime | None | Unset):
    """

    status: JobBaseSchemaStatus
    title: str
    type_: JobBaseSchemaType
    action_context: ActionContextSchema | None | Unset = UNSET
    children_progress: JobBaseSchemaChildrenProgressType0 | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    custom_type: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    has_children: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    job_context: JobBaseSchemaJobContextType0 | None | Unset = UNSET
    message: None | str | Unset = UNSET
    metadata: JobBaseSchemaMetadataType0 | None | Unset = UNSET
    object_id: None | Unset | UUID = UNSET
    object_type: None | str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    priority: int | None | Unset = UNSET
    progress: int | None | Unset = UNSET
    progress_processed: int | None | Unset = UNSET
    progress_total: int | None | Unset = UNSET
    related_objects: list[RelatedObject] | None | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_context_schema import ActionContextSchema
        from ..models.job_base_schema_children_progress_type_0 import (
            JobBaseSchemaChildrenProgressType0,
        )
        from ..models.job_base_schema_job_context_type_0 import (
            JobBaseSchemaJobContextType0,
        )
        from ..models.job_base_schema_metadata_type_0 import JobBaseSchemaMetadataType0

        status = self.status.value

        title = self.title

        type_ = self.type_.value

        action_context: dict[str, Any] | None | Unset
        if isinstance(self.action_context, Unset):
            action_context = UNSET
        elif isinstance(self.action_context, ActionContextSchema):
            action_context = self.action_context.to_dict()
        else:
            action_context = self.action_context

        children_progress: dict[str, Any] | None | Unset
        if isinstance(self.children_progress, Unset):
            children_progress = UNSET
        elif isinstance(self.children_progress, JobBaseSchemaChildrenProgressType0):
            children_progress = self.children_progress.to_dict()
        else:
            children_progress = self.children_progress

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        custom_type: None | str | Unset
        if isinstance(self.custom_type, Unset):
            custom_type = UNSET
        else:
            custom_type = self.custom_type

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

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        has_children: bool | None | Unset
        if isinstance(self.has_children, Unset):
            has_children = UNSET
        else:
            has_children = self.has_children

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        job_context: dict[str, Any] | None | Unset
        if isinstance(self.job_context, Unset):
            job_context = UNSET
        elif isinstance(self.job_context, JobBaseSchemaJobContextType0):
            job_context = self.job_context.to_dict()
        else:
            job_context = self.job_context

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, JobBaseSchemaMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        elif isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        progress: int | None | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

        progress_processed: int | None | Unset
        if isinstance(self.progress_processed, Unset):
            progress_processed = UNSET
        else:
            progress_processed = self.progress_processed

        progress_total: int | None | Unset
        if isinstance(self.progress_total, Unset):
            progress_total = UNSET
        else:
            progress_total = self.progress_total

        related_objects: list[dict[str, Any]] | None | Unset
        if isinstance(self.related_objects, Unset):
            related_objects = UNSET
        elif isinstance(self.related_objects, list):
            related_objects = []
            for related_objects_type_0_item_data in self.related_objects:
                related_objects_type_0_item = related_objects_type_0_item_data.to_dict()
                related_objects.append(related_objects_type_0_item)

        else:
            related_objects = self.related_objects

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "title": title,
                "type": type_,
            }
        )
        if action_context is not UNSET:
            field_dict["action_context"] = action_context
        if children_progress is not UNSET:
            field_dict["children_progress"] = children_progress
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if custom_type is not UNSET:
            field_dict["custom_type"] = custom_type
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if has_children is not UNSET:
            field_dict["has_children"] = has_children
        if id is not UNSET:
            field_dict["id"] = id
        if job_context is not UNSET:
            field_dict["job_context"] = job_context
        if message is not UNSET:
            field_dict["message"] = message
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if progress is not UNSET:
            field_dict["progress"] = progress
        if progress_processed is not UNSET:
            field_dict["progress_processed"] = progress_processed
        if progress_total is not UNSET:
            field_dict["progress_total"] = progress_total
        if related_objects is not UNSET:
            field_dict["related_objects"] = related_objects
        if started_at is not UNSET:
            field_dict["started_at"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_context_schema import ActionContextSchema
        from ..models.job_base_schema_children_progress_type_0 import (
            JobBaseSchemaChildrenProgressType0,
        )
        from ..models.job_base_schema_job_context_type_0 import (
            JobBaseSchemaJobContextType0,
        )
        from ..models.job_base_schema_metadata_type_0 import JobBaseSchemaMetadataType0
        from ..models.related_object import RelatedObject

        d = dict(src_dict)
        status = JobBaseSchemaStatus(d.pop("status"))

        title = d.pop("title")

        type_ = JobBaseSchemaType(d.pop("type"))

        def _parse_action_context(data: object) -> ActionContextSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_context_type_1 = ActionContextSchema.from_dict(data)

                return action_context_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionContextSchema | None | Unset, data)

        action_context = _parse_action_context(d.pop("action_context", UNSET))

        def _parse_children_progress(
            data: object,
        ) -> JobBaseSchemaChildrenProgressType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                children_progress_type_0 = JobBaseSchemaChildrenProgressType0.from_dict(
                    data
                )

                return children_progress_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobBaseSchemaChildrenProgressType0 | None | Unset, data)

        children_progress = _parse_children_progress(d.pop("children_progress", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_custom_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_type = _parse_custom_type(d.pop("custom_type", UNSET))

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

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_has_children(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_children = _parse_has_children(d.pop("has_children", UNSET))

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

        def _parse_job_context(
            data: object,
        ) -> JobBaseSchemaJobContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_context_type_0 = JobBaseSchemaJobContextType0.from_dict(data)

                return job_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobBaseSchemaJobContextType0 | None | Unset, data)

        job_context = _parse_job_context(d.pop("job_context", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_metadata(data: object) -> JobBaseSchemaMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = JobBaseSchemaMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobBaseSchemaMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_id_type_0 = UUID(data)

                return object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_progress(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress = _parse_progress(d.pop("progress", UNSET))

        def _parse_progress_processed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress_processed = _parse_progress_processed(
            d.pop("progress_processed", UNSET)
        )

        def _parse_progress_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress_total = _parse_progress_total(d.pop("progress_total", UNSET))

        def _parse_related_objects(data: object) -> list[RelatedObject] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                related_objects_type_0 = []
                _related_objects_type_0 = data
                for related_objects_type_0_item_data in _related_objects_type_0:
                    related_objects_type_0_item = RelatedObject.from_dict(
                        related_objects_type_0_item_data
                    )

                    related_objects_type_0.append(related_objects_type_0_item)

                return related_objects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RelatedObject] | None | Unset, data)

        related_objects = _parse_related_objects(d.pop("related_objects", UNSET))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        job_base_schema = cls(
            status=status,
            title=title,
            type_=type_,
            action_context=action_context,
            children_progress=children_progress,
            completed_at=completed_at,
            custom_type=custom_type,
            date_created=date_created,
            date_modified=date_modified,
            error_message=error_message,
            has_children=has_children,
            id=id,
            job_context=job_context,
            message=message,
            metadata=metadata,
            object_id=object_id,
            object_type=object_type,
            parent_id=parent_id,
            priority=priority,
            progress=progress,
            progress_processed=progress_processed,
            progress_total=progress_total,
            related_objects=related_objects,
            started_at=started_at,
        )

        job_base_schema.additional_properties = d
        return job_base_schema

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
