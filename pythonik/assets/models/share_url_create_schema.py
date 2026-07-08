from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.share_url_create_schema_drm_type_1 import ShareURLCreateSchemaDrmType1
    from ..models.share_url_create_schema_watermark_type_1 import (
        ShareURLCreateSchemaWatermarkType1,
    )


T = TypeVar("T", bound="ShareURLCreateSchema")


@_attrs_define
class ShareURLCreateSchema:
    """
    Attributes:
        allow_approving_comments (bool):
        allow_comments (bool):
        allow_download (bool):
        allow_setting_approve_status (bool):
        allow_custom_actions (bool | None | Unset):
        allow_download_proxy (bool | None | Unset):
        allow_sync (bool | None | Unset):
        allow_upload (bool | None | Unset):
        allow_user_search_for_mentions (bool | None | Unset):
        allow_view_transcriptions (bool | None | Unset):
        allow_view_versions (bool | None | Unset):
        automatic_approval_share (bool | None | Unset):
        drm (None | ShareURLCreateSchemaDrmType1 | Unset):
        expires (datetime.datetime | None | Unset):
        is_approval (bool | None | Unset):
        metadata_views (list[str] | None | Unset):
        object_id (None | str | Unset):
        object_type (None | str | Unset):
        owner_id (None | str | Unset):
        password (None | str | Unset):
        review_experience_public_beta (bool | None | Unset):
        show_existing_comments (bool | None | Unset):
        show_watermark (bool | None | Unset):
        system_domain_id (None | str | Unset):
        title (None | str | Unset):
        upload_storage_id (None | Unset | UUID):
        watermark (None | ShareURLCreateSchemaWatermarkType1 | Unset):
    """

    allow_approving_comments: bool
    allow_comments: bool
    allow_download: bool
    allow_setting_approve_status: bool
    allow_custom_actions: bool | None | Unset = UNSET
    allow_download_proxy: bool | None | Unset = UNSET
    allow_sync: bool | None | Unset = UNSET
    allow_upload: bool | None | Unset = UNSET
    allow_user_search_for_mentions: bool | None | Unset = UNSET
    allow_view_transcriptions: bool | None | Unset = UNSET
    allow_view_versions: bool | None | Unset = UNSET
    automatic_approval_share: bool | None | Unset = UNSET
    drm: None | ShareURLCreateSchemaDrmType1 | Unset = UNSET
    expires: datetime.datetime | None | Unset = UNSET
    is_approval: bool | None | Unset = UNSET
    metadata_views: list[str] | None | Unset = UNSET
    object_id: None | str | Unset = UNSET
    object_type: None | str | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    review_experience_public_beta: bool | None | Unset = UNSET
    show_existing_comments: bool | None | Unset = UNSET
    show_watermark: bool | None | Unset = UNSET
    system_domain_id: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    upload_storage_id: None | Unset | UUID = UNSET
    watermark: None | ShareURLCreateSchemaWatermarkType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.share_url_create_schema_drm_type_1 import (
            ShareURLCreateSchemaDrmType1,
        )
        from ..models.share_url_create_schema_watermark_type_1 import (
            ShareURLCreateSchemaWatermarkType1,
        )

        allow_approving_comments = self.allow_approving_comments

        allow_comments = self.allow_comments

        allow_download = self.allow_download

        allow_setting_approve_status = self.allow_setting_approve_status

        allow_custom_actions: bool | None | Unset
        if isinstance(self.allow_custom_actions, Unset):
            allow_custom_actions = UNSET
        else:
            allow_custom_actions = self.allow_custom_actions

        allow_download_proxy: bool | None | Unset
        if isinstance(self.allow_download_proxy, Unset):
            allow_download_proxy = UNSET
        else:
            allow_download_proxy = self.allow_download_proxy

        allow_sync: bool | None | Unset
        if isinstance(self.allow_sync, Unset):
            allow_sync = UNSET
        else:
            allow_sync = self.allow_sync

        allow_upload: bool | None | Unset
        if isinstance(self.allow_upload, Unset):
            allow_upload = UNSET
        else:
            allow_upload = self.allow_upload

        allow_user_search_for_mentions: bool | None | Unset
        if isinstance(self.allow_user_search_for_mentions, Unset):
            allow_user_search_for_mentions = UNSET
        else:
            allow_user_search_for_mentions = self.allow_user_search_for_mentions

        allow_view_transcriptions: bool | None | Unset
        if isinstance(self.allow_view_transcriptions, Unset):
            allow_view_transcriptions = UNSET
        else:
            allow_view_transcriptions = self.allow_view_transcriptions

        allow_view_versions: bool | None | Unset
        if isinstance(self.allow_view_versions, Unset):
            allow_view_versions = UNSET
        else:
            allow_view_versions = self.allow_view_versions

        automatic_approval_share: bool | None | Unset
        if isinstance(self.automatic_approval_share, Unset):
            automatic_approval_share = UNSET
        else:
            automatic_approval_share = self.automatic_approval_share

        drm: dict[str, Any] | None | Unset
        if isinstance(self.drm, Unset):
            drm = UNSET
        elif isinstance(self.drm, ShareURLCreateSchemaDrmType1):
            drm = self.drm.to_dict()
        else:
            drm = self.drm

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        is_approval: bool | None | Unset
        if isinstance(self.is_approval, Unset):
            is_approval = UNSET
        else:
            is_approval = self.is_approval

        metadata_views: list[str] | None | Unset
        if isinstance(self.metadata_views, Unset):
            metadata_views = UNSET
        elif isinstance(self.metadata_views, list):
            metadata_views = self.metadata_views

        else:
            metadata_views = self.metadata_views

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        else:
            object_id = self.object_id

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        review_experience_public_beta: bool | None | Unset
        if isinstance(self.review_experience_public_beta, Unset):
            review_experience_public_beta = UNSET
        else:
            review_experience_public_beta = self.review_experience_public_beta

        show_existing_comments: bool | None | Unset
        if isinstance(self.show_existing_comments, Unset):
            show_existing_comments = UNSET
        else:
            show_existing_comments = self.show_existing_comments

        show_watermark: bool | None | Unset
        if isinstance(self.show_watermark, Unset):
            show_watermark = UNSET
        else:
            show_watermark = self.show_watermark

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = self.system_domain_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        upload_storage_id: None | str | Unset
        if isinstance(self.upload_storage_id, Unset):
            upload_storage_id = UNSET
        elif isinstance(self.upload_storage_id, UUID):
            upload_storage_id = str(self.upload_storage_id)
        else:
            upload_storage_id = self.upload_storage_id

        watermark: dict[str, Any] | None | Unset
        if isinstance(self.watermark, Unset):
            watermark = UNSET
        elif isinstance(self.watermark, ShareURLCreateSchemaWatermarkType1):
            watermark = self.watermark.to_dict()
        else:
            watermark = self.watermark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allow_approving_comments": allow_approving_comments,
                "allow_comments": allow_comments,
                "allow_download": allow_download,
                "allow_setting_approve_status": allow_setting_approve_status,
            }
        )
        if allow_custom_actions is not UNSET:
            field_dict["allow_custom_actions"] = allow_custom_actions
        if allow_download_proxy is not UNSET:
            field_dict["allow_download_proxy"] = allow_download_proxy
        if allow_sync is not UNSET:
            field_dict["allow_sync"] = allow_sync
        if allow_upload is not UNSET:
            field_dict["allow_upload"] = allow_upload
        if allow_user_search_for_mentions is not UNSET:
            field_dict["allow_user_search_for_mentions"] = (
                allow_user_search_for_mentions
            )
        if allow_view_transcriptions is not UNSET:
            field_dict["allow_view_transcriptions"] = allow_view_transcriptions
        if allow_view_versions is not UNSET:
            field_dict["allow_view_versions"] = allow_view_versions
        if automatic_approval_share is not UNSET:
            field_dict["automatic_approval_share"] = automatic_approval_share
        if drm is not UNSET:
            field_dict["drm"] = drm
        if expires is not UNSET:
            field_dict["expires"] = expires
        if is_approval is not UNSET:
            field_dict["is_approval"] = is_approval
        if metadata_views is not UNSET:
            field_dict["metadata_views"] = metadata_views
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if password is not UNSET:
            field_dict["password"] = password
        if review_experience_public_beta is not UNSET:
            field_dict["review_experience_public_beta"] = review_experience_public_beta
        if show_existing_comments is not UNSET:
            field_dict["show_existing_comments"] = show_existing_comments
        if show_watermark is not UNSET:
            field_dict["show_watermark"] = show_watermark
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if title is not UNSET:
            field_dict["title"] = title
        if upload_storage_id is not UNSET:
            field_dict["upload_storage_id"] = upload_storage_id
        if watermark is not UNSET:
            field_dict["watermark"] = watermark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.share_url_create_schema_drm_type_1 import (
            ShareURLCreateSchemaDrmType1,
        )
        from ..models.share_url_create_schema_watermark_type_1 import (
            ShareURLCreateSchemaWatermarkType1,
        )

        d = dict(src_dict)
        allow_approving_comments = d.pop("allow_approving_comments")

        allow_comments = d.pop("allow_comments")

        allow_download = d.pop("allow_download")

        allow_setting_approve_status = d.pop("allow_setting_approve_status")

        def _parse_allow_custom_actions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_custom_actions = _parse_allow_custom_actions(
            d.pop("allow_custom_actions", UNSET)
        )

        def _parse_allow_download_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_download_proxy = _parse_allow_download_proxy(
            d.pop("allow_download_proxy", UNSET)
        )

        def _parse_allow_sync(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_sync = _parse_allow_sync(d.pop("allow_sync", UNSET))

        def _parse_allow_upload(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_upload = _parse_allow_upload(d.pop("allow_upload", UNSET))

        def _parse_allow_user_search_for_mentions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_user_search_for_mentions = _parse_allow_user_search_for_mentions(
            d.pop("allow_user_search_for_mentions", UNSET)
        )

        def _parse_allow_view_transcriptions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_view_transcriptions = _parse_allow_view_transcriptions(
            d.pop("allow_view_transcriptions", UNSET)
        )

        def _parse_allow_view_versions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_view_versions = _parse_allow_view_versions(
            d.pop("allow_view_versions", UNSET)
        )

        def _parse_automatic_approval_share(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        automatic_approval_share = _parse_automatic_approval_share(
            d.pop("automatic_approval_share", UNSET)
        )

        def _parse_drm(data: object) -> None | ShareURLCreateSchemaDrmType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                drm_type_1 = ShareURLCreateSchemaDrmType1.from_dict(data)

                return drm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ShareURLCreateSchemaDrmType1 | Unset, data)

        drm = _parse_drm(d.pop("drm", UNSET))

        def _parse_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = datetime.datetime.fromisoformat(data)

                return expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))

        def _parse_is_approval(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_approval = _parse_is_approval(d.pop("is_approval", UNSET))

        def _parse_metadata_views(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_views_type_0 = cast(list[str], data)

                return metadata_views_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        metadata_views = _parse_metadata_views(d.pop("metadata_views", UNSET))

        def _parse_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_review_experience_public_beta(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        review_experience_public_beta = _parse_review_experience_public_beta(
            d.pop("review_experience_public_beta", UNSET)
        )

        def _parse_show_existing_comments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_existing_comments = _parse_show_existing_comments(
            d.pop("show_existing_comments", UNSET)
        )

        def _parse_show_watermark(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_watermark = _parse_show_watermark(d.pop("show_watermark", UNSET))

        def _parse_system_domain_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_upload_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upload_storage_id_type_0 = UUID(data)

                return upload_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        upload_storage_id = _parse_upload_storage_id(d.pop("upload_storage_id", UNSET))

        def _parse_watermark(
            data: object,
        ) -> None | ShareURLCreateSchemaWatermarkType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                watermark_type_1 = ShareURLCreateSchemaWatermarkType1.from_dict(data)

                return watermark_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ShareURLCreateSchemaWatermarkType1 | Unset, data)

        watermark = _parse_watermark(d.pop("watermark", UNSET))

        share_url_create_schema = cls(
            allow_approving_comments=allow_approving_comments,
            allow_comments=allow_comments,
            allow_download=allow_download,
            allow_setting_approve_status=allow_setting_approve_status,
            allow_custom_actions=allow_custom_actions,
            allow_download_proxy=allow_download_proxy,
            allow_sync=allow_sync,
            allow_upload=allow_upload,
            allow_user_search_for_mentions=allow_user_search_for_mentions,
            allow_view_transcriptions=allow_view_transcriptions,
            allow_view_versions=allow_view_versions,
            automatic_approval_share=automatic_approval_share,
            drm=drm,
            expires=expires,
            is_approval=is_approval,
            metadata_views=metadata_views,
            object_id=object_id,
            object_type=object_type,
            owner_id=owner_id,
            password=password,
            review_experience_public_beta=review_experience_public_beta,
            show_existing_comments=show_existing_comments,
            show_watermark=show_watermark,
            system_domain_id=system_domain_id,
            title=title,
            upload_storage_id=upload_storage_id,
            watermark=watermark,
        )

        share_url_create_schema.additional_properties = d
        return share_url_create_schema

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
