from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        facetable (bool | None | Unset):
        label (None | str | Unset):
        name (None | str | Unset):
        origin_field_name (None | str | Unset):
        sortable (bool | None | Unset):
        type_ (None | str | Unset):
        width (None | SearchViewFieldTypeWidth | Unset):
    """

    facetable: bool | None | Unset = UNSET
    label: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    origin_field_name: None | str | Unset = UNSET
    sortable: bool | None | Unset = UNSET
    type_: None | str | Unset = UNSET
    width: None | SearchViewFieldTypeWidth | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_view_field_type_width import SearchViewFieldTypeWidth

        facetable: bool | None | Unset
        if isinstance(self.facetable, Unset):
            facetable = UNSET
        else:
            facetable = self.facetable

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        origin_field_name: None | str | Unset
        if isinstance(self.origin_field_name, Unset):
            origin_field_name = UNSET
        else:
            origin_field_name = self.origin_field_name

        sortable: bool | None | Unset
        if isinstance(self.sortable, Unset):
            sortable = UNSET
        else:
            sortable = self.sortable

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        width: dict[str, Any] | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        elif isinstance(self.width, SearchViewFieldTypeWidth):
            width = self.width.to_dict()
        else:
            width = self.width

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

        def _parse_facetable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        facetable = _parse_facetable(d.pop("facetable", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_origin_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_field_name = _parse_origin_field_name(d.pop("origin_field_name", UNSET))

        def _parse_sortable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sortable = _parse_sortable(d.pop("sortable", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_width(data: object) -> None | SearchViewFieldTypeWidth | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                width_type_1 = SearchViewFieldTypeWidth.from_dict(data)

                return width_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchViewFieldTypeWidth | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

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
