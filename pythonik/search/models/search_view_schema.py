from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_view_field_type_schema import SearchViewFieldTypeSchema


T = TypeVar("T", bound="SearchViewSchema")


@_attrs_define
class SearchViewSchema:
    """
    Attributes:
        auto_resize_title_column (bool | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        id (UUID | Unset):
        name (str | Unset):
        view_fields (list[SearchViewFieldTypeSchema] | Unset):
    """

    auto_resize_title_column: bool | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    view_fields: list[SearchViewFieldTypeSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_resize_title_column = self.auto_resize_title_column

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        view_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.view_fields, Unset):
            view_fields = []
            for view_fields_item_data in self.view_fields:
                view_fields_item = view_fields_item_data.to_dict()
                view_fields.append(view_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_resize_title_column is not UNSET:
            field_dict["auto_resize_title_column"] = auto_resize_title_column
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if view_fields is not UNSET:
            field_dict["view_fields"] = view_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_view_field_type_schema import SearchViewFieldTypeSchema

        d = dict(src_dict)
        auto_resize_title_column = d.pop("auto_resize_title_column", UNSET)

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

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        _view_fields = d.pop("view_fields", UNSET)
        view_fields: list[SearchViewFieldTypeSchema] | Unset = UNSET
        if _view_fields is not UNSET:
            view_fields = []
            for view_fields_item_data in _view_fields:
                view_fields_item = SearchViewFieldTypeSchema.from_dict(
                    view_fields_item_data
                )

                view_fields.append(view_fields_item)

        search_view_schema = cls(
            auto_resize_title_column=auto_resize_title_column,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            id=id,
            name=name,
            view_fields=view_fields,
        )

        search_view_schema.additional_properties = d
        return search_view_schema

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
