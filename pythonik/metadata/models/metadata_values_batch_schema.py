from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_values_batch_schema_metadata_values import (
        MetadataValuesBatchSchemaMetadataValues,
    )


T = TypeVar("T", bound="MetadataValuesBatchSchema")


@_attrs_define
class MetadataValuesBatchSchema:
    """
    Attributes:
        metadata_values (MetadataValuesBatchSchemaMetadataValues):
        object_ids (list[UUID]):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        object_type (str | Unset):
    """

    metadata_values: MetadataValuesBatchSchemaMetadataValues
    object_ids: list[UUID]
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    object_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_values = self.metadata_values.to_dict()

        object_ids = []
        for object_ids_item_data in self.object_ids:
            object_ids_item = str(object_ids_item_data)
            object_ids.append(object_ids_item)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        object_type = self.object_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata_values": metadata_values,
                "object_ids": object_ids,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if object_type is not UNSET:
            field_dict["object_type"] = object_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_values_batch_schema_metadata_values import (
            MetadataValuesBatchSchemaMetadataValues,
        )

        d = dict(src_dict)
        metadata_values = MetadataValuesBatchSchemaMetadataValues.from_dict(
            d.pop("metadata_values")
        )

        object_ids = []
        _object_ids = d.pop("object_ids")
        for object_ids_item_data in _object_ids:
            object_ids_item = UUID(object_ids_item_data)

            object_ids.append(object_ids_item)

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

        object_type = d.pop("object_type", UNSET)

        metadata_values_batch_schema = cls(
            metadata_values=metadata_values,
            object_ids=object_ids,
            date_created=date_created,
            date_modified=date_modified,
            object_type=object_type,
        )

        metadata_values_batch_schema.additional_properties = d
        return metadata_values_batch_schema

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
