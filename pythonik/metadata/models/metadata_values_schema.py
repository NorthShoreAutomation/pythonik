from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_values_schema_metadata_values import (
        MetadataValuesSchemaMetadataValues,
    )


T = TypeVar("T", bound="MetadataValuesSchema")


@_attrs_define
class MetadataValuesSchema:
    """
    Attributes:
        metadata_values (MetadataValuesSchemaMetadataValues):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        job_id (UUID | Unset):
        object_id (UUID | Unset):
        object_type (str | Unset):
        version_id (UUID | Unset):
    """

    metadata_values: MetadataValuesSchemaMetadataValues
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    job_id: UUID | Unset = UNSET
    object_id: UUID | Unset = UNSET
    object_type: str | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_values = self.metadata_values.to_dict()

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

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        object_id: str | Unset = UNSET
        if not isinstance(self.object_id, Unset):
            object_id = str(self.object_id)

        object_type = self.object_type

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata_values": metadata_values,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_values_schema_metadata_values import (
            MetadataValuesSchemaMetadataValues,
        )

        d = dict(src_dict)
        metadata_values = MetadataValuesSchemaMetadataValues.from_dict(
            d.pop("metadata_values")
        )

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

        _job_id = d.pop("job_id", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        _object_id = d.pop("object_id", UNSET)
        object_id: UUID | Unset
        if isinstance(_object_id, Unset):
            object_id = UNSET
        else:
            object_id = UUID(_object_id)

        object_type = d.pop("object_type", UNSET)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        metadata_values_schema = cls(
            metadata_values=metadata_values,
            date_created=date_created,
            date_modified=date_modified,
            job_id=job_id,
            object_id=object_id,
            object_type=object_type,
            version_id=version_id,
        )

        metadata_values_schema.additional_properties = d
        return metadata_values_schema

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
