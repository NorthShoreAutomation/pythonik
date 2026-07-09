from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_options_schema import FieldOptionsSchema


T = TypeVar("T", bound="MetadataFieldBaseSchema")


@_attrs_define
class MetadataFieldBaseSchema:
    """
    Attributes:
        field_type (str):
        ai_prompt_description (None | str | Unset): LLM prompt override used when generating values for this field. If
            unset, the LLM prompt falls back to `description`.
        auto_set (bool | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        description (None | str | Unset):
        external_id (None | str | Unset):
        hide_if_not_set (bool | None | Unset):
        is_block_field (bool | None | Unset):
        is_warning_field (bool | None | Unset):
        mapped_field_name (None | str | Unset):
        max_value (float | None | Unset):
        min_value (float | None | Unset):
        multi (bool | None | Unset):
        options (list[FieldOptionsSchema] | None | Unset):
        read_only (bool | None | Unset):
        representative (bool | None | Unset):
        required (bool | None | Unset):
        sortable (bool | None | Unset):
        source_url (None | str | Unset): Will be used to upload MetadataField's `options`. Cannot be set or used as long
            as `options` are set.  **Example**: The value is `https://external-url.com/foo/`. In that case `GET` request
            will be sent to `https://external-
            url.com/foo/?user_id=uuid1&view_id=uuid1&field_name=bar&view_name=user_view&system_domain_id=uuid1`. Please note
            that some query parameters were added by *iconik* to get values that were predefined in your system for each
            user [user_id] and view [view_id]. Metadata field name [field_name], view's name [view_name] and system domain
            identifier [system_domain_id] will be also passed in each request. *iconik* will successfully parse the response
            from that URL if it will be sent in JSON formatted string: `{"bar": [{"value": "1", "label": "1st"}, {"value":
            "2", "label": "2nd"}]}`
        use_as_facet (bool | None | Unset):
    """

    field_type: str
    ai_prompt_description: None | str | Unset = UNSET
    auto_set: bool | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    hide_if_not_set: bool | None | Unset = UNSET
    is_block_field: bool | None | Unset = UNSET
    is_warning_field: bool | None | Unset = UNSET
    mapped_field_name: None | str | Unset = UNSET
    max_value: float | None | Unset = UNSET
    min_value: float | None | Unset = UNSET
    multi: bool | None | Unset = UNSET
    options: list[FieldOptionsSchema] | None | Unset = UNSET
    read_only: bool | None | Unset = UNSET
    representative: bool | None | Unset = UNSET
    required: bool | None | Unset = UNSET
    sortable: bool | None | Unset = UNSET
    source_url: None | str | Unset = UNSET
    use_as_facet: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_type = self.field_type

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

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        hide_if_not_set: bool | None | Unset
        if isinstance(self.hide_if_not_set, Unset):
            hide_if_not_set = UNSET
        else:
            hide_if_not_set = self.hide_if_not_set

        is_block_field: bool | None | Unset
        if isinstance(self.is_block_field, Unset):
            is_block_field = UNSET
        else:
            is_block_field = self.is_block_field

        is_warning_field: bool | None | Unset
        if isinstance(self.is_warning_field, Unset):
            is_warning_field = UNSET
        else:
            is_warning_field = self.is_warning_field

        mapped_field_name: None | str | Unset
        if isinstance(self.mapped_field_name, Unset):
            mapped_field_name = UNSET
        else:
            mapped_field_name = self.mapped_field_name

        max_value: float | None | Unset
        if isinstance(self.max_value, Unset):
            max_value = UNSET
        else:
            max_value = self.max_value

        min_value: float | None | Unset
        if isinstance(self.min_value, Unset):
            min_value = UNSET
        else:
            min_value = self.min_value

        multi: bool | None | Unset
        if isinstance(self.multi, Unset):
            multi = UNSET
        else:
            multi = self.multi

        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)

        else:
            options = self.options

        read_only: bool | None | Unset
        if isinstance(self.read_only, Unset):
            read_only = UNSET
        else:
            read_only = self.read_only

        representative: bool | None | Unset
        if isinstance(self.representative, Unset):
            representative = UNSET
        else:
            representative = self.representative

        required: bool | None | Unset
        if isinstance(self.required, Unset):
            required = UNSET
        else:
            required = self.required

        sortable: bool | None | Unset
        if isinstance(self.sortable, Unset):
            sortable = UNSET
        else:
            sortable = self.sortable

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        use_as_facet: bool | None | Unset
        if isinstance(self.use_as_facet, Unset):
            use_as_facet = UNSET
        else:
            use_as_facet = self.use_as_facet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_type": field_type,
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

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_hide_if_not_set(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_if_not_set = _parse_hide_if_not_set(d.pop("hide_if_not_set", UNSET))

        def _parse_is_block_field(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_block_field = _parse_is_block_field(d.pop("is_block_field", UNSET))

        def _parse_is_warning_field(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_warning_field = _parse_is_warning_field(d.pop("is_warning_field", UNSET))

        def _parse_mapped_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mapped_field_name = _parse_mapped_field_name(d.pop("mapped_field_name", UNSET))

        def _parse_max_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_value = _parse_max_value(d.pop("max_value", UNSET))

        def _parse_min_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_value = _parse_min_value(d.pop("min_value", UNSET))

        def _parse_multi(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        multi = _parse_multi(d.pop("multi", UNSET))

        def _parse_options(data: object) -> list[FieldOptionsSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in _options_type_0:
                    options_type_0_item = FieldOptionsSchema.from_dict(
                        options_type_0_item_data
                    )

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FieldOptionsSchema] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_read_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_only = _parse_read_only(d.pop("read_only", UNSET))

        def _parse_representative(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        representative = _parse_representative(d.pop("representative", UNSET))

        def _parse_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        required = _parse_required(d.pop("required", UNSET))

        def _parse_sortable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sortable = _parse_sortable(d.pop("sortable", UNSET))

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        def _parse_use_as_facet(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_as_facet = _parse_use_as_facet(d.pop("use_as_facet", UNSET))

        metadata_field_base_schema = cls(
            field_type=field_type,
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

        metadata_field_base_schema.additional_properties = d
        return metadata_field_base_schema

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
