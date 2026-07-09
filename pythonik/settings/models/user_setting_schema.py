from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowed_ip_schema import AllowedIPSchema
    from ..models.dashboard_schema import DashboardSchema
    from ..models.facet_field_schema import FacetFieldSchema
    from ..models.jobs_dashboard_schema import JobsDashboardSchema
    from ..models.search_display_field_schema import SearchDisplayFieldSchema
    from ..models.usage_history_schema import UsageHistorySchema


T = TypeVar("T", bound="UserSettingSchema")


@_attrs_define
class UserSettingSchema:
    """
    Attributes:
        acl_template_id (None | Unset | UUID):
        allowed_ips (list[AllowedIPSchema] | None | Unset):
        append_asset_uuid_to_downloads (bool | None | Unset):
        asset_default_sections (list[str] | None | Unset):
        client_ip (None | str | Unset):
        collections_get_parent_acls (bool | None | Unset):
        dashboard (DashboardSchema | None | Unset):
        date_format (None | str | Unset):
        datetime_format (None | str | Unset):
        default_upload_storage_id (None | Unset | UUID):
        delete_grace_period (int | None | Unset): Grace period that indicate how long objects will live in recycle bin.
            Unit: hours
        facet_fields (list[FacetFieldSchema] | None | Unset):
        filters_default_metadata_view_id (None | Unset | UUID):
        genesis (None | str | Unset):
        hide_favourites (bool | None | Unset):
        home_page (None | str | Unset):
        jobs_dashboard (JobsDashboardSchema | None | Unset):
        search_auto_resize_title_column (bool | None | Unset):
        search_default_sections (list[str] | None | Unset):
        search_display_fields (list[SearchDisplayFieldSchema] | None | Unset):
        search_in_transcriptions (bool | None | Unset):
        search_results_asset_metadata_view_id (None | Unset | UUID):
        search_results_collection_metadata_view_id (None | Unset | UUID):
        search_view_id (None | Unset | UUID):
        share_expiration_time (int | None | Unset): Default share expiration time that indicate how long share will be
            valid. Unit: days
        show_persons_confirmation_modal (bool | None | Unset):
        usage_history (None | Unset | UsageHistorySchema):
        use_asset_name_on_download (bool | None | Unset):
    """

    acl_template_id: None | Unset | UUID = UNSET
    allowed_ips: list[AllowedIPSchema] | None | Unset = UNSET
    append_asset_uuid_to_downloads: bool | None | Unset = UNSET
    asset_default_sections: list[str] | None | Unset = UNSET
    client_ip: None | str | Unset = UNSET
    collections_get_parent_acls: bool | None | Unset = UNSET
    dashboard: DashboardSchema | None | Unset = UNSET
    date_format: None | str | Unset = UNSET
    datetime_format: None | str | Unset = UNSET
    default_upload_storage_id: None | Unset | UUID = UNSET
    delete_grace_period: int | None | Unset = UNSET
    facet_fields: list[FacetFieldSchema] | None | Unset = UNSET
    filters_default_metadata_view_id: None | Unset | UUID = UNSET
    genesis: None | str | Unset = UNSET
    hide_favourites: bool | None | Unset = UNSET
    home_page: None | str | Unset = UNSET
    jobs_dashboard: JobsDashboardSchema | None | Unset = UNSET
    search_auto_resize_title_column: bool | None | Unset = UNSET
    search_default_sections: list[str] | None | Unset = UNSET
    search_display_fields: list[SearchDisplayFieldSchema] | None | Unset = UNSET
    search_in_transcriptions: bool | None | Unset = UNSET
    search_results_asset_metadata_view_id: None | Unset | UUID = UNSET
    search_results_collection_metadata_view_id: None | Unset | UUID = UNSET
    search_view_id: None | Unset | UUID = UNSET
    share_expiration_time: int | None | Unset = UNSET
    show_persons_confirmation_modal: bool | None | Unset = UNSET
    usage_history: None | Unset | UsageHistorySchema = UNSET
    use_asset_name_on_download: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_schema import DashboardSchema
        from ..models.jobs_dashboard_schema import JobsDashboardSchema
        from ..models.usage_history_schema import UsageHistorySchema

        acl_template_id: None | str | Unset
        if isinstance(self.acl_template_id, Unset):
            acl_template_id = UNSET
        elif isinstance(self.acl_template_id, UUID):
            acl_template_id = str(self.acl_template_id)
        else:
            acl_template_id = self.acl_template_id

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

        dashboard: dict[str, Any] | None | Unset
        if isinstance(self.dashboard, Unset):
            dashboard = UNSET
        elif isinstance(self.dashboard, DashboardSchema):
            dashboard = self.dashboard.to_dict()
        else:
            dashboard = self.dashboard

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

        genesis: None | str | Unset
        if isinstance(self.genesis, Unset):
            genesis = UNSET
        else:
            genesis = self.genesis

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
        elif isinstance(self.jobs_dashboard, JobsDashboardSchema):
            jobs_dashboard = self.jobs_dashboard.to_dict()
        else:
            jobs_dashboard = self.jobs_dashboard

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

        show_persons_confirmation_modal: bool | None | Unset
        if isinstance(self.show_persons_confirmation_modal, Unset):
            show_persons_confirmation_modal = UNSET
        else:
            show_persons_confirmation_modal = self.show_persons_confirmation_modal

        usage_history: dict[str, Any] | None | Unset
        if isinstance(self.usage_history, Unset):
            usage_history = UNSET
        elif isinstance(self.usage_history, UsageHistorySchema):
            usage_history = self.usage_history.to_dict()
        else:
            usage_history = self.usage_history

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
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
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
        if genesis is not UNSET:
            field_dict["genesis"] = genesis
        if hide_favourites is not UNSET:
            field_dict["hide_favourites"] = hide_favourites
        if home_page is not UNSET:
            field_dict["home_page"] = home_page
        if jobs_dashboard is not UNSET:
            field_dict["jobs_dashboard"] = jobs_dashboard
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
        if show_persons_confirmation_modal is not UNSET:
            field_dict["show_persons_confirmation_modal"] = (
                show_persons_confirmation_modal
            )
        if usage_history is not UNSET:
            field_dict["usage_history"] = usage_history
        if use_asset_name_on_download is not UNSET:
            field_dict["use_asset_name_on_download"] = use_asset_name_on_download

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_ip_schema import AllowedIPSchema
        from ..models.dashboard_schema import DashboardSchema
        from ..models.facet_field_schema import FacetFieldSchema
        from ..models.jobs_dashboard_schema import JobsDashboardSchema
        from ..models.search_display_field_schema import SearchDisplayFieldSchema
        from ..models.usage_history_schema import UsageHistorySchema

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

        def _parse_dashboard(data: object) -> DashboardSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dashboard_type_1 = DashboardSchema.from_dict(data)

                return dashboard_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardSchema | None | Unset, data)

        dashboard = _parse_dashboard(d.pop("dashboard", UNSET))

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

        def _parse_genesis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        genesis = _parse_genesis(d.pop("genesis", UNSET))

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

        def _parse_show_persons_confirmation_modal(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_persons_confirmation_modal = _parse_show_persons_confirmation_modal(
            d.pop("show_persons_confirmation_modal", UNSET)
        )

        def _parse_usage_history(data: object) -> None | Unset | UsageHistorySchema:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_history_type_1 = UsageHistorySchema.from_dict(data)

                return usage_history_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UsageHistorySchema, data)

        usage_history = _parse_usage_history(d.pop("usage_history", UNSET))

        def _parse_use_asset_name_on_download(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_asset_name_on_download = _parse_use_asset_name_on_download(
            d.pop("use_asset_name_on_download", UNSET)
        )

        user_setting_schema = cls(
            acl_template_id=acl_template_id,
            allowed_ips=allowed_ips,
            append_asset_uuid_to_downloads=append_asset_uuid_to_downloads,
            asset_default_sections=asset_default_sections,
            client_ip=client_ip,
            collections_get_parent_acls=collections_get_parent_acls,
            dashboard=dashboard,
            date_format=date_format,
            datetime_format=datetime_format,
            default_upload_storage_id=default_upload_storage_id,
            delete_grace_period=delete_grace_period,
            facet_fields=facet_fields,
            filters_default_metadata_view_id=filters_default_metadata_view_id,
            genesis=genesis,
            hide_favourites=hide_favourites,
            home_page=home_page,
            jobs_dashboard=jobs_dashboard,
            search_auto_resize_title_column=search_auto_resize_title_column,
            search_default_sections=search_default_sections,
            search_display_fields=search_display_fields,
            search_in_transcriptions=search_in_transcriptions,
            search_results_asset_metadata_view_id=search_results_asset_metadata_view_id,
            search_results_collection_metadata_view_id=search_results_collection_metadata_view_id,
            search_view_id=search_view_id,
            share_expiration_time=share_expiration_time,
            show_persons_confirmation_modal=show_persons_confirmation_modal,
            usage_history=usage_history,
            use_asset_name_on_download=use_asset_name_on_download,
        )

        user_setting_schema.additional_properties = d
        return user_setting_schema

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
