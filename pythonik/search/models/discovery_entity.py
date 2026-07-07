from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_entity_object_type import DiscoveryEntityObjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_entity_metadata import DiscoveryEntityMetadata


T = TypeVar("T", bound="DiscoveryEntity")


@_attrs_define
class DiscoveryEntity:
    """
    Attributes:
        object_id (UUID):
        object_type (DiscoveryEntityObjectType):
        title (str):
        user_id (str):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        id (UUID | Unset):
        metadata (DiscoveryEntityMetadata | Unset):
    """

    object_id: UUID
    object_type: DiscoveryEntityObjectType
    title: str
    user_id: str
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    metadata: DiscoveryEntityMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = str(self.object_id)

        object_type = self.object_type.value

        title = self.title

        user_id = self.user_id

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

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
        from ..models.discovery_entity_metadata import DiscoveryEntityMetadata

        d = dict(src_dict)
        object_id = UUID(d.pop("object_id"))

        object_type = DiscoveryEntityObjectType(d.pop("object_type"))

        title = d.pop("title")

        user_id = d.pop("user_id")

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

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _metadata = d.pop("metadata", UNSET)
        metadata: DiscoveryEntityMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DiscoveryEntityMetadata.from_dict(_metadata)

        discovery_entity = cls(
            object_id=object_id,
            object_type=object_type,
            title=title,
            user_id=user_id,
            date_created=date_created,
            date_modified=date_modified,
            id=id,
            metadata=metadata,
        )

        discovery_entity.additional_properties = d
        return discovery_entity

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
