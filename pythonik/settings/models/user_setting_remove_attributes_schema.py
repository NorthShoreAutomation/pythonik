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
    from ..models.jobs_dashboard_schema import JobsDashboardSchema
    from ..models.search_display_field_schema import SearchDisplayFieldSchema


T = TypeVar("T", bound="UserSettingRemoveAttributesSchema")


@_attrs_define
class UserSettingRemoveAttributesSchema:
    """
    Attributes:
        user_ids (list[UUID]):
        allowed_ips (list[AllowedIPSchema] | Unset):
        asset_default_sections (list[str] | Unset):
        facet_fields (list[FacetFieldSchema] | Unset):
        jobs_dashboard (JobsDashboardSchema | None | Unset):
        search_default_sections (list[str] | Unset):
        search_display_fields (list[SearchDisplayFieldSchema] | Unset):
    """

    user_ids: list[UUID]
    allowed_ips: list[AllowedIPSchema] | Unset = UNSET
    asset_default_sections: list[str] | Unset = UNSET
    facet_fields: list[FacetFieldSchema] | Unset = UNSET
    jobs_dashboard: JobsDashboardSchema | None | Unset = UNSET
    search_default_sections: list[str] | Unset = UNSET
    search_display_fields: list[SearchDisplayFieldSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.jobs_dashboard_schema import JobsDashboardSchema

        user_ids = []
        for user_ids_item_data in self.user_ids:
            user_ids_item = str(user_ids_item_data)
            user_ids.append(user_ids_item)

        allowed_ips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = []
            for allowed_ips_item_data in self.allowed_ips:
                allowed_ips_item = allowed_ips_item_data.to_dict()
                allowed_ips.append(allowed_ips_item)

        asset_default_sections: list[str] | Unset = UNSET
        if not isinstance(self.asset_default_sections, Unset):
            asset_default_sections = self.asset_default_sections

        facet_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.facet_fields, Unset):
            facet_fields = []
            for facet_fields_item_data in self.facet_fields:
                facet_fields_item = facet_fields_item_data.to_dict()
                facet_fields.append(facet_fields_item)

        jobs_dashboard: dict[str, Any] | None | Unset
        if isinstance(self.jobs_dashboard, Unset):
            jobs_dashboard = UNSET
        elif isinstance(self.jobs_dashboard, JobsDashboardSchema):
            jobs_dashboard = self.jobs_dashboard.to_dict()
        else:
            jobs_dashboard = self.jobs_dashboard

        search_default_sections: list[str] | Unset = UNSET
        if not isinstance(self.search_default_sections, Unset):
            search_default_sections = self.search_default_sections

        search_display_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.search_display_fields, Unset):
            search_display_fields = []
            for search_display_fields_item_data in self.search_display_fields:
                search_display_fields_item = search_display_fields_item_data.to_dict()
                search_display_fields.append(search_display_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_ids": user_ids,
            }
        )
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips
        if asset_default_sections is not UNSET:
            field_dict["asset_default_sections"] = asset_default_sections
        if facet_fields is not UNSET:
            field_dict["facet_fields"] = facet_fields
        if jobs_dashboard is not UNSET:
            field_dict["jobs_dashboard"] = jobs_dashboard
        if search_default_sections is not UNSET:
            field_dict["search_default_sections"] = search_default_sections
        if search_display_fields is not UNSET:
            field_dict["search_display_fields"] = search_display_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_ip_schema import AllowedIPSchema
        from ..models.facet_field_schema import FacetFieldSchema
        from ..models.jobs_dashboard_schema import JobsDashboardSchema
        from ..models.search_display_field_schema import SearchDisplayFieldSchema

        d = dict(src_dict)
        user_ids = []
        _user_ids = d.pop("user_ids")
        for user_ids_item_data in _user_ids:
            user_ids_item = UUID(user_ids_item_data)

            user_ids.append(user_ids_item)

        _allowed_ips = d.pop("allowed_ips", UNSET)
        allowed_ips: list[AllowedIPSchema] | Unset = UNSET
        if _allowed_ips is not UNSET:
            allowed_ips = []
            for allowed_ips_item_data in _allowed_ips:
                allowed_ips_item = AllowedIPSchema.from_dict(allowed_ips_item_data)

                allowed_ips.append(allowed_ips_item)

        asset_default_sections = cast(list[str], d.pop("asset_default_sections", UNSET))

        _facet_fields = d.pop("facet_fields", UNSET)
        facet_fields: list[FacetFieldSchema] | Unset = UNSET
        if _facet_fields is not UNSET:
            facet_fields = []
            for facet_fields_item_data in _facet_fields:
                facet_fields_item = FacetFieldSchema.from_dict(facet_fields_item_data)

                facet_fields.append(facet_fields_item)

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

        search_default_sections = cast(
            list[str], d.pop("search_default_sections", UNSET)
        )

        _search_display_fields = d.pop("search_display_fields", UNSET)
        search_display_fields: list[SearchDisplayFieldSchema] | Unset = UNSET
        if _search_display_fields is not UNSET:
            search_display_fields = []
            for search_display_fields_item_data in _search_display_fields:
                search_display_fields_item = SearchDisplayFieldSchema.from_dict(
                    search_display_fields_item_data
                )

                search_display_fields.append(search_display_fields_item)

        user_setting_remove_attributes_schema = cls(
            user_ids=user_ids,
            allowed_ips=allowed_ips,
            asset_default_sections=asset_default_sections,
            facet_fields=facet_fields,
            jobs_dashboard=jobs_dashboard,
            search_default_sections=search_default_sections,
            search_display_fields=search_display_fields,
        )

        user_setting_remove_attributes_schema.additional_properties = d
        return user_setting_remove_attributes_schema

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
