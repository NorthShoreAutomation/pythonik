from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonInstancesQueryParamsSchema")


@_attrs_define
class PersonInstancesQueryParamsSchema:
    """
    Attributes:
        include_admin_details (bool | Unset):  Default: True.
        page (int | None | Unset): Which page number to fetch Default: 1.
        per_page (int | None | Unset): The number of items for each page Default: 10.
        scroll (bool | Unset):
        scroll_id (UUID | Unset):
        sort (str | Unset): A comma separated list of fieldnames with order (asc/desc)
        use_instance_as_main_face (bool | Unset):  Default: True.
    """

    include_admin_details: bool | Unset = True
    page: int | None | Unset = 1
    per_page: int | None | Unset = 10
    scroll: bool | Unset = UNSET
    scroll_id: UUID | Unset = UNSET
    sort: str | Unset = UNSET
    use_instance_as_main_face: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_admin_details = self.include_admin_details

        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        per_page: int | None | Unset
        if isinstance(self.per_page, Unset):
            per_page = UNSET
        else:
            per_page = self.per_page

        scroll = self.scroll

        scroll_id: str | Unset = UNSET
        if not isinstance(self.scroll_id, Unset):
            scroll_id = str(self.scroll_id)

        sort = self.sort

        use_instance_as_main_face = self.use_instance_as_main_face

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_admin_details is not UNSET:
            field_dict["include_admin_details"] = include_admin_details
        if page is not UNSET:
            field_dict["page"] = page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if scroll is not UNSET:
            field_dict["scroll"] = scroll
        if scroll_id is not UNSET:
            field_dict["scroll_id"] = scroll_id
        if sort is not UNSET:
            field_dict["sort"] = sort
        if use_instance_as_main_face is not UNSET:
            field_dict["use_instance_as_main_face"] = use_instance_as_main_face

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_admin_details = d.pop("include_admin_details", UNSET)

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        def _parse_per_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        per_page = _parse_per_page(d.pop("per_page", UNSET))

        scroll = d.pop("scroll", UNSET)

        _scroll_id = d.pop("scroll_id", UNSET)
        scroll_id: UUID | Unset
        if isinstance(_scroll_id, Unset):
            scroll_id = UNSET
        else:
            scroll_id = UUID(_scroll_id)

        sort = d.pop("sort", UNSET)

        use_instance_as_main_face = d.pop("use_instance_as_main_face", UNSET)

        person_instances_query_params_schema = cls(
            include_admin_details=include_admin_details,
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            use_instance_as_main_face=use_instance_as_main_face,
        )

        person_instances_query_params_schema.additional_properties = d
        return person_instances_query_params_schema

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
