from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.share_token_schema_drm import ShareTokenSchemaDrm
from ..models.share_token_schema_watermark import ShareTokenSchemaWatermark

T = TypeVar("T", bound="ShareTokenSchema")


@_attrs_define
class ShareTokenSchema:
    """
    Attributes:
        app_id (str):
        drm (ShareTokenSchemaDrm): DRM information for the share token, if applicable
        email (str):
        expires (datetime.datetime):
        is_internal_user (bool):
        object_id (str):
        object_type (str):
        roles (list[str]):
        share_id (str):
        share_user_id (str):
        system_domain_id (str):
        token (str):
        user_id (str):
        watermark (ShareTokenSchemaWatermark): Watermark information for the share token, if applicable
    """

    app_id: str
    drm: ShareTokenSchemaDrm
    email: str
    expires: datetime.datetime
    is_internal_user: bool
    object_id: str
    object_type: str
    roles: list[str]
    share_id: str
    share_user_id: str
    system_domain_id: str
    token: str
    user_id: str
    watermark: ShareTokenSchemaWatermark
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        drm = self.drm.value

        email = self.email

        expires = self.expires.isoformat()

        is_internal_user = self.is_internal_user

        object_id = self.object_id

        object_type = self.object_type

        roles = self.roles

        share_id = self.share_id

        share_user_id = self.share_user_id

        system_domain_id = self.system_domain_id

        token = self.token

        user_id = self.user_id

        watermark = self.watermark.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "drm": drm,
                "email": email,
                "expires": expires,
                "is_internal_user": is_internal_user,
                "object_id": object_id,
                "object_type": object_type,
                "roles": roles,
                "share_id": share_id,
                "share_user_id": share_user_id,
                "system_domain_id": system_domain_id,
                "token": token,
                "user_id": user_id,
                "watermark": watermark,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id")

        drm = ShareTokenSchemaDrm(d.pop("drm"))

        email = d.pop("email")

        expires = datetime.datetime.fromisoformat(d.pop("expires"))

        is_internal_user = d.pop("is_internal_user")

        object_id = d.pop("object_id")

        object_type = d.pop("object_type")

        roles = cast(list[str], d.pop("roles"))

        share_id = d.pop("share_id")

        share_user_id = d.pop("share_user_id")

        system_domain_id = d.pop("system_domain_id")

        token = d.pop("token")

        user_id = d.pop("user_id")

        watermark = ShareTokenSchemaWatermark(d.pop("watermark"))

        share_token_schema = cls(
            app_id=app_id,
            drm=drm,
            email=email,
            expires=expires,
            is_internal_user=is_internal_user,
            object_id=object_id,
            object_type=object_type,
            roles=roles,
            share_id=share_id,
            share_user_id=share_user_id,
            system_domain_id=system_domain_id,
            token=token,
            user_id=user_id,
            watermark=watermark,
        )

        share_token_schema.additional_properties = d
        return share_token_schema

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
