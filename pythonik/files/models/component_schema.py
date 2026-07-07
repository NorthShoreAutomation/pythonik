from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_schema_type import ComponentSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_schema_metadata import ComponentSchemaMetadata


T = TypeVar("T", bound="ComponentSchema")


@_attrs_define
class ComponentSchema:
    """
    Attributes:
        name (str):
        type_ (ComponentSchemaType):
        id (UUID | Unset):
        metadata (ComponentSchemaMetadata | Unset): Sequence cannot have more than 10000. Excess values will be stripped
    """

    name: str
    type_: ComponentSchemaType
    id: UUID | Unset = UNSET
    metadata: ComponentSchemaMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

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
                "name": name,
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.component_schema_metadata import ComponentSchemaMetadata

        d = dict(src_dict)
        name = d.pop("name")

        type_ = ComponentSchemaType(d.pop("type"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _metadata = d.pop("metadata", UNSET)
        metadata: ComponentSchemaMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ComponentSchemaMetadata.from_dict(_metadata)

        component_schema = cls(
            name=name,
            type_=type_,
            id=id,
            metadata=metadata,
        )

        component_schema.additional_properties = d
        return component_schema

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
