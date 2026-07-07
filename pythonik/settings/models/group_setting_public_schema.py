from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowed_ip_schema import AllowedIPSchema
    from ..models.facet_field_schema import FacetFieldSchema
    from ..models.jobs_dashboard import JobsDashboard
    from ..models.search_display_field import SearchDisplayField


T = TypeVar("T", bound="GroupSettingPublicSchema")


@_attrs_define
class GroupSettingPublicSchema:
    """
    Attributes:
        acl_template_id (None | Unset | UUID):
        allowed_ips (list[AllowedIPSchema] | Unset):
        append_asset_uuid_to_downloads (bool | None | Unset):
        asset_default_sections (list[str] | Unset):
        client_ip (str | Unset):
        collections_get_parent_acls (bool | None | Unset):
        date_format (None | str | Unset):
        datetime_format (None | str | Unset):
        default_upload_storage_id (None | Unset | UUID):
        delete_grace_period (int | None | Unset): Grace period that indicate how long objects will live in recycle bin.
            Unit: hours
        facet_fields (list[FacetFieldSchema] | Unset):
        filters_default_metadata_view_id (None | Unset | UUID):
        group_id (UUID | Unset):
        hide_favourites (bool | None | Unset):
        home_page (None | str | Unset):
        jobs_dashboard (JobsDashboard | None | Unset):
        logo_storage_id (None | Unset | UUID):
        logo_url (str | Unset):
        required_metadata_views (list[str] | Unset):
        search_auto_resize_title_column (bool | None | Unset):
        search_default_sections (list[str] | Unset):
        search_display_fields (list[SearchDisplayField] | Unset):
        search_in_transcriptions (bool | None | Unset):
        search_results_asset_metadata_view_id (None | Unset | UUID):
        search_results_collection_metadata_view_id (None | Unset | UUID):
        search_view_id (None | Unset | UUID):
        share_expiration_time (int | None | Unset): Default share expiration time that indicate how long share will be
            valid. Unit: days
        system_domain_id (UUID | Unset):
        use_asset_name_on_download (bool | None | Unset):
    """

    acl_template_id: None | Unset | UUID = UNSET
    allowed_ips: list[AllowedIPSchema] | Unset = UNSET
    append_asset_uuid_to_downloads: bool | None | Unset = UNSET
    asset_default_sections: list[str] | Unset = UNSET
    client_ip: str | Unset = UNSET
    collections_get_parent_acls: bool | None | Unset = UNSET
    date_format: None | str | Unset = UNSET
    datetime_format: None | str | Unset = UNSET
    default_upload_storage_id: None | Unset | UUID = UNSET
    delete_grace_period: int | None | Unset = UNSET
    facet_fields: list[FacetFieldSchema] | Unset = UNSET
    filters_default_metadata_view_id: None | Unset | UUID = UNSET
    group_id: UUID | Unset = UNSET
    hide_favourites: bool | None | Unset = UNSET
    home_page: None | str | Unset = UNSET
    jobs_dashboard: JobsDashboard | None | Unset = UNSET
    logo_storage_id: None | Unset | UUID = UNSET
    logo_url: str | Unset = UNSET
    required_metadata_views: list[str] | Unset = UNSET
    search_auto_resize_title_column: bool | None | Unset = UNSET
    search_default_sections: list[str] | Unset = UNSET
    search_display_fields: list[SearchDisplayField] | Unset = UNSET
    search_in_transcriptions: bool | None | Unset = UNSET
    search_results_asset_metadata_view_id: None | Unset | UUID = UNSET
    search_results_collection_metadata_view_id: None | Unset | UUID = UNSET
    search_view_id: None | Unset | UUID = UNSET
    share_expiration_time: int | None | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    use_asset_name_on_download: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.jobs_dashboard import JobsDashboard

        acl_template_id: None | str | Unset
        if isinstance(self.acl_template_id, Unset):
            acl_template_id = UNSET
        elif isinstance(self.acl_template_id, UUID):
            acl_template_id = str(self.acl_template_id)
        else:
            acl_template_id = self.acl_template_id

        allowed_ips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = []
            for allowed_ips_item_data in self.allowed_ips:
                allowed_ips_item = allowed_ips_item_data.to_dict()
                allowed_ips.append(allowed_ips_item)

        append_asset_uuid_to_downloads: bool | None | Unset
        if isinstance(self.append_asset_uuid_to_downloads, Unset):
            append_asset_uuid_to_downloads = UNSET
        else:
            append_asset_uuid_to_downloads = self.append_asset_uuid_to_downloads

        asset_default_sections: list[str] | Unset = UNSET
        if not isinstance(self.asset_default_sections, Unset):
            asset_default_sections = self.asset_default_sections

        client_ip = self.client_ip

        collections_get_parent_acls: bool | None | Unset
        if isinstance(self.collections_get_parent_acls, Unset):
            collections_get_parent_acls = UNSET
        else:
            collections_get_parent_acls = self.collections_get_parent_acls

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

        default_upload_storage_id: None | str | Unset
        if isinstance(self.default_upload_storage_id, Unset):
            default_upload_storage_id = UNSET
        elif isinstance(self.default_upload_storage_id, UUID):
            default_upload_storage_id = str(self.default_upload_storage_id)
        else:
            default_upload_storage_id = self.default_upload_storage_id

        delete_grace_period: int | None | Unset
        if isinstance(self.delete_grace_period, Unset):
            delete_grace_period = UNSET
        else:
            delete_grace_period = self.delete_grace_period

        facet_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.facet_fields, Unset):
            facet_fields = []
            for facet_fields_item_data in self.facet_fields:
                facet_fields_item = facet_fields_item_data.to_dict()
                facet_fields.append(facet_fields_item)

        filters_default_metadata_view_id: None | str | Unset
        if isinstance(self.filters_default_metadata_view_id, Unset):
            filters_default_metadata_view_id = UNSET
        elif isinstance(self.filters_default_metadata_view_id, UUID):
            filters_default_metadata_view_id = str(
                self.filters_default_metadata_view_id
            )
        else:
            filters_default_metadata_view_id = self.filters_default_metadata_view_id

        group_id: str | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

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

        jobs_dashboard: dict[str, Any] | None | Unset
        if isinstance(self.jobs_dashboard, Unset):
            jobs_dashboard = UNSET
        elif isinstance(self.jobs_dashboard, JobsDashboard):
            jobs_dashboard = self.jobs_dashboard.to_dict()
        else:
            jobs_dashboard = self.jobs_dashboard

        logo_storage_id: None | str | Unset
        if isinstance(self.logo_storage_id, Unset):
            logo_storage_id = UNSET
        elif isinstance(self.logo_storage_id, UUID):
            logo_storage_id = str(self.logo_storage_id)
        else:
            logo_storage_id = self.logo_storage_id

        logo_url = self.logo_url

        required_metadata_views: list[str] | Unset = UNSET
        if not isinstance(self.required_metadata_views, Unset):
            required_metadata_views = self.required_metadata_views

        search_auto_resize_title_column: bool | None | Unset
        if isinstance(self.search_auto_resize_title_column, Unset):
            search_auto_resize_title_column = UNSET
        else:
            search_auto_resize_title_column = self.search_auto_resize_title_column

        search_default_sections: list[str] | Unset = UNSET
        if not isinstance(self.search_default_sections, Unset):
            search_default_sections = self.search_default_sections

        search_display_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.search_display_fields, Unset):
            search_display_fields = []
            for search_display_fields_item_data in self.search_display_fields:
                search_display_fields_item = search_display_fields_item_data.to_dict()
                search_display_fields.append(search_display_fields_item)

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

        search_view_id: None | str | Unset
        if isinstance(self.search_view_id, Unset):
            search_view_id = UNSET
        elif isinstance(self.search_view_id, UUID):
            search_view_id = str(self.search_view_id)
        else:
            search_view_id = self.search_view_id

        share_expiration_time: int | None | Unset
        if isinstance(self.share_expiration_time, Unset):
            share_expiration_time = UNSET
        else:
            share_expiration_time = self.share_expiration_time

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        use_asset_name_on_download: bool | None | Unset
        if isinstance(self.use_asset_name_on_download, Unset):
            use_asset_name_on_download = UNSET
        else:
            use_asset_name_on_download = self.use_asset_name_on_download

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acl_template_id is not UNSET:
            field_dict["acl_template_id"] = acl_template_id
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
        if date_format is not UNSET:
            field_dict["date_format"] = date_format
        if datetime_format is not UNSET:
            field_dict["datetime_format"] = datetime_format
        if default_upload_storage_id is not UNSET:
            field_dict["default_upload_storage_id"] = default_upload_storage_id
        if delete_grace_period is not UNSET:
            field_dict["delete_grace_period"] = delete_grace_period
        if facet_fields is not UNSET:
            field_dict["facet_fields"] = facet_fields
        if filters_default_metadata_view_id is not UNSET:
            field_dict["filters_default_metadata_view_id"] = (
                filters_default_metadata_view_id
            )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if hide_favourites is not UNSET:
            field_dict["hide_favourites"] = hide_favourites
        if home_page is not UNSET:
            field_dict["home_page"] = home_page
        if jobs_dashboard is not UNSET:
            field_dict["jobs_dashboard"] = jobs_dashboard
        if logo_storage_id is not UNSET:
            field_dict["logo_storage_id"] = logo_storage_id
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if required_metadata_views is not UNSET:
            field_dict["required_metadata_views"] = required_metadata_views
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
        if search_view_id is not UNSET:
            field_dict["search_view_id"] = search_view_id
        if share_expiration_time is not UNSET:
            field_dict["share_expiration_time"] = share_expiration_time
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if use_asset_name_on_download is not UNSET:
            field_dict["use_asset_name_on_download"] = use_asset_name_on_download

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_ip_schema import AllowedIPSchema
        from ..models.facet_field_schema import FacetFieldSchema
        from ..models.jobs_dashboard import JobsDashboard
        from ..models.search_display_field import SearchDisplayField

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

        _allowed_ips = d.pop("allowed_ips", UNSET)
        allowed_ips: list[AllowedIPSchema] | Unset = UNSET
        if _allowed_ips is not UNSET:
            allowed_ips = []
            for allowed_ips_item_data in _allowed_ips:
                allowed_ips_item = AllowedIPSchema.from_dict(allowed_ips_item_data)

                allowed_ips.append(allowed_ips_item)

        def _parse_append_asset_uuid_to_downloads(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        append_asset_uuid_to_downloads = _parse_append_asset_uuid_to_downloads(
            d.pop("append_asset_uuid_to_downloads", UNSET)
        )

        asset_default_sections = cast(list[str], d.pop("asset_default_sections", UNSET))

        client_ip = d.pop("client_ip", UNSET)

        def _parse_collections_get_parent_acls(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        collections_get_parent_acls = _parse_collections_get_parent_acls(
            d.pop("collections_get_parent_acls", UNSET)
        )

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

        def _parse_delete_grace_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        delete_grace_period = _parse_delete_grace_period(
            d.pop("delete_grace_period", UNSET)
        )

        _facet_fields = d.pop("facet_fields", UNSET)
        facet_fields: list[FacetFieldSchema] | Unset = UNSET
        if _facet_fields is not UNSET:
            facet_fields = []
            for facet_fields_item_data in _facet_fields:
                facet_fields_item = FacetFieldSchema.from_dict(facet_fields_item_data)

                facet_fields.append(facet_fields_item)

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

        _group_id = d.pop("group_id", UNSET)
        group_id: UUID | Unset
        if isinstance(_group_id, Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)

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

        def _parse_jobs_dashboard(data: object) -> JobsDashboard | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                jobs_dashboard_type_1 = JobsDashboard.from_dict(data)

                return jobs_dashboard_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobsDashboard | None | Unset, data)

        jobs_dashboard = _parse_jobs_dashboard(d.pop("jobs_dashboard", UNSET))

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

        logo_url = d.pop("logo_url", UNSET)

        required_metadata_views = cast(
            list[str], d.pop("required_metadata_views", UNSET)
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

        search_default_sections = cast(
            list[str], d.pop("search_default_sections", UNSET)
        )

        _search_display_fields = d.pop("search_display_fields", UNSET)
        search_display_fields: list[SearchDisplayField] | Unset = UNSET
        if _search_display_fields is not UNSET:
            search_display_fields = []
            for search_display_fields_item_data in _search_display_fields:
                search_display_fields_item = SearchDisplayField.from_dict(
                    search_display_fields_item_data
                )

                search_display_fields.append(search_display_fields_item)

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

        def _parse_search_view_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                search_view_id_type_0 = UUID(data)

                return search_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        search_view_id = _parse_search_view_id(d.pop("search_view_id", UNSET))

        def _parse_share_expiration_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        share_expiration_time = _parse_share_expiration_time(
            d.pop("share_expiration_time", UNSET)
        )

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        def _parse_use_asset_name_on_download(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_asset_name_on_download = _parse_use_asset_name_on_download(
            d.pop("use_asset_name_on_download", UNSET)
        )

        group_setting_public_schema = cls(
            acl_template_id=acl_template_id,
            allowed_ips=allowed_ips,
            append_asset_uuid_to_downloads=append_asset_uuid_to_downloads,
            asset_default_sections=asset_default_sections,
            client_ip=client_ip,
            collections_get_parent_acls=collections_get_parent_acls,
            date_format=date_format,
            datetime_format=datetime_format,
            default_upload_storage_id=default_upload_storage_id,
            delete_grace_period=delete_grace_period,
            facet_fields=facet_fields,
            filters_default_metadata_view_id=filters_default_metadata_view_id,
            group_id=group_id,
            hide_favourites=hide_favourites,
            home_page=home_page,
            jobs_dashboard=jobs_dashboard,
            logo_storage_id=logo_storage_id,
            logo_url=logo_url,
            required_metadata_views=required_metadata_views,
            search_auto_resize_title_column=search_auto_resize_title_column,
            search_default_sections=search_default_sections,
            search_display_fields=search_display_fields,
            search_in_transcriptions=search_in_transcriptions,
            search_results_asset_metadata_view_id=search_results_asset_metadata_view_id,
            search_results_collection_metadata_view_id=search_results_collection_metadata_view_id,
            search_view_id=search_view_id,
            share_expiration_time=share_expiration_time,
            system_domain_id=system_domain_id,
            use_asset_name_on_download=use_asset_name_on_download,
        )

        group_setting_public_schema.additional_properties = d
        return group_setting_public_schema

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
