from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_create_schema_status import JobCreateSchemaStatus
from ..models.job_create_schema_type import JobCreateSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_context_schema import ActionContextSchema
    from ..models.job_create_schema_children_progress import (
        JobCreateSchemaChildrenProgress,
    )
    from ..models.job_create_schema_job_context import JobCreateSchemaJobContext
    from ..models.job_create_schema_metadata import JobCreateSchemaMetadata
    from ..models.job_step import JobStep
    from ..models.related_object import RelatedObject


T = TypeVar("T", bound="JobCreateSchema")


@_attrs_define
class JobCreateSchema:
    """
    Attributes:
        status (JobCreateSchemaStatus):
        title (str):
        type_ (JobCreateSchemaType):
        action_context (ActionContextSchema | Unset):
        children_progress (JobCreateSchemaChildrenProgress | Unset):
        completed_at (datetime.datetime | Unset):
        created_by (UUID | Unset):
        custom_type (None | str | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        error_message (str | Unset):
        has_children (bool | Unset):
        id (None | Unset | UUID):
        job_context (JobCreateSchemaJobContext | Unset):
        message (str | Unset):
        metadata (JobCreateSchemaMetadata | Unset):
        object_id (None | Unset | UUID):
        object_type (None | str | Unset):
        parent_id (None | Unset | UUID):
        priority (int | Unset):
        progress (int | Unset):
        progress_processed (int | Unset):
        progress_total (int | Unset):
        related_objects (list[RelatedObject] | Unset):
        started_at (datetime.datetime | Unset):
        steps (list[JobStep] | Unset):
    """

    status: JobCreateSchemaStatus
    title: str
    type_: JobCreateSchemaType
    action_context: ActionContextSchema | Unset = UNSET
    children_progress: JobCreateSchemaChildrenProgress | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    custom_type: None | str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    error_message: str | Unset = UNSET
    has_children: bool | Unset = UNSET
    id: None | Unset | UUID = UNSET
    job_context: JobCreateSchemaJobContext | Unset = UNSET
    message: str | Unset = UNSET
    metadata: JobCreateSchemaMetadata | Unset = UNSET
    object_id: None | Unset | UUID = UNSET
    object_type: None | str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    priority: int | Unset = UNSET
    progress: int | Unset = UNSET
    progress_processed: int | Unset = UNSET
    progress_total: int | Unset = UNSET
    related_objects: list[RelatedObject] | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    steps: list[JobStep] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        title = self.title

        type_ = self.type_.value

        action_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_context, Unset):
            action_context = self.action_context.to_dict()

        children_progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.children_progress, Unset):
            children_progress = self.children_progress.to_dict()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        custom_type: None | str | Unset
        if isinstance(self.custom_type, Unset):
            custom_type = UNSET
        else:
            custom_type = self.custom_type

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        error_message = self.error_message

        has_children = self.has_children

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        job_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_context, Unset):
            job_context = self.job_context.to_dict()

        message = self.message

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

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

        priority = self.priority

        progress = self.progress

        progress_processed = self.progress_processed

        progress_total = self.progress_total

        related_objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.related_objects, Unset):
            related_objects = []
            for related_objects_item_data in self.related_objects:
                related_objects_item = related_objects_item_data.to_dict()
                related_objects.append(related_objects_item)

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

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
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
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
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_context_schema import ActionContextSchema
        from ..models.job_create_schema_children_progress import (
            JobCreateSchemaChildrenProgress,
        )
        from ..models.job_create_schema_job_context import JobCreateSchemaJobContext
        from ..models.job_create_schema_metadata import JobCreateSchemaMetadata
        from ..models.job_step import JobStep
        from ..models.related_object import RelatedObject

        d = dict(src_dict)
        status = JobCreateSchemaStatus(d.pop("status"))

        title = d.pop("title")

        type_ = JobCreateSchemaType(d.pop("type"))

        _action_context = d.pop("action_context", UNSET)
        action_context: ActionContextSchema | Unset
        if isinstance(_action_context, Unset):
            action_context = UNSET
        else:
            action_context = ActionContextSchema.from_dict(_action_context)

        _children_progress = d.pop("children_progress", UNSET)
        children_progress: JobCreateSchemaChildrenProgress | Unset
        if isinstance(_children_progress, Unset):
            children_progress = UNSET
        else:
            children_progress = JobCreateSchemaChildrenProgress.from_dict(
                _children_progress
            )

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = datetime.datetime.fromisoformat(_completed_at)

        _created_by = d.pop("created_by", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)

        def _parse_custom_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_type = _parse_custom_type(d.pop("custom_type", UNSET))

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

        error_message = d.pop("error_message", UNSET)

        has_children = d.pop("has_children", UNSET)

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

        _job_context = d.pop("job_context", UNSET)
        job_context: JobCreateSchemaJobContext | Unset
        if isinstance(_job_context, Unset):
            job_context = UNSET
        else:
            job_context = JobCreateSchemaJobContext.from_dict(_job_context)

        message = d.pop("message", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: JobCreateSchemaMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = JobCreateSchemaMetadata.from_dict(_metadata)

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

        priority = d.pop("priority", UNSET)

        progress = d.pop("progress", UNSET)

        progress_processed = d.pop("progress_processed", UNSET)

        progress_total = d.pop("progress_total", UNSET)

        _related_objects = d.pop("related_objects", UNSET)
        related_objects: list[RelatedObject] | Unset = UNSET
        if _related_objects is not UNSET:
            related_objects = []
            for related_objects_item_data in _related_objects:
                related_objects_item = RelatedObject.from_dict(
                    related_objects_item_data
                )

                related_objects.append(related_objects_item)

        _started_at = d.pop("started_at", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)

        _steps = d.pop("steps", UNSET)
        steps: list[JobStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = JobStep.from_dict(steps_item_data)

                steps.append(steps_item)

        job_create_schema = cls(
            status=status,
            title=title,
            type_=type_,
            action_context=action_context,
            children_progress=children_progress,
            completed_at=completed_at,
            created_by=created_by,
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
            steps=steps,
        )

        job_create_schema.additional_properties = d
        return job_create_schema

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
