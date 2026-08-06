from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxyContainerByUserSchema")


@_attrs_define
class ProxyContainerByUserSchema:
    """
    Attributes:
        bit_profile (int | None | Unset):
        deep_fake (int | None | Unset):
        drm (None | str | Unset):
        fingerprint (None | str | Unset):
        height (int | None | Unset):
        id (None | Unset | UUID):
        original_proxy_url (None | str | Unset):
        pixel_density (float | None | Unset):
        proxy_id (None | Unset | UUID):
        sp_height (int | None | Unset):
        sp_width (int | None | Unset):
        strength (int | None | Unset):
        super_pixel_density (float | None | Unset):
        user_id (None | Unset | UUID):
        watermark (None | str | Unset):
        width (int | None | Unset):
    """

    bit_profile: int | None | Unset = UNSET
    deep_fake: int | None | Unset = UNSET
    drm: None | str | Unset = UNSET
    fingerprint: None | str | Unset = UNSET
    height: int | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    original_proxy_url: None | str | Unset = UNSET
    pixel_density: float | None | Unset = UNSET
    proxy_id: None | Unset | UUID = UNSET
    sp_height: int | None | Unset = UNSET
    sp_width: int | None | Unset = UNSET
    strength: int | None | Unset = UNSET
    super_pixel_density: float | None | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    watermark: None | str | Unset = UNSET
    width: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bit_profile: int | None | Unset
        if isinstance(self.bit_profile, Unset):
            bit_profile = UNSET
        else:
            bit_profile = self.bit_profile

        deep_fake: int | None | Unset
        if isinstance(self.deep_fake, Unset):
            deep_fake = UNSET
        else:
            deep_fake = self.deep_fake

        drm: None | str | Unset
        if isinstance(self.drm, Unset):
            drm = UNSET
        else:
            drm = self.drm

        fingerprint: None | str | Unset
        if isinstance(self.fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = self.fingerprint

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        original_proxy_url: None | str | Unset
        if isinstance(self.original_proxy_url, Unset):
            original_proxy_url = UNSET
        else:
            original_proxy_url = self.original_proxy_url

        pixel_density: float | None | Unset
        if isinstance(self.pixel_density, Unset):
            pixel_density = UNSET
        else:
            pixel_density = self.pixel_density

        proxy_id: None | str | Unset
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        elif isinstance(self.proxy_id, UUID):
            proxy_id = str(self.proxy_id)
        else:
            proxy_id = self.proxy_id

        sp_height: int | None | Unset
        if isinstance(self.sp_height, Unset):
            sp_height = UNSET
        else:
            sp_height = self.sp_height

        sp_width: int | None | Unset
        if isinstance(self.sp_width, Unset):
            sp_width = UNSET
        else:
            sp_width = self.sp_width

        strength: int | None | Unset
        if isinstance(self.strength, Unset):
            strength = UNSET
        else:
            strength = self.strength

        super_pixel_density: float | None | Unset
        if isinstance(self.super_pixel_density, Unset):
            super_pixel_density = UNSET
        else:
            super_pixel_density = self.super_pixel_density

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        watermark: None | str | Unset
        if isinstance(self.watermark, Unset):
            watermark = UNSET
        else:
            watermark = self.watermark

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
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

        def _parse_bit_profile(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bit_profile = _parse_bit_profile(d.pop("bit_profile", UNSET))

        def _parse_deep_fake(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deep_fake = _parse_deep_fake(d.pop("deep_fake", UNSET))

        def _parse_drm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drm = _parse_drm(d.pop("drm", UNSET))

        def _parse_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

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

        def _parse_original_proxy_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_proxy_url = _parse_original_proxy_url(
            d.pop("original_proxy_url", UNSET)
        )

        def _parse_pixel_density(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pixel_density = _parse_pixel_density(d.pop("pixel_density", UNSET))

        def _parse_proxy_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_id_type_0 = UUID(data)

                return proxy_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_id = _parse_proxy_id(d.pop("proxy_id", UNSET))

        def _parse_sp_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sp_height = _parse_sp_height(d.pop("sp_height", UNSET))

        def _parse_sp_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sp_width = _parse_sp_width(d.pop("sp_width", UNSET))

        def _parse_strength(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        strength = _parse_strength(d.pop("strength", UNSET))

        def _parse_super_pixel_density(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        super_pixel_density = _parse_super_pixel_density(
            d.pop("super_pixel_density", UNSET)
        )

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_watermark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        watermark = _parse_watermark(d.pop("watermark", UNSET))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

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
