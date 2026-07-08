from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateShareActionParameters")


@_attrs_define
class CreateShareActionParameters:
    """
    Attributes:
        allow_approving_comments (bool):
        allow_comments (bool):
        allow_download (bool):
        allow_setting_approve_status (bool):
        emails (list[str]):
        user_id (UUID):
        allow_custom_actions (bool | None | Unset):
        allow_download_proxy (bool | None | Unset):
        allow_upload (bool | None | Unset):
        allow_user_search_for_mentions (bool | None | Unset):
        allow_view_transcriptions (bool | None | Unset):
        allow_view_versions (bool | None | Unset):
        expires_in_days (int | None | Unset):
        has_password (Any | Unset):
        message (None | str | Unset):
        metadata_views (list[str] | None | Unset):
        password (None | str | Unset):
        show_watermark (bool | None | Unset):
        title (None | str | Unset):
        upload_storage_id (None | Unset | UUID):
    """

    allow_approving_comments: bool
    allow_comments: bool
    allow_download: bool
    allow_setting_approve_status: bool
    emails: list[str]
    user_id: UUID
    allow_custom_actions: bool | None | Unset = UNSET
    allow_download_proxy: bool | None | Unset = UNSET
    allow_upload: bool | None | Unset = UNSET
    allow_user_search_for_mentions: bool | None | Unset = UNSET
    allow_view_transcriptions: bool | None | Unset = UNSET
    allow_view_versions: bool | None | Unset = UNSET
    expires_in_days: int | None | Unset = UNSET
    has_password: Any | Unset = UNSET
    message: None | str | Unset = UNSET
    metadata_views: list[str] | None | Unset = UNSET
    password: None | str | Unset = UNSET
    show_watermark: bool | None | Unset = UNSET
    title: None | str | Unset = UNSET
    upload_storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_approving_comments = self.allow_approving_comments

        allow_comments = self.allow_comments

        allow_download = self.allow_download

        allow_setting_approve_status = self.allow_setting_approve_status

        emails = self.emails

        user_id = str(self.user_id)

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

        expires_in_days: int | None | Unset
        if isinstance(self.expires_in_days, Unset):
            expires_in_days = UNSET
        else:
            expires_in_days = self.expires_in_days

        has_password = self.has_password

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        metadata_views: list[str] | None | Unset
        if isinstance(self.metadata_views, Unset):
            metadata_views = UNSET
        elif isinstance(self.metadata_views, list):
            metadata_views = self.metadata_views

        else:
            metadata_views = self.metadata_views

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        show_watermark: bool | None | Unset
        if isinstance(self.show_watermark, Unset):
            show_watermark = UNSET
        else:
            show_watermark = self.show_watermark

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allow_approving_comments": allow_approving_comments,
                "allow_comments": allow_comments,
                "allow_download": allow_download,
                "allow_setting_approve_status": allow_setting_approve_status,
                "emails": emails,
                "user_id": user_id,
            }
        )
        if allow_custom_actions is not UNSET:
            field_dict["allow_custom_actions"] = allow_custom_actions
        if allow_download_proxy is not UNSET:
            field_dict["allow_download_proxy"] = allow_download_proxy
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
        if expires_in_days is not UNSET:
            field_dict["expires_in_days"] = expires_in_days
        if has_password is not UNSET:
            field_dict["has_password"] = has_password
        if message is not UNSET:
            field_dict["message"] = message
        if metadata_views is not UNSET:
            field_dict["metadata_views"] = metadata_views
        if password is not UNSET:
            field_dict["password"] = password
        if show_watermark is not UNSET:
            field_dict["show_watermark"] = show_watermark
        if title is not UNSET:
            field_dict["title"] = title
        if upload_storage_id is not UNSET:
            field_dict["upload_storage_id"] = upload_storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_approving_comments = d.pop("allow_approving_comments")

        allow_comments = d.pop("allow_comments")

        allow_download = d.pop("allow_download")

        allow_setting_approve_status = d.pop("allow_setting_approve_status")

        emails = cast(list[str], d.pop("emails"))

        user_id = UUID(d.pop("user_id"))

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

        def _parse_expires_in_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_in_days = _parse_expires_in_days(d.pop("expires_in_days", UNSET))

        has_password = d.pop("has_password", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

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

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_show_watermark(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_watermark = _parse_show_watermark(d.pop("show_watermark", UNSET))

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

        create_share_action_parameters = cls(
            allow_approving_comments=allow_approving_comments,
            allow_comments=allow_comments,
            allow_download=allow_download,
            allow_setting_approve_status=allow_setting_approve_status,
            emails=emails,
            user_id=user_id,
            allow_custom_actions=allow_custom_actions,
            allow_download_proxy=allow_download_proxy,
            allow_upload=allow_upload,
            allow_user_search_for_mentions=allow_user_search_for_mentions,
            allow_view_transcriptions=allow_view_transcriptions,
            allow_view_versions=allow_view_versions,
            expires_in_days=expires_in_days,
            has_password=has_password,
            message=message,
            metadata_views=metadata_views,
            password=password,
            show_watermark=show_watermark,
            title=title,
            upload_storage_id=upload_storage_id,
        )

        create_share_action_parameters.additional_properties = d
        return create_share_action_parameters

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
