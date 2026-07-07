from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_view import MetadataView


T = TypeVar("T", bound="MetadataCategorySchema")


@_attrs_define
class MetadataCategorySchema:
    """
    Attributes:
        label (str):
        name (str):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        object_type (str | Unset):
        view_ids (list[str] | Unset):
        views (list[MetadataView] | Unset):
    """

    label: str
    name: str
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    object_type: str | Unset = UNSET
    view_ids: list[str] | Unset = UNSET
    views: list[MetadataView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        name = self.name

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        object_type = self.object_type

        view_ids: list[str] | Unset = UNSET
        if not isinstance(self.view_ids, Unset):
            view_ids = self.view_ids

        views: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.views, Unset):
            views = []
            for views_item_data in self.views:
                views_item = views_item_data.to_dict()
                views.append(views_item)

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

        object_type = d.pop("object_type", UNSET)

        view_ids = cast(list[str], d.pop("view_ids", UNSET))

        _views = d.pop("views", UNSET)
        views: list[MetadataView] | Unset = UNSET
        if _views is not UNSET:
            views = []
            for views_item_data in _views:
                views_item = MetadataView.from_dict(views_item_data)

                views.append(views_item)

        metadata_category_schema = cls(
            label=label,
            name=name,
            date_created=date_created,
            date_modified=date_modified,
            object_type=object_type,
            view_ids=view_ids,
            views=views,
        )

        metadata_category_schema.additional_properties = d
        return metadata_category_schema

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
