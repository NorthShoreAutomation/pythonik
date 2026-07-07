from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_options_schema import FieldOptionsSchema


T = TypeVar("T", bound="MetadataField")


@_attrs_define
class MetadataField:
    """
    Attributes:
        field_type (str):
        label (str):
        name (str):
        ai_prompt_description (None | str | Unset): LLM prompt override used when generating values for this field. If
            unset, the LLM prompt falls back to `description`.
        auto_set (bool | None | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        external_id (str | Unset):
        hide_if_not_set (bool | None | Unset):
        is_block_field (bool | Unset):
        is_warning_field (bool | Unset):
        mapped_field_name (str | Unset):
        max_value (float | Unset):
        min_value (float | Unset):
        multi (bool | Unset):
        options (list[FieldOptionsSchema] | Unset):
        read_only (bool | None | Unset):
        representative (bool | Unset):
        required (bool | None | Unset):
        sortable (bool | Unset):
        source_url (None | str | Unset): Will be used to upload MetadataField's `options`. Cannot be set or used as long
            as `options` are set.  **Example**: The value is `https://external-url.com/foo/`. In that case `GET` request
            will be sent to `https://external-
            url.com/foo/?user_id=uuid1&view_id=uuid1&field_name=bar&view_name=user_view&system_domain_id=uuid1`. Please note
            that some query parameters were added by *iconik* to get values that were predefined in your system for each
            user [user_id] and view [view_id]. Metadata field name [field_name], view's name [view_name] and system domain
            identifier [system_domain_id] will be also passed in each request. *iconik* will successfully parse the response
            from that URL if it will be sent in JSON formatted string: `{"bar": [{"value": "1", "label": "1st"}, {"value":
            "2", "label": "2nd"}]}`
        use_as_facet (bool | Unset):
    """

    field_type: str
    label: str
    name: str
    ai_prompt_description: None | str | Unset = UNSET
    auto_set: bool | None | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    external_id: str | Unset = UNSET
    hide_if_not_set: bool | None | Unset = UNSET
    is_block_field: bool | Unset = UNSET
    is_warning_field: bool | Unset = UNSET
    mapped_field_name: str | Unset = UNSET
    max_value: float | Unset = UNSET
    min_value: float | Unset = UNSET
    multi: bool | Unset = UNSET
    options: list[FieldOptionsSchema] | Unset = UNSET
    read_only: bool | None | Unset = UNSET
    representative: bool | Unset = UNSET
    required: bool | None | Unset = UNSET
    sortable: bool | Unset = UNSET
    source_url: None | str | Unset = UNSET
    use_as_facet: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_type = self.field_type

        label = self.label

        name = self.name

        ai_prompt_description: None | str | Unset
        if isinstance(self.ai_prompt_description, Unset):
            ai_prompt_description = UNSET
        else:
            ai_prompt_description = self.ai_prompt_description

        auto_set: bool | None | Unset
        if isinstance(self.auto_set, Unset):
            auto_set = UNSET
        else:
            auto_set = self.auto_set

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        external_id = self.external_id

        hide_if_not_set: bool | None | Unset
        if isinstance(self.hide_if_not_set, Unset):
            hide_if_not_set = UNSET
        else:
            hide_if_not_set = self.hide_if_not_set

        is_block_field = self.is_block_field

        is_warning_field = self.is_warning_field

        mapped_field_name = self.mapped_field_name

        max_value = self.max_value

        min_value = self.min_value

        multi = self.multi

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        read_only: bool | None | Unset
        if isinstance(self.read_only, Unset):
            read_only = UNSET
        else:
            read_only = self.read_only

        representative = self.representative

        required: bool | None | Unset
        if isinstance(self.required, Unset):
            required = UNSET
        else:
            required = self.required

        sortable = self.sortable

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        use_as_facet = self.use_as_facet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_type": field_type,
                "label": label,
                "name": name,
            }
        )
        if ai_prompt_description is not UNSET:
            field_dict["ai_prompt_description"] = ai_prompt_description
        if auto_set is not UNSET:
            field_dict["auto_set"] = auto_set
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if hide_if_not_set is not UNSET:
            field_dict["hide_if_not_set"] = hide_if_not_set
        if is_block_field is not UNSET:
            field_dict["is_block_field"] = is_block_field
        if is_warning_field is not UNSET:
            field_dict["is_warning_field"] = is_warning_field
        if mapped_field_name is not UNSET:
            field_dict["mapped_field_name"] = mapped_field_name
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if multi is not UNSET:
            field_dict["multi"] = multi
        if options is not UNSET:
            field_dict["options"] = options
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if representative is not UNSET:
            field_dict["representative"] = representative
        if required is not UNSET:
            field_dict["required"] = required
        if sortable is not UNSET:
            field_dict["sortable"] = sortable
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if use_as_facet is not UNSET:
            field_dict["use_as_facet"] = use_as_facet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_options_schema import FieldOptionsSchema

        d = dict(src_dict)
        field_type = d.pop("field_type")

        label = d.pop("label")

        name = d.pop("name")

        def _parse_ai_prompt_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_prompt_description = _parse_ai_prompt_description(
            d.pop("ai_prompt_description", UNSET)
        )

        def _parse_auto_set(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_set = _parse_auto_set(d.pop("auto_set", UNSET))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        description = d.pop("description", UNSET)

        external_id = d.pop("external_id", UNSET)

        def _parse_hide_if_not_set(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_if_not_set = _parse_hide_if_not_set(d.pop("hide_if_not_set", UNSET))

        is_block_field = d.pop("is_block_field", UNSET)

        is_warning_field = d.pop("is_warning_field", UNSET)

        mapped_field_name = d.pop("mapped_field_name", UNSET)

        max_value = d.pop("max_value", UNSET)

        min_value = d.pop("min_value", UNSET)

        multi = d.pop("multi", UNSET)

        _options = d.pop("options", UNSET)
        options: list[FieldOptionsSchema] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = FieldOptionsSchema.from_dict(options_item_data)

                options.append(options_item)

        def _parse_read_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_only = _parse_read_only(d.pop("read_only", UNSET))

        representative = d.pop("representative", UNSET)

        def _parse_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        required = _parse_required(d.pop("required", UNSET))

        sortable = d.pop("sortable", UNSET)

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        use_as_facet = d.pop("use_as_facet", UNSET)

        metadata_field = cls(
            field_type=field_type,
            label=label,
            name=name,
            ai_prompt_description=ai_prompt_description,
            auto_set=auto_set,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            external_id=external_id,
            hide_if_not_set=hide_if_not_set,
            is_block_field=is_block_field,
            is_warning_field=is_warning_field,
            mapped_field_name=mapped_field_name,
            max_value=max_value,
            min_value=min_value,
            multi=multi,
            options=options,
            read_only=read_only,
            representative=representative,
            required=required,
            sortable=sortable,
            source_url=source_url,
            use_as_facet=use_as_facet,
        )

        metadata_field.additional_properties = d
        return metadata_field

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
