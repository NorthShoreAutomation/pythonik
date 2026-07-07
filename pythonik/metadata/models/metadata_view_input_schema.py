from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_view_field_schema import MetadataViewFieldSchema


T = TypeVar("T", bound="MetadataViewInputSchema")


@_attrs_define
class MetadataViewInputSchema:
    """
    Attributes:
        name (str):
        view_fields (list[MetadataViewFieldSchema]):
        description (None | str | Unset):
        id (UUID | Unset):
    """

    name: str
    view_fields: list[MetadataViewFieldSchema]
    description: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        view_fields = []
        for view_fields_item_data in self.view_fields:
            view_fields_item = view_fields_item_data.to_dict()
            view_fields.append(view_fields_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "view_fields": view_fields,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_view_field_schema import MetadataViewFieldSchema

        d = dict(src_dict)
        name = d.pop("name")

        view_fields = []
        _view_fields = d.pop("view_fields")
        for view_fields_item_data in _view_fields:
            view_fields_item = MetadataViewFieldSchema.from_dict(view_fields_item_data)

            view_fields.append(view_fields_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        metadata_view_input_schema = cls(
            name=name,
            view_fields=view_fields,
            description=description,
            id=id,
        )

        metadata_view_input_schema.additional_properties = d
        return metadata_view_input_schema

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
