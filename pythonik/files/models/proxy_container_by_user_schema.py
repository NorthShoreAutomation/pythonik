from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxyContainerByUserSchema")


@_attrs_define
class ProxyContainerByUserSchema:
    """
    Attributes:
        bit_profile (int | Unset):
        deep_fake (int | Unset):
        drm (str | Unset):
        fingerprint (str | Unset):
        height (int | Unset):
        id (UUID | Unset):
        original_proxy_url (str | Unset):
        pixel_density (float | Unset):
        proxy_id (UUID | Unset):
        sp_height (int | Unset):
        sp_width (int | Unset):
        strength (int | Unset):
        super_pixel_density (float | Unset):
        user_id (UUID | Unset):
        watermark (str | Unset):
        width (int | Unset):
    """

    bit_profile: int | Unset = UNSET
    deep_fake: int | Unset = UNSET
    drm: str | Unset = UNSET
    fingerprint: str | Unset = UNSET
    height: int | Unset = UNSET
    id: UUID | Unset = UNSET
    original_proxy_url: str | Unset = UNSET
    pixel_density: float | Unset = UNSET
    proxy_id: UUID | Unset = UNSET
    sp_height: int | Unset = UNSET
    sp_width: int | Unset = UNSET
    strength: int | Unset = UNSET
    super_pixel_density: float | Unset = UNSET
    user_id: UUID | Unset = UNSET
    watermark: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bit_profile = self.bit_profile

        deep_fake = self.deep_fake

        drm = self.drm

        fingerprint = self.fingerprint

        height = self.height

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        original_proxy_url = self.original_proxy_url

        pixel_density = self.pixel_density

        proxy_id: str | Unset = UNSET
        if not isinstance(self.proxy_id, Unset):
            proxy_id = str(self.proxy_id)

        sp_height = self.sp_height

        sp_width = self.sp_width

        strength = self.strength

        super_pixel_density = self.super_pixel_density

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        watermark = self.watermark

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bit_profile is not UNSET:
            field_dict["bit_profile"] = bit_profile
        if deep_fake is not UNSET:
            field_dict["deep_fake"] = deep_fake
        if drm is not UNSET:
            field_dict["drm"] = drm
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if original_proxy_url is not UNSET:
            field_dict["original_proxy_url"] = original_proxy_url
        if pixel_density is not UNSET:
            field_dict["pixel_density"] = pixel_density
        if proxy_id is not UNSET:
            field_dict["proxy_id"] = proxy_id
        if sp_height is not UNSET:
            field_dict["sp_height"] = sp_height
        if sp_width is not UNSET:
            field_dict["sp_width"] = sp_width
        if strength is not UNSET:
            field_dict["strength"] = strength
        if super_pixel_density is not UNSET:
            field_dict["super_pixel_density"] = super_pixel_density
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if watermark is not UNSET:
            field_dict["watermark"] = watermark
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bit_profile = d.pop("bit_profile", UNSET)

        deep_fake = d.pop("deep_fake", UNSET)

        drm = d.pop("drm", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        height = d.pop("height", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        original_proxy_url = d.pop("original_proxy_url", UNSET)

        pixel_density = d.pop("pixel_density", UNSET)

        _proxy_id = d.pop("proxy_id", UNSET)
        proxy_id: UUID | Unset
        if isinstance(_proxy_id, Unset):
            proxy_id = UNSET
        else:
            proxy_id = UUID(_proxy_id)

        sp_height = d.pop("sp_height", UNSET)

        sp_width = d.pop("sp_width", UNSET)

        strength = d.pop("strength", UNSET)

        super_pixel_density = d.pop("super_pixel_density", UNSET)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        watermark = d.pop("watermark", UNSET)

        width = d.pop("width", UNSET)

        proxy_container_by_user_schema = cls(
            bit_profile=bit_profile,
            deep_fake=deep_fake,
            drm=drm,
            fingerprint=fingerprint,
            height=height,
            id=id,
            original_proxy_url=original_proxy_url,
            pixel_density=pixel_density,
            proxy_id=proxy_id,
            sp_height=sp_height,
            sp_width=sp_width,
            strength=strength,
            super_pixel_density=super_pixel_density,
            user_id=user_id,
            watermark=watermark,
            width=width,
        )

        proxy_container_by_user_schema.additional_properties = d
        return proxy_container_by_user_schema

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
