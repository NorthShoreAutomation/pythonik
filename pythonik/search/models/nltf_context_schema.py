from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nltf_displayed_filters import NltfDisplayedFilters


T = TypeVar("T", bound="NltfContextSchema")


@_attrs_define
class NltfContextSchema:
    """
    Attributes:
        displayed_filters (NltfDisplayedFilters | None | Unset):
    """

    displayed_filters: NltfDisplayedFilters | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nltf_displayed_filters import NltfDisplayedFilters

        displayed_filters: dict[str, Any] | None | Unset
        if isinstance(self.displayed_filters, Unset):
            displayed_filters = UNSET
        elif isinstance(self.displayed_filters, NltfDisplayedFilters):
            displayed_filters = self.displayed_filters.to_dict()
        else:
            displayed_filters = self.displayed_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if displayed_filters is not UNSET:
            field_dict["displayed_filters"] = displayed_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nltf_displayed_filters import NltfDisplayedFilters

        d = dict(src_dict)

        def _parse_displayed_filters(
            data: object,
        ) -> NltfDisplayedFilters | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                displayed_filters_type_1 = NltfDisplayedFilters.from_dict(data)

                return displayed_filters_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfDisplayedFilters | None | Unset, data)

        displayed_filters = _parse_displayed_filters(d.pop("displayed_filters", UNSET))

        nltf_context_schema = cls(
            displayed_filters=displayed_filters,
        )

        nltf_context_schema.additional_properties = d
        return nltf_context_schema

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
