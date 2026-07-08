from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_entity_schema_object_type import DiscoveryEntitySchemaObjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_entity_schema_metadata_type_0 import (
        DiscoveryEntitySchemaMetadataType0,
    )


T = TypeVar("T", bound="DiscoveryEntitySchema")


@_attrs_define
class DiscoveryEntitySchema:
    """
    Attributes:
        object_id (UUID):
        object_type (DiscoveryEntitySchemaObjectType):
        title (str):
        user_id (str):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        id (None | Unset | UUID):
        metadata (DiscoveryEntitySchemaMetadataType0 | None | Unset):
    """

    object_id: UUID
    object_type: DiscoveryEntitySchemaObjectType
    title: str
    user_id: str
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    metadata: DiscoveryEntitySchemaMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.discovery_entity_schema_metadata_type_0 import (
            DiscoveryEntitySchemaMetadataType0,
        )

        object_id = str(self.object_id)

        object_type = self.object_type.value

        title = self.title

        user_id = self.user_id

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

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DiscoveryEntitySchemaMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_id": object_id,
                "object_type": object_type,
                "title": title,
                "user_id": user_id,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_entity_schema_metadata_type_0 import (
            DiscoveryEntitySchemaMetadataType0,
        )

        d = dict(src_dict)
        object_id = UUID(d.pop("object_id"))

        object_type = DiscoveryEntitySchemaObjectType(d.pop("object_type"))

        title = d.pop("title")

        user_id = d.pop("user_id")

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

        def _parse_metadata(
            data: object,
        ) -> DiscoveryEntitySchemaMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DiscoveryEntitySchemaMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DiscoveryEntitySchemaMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        discovery_entity_schema = cls(
            object_id=object_id,
            object_type=object_type,
            title=title,
            user_id=user_id,
            date_created=date_created,
            date_modified=date_modified,
            id=id,
            metadata=metadata,
        )

        discovery_entity_schema.additional_properties = d
        return discovery_entity_schema

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
