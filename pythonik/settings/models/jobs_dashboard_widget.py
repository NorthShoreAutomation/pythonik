from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_dashboard_widget_type_type_1 import JobsDashboardWidgetTypeType1
    from ..models.jobs_widget_option import JobsWidgetOption


T = TypeVar("T", bound="JobsDashboardWidget")


@_attrs_define
class JobsDashboardWidget:
    """
    Attributes:
        id (None | str | Unset):
        options (JobsWidgetOption | None | Unset):
        title (None | str | Unset):
        type_ (JobsDashboardWidgetTypeType1 | None | Unset):
    """

    id: None | str | Unset = UNSET
    options: JobsWidgetOption | None | Unset = UNSET
    title: None | str | Unset = UNSET
    type_: JobsDashboardWidgetTypeType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.jobs_dashboard_widget_type_type_1 import (
            JobsDashboardWidgetTypeType1,
        )
        from ..models.jobs_widget_option import JobsWidgetOption

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, JobsWidgetOption):
            options = self.options.to_dict()
        else:
            options = self.options

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, JobsDashboardWidgetTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if options is not UNSET:
            field_dict["options"] = options
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jobs_dashboard_widget_type_type_1 import (
            JobsDashboardWidgetTypeType1,
        )
        from ..models.jobs_widget_option import JobsWidgetOption

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_options(data: object) -> JobsWidgetOption | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_1 = JobsWidgetOption.from_dict(data)

                return options_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobsWidgetOption | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_type_(data: object) -> JobsDashboardWidgetTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = JobsDashboardWidgetTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobsDashboardWidgetTypeType1 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        jobs_dashboard_widget = cls(
            id=id,
            options=options,
            title=title,
            type_=type_,
        )

        jobs_dashboard_widget.additional_properties = d
        return jobs_dashboard_widget

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
