from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultShareOptionsTypeSchema")


@_attrs_define
class DefaultShareOptionsTypeSchema:
    """
    Attributes:
        allow_approving_comments (bool | None | Unset):
        allow_comments (bool | None | Unset):
        allow_custom_actions (bool | None | Unset):
        allow_download (bool | None | Unset):
        allow_download_proxy (bool | None | Unset):
        allow_setting_approve_status (bool | None | Unset):
        allow_upload (bool | None | Unset):
        allow_view_transcriptions (bool | None | Unset):
        allow_view_versions (bool | None | Unset):
        can_change_allow_approving_comments (bool | None | Unset):
        can_change_allow_comments (bool | None | Unset):
        can_change_allow_custom_actions (bool | None | Unset):
        can_change_allow_download (bool | None | Unset):
        can_change_allow_download_proxy (bool | None | Unset):
        can_change_allow_setting_approve_status (bool | None | Unset):
        can_change_allow_upload (bool | None | Unset):
        can_change_allow_view_transcriptions (bool | None | Unset):
        can_change_allow_view_versions (bool | None | Unset):
        can_change_search_users_from_share (bool | None | Unset):
        can_change_share_expiration_time (bool | None | Unset):
        can_change_show_existing_comments (bool | None | Unset):
        can_change_show_watermark (bool | None | Unset):
        require_password (bool | None | Unset):
        show_existing_comments (bool | None | Unset):
        show_watermark (bool | None | Unset):
    """

    allow_approving_comments: bool | None | Unset = UNSET
    allow_comments: bool | None | Unset = UNSET
    allow_custom_actions: bool | None | Unset = UNSET
    allow_download: bool | None | Unset = UNSET
    allow_download_proxy: bool | None | Unset = UNSET
    allow_setting_approve_status: bool | None | Unset = UNSET
    allow_upload: bool | None | Unset = UNSET
    allow_view_transcriptions: bool | None | Unset = UNSET
    allow_view_versions: bool | None | Unset = UNSET
    can_change_allow_approving_comments: bool | None | Unset = UNSET
    can_change_allow_comments: bool | None | Unset = UNSET
    can_change_allow_custom_actions: bool | None | Unset = UNSET
    can_change_allow_download: bool | None | Unset = UNSET
    can_change_allow_download_proxy: bool | None | Unset = UNSET
    can_change_allow_setting_approve_status: bool | None | Unset = UNSET
    can_change_allow_upload: bool | None | Unset = UNSET
    can_change_allow_view_transcriptions: bool | None | Unset = UNSET
    can_change_allow_view_versions: bool | None | Unset = UNSET
    can_change_search_users_from_share: bool | None | Unset = UNSET
    can_change_share_expiration_time: bool | None | Unset = UNSET
    can_change_show_existing_comments: bool | None | Unset = UNSET
    can_change_show_watermark: bool | None | Unset = UNSET
    require_password: bool | None | Unset = UNSET
    show_existing_comments: bool | None | Unset = UNSET
    show_watermark: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_approving_comments: bool | None | Unset
        if isinstance(self.allow_approving_comments, Unset):
            allow_approving_comments = UNSET
        else:
            allow_approving_comments = self.allow_approving_comments

        allow_comments: bool | None | Unset
        if isinstance(self.allow_comments, Unset):
            allow_comments = UNSET
        else:
            allow_comments = self.allow_comments

        allow_custom_actions: bool | None | Unset
        if isinstance(self.allow_custom_actions, Unset):
            allow_custom_actions = UNSET
        else:
            allow_custom_actions = self.allow_custom_actions

        allow_download: bool | None | Unset
        if isinstance(self.allow_download, Unset):
            allow_download = UNSET
        else:
            allow_download = self.allow_download

        allow_download_proxy: bool | None | Unset
        if isinstance(self.allow_download_proxy, Unset):
            allow_download_proxy = UNSET
        else:
            allow_download_proxy = self.allow_download_proxy

        allow_setting_approve_status: bool | None | Unset
        if isinstance(self.allow_setting_approve_status, Unset):
            allow_setting_approve_status = UNSET
        else:
            allow_setting_approve_status = self.allow_setting_approve_status

        allow_upload: bool | None | Unset
        if isinstance(self.allow_upload, Unset):
            allow_upload = UNSET
        else:
            allow_upload = self.allow_upload

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

        can_change_allow_approving_comments: bool | None | Unset
        if isinstance(self.can_change_allow_approving_comments, Unset):
            can_change_allow_approving_comments = UNSET
        else:
            can_change_allow_approving_comments = (
                self.can_change_allow_approving_comments
            )

        can_change_allow_comments: bool | None | Unset
        if isinstance(self.can_change_allow_comments, Unset):
            can_change_allow_comments = UNSET
        else:
            can_change_allow_comments = self.can_change_allow_comments

        can_change_allow_custom_actions: bool | None | Unset
        if isinstance(self.can_change_allow_custom_actions, Unset):
            can_change_allow_custom_actions = UNSET
        else:
            can_change_allow_custom_actions = self.can_change_allow_custom_actions

        can_change_allow_download: bool | None | Unset
        if isinstance(self.can_change_allow_download, Unset):
            can_change_allow_download = UNSET
        else:
            can_change_allow_download = self.can_change_allow_download

        can_change_allow_download_proxy: bool | None | Unset
        if isinstance(self.can_change_allow_download_proxy, Unset):
            can_change_allow_download_proxy = UNSET
        else:
            can_change_allow_download_proxy = self.can_change_allow_download_proxy

        can_change_allow_setting_approve_status: bool | None | Unset
        if isinstance(self.can_change_allow_setting_approve_status, Unset):
            can_change_allow_setting_approve_status = UNSET
        else:
            can_change_allow_setting_approve_status = (
                self.can_change_allow_setting_approve_status
            )

        can_change_allow_upload: bool | None | Unset
        if isinstance(self.can_change_allow_upload, Unset):
            can_change_allow_upload = UNSET
        else:
            can_change_allow_upload = self.can_change_allow_upload

        can_change_allow_view_transcriptions: bool | None | Unset
        if isinstance(self.can_change_allow_view_transcriptions, Unset):
            can_change_allow_view_transcriptions = UNSET
        else:
            can_change_allow_view_transcriptions = (
                self.can_change_allow_view_transcriptions
            )

        can_change_allow_view_versions: bool | None | Unset
        if isinstance(self.can_change_allow_view_versions, Unset):
            can_change_allow_view_versions = UNSET
        else:
            can_change_allow_view_versions = self.can_change_allow_view_versions

        can_change_search_users_from_share: bool | None | Unset
        if isinstance(self.can_change_search_users_from_share, Unset):
            can_change_search_users_from_share = UNSET
        else:
            can_change_search_users_from_share = self.can_change_search_users_from_share

        can_change_share_expiration_time: bool | None | Unset
        if isinstance(self.can_change_share_expiration_time, Unset):
            can_change_share_expiration_time = UNSET
        else:
            can_change_share_expiration_time = self.can_change_share_expiration_time

        can_change_show_existing_comments: bool | None | Unset
        if isinstance(self.can_change_show_existing_comments, Unset):
            can_change_show_existing_comments = UNSET
        else:
            can_change_show_existing_comments = self.can_change_show_existing_comments

        can_change_show_watermark: bool | None | Unset
        if isinstance(self.can_change_show_watermark, Unset):
            can_change_show_watermark = UNSET
        else:
            can_change_show_watermark = self.can_change_show_watermark

        require_password: bool | None | Unset
        if isinstance(self.require_password, Unset):
            require_password = UNSET
        else:
            require_password = self.require_password

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

        def _parse_allow_approving_comments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_approving_comments = _parse_allow_approving_comments(
            d.pop("allow_approving_comments", UNSET)
        )

        def _parse_allow_comments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_comments = _parse_allow_comments(d.pop("allow_comments", UNSET))

        def _parse_allow_custom_actions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_custom_actions = _parse_allow_custom_actions(
            d.pop("allow_custom_actions", UNSET)
        )

        def _parse_allow_download(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_download = _parse_allow_download(d.pop("allow_download", UNSET))

        def _parse_allow_download_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_download_proxy = _parse_allow_download_proxy(
            d.pop("allow_download_proxy", UNSET)
        )

        def _parse_allow_setting_approve_status(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_setting_approve_status = _parse_allow_setting_approve_status(
            d.pop("allow_setting_approve_status", UNSET)
        )

        def _parse_allow_upload(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_upload = _parse_allow_upload(d.pop("allow_upload", UNSET))

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

        def _parse_can_change_allow_approving_comments(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_approving_comments = (
            _parse_can_change_allow_approving_comments(
                d.pop("can_change_allow_approving_comments", UNSET)
            )
        )

        def _parse_can_change_allow_comments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_comments = _parse_can_change_allow_comments(
            d.pop("can_change_allow_comments", UNSET)
        )

        def _parse_can_change_allow_custom_actions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_custom_actions = _parse_can_change_allow_custom_actions(
            d.pop("can_change_allow_custom_actions", UNSET)
        )

        def _parse_can_change_allow_download(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_download = _parse_can_change_allow_download(
            d.pop("can_change_allow_download", UNSET)
        )

        def _parse_can_change_allow_download_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_download_proxy = _parse_can_change_allow_download_proxy(
            d.pop("can_change_allow_download_proxy", UNSET)
        )

        def _parse_can_change_allow_setting_approve_status(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_setting_approve_status = (
            _parse_can_change_allow_setting_approve_status(
                d.pop("can_change_allow_setting_approve_status", UNSET)
            )
        )

        def _parse_can_change_allow_upload(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_upload = _parse_can_change_allow_upload(
            d.pop("can_change_allow_upload", UNSET)
        )

        def _parse_can_change_allow_view_transcriptions(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_view_transcriptions = (
            _parse_can_change_allow_view_transcriptions(
                d.pop("can_change_allow_view_transcriptions", UNSET)
            )
        )

        def _parse_can_change_allow_view_versions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_allow_view_versions = _parse_can_change_allow_view_versions(
            d.pop("can_change_allow_view_versions", UNSET)
        )

        def _parse_can_change_search_users_from_share(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_search_users_from_share = _parse_can_change_search_users_from_share(
            d.pop("can_change_search_users_from_share", UNSET)
        )

        def _parse_can_change_share_expiration_time(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_share_expiration_time = _parse_can_change_share_expiration_time(
            d.pop("can_change_share_expiration_time", UNSET)
        )

        def _parse_can_change_show_existing_comments(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_show_existing_comments = _parse_can_change_show_existing_comments(
            d.pop("can_change_show_existing_comments", UNSET)
        )

        def _parse_can_change_show_watermark(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_change_show_watermark = _parse_can_change_show_watermark(
            d.pop("can_change_show_watermark", UNSET)
        )

        def _parse_require_password(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        require_password = _parse_require_password(d.pop("require_password", UNSET))

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
