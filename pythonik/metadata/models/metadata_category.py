from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_view import MetadataView


T = TypeVar("T", bound="MetadataCategory")


@_attrs_define
class MetadataCategory:
    """
    Attributes:
        label (str):
        name (str):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        object_type (None | str | Unset):
        view_ids (list[str] | None | Unset):
        views (list[MetadataView] | None | Unset):
    """

    label: str
    name: str
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    object_type: None | str | Unset = UNSET
    view_ids: list[str] | None | Unset = UNSET
    views: list[MetadataView] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        name = self.name

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

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        view_ids: list[str] | None | Unset
        if isinstance(self.view_ids, Unset):
            view_ids = UNSET
        elif isinstance(self.view_ids, list):
            view_ids = self.view_ids

        else:
            view_ids = self.view_ids

        views: list[dict[str, Any]] | None | Unset
        if isinstance(self.views, Unset):
            views = UNSET
        elif isinstance(self.views, list):
            views = []
            for views_type_0_item_data in self.views:
                views_type_0_item = views_type_0_item_data.to_dict()
                views.append(views_type_0_item)

        else:
            views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "name": name,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if view_ids is not UNSET:
            field_dict["view_ids"] = view_ids
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_view import MetadataView

        d = dict(src_dict)
        label = d.pop("label")

        name = d.pop("name")

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

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_view_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                view_ids_type_0 = cast(list[str], data)

                return view_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        view_ids = _parse_view_ids(d.pop("view_ids", UNSET))

        def _parse_views(data: object) -> list[MetadataView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                views_type_0 = []
                _views_type_0 = data
                for views_type_0_item_data in _views_type_0:
                    views_type_0_item = MetadataView.from_dict(views_type_0_item_data)

                    views_type_0.append(views_type_0_item)

                return views_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MetadataView] | None | Unset, data)

        views = _parse_views(d.pop("views", UNSET))

        metadata_category = cls(
            label=label,
            name=name,
            date_created=date_created,
            date_modified=date_modified,
            object_type=object_type,
            view_ids=view_ids,
            views=views,
        )

        metadata_category.additional_properties = d
        return metadata_category

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
