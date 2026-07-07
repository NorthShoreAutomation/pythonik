from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.share_url_schema_drm import ShareURLSchemaDrm
from ..models.share_url_schema_population_status import ShareURLSchemaPopulationStatus
from ..models.share_url_schema_watermark import ShareURLSchemaWatermark
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareURLSchema")


@_attrs_define
class ShareURLSchema:
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
        date_created (datetime.datetime | Unset):
        drm (ShareURLSchemaDrm | Unset): DRM settings for the share
        expires (datetime.datetime | Unset):
        has_password (bool | Unset):
        id (str | Unset):
        is_approval (bool | None | Unset):
        message (None | str | Unset):
        metadata_views (list[str] | None | Unset):
        object_id (str | Unset):
        object_type (str | Unset):
        owner_id (str | Unset):
        population_status (ShareURLSchemaPopulationStatus | Unset):
        project_id (None | Unset | UUID): Project ID if the share is created from a project
        review_experience_public_beta (bool | None | Unset):
        show_existing_comments (bool | None | Unset):
        show_watermark (bool | None | Unset):
        system_domain_id (str | Unset):
        title (None | str | Unset):
        upload_storage_id (None | Unset | UUID):
        url (str | Unset):
        watermark (ShareURLSchemaWatermark | Unset): Watermark settings for the share
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
    date_created: datetime.datetime | Unset = UNSET
    drm: ShareURLSchemaDrm | Unset = UNSET
    expires: datetime.datetime | Unset = UNSET
    has_password: bool | Unset = UNSET
    id: str | Unset = UNSET
    is_approval: bool | None | Unset = UNSET
    message: None | str | Unset = UNSET
    metadata_views: list[str] | None | Unset = UNSET
    object_id: str | Unset = UNSET
    object_type: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    population_status: ShareURLSchemaPopulationStatus | Unset = UNSET
    project_id: None | Unset | UUID = UNSET
    review_experience_public_beta: bool | None | Unset = UNSET
    show_existing_comments: bool | None | Unset = UNSET
    show_watermark: bool | None | Unset = UNSET
    system_domain_id: str | Unset = UNSET
    title: None | str | Unset = UNSET
    upload_storage_id: None | Unset | UUID = UNSET
    url: str | Unset = UNSET
    watermark: ShareURLSchemaWatermark | Unset = UNSET
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

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        drm: str | Unset = UNSET
        if not isinstance(self.drm, Unset):
            drm = self.drm.value

        expires: str | Unset = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        has_password = self.has_password

        id = self.id

        is_approval: bool | None | Unset
        if isinstance(self.is_approval, Unset):
            is_approval = UNSET
        else:
            is_approval = self.is_approval

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

        object_id = self.object_id

        object_type = self.object_type

        owner_id = self.owner_id

        population_status: str | Unset = UNSET
        if not isinstance(self.population_status, Unset):
            population_status = self.population_status.value

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

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

        url = self.url

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
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if drm is not UNSET:
            field_dict["drm"] = drm
        if expires is not UNSET:
            field_dict["expires"] = expires
        if has_password is not UNSET:
            field_dict["has_password"] = has_password
        if id is not UNSET:
            field_dict["id"] = id
        if is_approval is not UNSET:
            field_dict["is_approval"] = is_approval
        if message is not UNSET:
            field_dict["message"] = message
        if metadata_views is not UNSET:
            field_dict["metadata_views"] = metadata_views
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if population_status is not UNSET:
            field_dict["population_status"] = population_status
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
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
        if url is not UNSET:
            field_dict["url"] = url
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

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _drm = d.pop("drm", UNSET)
        drm: ShareURLSchemaDrm | Unset
        if isinstance(_drm, Unset):
            drm = UNSET
        else:
            drm = ShareURLSchemaDrm(_drm)

        _expires = d.pop("expires", UNSET)
        expires: datetime.datetime | Unset
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = datetime.datetime.fromisoformat(_expires)

        has_password = d.pop("has_password", UNSET)

        id = d.pop("id", UNSET)

        def _parse_is_approval(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_approval = _parse_is_approval(d.pop("is_approval", UNSET))

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

        object_id = d.pop("object_id", UNSET)

        object_type = d.pop("object_type", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        _population_status = d.pop("population_status", UNSET)
        population_status: ShareURLSchemaPopulationStatus | Unset
        if isinstance(_population_status, Unset):
            population_status = UNSET
        else:
            population_status = ShareURLSchemaPopulationStatus(_population_status)

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

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

        system_domain_id = d.pop("system_domain_id", UNSET)

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

        url = d.pop("url", UNSET)

        _watermark = d.pop("watermark", UNSET)
        watermark: ShareURLSchemaWatermark | Unset
        if isinstance(_watermark, Unset):
            watermark = UNSET
        else:
            watermark = ShareURLSchemaWatermark(_watermark)

        share_url_schema = cls(
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
            date_created=date_created,
            drm=drm,
            expires=expires,
            has_password=has_password,
            id=id,
            is_approval=is_approval,
            message=message,
            metadata_views=metadata_views,
            object_id=object_id,
            object_type=object_type,
            owner_id=owner_id,
            population_status=population_status,
            project_id=project_id,
            review_experience_public_beta=review_experience_public_beta,
            show_existing_comments=show_existing_comments,
            show_watermark=show_watermark,
            system_domain_id=system_domain_id,
            title=title,
            upload_storage_id=upload_storage_id,
            url=url,
            watermark=watermark,
        )

        share_url_schema.additional_properties = d
        return share_url_schema

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
