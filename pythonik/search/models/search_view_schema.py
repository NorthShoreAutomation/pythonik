from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
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
        auto_resize_title_column (bool | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        description (None | str | Unset):
        id (None | Unset | UUID):
        name (None | str | Unset):
        view_fields (list[SearchViewFieldTypeSchema] | None | Unset):
    """

    auto_resize_title_column: bool | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    view_fields: list[SearchViewFieldTypeSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_resize_title_column: bool | None | Unset
        if isinstance(self.auto_resize_title_column, Unset):
            auto_resize_title_column = UNSET
        else:
            auto_resize_title_column = self.auto_resize_title_column

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        view_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.view_fields, Unset):
            view_fields = UNSET
        elif isinstance(self.view_fields, list):
            view_fields = []
            for view_fields_type_0_item_data in self.view_fields:
                view_fields_type_0_item = view_fields_type_0_item_data.to_dict()
                view_fields.append(view_fields_type_0_item)

        else:
            view_fields = self.view_fields

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

        def _parse_auto_resize_title_column(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_resize_title_column = _parse_auto_resize_title_column(
            d.pop("auto_resize_title_column", UNSET)
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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_view_fields(
            data: object,
        ) -> list[SearchViewFieldTypeSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                view_fields_type_0 = []
                _view_fields_type_0 = data
                for view_fields_type_0_item_data in _view_fields_type_0:
                    view_fields_type_0_item = SearchViewFieldTypeSchema.from_dict(
                        view_fields_type_0_item_data
                    )

                    view_fields_type_0.append(view_fields_type_0_item)

                return view_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SearchViewFieldTypeSchema] | None | Unset, data)

        view_fields = _parse_view_fields(d.pop("view_fields", UNSET))

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
