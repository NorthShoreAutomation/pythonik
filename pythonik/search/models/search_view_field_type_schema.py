from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_view_field_type_width import SearchViewFieldTypeWidth


T = TypeVar("T", bound="SearchViewFieldTypeSchema")


@_attrs_define
class SearchViewFieldTypeSchema:
    """
    Attributes:
        facetable (bool | Unset):
        label (str | Unset):
        name (str | Unset):
        origin_field_name (str | Unset):
        sortable (bool | Unset):
        type_ (str | Unset):
        width (SearchViewFieldTypeWidth | Unset):
    """

    facetable: bool | Unset = UNSET
    label: str | Unset = UNSET
    name: str | Unset = UNSET
    origin_field_name: str | Unset = UNSET
    sortable: bool | Unset = UNSET
    type_: str | Unset = UNSET
    width: SearchViewFieldTypeWidth | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facetable = self.facetable

        label = self.label

        name = self.name

        origin_field_name = self.origin_field_name

        sortable = self.sortable

        type_ = self.type_

        width: dict[str, Any] | Unset = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if facetable is not UNSET:
            field_dict["facetable"] = facetable
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if origin_field_name is not UNSET:
            field_dict["origin_field_name"] = origin_field_name
        if sortable is not UNSET:
            field_dict["sortable"] = sortable
        if type_ is not UNSET:
            field_dict["type"] = type_
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_view_field_type_width import SearchViewFieldTypeWidth

        d = dict(src_dict)
        facetable = d.pop("facetable", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        origin_field_name = d.pop("origin_field_name", UNSET)

        sortable = d.pop("sortable", UNSET)

        type_ = d.pop("type", UNSET)

        _width = d.pop("width", UNSET)
        width: SearchViewFieldTypeWidth | Unset
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = SearchViewFieldTypeWidth.from_dict(_width)

        search_view_field_type_schema = cls(
            facetable=facetable,
            label=label,
            name=name,
            origin_field_name=origin_field_name,
            sortable=sortable,
            type_=type_,
            width=width,
        )

        search_view_field_type_schema.additional_properties = d
        return search_view_field_type_schema

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
