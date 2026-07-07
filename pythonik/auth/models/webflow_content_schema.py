from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebflowContentSchema")


@_attrs_define
class WebflowContentSchema:
    """
    Attributes:
        slug (str):
        caption (str | Unset):
        category (str | Unset):
        image (str | Unset):
        name (str | Unset):
    """

    slug: str
    caption: str | Unset = UNSET
    category: str | Unset = UNSET
    image: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        caption = self.caption

        category = self.category

        image = self.image

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
            }
        )
        if caption is not UNSET:
            field_dict["caption"] = caption
        if category is not UNSET:
            field_dict["category"] = category
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        caption = d.pop("caption", UNSET)

        category = d.pop("category", UNSET)

        image = d.pop("image", UNSET)

        name = d.pop("name", UNSET)

        webflow_content_schema = cls(
            slug=slug,
            caption=caption,
            category=category,
            image=image,
            name=name,
        )

        webflow_content_schema.additional_properties = d
        return webflow_content_schema

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
