from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.share_options_base_schema_drm import ShareOptionsBaseSchemaDrm
from ..models.share_options_base_schema_watermark import ShareOptionsBaseSchemaWatermark
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareOptionsBaseSchema")


@_attrs_define
class ShareOptionsBaseSchema:
    """
    Attributes:
        allow_approving_comments (bool):
        allow_comments (bool):
        allow_download (bool):
        allow_setting_approve_status (bool):
        allow_custom_actions (bool | Unset):
        allow_download_proxy (bool | Unset):
        allow_sync (bool | None | Unset):
        allow_upload (bool | Unset):
        allow_user_search_for_mentions (bool | Unset):
        allow_view_transcriptions (bool | Unset):
        allow_view_versions (bool | Unset):
        automatic_approval_share (bool | Unset):
        drm (ShareOptionsBaseSchemaDrm | Unset): DRM settings for the share
        is_approval (bool | None | Unset):
        metadata_views (list[str] | None | Unset):
        review_experience_public_beta (bool | None | Unset):
        show_existing_comments (bool | None | Unset):
        show_watermark (bool | None | Unset):
        upload_storage_id (None | Unset | UUID):
        watermark (ShareOptionsBaseSchemaWatermark | Unset): Watermark settings for the share
    """

    allow_approving_comments: bool
    allow_comments: bool
    allow_download: bool
    allow_setting_approve_status: bool
    allow_custom_actions: bool | Unset = UNSET
    allow_download_proxy: bool | Unset = UNSET
    allow_sync: bool | None | Unset = UNSET
    allow_upload: bool | Unset = UNSET
    allow_user_search_for_mentions: bool | Unset = UNSET
    allow_view_transcriptions: bool | Unset = UNSET
    allow_view_versions: bool | Unset = UNSET
    automatic_approval_share: bool | Unset = UNSET
    drm: ShareOptionsBaseSchemaDrm | Unset = UNSET
    is_approval: bool | None | Unset = UNSET
    metadata_views: list[str] | None | Unset = UNSET
    review_experience_public_beta: bool | None | Unset = UNSET
    show_existing_comments: bool | None | Unset = UNSET
    show_watermark: bool | None | Unset = UNSET
    upload_storage_id: None | Unset | UUID = UNSET
    watermark: ShareOptionsBaseSchemaWatermark | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_approving_comments = self.allow_approving_comments

        allow_comments = self.allow_comments

        allow_download = self.allow_download

        allow_setting_approve_status = self.allow_setting_approve_status

        allow_custom_actions = self.allow_custom_actions

        allow_download_proxy = self.allow_download_proxy

        allow_sync: bool | None | Unset
        if isinstance(self.allow_sync, Unset):
            allow_sync = UNSET
        else:
            allow_sync = self.allow_sync

        allow_upload = self.allow_upload

        allow_user_search_for_mentions = self.allow_user_search_for_mentions

        allow_view_transcriptions = self.allow_view_transcriptions

        allow_view_versions = self.allow_view_versions

        automatic_approval_share = self.automatic_approval_share

        drm: str | Unset = UNSET
        if not isinstance(self.drm, Unset):
            drm = self.drm.value

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

        upload_storage_id: None | str | Unset
        if isinstance(self.upload_storage_id, Unset):
            upload_storage_id = UNSET
        elif isinstance(self.upload_storage_id, UUID):
            upload_storage_id = str(self.upload_storage_id)
        else:
            upload_storage_id = self.upload_storage_id

        watermark: str | Unset = UNSET
        if not isinstance(self.watermark, Unset):
            watermark = self.watermark.value

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
        if is_approval is not UNSET:
            field_dict["is_approval"] = is_approval
        if metadata_views is not UNSET:
            field_dict["metadata_views"] = metadata_views
        if review_experience_public_beta is not UNSET:
            field_dict["review_experience_public_beta"] = review_experience_public_beta
        if show_existing_comments is not UNSET:
            field_dict["show_existing_comments"] = show_existing_comments
        if show_watermark is not UNSET:
            field_dict["show_watermark"] = show_watermark
        if upload_storage_id is not UNSET:
            field_dict["upload_storage_id"] = upload_storage_id
        if watermark is not UNSET:
            field_dict["watermark"] = watermark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_approving_comments = d.pop("allow_approving_comments")

        allow_comments = d.pop("allow_comments")

        allow_download = d.pop("allow_download")

        allow_setting_approve_status = d.pop("allow_setting_approve_status")

        allow_custom_actions = d.pop("allow_custom_actions", UNSET)

        allow_download_proxy = d.pop("allow_download_proxy", UNSET)

        def _parse_allow_sync(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_sync = _parse_allow_sync(d.pop("allow_sync", UNSET))

        allow_upload = d.pop("allow_upload", UNSET)

        allow_user_search_for_mentions = d.pop("allow_user_search_for_mentions", UNSET)

        allow_view_transcriptions = d.pop("allow_view_transcriptions", UNSET)

        allow_view_versions = d.pop("allow_view_versions", UNSET)

        automatic_approval_share = d.pop("automatic_approval_share", UNSET)

        _drm = d.pop("drm", UNSET)
        drm: ShareOptionsBaseSchemaDrm | Unset
        if isinstance(_drm, Unset):
            drm = UNSET
        else:
            drm = ShareOptionsBaseSchemaDrm(_drm)

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

        _watermark = d.pop("watermark", UNSET)
        watermark: ShareOptionsBaseSchemaWatermark | Unset
        if isinstance(_watermark, Unset):
            watermark = UNSET
        else:
            watermark = ShareOptionsBaseSchemaWatermark(_watermark)

        share_options_base_schema = cls(
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
            is_approval=is_approval,
            metadata_views=metadata_views,
            review_experience_public_beta=review_experience_public_beta,
            show_existing_comments=show_existing_comments,
            show_watermark=show_watermark,
            upload_storage_id=upload_storage_id,
            watermark=watermark,
        )

        share_options_base_schema.additional_properties = d
        return share_options_base_schema

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
