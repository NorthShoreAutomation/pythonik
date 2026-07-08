from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_schema_type import ComponentSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_schema_metadata_type_0 import ComponentSchemaMetadataType0


T = TypeVar("T", bound="ComponentSchema")


@_attrs_define
class ComponentSchema:
    """
    Attributes:
        name (str):
        type_ (ComponentSchemaType):
        id (None | Unset | UUID):
        metadata (ComponentSchemaMetadataType0 | None | Unset): Sequence cannot have more than 10000. Excess values will
            be stripped
    """

    name: str
    type_: ComponentSchemaType
    id: None | Unset | UUID = UNSET
    metadata: ComponentSchemaMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.component_schema_metadata_type_0 import (
            ComponentSchemaMetadataType0,
        )

        name = self.name

        type_ = self.type_.value

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
        elif isinstance(self.metadata, ComponentSchemaMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

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
        from ..models.component_schema_metadata_type_0 import (
            ComponentSchemaMetadataType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = ComponentSchemaType(d.pop("type"))

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
        ) -> ComponentSchemaMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ComponentSchemaMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ComponentSchemaMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

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
