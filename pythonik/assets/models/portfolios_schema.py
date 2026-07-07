from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio_schema import PortfolioSchema


T = TypeVar("T", bound="PortfoliosSchema")


@_attrs_define
class PortfoliosSchema:
    """
    Attributes:
        first_url (str | Unset):
        last_url (str | Unset):
        next_url (str | Unset):
        objects (list[PortfolioSchema] | Unset):
        page (int | Unset):
        pages (int | Unset):
        per_page (int | Unset):
        prev_url (str | Unset):
        scroll_id (str | Unset):
        search_after (list[Any] | Unset):
        total (int | Unset):
    """

    first_url: str | Unset = UNSET
    last_url: str | Unset = UNSET
    next_url: str | Unset = UNSET
    objects: list[PortfolioSchema] | Unset = UNSET
    page: int | Unset = UNSET
    pages: int | Unset = UNSET
    per_page: int | Unset = UNSET
    prev_url: str | Unset = UNSET
    scroll_id: str | Unset = UNSET
    search_after: list[Any] | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_url = self.first_url

        last_url = self.last_url

        next_url = self.next_url

        objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()
                objects.append(objects_item)

        page = self.page

        pages = self.pages

        per_page = self.per_page

        prev_url = self.prev_url

        scroll_id = self.scroll_id

        search_after: list[Any] | Unset = UNSET
        if not isinstance(self.search_after, Unset):
            search_after = self.search_after

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_url is not UNSET:
            field_dict["first_url"] = first_url
        if last_url is not UNSET:
            field_dict["last_url"] = last_url
        if next_url is not UNSET:
            field_dict["next_url"] = next_url
        if objects is not UNSET:
            field_dict["objects"] = objects
        if page is not UNSET:
            field_dict["page"] = page
        if pages is not UNSET:
            field_dict["pages"] = pages
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if prev_url is not UNSET:
            field_dict["prev_url"] = prev_url
        if scroll_id is not UNSET:
            field_dict["scroll_id"] = scroll_id
        if search_after is not UNSET:
            field_dict["search_after"] = search_after
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_schema import PortfolioSchema

        d = dict(src_dict)
        first_url = d.pop("first_url", UNSET)

        last_url = d.pop("last_url", UNSET)

        next_url = d.pop("next_url", UNSET)

        _objects = d.pop("objects", UNSET)
        objects: list[PortfolioSchema] | Unset = UNSET
        if _objects is not UNSET:
            objects = []
            for objects_item_data in _objects:
                objects_item = PortfolioSchema.from_dict(objects_item_data)

                objects.append(objects_item)

        page = d.pop("page", UNSET)

        pages = d.pop("pages", UNSET)

        per_page = d.pop("per_page", UNSET)

        prev_url = d.pop("prev_url", UNSET)

        scroll_id = d.pop("scroll_id", UNSET)

        search_after = cast(list[Any], d.pop("search_after", UNSET))

        total = d.pop("total", UNSET)

        portfolios_schema = cls(
            first_url=first_url,
            last_url=last_url,
            next_url=next_url,
            objects=objects,
            page=page,
            pages=pages,
            per_page=per_page,
            prev_url=prev_url,
            scroll_id=scroll_id,
            search_after=search_after,
            total=total,
        )

        portfolios_schema.additional_properties = d
        return portfolios_schema

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
