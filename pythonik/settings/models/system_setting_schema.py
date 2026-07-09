from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_setting_schema_drm import SystemSettingSchemaDrm
from ..models.system_setting_schema_mfa_methods_type_0_item import (
    SystemSettingSchemaMfaMethodsType0Item,
)
from ..models.system_setting_schema_watermark import SystemSettingSchemaWatermark
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowed_ip_schema import AllowedIPSchema
    from ..models.default_share_options_type_schema import DefaultShareOptionsTypeSchema
    from ..models.facet_field_schema import FacetFieldSchema
    from ..models.jobs_dashboard_schema import JobsDashboardSchema
    from ..models.password_checks_type_schema import PasswordChecksTypeSchema
    from ..models.search_display_field_schema import SearchDisplayFieldSchema
    from ..models.watermark_options_type import WatermarkOptionsType


T = TypeVar("T", bound="SystemSettingSchema")


@_attrs_define
class SystemSettingSchema:
    """
    Attributes:
        acl_template_id (None | Unset | UUID):
        allow_invites_by_link (bool | None | Unset):
        allow_play_original_during_transcoding (bool | None | Unset): Allow playing the original file while transcoding
            is in progress.
        allow_share_magic_link_creation (bool | None | Unset):
        allowed_ips (list[AllowedIPSchema] | None | Unset):
        append_asset_uuid_to_downloads (bool | None | Unset):
        asset_default_sections (list[str] | None | Unset):
        client_ip (None | str | Unset):
        collections_get_parent_acls (bool | None | Unset):
        cors_hosts (list[str] | None | Unset):
        date_format (None | str | Unset):
        datetime_format (None | str | Unset):
        default_app_token_ttl (int | None | Unset): Default time to live for app tokens in seconds.
        default_refresh_token_ttl (int | None | Unset): Default time to live for refresh tokens in seconds.
        default_share_options (DefaultShareOptionsTypeSchema | None | Unset):
        default_upload_storage_id (None | Unset | UUID):
        default_user_token_ttl (int | None | Unset): Default time to live for user tokens in seconds.
        delete_grace_period (int | None | Unset): Grace period that indicate how long objects will live in recycle bin.
            Unit: hours
        drm (None | SystemSettingSchemaDrm | Unset):
        drm_enforce (bool | None | Unset): Whether to require hardware DRM for playback when DRM is enabled Default:
            True.
        enable_ai_metadata_filling (bool | None | Unset):
        enable_face_recognition (bool | None | Unset):
        enable_nltf (bool | None | Unset):
        enable_shield (bool | None | Unset):
        enforce_magic_link_allowlist (bool | None | Unset): When enabled, magic links can only be sent to allowlisted
            emails/domains
        external_share (bool | None | Unset):
        facet_fields (list[FacetFieldSchema] | None | Unset):
        filters_default_metadata_view_id (None | Unset | UUID):
        hide_favourites (bool | None | Unset):
        home_page (None | str | Unset):
        image_properties_metadata_field (None | str | Unset):
        jobs_dashboard (JobsDashboardSchema | None | Unset):
        locations_metadata_field (None | str | Unset):
        lock_mapped_collections (bool | None | Unset): Forbid regular users to edit or delete mapped collections.
        logo_storage_id (None | Unset | UUID):
        logo_url (None | str | Unset):
        logos_metadata_field (None | str | Unset):
        max_browse_users (int | None | Unset):
        max_power_users (int | None | Unset):
        max_standard_users (int | None | Unset):
        max_storage_bytes (int | None | Unset):
        max_traffic_bytes (int | None | Unset):
        mfa_methods (list[SystemSettingSchemaMfaMethodsType0Item] | None | Unset):
        mfa_required (bool | None | Unset):
        password_checks (None | PasswordChecksTypeSchema | Unset):
        require_limit_download_groups (bool | None | Unset):
        required_metadata_views (list[str] | None | Unset):
        review_experience_disabled (bool | None | Unset):
        review_experience_disabled_per_share (bool | None | Unset):
        safe_searches_metadata_field (None | str | Unset):
        saml_require_groups (bool | None | Unset):
        search_auto_resize_title_column (bool | None | Unset):
        search_default_sections (list[str] | None | Unset):
        search_display_fields (list[SearchDisplayFieldSchema] | None | Unset):
        search_in_transcriptions (bool | None | Unset):
        search_results_asset_metadata_view_id (None | Unset | UUID):
        search_results_collection_metadata_view_id (None | Unset | UUID):
        search_users_from_share (bool | None | Unset):
        share_expiration_time (int | None | Unset): Default share expiration time that indicate how long share will be
            valid. Unit: days
        support_access (bool | None | Unset):
        system_domain_id (None | Unset | UUID):
        system_domain_name (None | str | Unset):
        tags_metadata_field (None | str | Unset):
        texts_metadata_field (None | str | Unset):
        update_saml_primary_group_on_login (bool | None | Unset):
        use_asset_name_on_download (bool | None | Unset):
        watermark (None | SystemSettingSchemaWatermark | Unset):
        watermark_options (None | Unset | WatermarkOptionsType):
    """

    acl_template_id: None | Unset | UUID = UNSET
    allow_invites_by_link: bool | None | Unset = UNSET
    allow_play_original_during_transcoding: bool | None | Unset = UNSET
    allow_share_magic_link_creation: bool | None | Unset = UNSET
    allowed_ips: list[AllowedIPSchema] | None | Unset = UNSET
    append_asset_uuid_to_downloads: bool | None | Unset = UNSET
    asset_default_sections: list[str] | None | Unset = UNSET
    client_ip: None | str | Unset = UNSET
    collections_get_parent_acls: bool | None | Unset = UNSET
    cors_hosts: list[str] | None | Unset = UNSET
    date_format: None | str | Unset = UNSET
    datetime_format: None | str | Unset = UNSET
    default_app_token_ttl: int | None | Unset = UNSET
    default_refresh_token_ttl: int | None | Unset = UNSET
    default_share_options: DefaultShareOptionsTypeSchema | None | Unset = UNSET
    default_upload_storage_id: None | Unset | UUID = UNSET
    default_user_token_ttl: int | None | Unset = UNSET
    delete_grace_period: int | None | Unset = UNSET
    drm: None | SystemSettingSchemaDrm | Unset = UNSET
    drm_enforce: bool | None | Unset = True
    enable_ai_metadata_filling: bool | None | Unset = UNSET
    enable_face_recognition: bool | None | Unset = UNSET
    enable_nltf: bool | None | Unset = UNSET
    enable_shield: bool | None | Unset = UNSET
    enforce_magic_link_allowlist: bool | None | Unset = UNSET
    external_share: bool | None | Unset = UNSET
    facet_fields: list[FacetFieldSchema] | None | Unset = UNSET
    filters_default_metadata_view_id: None | Unset | UUID = UNSET
    hide_favourites: bool | None | Unset = UNSET
    home_page: None | str | Unset = UNSET
    image_properties_metadata_field: None | str | Unset = UNSET
    jobs_dashboard: JobsDashboardSchema | None | Unset = UNSET
    locations_metadata_field: None | str | Unset = UNSET
    lock_mapped_collections: bool | None | Unset = UNSET
    logo_storage_id: None | Unset | UUID = UNSET
    logo_url: None | str | Unset = UNSET
    logos_metadata_field: None | str | Unset = UNSET
    max_browse_users: int | None | Unset = UNSET
    max_power_users: int | None | Unset = UNSET
    max_standard_users: int | None | Unset = UNSET
    max_storage_bytes: int | None | Unset = UNSET
    max_traffic_bytes: int | None | Unset = UNSET
    mfa_methods: list[SystemSettingSchemaMfaMethodsType0Item] | None | Unset = UNSET
    mfa_required: bool | None | Unset = UNSET
    password_checks: None | PasswordChecksTypeSchema | Unset = UNSET
    require_limit_download_groups: bool | None | Unset = UNSET
    required_metadata_views: list[str] | None | Unset = UNSET
    review_experience_disabled: bool | None | Unset = UNSET
    review_experience_disabled_per_share: bool | None | Unset = UNSET
    safe_searches_metadata_field: None | str | Unset = UNSET
    saml_require_groups: bool | None | Unset = UNSET
    search_auto_resize_title_column: bool | None | Unset = UNSET
    search_default_sections: list[str] | None | Unset = UNSET
    search_display_fields: list[SearchDisplayFieldSchema] | None | Unset = UNSET
    search_in_transcriptions: bool | None | Unset = UNSET
    search_results_asset_metadata_view_id: None | Unset | UUID = UNSET
    search_results_collection_metadata_view_id: None | Unset | UUID = UNSET
    search_users_from_share: bool | None | Unset = UNSET
    share_expiration_time: int | None | Unset = UNSET
    support_access: bool | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    system_domain_name: None | str | Unset = UNSET
    tags_metadata_field: None | str | Unset = UNSET
    texts_metadata_field: None | str | Unset = UNSET
    update_saml_primary_group_on_login: bool | None | Unset = UNSET
    use_asset_name_on_download: bool | None | Unset = UNSET
    watermark: None | SystemSettingSchemaWatermark | Unset = UNSET
    watermark_options: None | Unset | WatermarkOptionsType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.default_share_options_type_schema import (
            DefaultShareOptionsTypeSchema,
        )
        from ..models.jobs_dashboard_schema import JobsDashboardSchema
        from ..models.password_checks_type_schema import PasswordChecksTypeSchema
        from ..models.watermark_options_type import WatermarkOptionsType

        acl_template_id: None | str | Unset
        if isinstance(self.acl_template_id, Unset):
            acl_template_id = UNSET
        elif isinstance(self.acl_template_id, UUID):
            acl_template_id = str(self.acl_template_id)
        else:
            acl_template_id = self.acl_template_id

        allow_invites_by_link: bool | None | Unset
        if isinstance(self.allow_invites_by_link, Unset):
            allow_invites_by_link = UNSET
        else:
            allow_invites_by_link = self.allow_invites_by_link

        allow_play_original_during_transcoding: bool | None | Unset
        if isinstance(self.allow_play_original_during_transcoding, Unset):
            allow_play_original_during_transcoding = UNSET
        else:
            allow_play_original_during_transcoding = (
                self.allow_play_original_during_transcoding
            )

        allow_share_magic_link_creation: bool | None | Unset
        if isinstance(self.allow_share_magic_link_creation, Unset):
            allow_share_magic_link_creation = UNSET
        else:
            allow_share_magic_link_creation = self.allow_share_magic_link_creation

        allowed_ips: list[dict[str, Any]] | None | Unset
        if isinstance(self.allowed_ips, Unset):
            allowed_ips = UNSET
        elif isinstance(self.allowed_ips, list):
            allowed_ips = []
            for allowed_ips_type_0_item_data in self.allowed_ips:
                allowed_ips_type_0_item = allowed_ips_type_0_item_data.to_dict()
                allowed_ips.append(allowed_ips_type_0_item)

        else:
            allowed_ips = self.allowed_ips

        append_asset_uuid_to_downloads: bool | None | Unset
        if isinstance(self.append_asset_uuid_to_downloads, Unset):
            append_asset_uuid_to_downloads = UNSET
        else:
            append_asset_uuid_to_downloads = self.append_asset_uuid_to_downloads

        asset_default_sections: list[str] | None | Unset
        if isinstance(self.asset_default_sections, Unset):
            asset_default_sections = UNSET
        elif isinstance(self.asset_default_sections, list):
            asset_default_sections = self.asset_default_sections

        else:
            asset_default_sections = self.asset_default_sections

        client_ip: None | str | Unset
        if isinstance(self.client_ip, Unset):
            client_ip = UNSET
        else:
            client_ip = self.client_ip

        collections_get_parent_acls: bool | None | Unset
        if isinstance(self.collections_get_parent_acls, Unset):
            collections_get_parent_acls = UNSET
        else:
            collections_get_parent_acls = self.collections_get_parent_acls

        cors_hosts: list[str] | None | Unset
        if isinstance(self.cors_hosts, Unset):
            cors_hosts = UNSET
        elif isinstance(self.cors_hosts, list):
            cors_hosts = self.cors_hosts

        else:
            cors_hosts = self.cors_hosts

        date_format: None | str | Unset
        if isinstance(self.date_format, Unset):
            date_format = UNSET
        else:
            date_format = self.date_format

        datetime_format: None | str | Unset
        if isinstance(self.datetime_format, Unset):
            datetime_format = UNSET
        else:
            datetime_format = self.datetime_format

        default_app_token_ttl: int | None | Unset
        if isinstance(self.default_app_token_ttl, Unset):
            default_app_token_ttl = UNSET
        else:
            default_app_token_ttl = self.default_app_token_ttl

        default_refresh_token_ttl: int | None | Unset
        if isinstance(self.default_refresh_token_ttl, Unset):
            default_refresh_token_ttl = UNSET
        else:
            default_refresh_token_ttl = self.default_refresh_token_ttl

        default_share_options: dict[str, Any] | None | Unset
        if isinstance(self.default_share_options, Unset):
            default_share_options = UNSET
        elif isinstance(self.default_share_options, DefaultShareOptionsTypeSchema):
            default_share_options = self.default_share_options.to_dict()
        else:
            default_share_options = self.default_share_options

        default_upload_storage_id: None | str | Unset
        if isinstance(self.default_upload_storage_id, Unset):
            default_upload_storage_id = UNSET
        elif isinstance(self.default_upload_storage_id, UUID):
            default_upload_storage_id = str(self.default_upload_storage_id)
        else:
            default_upload_storage_id = self.default_upload_storage_id

        default_user_token_ttl: int | None | Unset
        if isinstance(self.default_user_token_ttl, Unset):
            default_user_token_ttl = UNSET
        else:
            default_user_token_ttl = self.default_user_token_ttl

        delete_grace_period: int | None | Unset
        if isinstance(self.delete_grace_period, Unset):
            delete_grace_period = UNSET
        else:
            delete_grace_period = self.delete_grace_period

        drm: None | str | Unset
        if isinstance(self.drm, Unset):
            drm = UNSET
        elif isinstance(self.drm, SystemSettingSchemaDrm):
            drm = self.drm.value
        else:
            drm = self.drm

        drm_enforce: bool | None | Unset
        if isinstance(self.drm_enforce, Unset):
            drm_enforce = UNSET
        else:
            drm_enforce = self.drm_enforce

        enable_ai_metadata_filling: bool | None | Unset
        if isinstance(self.enable_ai_metadata_filling, Unset):
            enable_ai_metadata_filling = UNSET
        else:
            enable_ai_metadata_filling = self.enable_ai_metadata_filling

        enable_face_recognition: bool | None | Unset
        if isinstance(self.enable_face_recognition, Unset):
            enable_face_recognition = UNSET
        else:
            enable_face_recognition = self.enable_face_recognition

        enable_nltf: bool | None | Unset
        if isinstance(self.enable_nltf, Unset):
            enable_nltf = UNSET
        else:
            enable_nltf = self.enable_nltf

        enable_shield: bool | None | Unset
        if isinstance(self.enable_shield, Unset):
            enable_shield = UNSET
        else:
            enable_shield = self.enable_shield

        enforce_magic_link_allowlist: bool | None | Unset
        if isinstance(self.enforce_magic_link_allowlist, Unset):
            enforce_magic_link_allowlist = UNSET
        else:
            enforce_magic_link_allowlist = self.enforce_magic_link_allowlist

        external_share: bool | None | Unset
        if isinstance(self.external_share, Unset):
            external_share = UNSET
        else:
            external_share = self.external_share

        facet_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.facet_fields, Unset):
            facet_fields = UNSET
        elif isinstance(self.facet_fields, list):
            facet_fields = []
            for facet_fields_type_0_item_data in self.facet_fields:
                facet_fields_type_0_item = facet_fields_type_0_item_data.to_dict()
                facet_fields.append(facet_fields_type_0_item)

        else:
            facet_fields = self.facet_fields

        filters_default_metadata_view_id: None | str | Unset
        if isinstance(self.filters_default_metadata_view_id, Unset):
            filters_default_metadata_view_id = UNSET
        elif isinstance(self.filters_default_metadata_view_id, UUID):
            filters_default_metadata_view_id = str(
                self.filters_default_metadata_view_id
            )
        else:
            filters_default_metadata_view_id = self.filters_default_metadata_view_id

        hide_favourites: bool | None | Unset
        if isinstance(self.hide_favourites, Unset):
            hide_favourites = UNSET
        else:
            hide_favourites = self.hide_favourites

        home_page: None | str | Unset
        if isinstance(self.home_page, Unset):
            home_page = UNSET
        else:
            home_page = self.home_page

        image_properties_metadata_field: None | str | Unset
        if isinstance(self.image_properties_metadata_field, Unset):
            image_properties_metadata_field = UNSET
        else:
            image_properties_metadata_field = self.image_properties_metadata_field

        jobs_dashboard: dict[str, Any] | None | Unset
        if isinstance(self.jobs_dashboard, Unset):
            jobs_dashboard = UNSET
        elif isinstance(self.jobs_dashboard, JobsDashboardSchema):
            jobs_dashboard = self.jobs_dashboard.to_dict()
        else:
            jobs_dashboard = self.jobs_dashboard

        locations_metadata_field: None | str | Unset
        if isinstance(self.locations_metadata_field, Unset):
            locations_metadata_field = UNSET
        else:
            locations_metadata_field = self.locations_metadata_field

        lock_mapped_collections: bool | None | Unset
        if isinstance(self.lock_mapped_collections, Unset):
            lock_mapped_collections = UNSET
        else:
            lock_mapped_collections = self.lock_mapped_collections

        logo_storage_id: None | str | Unset
        if isinstance(self.logo_storage_id, Unset):
            logo_storage_id = UNSET
        elif isinstance(self.logo_storage_id, UUID):
            logo_storage_id = str(self.logo_storage_id)
        else:
            logo_storage_id = self.logo_storage_id

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        logos_metadata_field: None | str | Unset
        if isinstance(self.logos_metadata_field, Unset):
            logos_metadata_field = UNSET
        else:
            logos_metadata_field = self.logos_metadata_field

        max_browse_users: int | None | Unset
        if isinstance(self.max_browse_users, Unset):
            max_browse_users = UNSET
        else:
            max_browse_users = self.max_browse_users

        max_power_users: int | None | Unset
        if isinstance(self.max_power_users, Unset):
            max_power_users = UNSET
        else:
            max_power_users = self.max_power_users

        max_standard_users: int | None | Unset
        if isinstance(self.max_standard_users, Unset):
            max_standard_users = UNSET
        else:
            max_standard_users = self.max_standard_users

        max_storage_bytes: int | None | Unset
        if isinstance(self.max_storage_bytes, Unset):
            max_storage_bytes = UNSET
        else:
            max_storage_bytes = self.max_storage_bytes

        max_traffic_bytes: int | None | Unset
        if isinstance(self.max_traffic_bytes, Unset):
            max_traffic_bytes = UNSET
        else:
            max_traffic_bytes = self.max_traffic_bytes

        mfa_methods: list[str] | None | Unset
        if isinstance(self.mfa_methods, Unset):
            mfa_methods = UNSET
        elif isinstance(self.mfa_methods, list):
            mfa_methods = []
            for mfa_methods_type_0_item_data in self.mfa_methods:
                mfa_methods_type_0_item = mfa_methods_type_0_item_data.value
                mfa_methods.append(mfa_methods_type_0_item)

        else:
            mfa_methods = self.mfa_methods

        mfa_required: bool | None | Unset
        if isinstance(self.mfa_required, Unset):
            mfa_required = UNSET
        else:
            mfa_required = self.mfa_required

        password_checks: dict[str, Any] | None | Unset
        if isinstance(self.password_checks, Unset):
            password_checks = UNSET
        elif isinstance(self.password_checks, PasswordChecksTypeSchema):
            password_checks = self.password_checks.to_dict()
        else:
            password_checks = self.password_checks

        require_limit_download_groups: bool | None | Unset
        if isinstance(self.require_limit_download_groups, Unset):
            require_limit_download_groups = UNSET
        else:
            require_limit_download_groups = self.require_limit_download_groups

        required_metadata_views: list[str] | None | Unset
        if isinstance(self.required_metadata_views, Unset):
            required_metadata_views = UNSET
        elif isinstance(self.required_metadata_views, list):
            required_metadata_views = self.required_metadata_views

        else:
            required_metadata_views = self.required_metadata_views

        review_experience_disabled: bool | None | Unset
        if isinstance(self.review_experience_disabled, Unset):
            review_experience_disabled = UNSET
        else:
            review_experience_disabled = self.review_experience_disabled

        review_experience_disabled_per_share: bool | None | Unset
        if isinstance(self.review_experience_disabled_per_share, Unset):
            review_experience_disabled_per_share = UNSET
        else:
            review_experience_disabled_per_share = (
                self.review_experience_disabled_per_share
            )

        safe_searches_metadata_field: None | str | Unset
        if isinstance(self.safe_searches_metadata_field, Unset):
            safe_searches_metadata_field = UNSET
        else:
            safe_searches_metadata_field = self.safe_searches_metadata_field

        saml_require_groups: bool | None | Unset
        if isinstance(self.saml_require_groups, Unset):
            saml_require_groups = UNSET
        else:
            saml_require_groups = self.saml_require_groups

        search_auto_resize_title_column: bool | None | Unset
        if isinstance(self.search_auto_resize_title_column, Unset):
            search_auto_resize_title_column = UNSET
        else:
            search_auto_resize_title_column = self.search_auto_resize_title_column

        search_default_sections: list[str] | None | Unset
        if isinstance(self.search_default_sections, Unset):
            search_default_sections = UNSET
        elif isinstance(self.search_default_sections, list):
            search_default_sections = self.search_default_sections

        else:
            search_default_sections = self.search_default_sections

        search_display_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.search_display_fields, Unset):
            search_display_fields = UNSET
        elif isinstance(self.search_display_fields, list):
            search_display_fields = []
            for search_display_fields_type_0_item_data in self.search_display_fields:
                search_display_fields_type_0_item = (
                    search_display_fields_type_0_item_data.to_dict()
                )
                search_display_fields.append(search_display_fields_type_0_item)

        else:
            search_display_fields = self.search_display_fields

        search_in_transcriptions: bool | None | Unset
        if isinstance(self.search_in_transcriptions, Unset):
            search_in_transcriptions = UNSET
        else:
            search_in_transcriptions = self.search_in_transcriptions

        search_results_asset_metadata_view_id: None | str | Unset
        if isinstance(self.search_results_asset_metadata_view_id, Unset):
            search_results_asset_metadata_view_id = UNSET
        elif isinstance(self.search_results_asset_metadata_view_id, UUID):
            search_results_asset_metadata_view_id = str(
                self.search_results_asset_metadata_view_id
            )
        else:
            search_results_asset_metadata_view_id = (
                self.search_results_asset_metadata_view_id
            )

        search_results_collection_metadata_view_id: None | str | Unset
        if isinstance(self.search_results_collection_metadata_view_id, Unset):
            search_results_collection_metadata_view_id = UNSET
        elif isinstance(self.search_results_collection_metadata_view_id, UUID):
            search_results_collection_metadata_view_id = str(
                self.search_results_collection_metadata_view_id
            )
        else:
            search_results_collection_metadata_view_id = (
                self.search_results_collection_metadata_view_id
            )

        search_users_from_share: bool | None | Unset
        if isinstance(self.search_users_from_share, Unset):
            search_users_from_share = UNSET
        else:
            search_users_from_share = self.search_users_from_share

        share_expiration_time: int | None | Unset
        if isinstance(self.share_expiration_time, Unset):
            share_expiration_time = UNSET
        else:
            share_expiration_time = self.share_expiration_time

        support_access: bool | None | Unset
        if isinstance(self.support_access, Unset):
            support_access = UNSET
        else:
            support_access = self.support_access

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        system_domain_name: None | str | Unset
        if isinstance(self.system_domain_name, Unset):
            system_domain_name = UNSET
        else:
            system_domain_name = self.system_domain_name

        tags_metadata_field: None | str | Unset
        if isinstance(self.tags_metadata_field, Unset):
            tags_metadata_field = UNSET
        else:
            tags_metadata_field = self.tags_metadata_field

        texts_metadata_field: None | str | Unset
        if isinstance(self.texts_metadata_field, Unset):
            texts_metadata_field = UNSET
        else:
            texts_metadata_field = self.texts_metadata_field

        update_saml_primary_group_on_login: bool | None | Unset
        if isinstance(self.update_saml_primary_group_on_login, Unset):
            update_saml_primary_group_on_login = UNSET
        else:
            update_saml_primary_group_on_login = self.update_saml_primary_group_on_login

        use_asset_name_on_download: bool | None | Unset
        if isinstance(self.use_asset_name_on_download, Unset):
            use_asset_name_on_download = UNSET
        else:
            use_asset_name_on_download = self.use_asset_name_on_download

        watermark: None | str | Unset
        if isinstance(self.watermark, Unset):
            watermark = UNSET
        elif isinstance(self.watermark, SystemSettingSchemaWatermark):
            watermark = self.watermark.value
        else:
            watermark = self.watermark

        watermark_options: dict[str, Any] | None | Unset
        if isinstance(self.watermark_options, Unset):
            watermark_options = UNSET
        elif isinstance(self.watermark_options, WatermarkOptionsType):
            watermark_options = self.watermark_options.to_dict()
        else:
            watermark_options = self.watermark_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acl_template_id is not UNSET:
            field_dict["acl_template_id"] = acl_template_id
        if allow_invites_by_link is not UNSET:
            field_dict["allow_invites_by_link"] = allow_invites_by_link
        if allow_play_original_during_transcoding is not UNSET:
            field_dict["allow_play_original_during_transcoding"] = (
                allow_play_original_during_transcoding
            )
        if allow_share_magic_link_creation is not UNSET:
            field_dict["allow_share_magic_link_creation"] = (
                allow_share_magic_link_creation
            )
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips
        if append_asset_uuid_to_downloads is not UNSET:
            field_dict["append_asset_uuid_to_downloads"] = (
                append_asset_uuid_to_downloads
            )
        if asset_default_sections is not UNSET:
            field_dict["asset_default_sections"] = asset_default_sections
        if client_ip is not UNSET:
            field_dict["client_ip"] = client_ip
        if collections_get_parent_acls is not UNSET:
            field_dict["collections_get_parent_acls"] = collections_get_parent_acls
        if cors_hosts is not UNSET:
            field_dict["cors_hosts"] = cors_hosts
        if date_format is not UNSET:
            field_dict["date_format"] = date_format
        if datetime_format is not UNSET:
            field_dict["datetime_format"] = datetime_format
        if default_app_token_ttl is not UNSET:
            field_dict["default_app_token_ttl"] = default_app_token_ttl
        if default_refresh_token_ttl is not UNSET:
            field_dict["default_refresh_token_ttl"] = default_refresh_token_ttl
        if default_share_options is not UNSET:
            field_dict["default_share_options"] = default_share_options
        if default_upload_storage_id is not UNSET:
            field_dict["default_upload_storage_id"] = default_upload_storage_id
        if default_user_token_ttl is not UNSET:
            field_dict["default_user_token_ttl"] = default_user_token_ttl
        if delete_grace_period is not UNSET:
            field_dict["delete_grace_period"] = delete_grace_period
        if drm is not UNSET:
            field_dict["drm"] = drm
        if drm_enforce is not UNSET:
            field_dict["drm_enforce"] = drm_enforce
        if enable_ai_metadata_filling is not UNSET:
            field_dict["enable_ai_metadata_filling"] = enable_ai_metadata_filling
        if enable_face_recognition is not UNSET:
            field_dict["enable_face_recognition"] = enable_face_recognition
        if enable_nltf is not UNSET:
            field_dict["enable_nltf"] = enable_nltf
        if enable_shield is not UNSET:
            field_dict["enable_shield"] = enable_shield
        if enforce_magic_link_allowlist is not UNSET:
            field_dict["enforce_magic_link_allowlist"] = enforce_magic_link_allowlist
        if external_share is not UNSET:
            field_dict["external_share"] = external_share
        if facet_fields is not UNSET:
            field_dict["facet_fields"] = facet_fields
        if filters_default_metadata_view_id is not UNSET:
            field_dict["filters_default_metadata_view_id"] = (
                filters_default_metadata_view_id
            )
        if hide_favourites is not UNSET:
            field_dict["hide_favourites"] = hide_favourites
        if home_page is not UNSET:
            field_dict["home_page"] = home_page
        if image_properties_metadata_field is not UNSET:
            field_dict["image_properties_metadata_field"] = (
                image_properties_metadata_field
            )
        if jobs_dashboard is not UNSET:
            field_dict["jobs_dashboard"] = jobs_dashboard
        if locations_metadata_field is not UNSET:
            field_dict["locations_metadata_field"] = locations_metadata_field
        if lock_mapped_collections is not UNSET:
            field_dict["lock_mapped_collections"] = lock_mapped_collections
        if logo_storage_id is not UNSET:
            field_dict["logo_storage_id"] = logo_storage_id
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if logos_metadata_field is not UNSET:
            field_dict["logos_metadata_field"] = logos_metadata_field
        if max_browse_users is not UNSET:
            field_dict["max_browse_users"] = max_browse_users
        if max_power_users is not UNSET:
            field_dict["max_power_users"] = max_power_users
        if max_standard_users is not UNSET:
            field_dict["max_standard_users"] = max_standard_users
        if max_storage_bytes is not UNSET:
            field_dict["max_storage_bytes"] = max_storage_bytes
        if max_traffic_bytes is not UNSET:
            field_dict["max_traffic_bytes"] = max_traffic_bytes
        if mfa_methods is not UNSET:
            field_dict["mfa_methods"] = mfa_methods
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required
        if password_checks is not UNSET:
            field_dict["password_checks"] = password_checks
        if require_limit_download_groups is not UNSET:
            field_dict["require_limit_download_groups"] = require_limit_download_groups
        if required_metadata_views is not UNSET:
            field_dict["required_metadata_views"] = required_metadata_views
        if review_experience_disabled is not UNSET:
            field_dict["review_experience_disabled"] = review_experience_disabled
        if review_experience_disabled_per_share is not UNSET:
            field_dict["review_experience_disabled_per_share"] = (
                review_experience_disabled_per_share
            )
        if safe_searches_metadata_field is not UNSET:
            field_dict["safe_searches_metadata_field"] = safe_searches_metadata_field
        if saml_require_groups is not UNSET:
            field_dict["saml_require_groups"] = saml_require_groups
        if search_auto_resize_title_column is not UNSET:
            field_dict["search_auto_resize_title_column"] = (
                search_auto_resize_title_column
            )
        if search_default_sections is not UNSET:
            field_dict["search_default_sections"] = search_default_sections
        if search_display_fields is not UNSET:
            field_dict["search_display_fields"] = search_display_fields
        if search_in_transcriptions is not UNSET:
            field_dict["search_in_transcriptions"] = search_in_transcriptions
        if search_results_asset_metadata_view_id is not UNSET:
            field_dict["search_results_asset_metadata_view_id"] = (
                search_results_asset_metadata_view_id
            )
        if search_results_collection_metadata_view_id is not UNSET:
            field_dict["search_results_collection_metadata_view_id"] = (
                search_results_collection_metadata_view_id
            )
        if search_users_from_share is not UNSET:
            field_dict["search_users_from_share"] = search_users_from_share
        if share_expiration_time is not UNSET:
            field_dict["share_expiration_time"] = share_expiration_time
        if support_access is not UNSET:
            field_dict["support_access"] = support_access
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if system_domain_name is not UNSET:
            field_dict["system_domain_name"] = system_domain_name
        if tags_metadata_field is not UNSET:
            field_dict["tags_metadata_field"] = tags_metadata_field
        if texts_metadata_field is not UNSET:
            field_dict["texts_metadata_field"] = texts_metadata_field
        if update_saml_primary_group_on_login is not UNSET:
            field_dict["update_saml_primary_group_on_login"] = (
                update_saml_primary_group_on_login
            )
        if use_asset_name_on_download is not UNSET:
            field_dict["use_asset_name_on_download"] = use_asset_name_on_download
        if watermark is not UNSET:
            field_dict["watermark"] = watermark
        if watermark_options is not UNSET:
            field_dict["watermark_options"] = watermark_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_ip_schema import AllowedIPSchema
        from ..models.default_share_options_type_schema import (
            DefaultShareOptionsTypeSchema,
        )
        from ..models.facet_field_schema import FacetFieldSchema
        from ..models.jobs_dashboard_schema import JobsDashboardSchema
        from ..models.password_checks_type_schema import PasswordChecksTypeSchema
        from ..models.search_display_field_schema import SearchDisplayFieldSchema
        from ..models.watermark_options_type import WatermarkOptionsType

        d = dict(src_dict)

        def _parse_acl_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acl_template_id_type_0 = UUID(data)

                return acl_template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        acl_template_id = _parse_acl_template_id(d.pop("acl_template_id", UNSET))

        def _parse_allow_invites_by_link(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_invites_by_link = _parse_allow_invites_by_link(
            d.pop("allow_invites_by_link", UNSET)
        )

        def _parse_allow_play_original_during_transcoding(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_play_original_during_transcoding = (
            _parse_allow_play_original_during_transcoding(
                d.pop("allow_play_original_during_transcoding", UNSET)
            )
        )

        def _parse_allow_share_magic_link_creation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_share_magic_link_creation = _parse_allow_share_magic_link_creation(
            d.pop("allow_share_magic_link_creation", UNSET)
        )

        def _parse_allowed_ips(data: object) -> list[AllowedIPSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_ips_type_0 = []
                _allowed_ips_type_0 = data
                for allowed_ips_type_0_item_data in _allowed_ips_type_0:
                    allowed_ips_type_0_item = AllowedIPSchema.from_dict(
                        allowed_ips_type_0_item_data
                    )

                    allowed_ips_type_0.append(allowed_ips_type_0_item)

                return allowed_ips_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AllowedIPSchema] | None | Unset, data)

        allowed_ips = _parse_allowed_ips(d.pop("allowed_ips", UNSET))

        def _parse_append_asset_uuid_to_downloads(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        append_asset_uuid_to_downloads = _parse_append_asset_uuid_to_downloads(
            d.pop("append_asset_uuid_to_downloads", UNSET)
        )

        def _parse_asset_default_sections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_default_sections_type_0 = cast(list[str], data)

                return asset_default_sections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        asset_default_sections = _parse_asset_default_sections(
            d.pop("asset_default_sections", UNSET)
        )

        def _parse_client_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_ip = _parse_client_ip(d.pop("client_ip", UNSET))

        def _parse_collections_get_parent_acls(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        collections_get_parent_acls = _parse_collections_get_parent_acls(
            d.pop("collections_get_parent_acls", UNSET)
        )

        def _parse_cors_hosts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cors_hosts_type_0 = cast(list[str], data)

                return cors_hosts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cors_hosts = _parse_cors_hosts(d.pop("cors_hosts", UNSET))

        def _parse_date_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_format = _parse_date_format(d.pop("date_format", UNSET))

        def _parse_datetime_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datetime_format = _parse_datetime_format(d.pop("datetime_format", UNSET))

        def _parse_default_app_token_ttl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_app_token_ttl = _parse_default_app_token_ttl(
            d.pop("default_app_token_ttl", UNSET)
        )

        def _parse_default_refresh_token_ttl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_refresh_token_ttl = _parse_default_refresh_token_ttl(
            d.pop("default_refresh_token_ttl", UNSET)
        )

        def _parse_default_share_options(
            data: object,
        ) -> DefaultShareOptionsTypeSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_share_options_type_1 = DefaultShareOptionsTypeSchema.from_dict(
                    data
                )

                return default_share_options_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DefaultShareOptionsTypeSchema | None | Unset, data)

        default_share_options = _parse_default_share_options(
            d.pop("default_share_options", UNSET)
        )

        def _parse_default_upload_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_upload_storage_id_type_0 = UUID(data)

                return default_upload_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_upload_storage_id = _parse_default_upload_storage_id(
            d.pop("default_upload_storage_id", UNSET)
        )

        def _parse_default_user_token_ttl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_user_token_ttl = _parse_default_user_token_ttl(
            d.pop("default_user_token_ttl", UNSET)
        )

        def _parse_delete_grace_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        delete_grace_period = _parse_delete_grace_period(
            d.pop("delete_grace_period", UNSET)
        )

        def _parse_drm(data: object) -> None | SystemSettingSchemaDrm | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                drm_type_1 = SystemSettingSchemaDrm(data)

                return drm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemSettingSchemaDrm | Unset, data)

        drm = _parse_drm(d.pop("drm", UNSET))

        def _parse_drm_enforce(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        drm_enforce = _parse_drm_enforce(d.pop("drm_enforce", UNSET))

        def _parse_enable_ai_metadata_filling(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_ai_metadata_filling = _parse_enable_ai_metadata_filling(
            d.pop("enable_ai_metadata_filling", UNSET)
        )

        def _parse_enable_face_recognition(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_face_recognition = _parse_enable_face_recognition(
            d.pop("enable_face_recognition", UNSET)
        )

        def _parse_enable_nltf(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_nltf = _parse_enable_nltf(d.pop("enable_nltf", UNSET))

        def _parse_enable_shield(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_shield = _parse_enable_shield(d.pop("enable_shield", UNSET))

        def _parse_enforce_magic_link_allowlist(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enforce_magic_link_allowlist = _parse_enforce_magic_link_allowlist(
            d.pop("enforce_magic_link_allowlist", UNSET)
        )

        def _parse_external_share(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        external_share = _parse_external_share(d.pop("external_share", UNSET))

        def _parse_facet_fields(data: object) -> list[FacetFieldSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facet_fields_type_0 = []
                _facet_fields_type_0 = data
                for facet_fields_type_0_item_data in _facet_fields_type_0:
                    facet_fields_type_0_item = FacetFieldSchema.from_dict(
                        facet_fields_type_0_item_data
                    )

                    facet_fields_type_0.append(facet_fields_type_0_item)

                return facet_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FacetFieldSchema] | None | Unset, data)

        facet_fields = _parse_facet_fields(d.pop("facet_fields", UNSET))

        def _parse_filters_default_metadata_view_id(
            data: object,
        ) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                filters_default_metadata_view_id_type_0 = UUID(data)

                return filters_default_metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        filters_default_metadata_view_id = _parse_filters_default_metadata_view_id(
            d.pop("filters_default_metadata_view_id", UNSET)
        )

        def _parse_hide_favourites(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_favourites = _parse_hide_favourites(d.pop("hide_favourites", UNSET))

        def _parse_home_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_page = _parse_home_page(d.pop("home_page", UNSET))

        def _parse_image_properties_metadata_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_properties_metadata_field = _parse_image_properties_metadata_field(
            d.pop("image_properties_metadata_field", UNSET)
        )

        def _parse_jobs_dashboard(data: object) -> JobsDashboardSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                jobs_dashboard_type_1 = JobsDashboardSchema.from_dict(data)

                return jobs_dashboard_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobsDashboardSchema | None | Unset, data)

        jobs_dashboard = _parse_jobs_dashboard(d.pop("jobs_dashboard", UNSET))

        def _parse_locations_metadata_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locations_metadata_field = _parse_locations_metadata_field(
            d.pop("locations_metadata_field", UNSET)
        )

        def _parse_lock_mapped_collections(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        lock_mapped_collections = _parse_lock_mapped_collections(
            d.pop("lock_mapped_collections", UNSET)
        )

        def _parse_logo_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logo_storage_id_type_0 = UUID(data)

                return logo_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        logo_storage_id = _parse_logo_storage_id(d.pop("logo_storage_id", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_logos_metadata_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logos_metadata_field = _parse_logos_metadata_field(
            d.pop("logos_metadata_field", UNSET)
        )

        def _parse_max_browse_users(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_browse_users = _parse_max_browse_users(d.pop("max_browse_users", UNSET))

        def _parse_max_power_users(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_power_users = _parse_max_power_users(d.pop("max_power_users", UNSET))

        def _parse_max_standard_users(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_standard_users = _parse_max_standard_users(
            d.pop("max_standard_users", UNSET)
        )

        def _parse_max_storage_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_storage_bytes = _parse_max_storage_bytes(d.pop("max_storage_bytes", UNSET))

        def _parse_max_traffic_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_traffic_bytes = _parse_max_traffic_bytes(d.pop("max_traffic_bytes", UNSET))

        def _parse_mfa_methods(
            data: object,
        ) -> list[SystemSettingSchemaMfaMethodsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mfa_methods_type_0 = []
                _mfa_methods_type_0 = data
                for mfa_methods_type_0_item_data in _mfa_methods_type_0:
                    mfa_methods_type_0_item = SystemSettingSchemaMfaMethodsType0Item(
                        mfa_methods_type_0_item_data
                    )

                    mfa_methods_type_0.append(mfa_methods_type_0_item)

                return mfa_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SystemSettingSchemaMfaMethodsType0Item] | None | Unset, data
            )

        mfa_methods = _parse_mfa_methods(d.pop("mfa_methods", UNSET))

        def _parse_mfa_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mfa_required = _parse_mfa_required(d.pop("mfa_required", UNSET))

        def _parse_password_checks(
            data: object,
        ) -> None | PasswordChecksTypeSchema | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                password_checks_type_1 = PasswordChecksTypeSchema.from_dict(data)

                return password_checks_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PasswordChecksTypeSchema | Unset, data)

        password_checks = _parse_password_checks(d.pop("password_checks", UNSET))

        def _parse_require_limit_download_groups(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        require_limit_download_groups = _parse_require_limit_download_groups(
            d.pop("require_limit_download_groups", UNSET)
        )

        def _parse_required_metadata_views(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_metadata_views_type_0 = cast(list[str], data)

                return required_metadata_views_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        required_metadata_views = _parse_required_metadata_views(
            d.pop("required_metadata_views", UNSET)
        )

        def _parse_review_experience_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        review_experience_disabled = _parse_review_experience_disabled(
            d.pop("review_experience_disabled", UNSET)
        )

        def _parse_review_experience_disabled_per_share(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        review_experience_disabled_per_share = (
            _parse_review_experience_disabled_per_share(
                d.pop("review_experience_disabled_per_share", UNSET)
            )
        )

        def _parse_safe_searches_metadata_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        safe_searches_metadata_field = _parse_safe_searches_metadata_field(
            d.pop("safe_searches_metadata_field", UNSET)
        )

        def _parse_saml_require_groups(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        saml_require_groups = _parse_saml_require_groups(
            d.pop("saml_require_groups", UNSET)
        )

        def _parse_search_auto_resize_title_column(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        search_auto_resize_title_column = _parse_search_auto_resize_title_column(
            d.pop("search_auto_resize_title_column", UNSET)
        )

        def _parse_search_default_sections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                search_default_sections_type_0 = cast(list[str], data)

                return search_default_sections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        search_default_sections = _parse_search_default_sections(
            d.pop("search_default_sections", UNSET)
        )

        def _parse_search_display_fields(
            data: object,
        ) -> list[SearchDisplayFieldSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                search_display_fields_type_0 = []
                _search_display_fields_type_0 = data
                for (
                    search_display_fields_type_0_item_data
                ) in _search_display_fields_type_0:
                    search_display_fields_type_0_item = (
                        SearchDisplayFieldSchema.from_dict(
                            search_display_fields_type_0_item_data
                        )
                    )

                    search_display_fields_type_0.append(
                        search_display_fields_type_0_item
                    )

                return search_display_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SearchDisplayFieldSchema] | None | Unset, data)

        search_display_fields = _parse_search_display_fields(
            d.pop("search_display_fields", UNSET)
        )

        def _parse_search_in_transcriptions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        search_in_transcriptions = _parse_search_in_transcriptions(
            d.pop("search_in_transcriptions", UNSET)
        )

        def _parse_search_results_asset_metadata_view_id(
            data: object,
        ) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                search_results_asset_metadata_view_id_type_0 = UUID(data)

                return search_results_asset_metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        search_results_asset_metadata_view_id = (
            _parse_search_results_asset_metadata_view_id(
                d.pop("search_results_asset_metadata_view_id", UNSET)
            )
        )

        def _parse_search_results_collection_metadata_view_id(
            data: object,
        ) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                search_results_collection_metadata_view_id_type_0 = UUID(data)

                return search_results_collection_metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        search_results_collection_metadata_view_id = (
            _parse_search_results_collection_metadata_view_id(
                d.pop("search_results_collection_metadata_view_id", UNSET)
            )
        )

        def _parse_search_users_from_share(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        search_users_from_share = _parse_search_users_from_share(
            d.pop("search_users_from_share", UNSET)
        )

        def _parse_share_expiration_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        share_expiration_time = _parse_share_expiration_time(
            d.pop("share_expiration_time", UNSET)
        )

        def _parse_support_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        support_access = _parse_support_access(d.pop("support_access", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        def _parse_system_domain_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_domain_name = _parse_system_domain_name(
            d.pop("system_domain_name", UNSET)
        )

        def _parse_tags_metadata_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tags_metadata_field = _parse_tags_metadata_field(
            d.pop("tags_metadata_field", UNSET)
        )

        def _parse_texts_metadata_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        texts_metadata_field = _parse_texts_metadata_field(
            d.pop("texts_metadata_field", UNSET)
        )

        def _parse_update_saml_primary_group_on_login(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        update_saml_primary_group_on_login = _parse_update_saml_primary_group_on_login(
            d.pop("update_saml_primary_group_on_login", UNSET)
        )

        def _parse_use_asset_name_on_download(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_asset_name_on_download = _parse_use_asset_name_on_download(
            d.pop("use_asset_name_on_download", UNSET)
        )

        def _parse_watermark(
            data: object,
        ) -> None | SystemSettingSchemaWatermark | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                watermark_type_1 = SystemSettingSchemaWatermark(data)

                return watermark_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemSettingSchemaWatermark | Unset, data)

        watermark = _parse_watermark(d.pop("watermark", UNSET))

        def _parse_watermark_options(
            data: object,
        ) -> None | Unset | WatermarkOptionsType:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                watermark_options_type_1 = WatermarkOptionsType.from_dict(data)

                return watermark_options_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WatermarkOptionsType, data)

        watermark_options = _parse_watermark_options(d.pop("watermark_options", UNSET))

        system_setting_schema = cls(
            acl_template_id=acl_template_id,
            allow_invites_by_link=allow_invites_by_link,
            allow_play_original_during_transcoding=allow_play_original_during_transcoding,
            allow_share_magic_link_creation=allow_share_magic_link_creation,
            allowed_ips=allowed_ips,
            append_asset_uuid_to_downloads=append_asset_uuid_to_downloads,
            asset_default_sections=asset_default_sections,
            client_ip=client_ip,
            collections_get_parent_acls=collections_get_parent_acls,
            cors_hosts=cors_hosts,
            date_format=date_format,
            datetime_format=datetime_format,
            default_app_token_ttl=default_app_token_ttl,
            default_refresh_token_ttl=default_refresh_token_ttl,
            default_share_options=default_share_options,
            default_upload_storage_id=default_upload_storage_id,
            default_user_token_ttl=default_user_token_ttl,
            delete_grace_period=delete_grace_period,
            drm=drm,
            drm_enforce=drm_enforce,
            enable_ai_metadata_filling=enable_ai_metadata_filling,
            enable_face_recognition=enable_face_recognition,
            enable_nltf=enable_nltf,
            enable_shield=enable_shield,
            enforce_magic_link_allowlist=enforce_magic_link_allowlist,
            external_share=external_share,
            facet_fields=facet_fields,
            filters_default_metadata_view_id=filters_default_metadata_view_id,
            hide_favourites=hide_favourites,
            home_page=home_page,
            image_properties_metadata_field=image_properties_metadata_field,
            jobs_dashboard=jobs_dashboard,
            locations_metadata_field=locations_metadata_field,
            lock_mapped_collections=lock_mapped_collections,
            logo_storage_id=logo_storage_id,
            logo_url=logo_url,
            logos_metadata_field=logos_metadata_field,
            max_browse_users=max_browse_users,
            max_power_users=max_power_users,
            max_standard_users=max_standard_users,
            max_storage_bytes=max_storage_bytes,
            max_traffic_bytes=max_traffic_bytes,
            mfa_methods=mfa_methods,
            mfa_required=mfa_required,
            password_checks=password_checks,
            require_limit_download_groups=require_limit_download_groups,
            required_metadata_views=required_metadata_views,
            review_experience_disabled=review_experience_disabled,
            review_experience_disabled_per_share=review_experience_disabled_per_share,
            safe_searches_metadata_field=safe_searches_metadata_field,
            saml_require_groups=saml_require_groups,
            search_auto_resize_title_column=search_auto_resize_title_column,
            search_default_sections=search_default_sections,
            search_display_fields=search_display_fields,
            search_in_transcriptions=search_in_transcriptions,
            search_results_asset_metadata_view_id=search_results_asset_metadata_view_id,
            search_results_collection_metadata_view_id=search_results_collection_metadata_view_id,
            search_users_from_share=search_users_from_share,
            share_expiration_time=share_expiration_time,
            support_access=support_access,
            system_domain_id=system_domain_id,
            system_domain_name=system_domain_name,
            tags_metadata_field=tags_metadata_field,
            texts_metadata_field=texts_metadata_field,
            update_saml_primary_group_on_login=update_saml_primary_group_on_login,
            use_asset_name_on_download=use_asset_name_on_download,
            watermark=watermark,
            watermark_options=watermark_options,
        )

        system_setting_schema.additional_properties = d
        return system_setting_schema

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
