from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sequence_item_schema_object_type import SequenceItemSchemaObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SequenceItemSchema")


@_attrs_define
class SequenceItemSchema:
    """
    Attributes:
        object_id (UUID):
        object_type (SequenceItemSchemaObjectType):
        id (UUID | Unset):
        position (int | Unset): Position of the item in the sequence.If not provided, the item will be appended to the
            end of the sequence
        version_id (UUID | Unset):
    """

    object_id: UUID
    object_type: SequenceItemSchemaObjectType
    id: UUID | Unset = UNSET
    position: int | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = str(self.object_id)

        object_type = self.object_type.value

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        position = self.position

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_id": object_id,
                "object_type": object_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if position is not UNSET:
            field_dict["position"] = position
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = UUID(d.pop("object_id"))

        object_type = SequenceItemSchemaObjectType(d.pop("object_type"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        position = d.pop("position", UNSET)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        sequence_item_schema = cls(
            object_id=object_id,
            object_type=object_type,
            id=id,
            position=position,
            version_id=version_id,
        )

        sequence_item_schema.additional_properties = d
        return sequence_item_schema

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
