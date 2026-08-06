from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_options_schema import FieldOptionsSchema


T = TypeVar("T", bound="MetadataViewFieldSchema")


@_attrs_define
class MetadataViewFieldSchema:
    """
    Attributes:
        name (str):
        auto_set (bool | None | Unset):
        hide_if_not_set (bool | None | Unset):
        label (None | str | Unset):
        mapped_field_name (None | str | Unset):
        options (list[FieldOptionsSchema] | None | Unset):
        read_only (bool | None | Unset):
        required (bool | None | Unset):
        source_url (None | str | Unset): Will be used to upload MetadataField's `options`. Cannot be set or used as long
            as `options` are set.  **Example**: The value is `https://external-url.com/foo/`. In that case `GET` request
            will be sent to `https://external-
            url.com/foo/?user_id=uuid1&view_id=uuid1&field_name=bar&view_name=user_view&system_domain_id=uuid1`. Please note
            that some query parameters were added by *iconik* to get values that were predefined in your system for each
            user [user_id] and view [view_id]. Metadata field name [field_name], view's name [view_name] and system domain
            identifier [system_domain_id] will be also passed in each request. *iconik* will successfully parse the response
            from that URL if it will be sent in JSON formatted string: `{"bar": [{"value": "1", "label": "1st"}, {"value":
            "2", "label": "2nd"}]}`
    """

    name: str
    auto_set: bool | None | Unset = UNSET
    hide_if_not_set: bool | None | Unset = UNSET
    label: None | str | Unset = UNSET
    mapped_field_name: None | str | Unset = UNSET
    options: list[FieldOptionsSchema] | None | Unset = UNSET
    read_only: bool | None | Unset = UNSET
    required: bool | None | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        auto_set: bool | None | Unset
        if isinstance(self.auto_set, Unset):
            auto_set = UNSET
        else:
            auto_set = self.auto_set

        hide_if_not_set: bool | None | Unset
        if isinstance(self.hide_if_not_set, Unset):
            hide_if_not_set = UNSET
        else:
            hide_if_not_set = self.hide_if_not_set

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        mapped_field_name: None | str | Unset
        if isinstance(self.mapped_field_name, Unset):
            mapped_field_name = UNSET
        else:
            mapped_field_name = self.mapped_field_name

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

        required: bool | None | Unset
        if isinstance(self.required, Unset):
            required = UNSET
        else:
            required = self.required

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if auto_set is not UNSET:
            field_dict["auto_set"] = auto_set
        if hide_if_not_set is not UNSET:
            field_dict["hide_if_not_set"] = hide_if_not_set
        if label is not UNSET:
            field_dict["label"] = label
        if mapped_field_name is not UNSET:
            field_dict["mapped_field_name"] = mapped_field_name
        if options is not UNSET:
            field_dict["options"] = options
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if required is not UNSET:
            field_dict["required"] = required
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_options_schema import FieldOptionsSchema

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_auto_set(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_set = _parse_auto_set(d.pop("auto_set", UNSET))

        def _parse_hide_if_not_set(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_if_not_set = _parse_hide_if_not_set(d.pop("hide_if_not_set", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_mapped_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mapped_field_name = _parse_mapped_field_name(d.pop("mapped_field_name", UNSET))

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

        def _parse_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        required = _parse_required(d.pop("required", UNSET))

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        metadata_view_field_schema = cls(
            name=name,
            auto_set=auto_set,
            hide_if_not_set=hide_if_not_set,
            label=label,
            mapped_field_name=mapped_field_name,
            options=options,
            read_only=read_only,
            required=required,
            source_url=source_url,
        )

        metadata_view_field_schema.additional_properties = d
        return metadata_view_field_schema

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
