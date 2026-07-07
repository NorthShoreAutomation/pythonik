from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jobs_dashboard_widget_schema_type import JobsDashboardWidgetSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_widget_option import JobsWidgetOption


T = TypeVar("T", bound="JobsDashboardWidgetSchema")


@_attrs_define
class JobsDashboardWidgetSchema:
    """
    Attributes:
        id (str | Unset):
        options (JobsWidgetOption | Unset):
        title (None | str | Unset):
        type_ (JobsDashboardWidgetSchemaType | Unset):
    """

    id: str | Unset = UNSET
    options: JobsWidgetOption | Unset = UNSET
    title: None | str | Unset = UNSET
    type_: JobsDashboardWidgetSchemaType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        from ..models.jobs_widget_option import JobsWidgetOption

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _options = d.pop("options", UNSET)
        options: JobsWidgetOption | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = JobsWidgetOption.from_dict(_options)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: JobsDashboardWidgetSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = JobsDashboardWidgetSchemaType(_type_)

        jobs_dashboard_widget_schema = cls(
            id=id,
            options=options,
            title=title,
            type_=type_,
        )

        jobs_dashboard_widget_schema.additional_properties = d
        return jobs_dashboard_widget_schema

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
