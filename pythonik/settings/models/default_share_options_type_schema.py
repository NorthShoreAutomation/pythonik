from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultShareOptionsTypeSchema")


@_attrs_define
class DefaultShareOptionsTypeSchema:
    """
    Attributes:
        allow_approving_comments (bool | Unset):
        allow_comments (bool | Unset):
        allow_custom_actions (bool | Unset):
        allow_download (bool | Unset):
        allow_download_proxy (bool | Unset):
        allow_setting_approve_status (bool | Unset):
        allow_upload (bool | Unset):
        allow_view_transcriptions (bool | Unset):
        allow_view_versions (bool | Unset):
        can_change_allow_approving_comments (bool | Unset):
        can_change_allow_comments (bool | Unset):
        can_change_allow_custom_actions (bool | Unset):
        can_change_allow_download (bool | Unset):
        can_change_allow_download_proxy (bool | Unset):
        can_change_allow_setting_approve_status (bool | Unset):
        can_change_allow_upload (bool | Unset):
        can_change_allow_view_transcriptions (bool | Unset):
        can_change_allow_view_versions (bool | Unset):
        can_change_search_users_from_share (bool | Unset):
        can_change_share_expiration_time (bool | Unset):
        can_change_show_existing_comments (bool | Unset):
        can_change_show_watermark (bool | Unset):
        require_password (bool | Unset):
        show_existing_comments (bool | Unset):
        show_watermark (bool | Unset):
    """

    allow_approving_comments: bool | Unset = UNSET
    allow_comments: bool | Unset = UNSET
    allow_custom_actions: bool | Unset = UNSET
    allow_download: bool | Unset = UNSET
    allow_download_proxy: bool | Unset = UNSET
    allow_setting_approve_status: bool | Unset = UNSET
    allow_upload: bool | Unset = UNSET
    allow_view_transcriptions: bool | Unset = UNSET
    allow_view_versions: bool | Unset = UNSET
    can_change_allow_approving_comments: bool | Unset = UNSET
    can_change_allow_comments: bool | Unset = UNSET
    can_change_allow_custom_actions: bool | Unset = UNSET
    can_change_allow_download: bool | Unset = UNSET
    can_change_allow_download_proxy: bool | Unset = UNSET
    can_change_allow_setting_approve_status: bool | Unset = UNSET
    can_change_allow_upload: bool | Unset = UNSET
    can_change_allow_view_transcriptions: bool | Unset = UNSET
    can_change_allow_view_versions: bool | Unset = UNSET
    can_change_search_users_from_share: bool | Unset = UNSET
    can_change_share_expiration_time: bool | Unset = UNSET
    can_change_show_existing_comments: bool | Unset = UNSET
    can_change_show_watermark: bool | Unset = UNSET
    require_password: bool | Unset = UNSET
    show_existing_comments: bool | Unset = UNSET
    show_watermark: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_approving_comments = self.allow_approving_comments

        allow_comments = self.allow_comments

        allow_custom_actions = self.allow_custom_actions

        allow_download = self.allow_download

        allow_download_proxy = self.allow_download_proxy

        allow_setting_approve_status = self.allow_setting_approve_status

        allow_upload = self.allow_upload

        allow_view_transcriptions = self.allow_view_transcriptions

        allow_view_versions = self.allow_view_versions

        can_change_allow_approving_comments = self.can_change_allow_approving_comments

        can_change_allow_comments = self.can_change_allow_comments

        can_change_allow_custom_actions = self.can_change_allow_custom_actions

        can_change_allow_download = self.can_change_allow_download

        can_change_allow_download_proxy = self.can_change_allow_download_proxy

        can_change_allow_setting_approve_status = (
            self.can_change_allow_setting_approve_status
        )

        can_change_allow_upload = self.can_change_allow_upload

        can_change_allow_view_transcriptions = self.can_change_allow_view_transcriptions

        can_change_allow_view_versions = self.can_change_allow_view_versions

        can_change_search_users_from_share = self.can_change_search_users_from_share

        can_change_share_expiration_time = self.can_change_share_expiration_time

        can_change_show_existing_comments = self.can_change_show_existing_comments

        can_change_show_watermark = self.can_change_show_watermark

        require_password = self.require_password

        show_existing_comments = self.show_existing_comments

        show_watermark = self.show_watermark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_approving_comments is not UNSET:
            field_dict["allow_approving_comments"] = allow_approving_comments
        if allow_comments is not UNSET:
            field_dict["allow_comments"] = allow_comments
        if allow_custom_actions is not UNSET:
            field_dict["allow_custom_actions"] = allow_custom_actions
        if allow_download is not UNSET:
            field_dict["allow_download"] = allow_download
        if allow_download_proxy is not UNSET:
            field_dict["allow_download_proxy"] = allow_download_proxy
        if allow_setting_approve_status is not UNSET:
            field_dict["allow_setting_approve_status"] = allow_setting_approve_status
        if allow_upload is not UNSET:
            field_dict["allow_upload"] = allow_upload
        if allow_view_transcriptions is not UNSET:
            field_dict["allow_view_transcriptions"] = allow_view_transcriptions
        if allow_view_versions is not UNSET:
            field_dict["allow_view_versions"] = allow_view_versions
        if can_change_allow_approving_comments is not UNSET:
            field_dict["can_change_allow_approving_comments"] = (
                can_change_allow_approving_comments
            )
        if can_change_allow_comments is not UNSET:
            field_dict["can_change_allow_comments"] = can_change_allow_comments
        if can_change_allow_custom_actions is not UNSET:
            field_dict["can_change_allow_custom_actions"] = (
                can_change_allow_custom_actions
            )
        if can_change_allow_download is not UNSET:
            field_dict["can_change_allow_download"] = can_change_allow_download
        if can_change_allow_download_proxy is not UNSET:
            field_dict["can_change_allow_download_proxy"] = (
                can_change_allow_download_proxy
            )
        if can_change_allow_setting_approve_status is not UNSET:
            field_dict["can_change_allow_setting_approve_status"] = (
                can_change_allow_setting_approve_status
            )
        if can_change_allow_upload is not UNSET:
            field_dict["can_change_allow_upload"] = can_change_allow_upload
        if can_change_allow_view_transcriptions is not UNSET:
            field_dict["can_change_allow_view_transcriptions"] = (
                can_change_allow_view_transcriptions
            )
        if can_change_allow_view_versions is not UNSET:
            field_dict["can_change_allow_view_versions"] = (
                can_change_allow_view_versions
            )
        if can_change_search_users_from_share is not UNSET:
            field_dict["can_change_search_users_from_share"] = (
                can_change_search_users_from_share
            )
        if can_change_share_expiration_time is not UNSET:
            field_dict["can_change_share_expiration_time"] = (
                can_change_share_expiration_time
            )
        if can_change_show_existing_comments is not UNSET:
            field_dict["can_change_show_existing_comments"] = (
                can_change_show_existing_comments
            )
        if can_change_show_watermark is not UNSET:
            field_dict["can_change_show_watermark"] = can_change_show_watermark
        if require_password is not UNSET:
            field_dict["require_password"] = require_password
        if show_existing_comments is not UNSET:
            field_dict["show_existing_comments"] = show_existing_comments
        if show_watermark is not UNSET:
            field_dict["show_watermark"] = show_watermark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_approving_comments = d.pop("allow_approving_comments", UNSET)

        allow_comments = d.pop("allow_comments", UNSET)

        allow_custom_actions = d.pop("allow_custom_actions", UNSET)

        allow_download = d.pop("allow_download", UNSET)

        allow_download_proxy = d.pop("allow_download_proxy", UNSET)

        allow_setting_approve_status = d.pop("allow_setting_approve_status", UNSET)

        allow_upload = d.pop("allow_upload", UNSET)

        allow_view_transcriptions = d.pop("allow_view_transcriptions", UNSET)

        allow_view_versions = d.pop("allow_view_versions", UNSET)

        can_change_allow_approving_comments = d.pop(
            "can_change_allow_approving_comments", UNSET
        )

        can_change_allow_comments = d.pop("can_change_allow_comments", UNSET)

        can_change_allow_custom_actions = d.pop(
            "can_change_allow_custom_actions", UNSET
        )

        can_change_allow_download = d.pop("can_change_allow_download", UNSET)

        can_change_allow_download_proxy = d.pop(
            "can_change_allow_download_proxy", UNSET
        )

        can_change_allow_setting_approve_status = d.pop(
            "can_change_allow_setting_approve_status", UNSET
        )

        can_change_allow_upload = d.pop("can_change_allow_upload", UNSET)

        can_change_allow_view_transcriptions = d.pop(
            "can_change_allow_view_transcriptions", UNSET
        )

        can_change_allow_view_versions = d.pop("can_change_allow_view_versions", UNSET)

        can_change_search_users_from_share = d.pop(
            "can_change_search_users_from_share", UNSET
        )

        can_change_share_expiration_time = d.pop(
            "can_change_share_expiration_time", UNSET
        )

        can_change_show_existing_comments = d.pop(
            "can_change_show_existing_comments", UNSET
        )

        can_change_show_watermark = d.pop("can_change_show_watermark", UNSET)

        require_password = d.pop("require_password", UNSET)

        show_existing_comments = d.pop("show_existing_comments", UNSET)

        show_watermark = d.pop("show_watermark", UNSET)

        default_share_options_type_schema = cls(
            allow_approving_comments=allow_approving_comments,
            allow_comments=allow_comments,
            allow_custom_actions=allow_custom_actions,
            allow_download=allow_download,
            allow_download_proxy=allow_download_proxy,
            allow_setting_approve_status=allow_setting_approve_status,
            allow_upload=allow_upload,
            allow_view_transcriptions=allow_view_transcriptions,
            allow_view_versions=allow_view_versions,
            can_change_allow_approving_comments=can_change_allow_approving_comments,
            can_change_allow_comments=can_change_allow_comments,
            can_change_allow_custom_actions=can_change_allow_custom_actions,
            can_change_allow_download=can_change_allow_download,
            can_change_allow_download_proxy=can_change_allow_download_proxy,
            can_change_allow_setting_approve_status=can_change_allow_setting_approve_status,
            can_change_allow_upload=can_change_allow_upload,
            can_change_allow_view_transcriptions=can_change_allow_view_transcriptions,
            can_change_allow_view_versions=can_change_allow_view_versions,
            can_change_search_users_from_share=can_change_search_users_from_share,
            can_change_share_expiration_time=can_change_share_expiration_time,
            can_change_show_existing_comments=can_change_show_existing_comments,
            can_change_show_watermark=can_change_show_watermark,
            require_password=require_password,
            show_existing_comments=show_existing_comments,
            show_watermark=show_watermark,
        )

        default_share_options_type_schema.additional_properties = d
        return default_share_options_type_schema

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
