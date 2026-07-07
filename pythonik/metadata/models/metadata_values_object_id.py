from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_values_object_id_metadata_values import (
        MetadataValuesObjectIdMetadataValues,
    )


T = TypeVar("T", bound="MetadataValuesObjectId")


@_attrs_define
class MetadataValuesObjectId:
    """
    Attributes:
        id (UUID):
        metadata_values (MetadataValuesObjectIdMetadataValues):
    """

    id: UUID
    metadata_values: MetadataValuesObjectIdMetadataValues
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        metadata_values = self.metadata_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "metadata_values": metadata_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_values_object_id_metadata_values import (
            MetadataValuesObjectIdMetadataValues,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        metadata_values = MetadataValuesObjectIdMetadataValues.from_dict(
            d.pop("metadata_values")
        )

        metadata_values_object_id = cls(
            id=id,
            metadata_values=metadata_values,
        )

        metadata_values_object_id.additional_properties = d
        return metadata_values_object_id

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
