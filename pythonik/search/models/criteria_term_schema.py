from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria_range_filter_schema import CriteriaRangeFilterSchema


T = TypeVar("T", bound="CriteriaTermSchema")


@_attrs_define
class CriteriaTermSchema:
    """
    Attributes:
        name (str):
        exists (bool | Unset):
        missing (bool | Unset):
        range_ (CriteriaRangeFilterSchema | Unset):
        value (str | Unset):
        value_in (list[str] | Unset):
    """

    name: str
    exists: bool | Unset = UNSET
    missing: bool | Unset = UNSET
    range_: CriteriaRangeFilterSchema | Unset = UNSET
    value: str | Unset = UNSET
    value_in: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        exists = self.exists

        missing = self.missing

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        value = self.value

        value_in: list[str] | Unset = UNSET
        if not isinstance(self.value_in, Unset):
            value_in = self.value_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if exists is not UNSET:
            field_dict["exists"] = exists
        if missing is not UNSET:
            field_dict["missing"] = missing
        if range_ is not UNSET:
            field_dict["range"] = range_
        if value is not UNSET:
            field_dict["value"] = value
        if value_in is not UNSET:
            field_dict["value_in"] = value_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_range_filter_schema import CriteriaRangeFilterSchema

        d = dict(src_dict)
        name = d.pop("name")

        exists = d.pop("exists", UNSET)

        missing = d.pop("missing", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: CriteriaRangeFilterSchema | Unset
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = CriteriaRangeFilterSchema.from_dict(_range_)

        value = d.pop("value", UNSET)

        value_in = cast(list[str], d.pop("value_in", UNSET))

        criteria_term_schema = cls(
            name=name,
            exists=exists,
            missing=missing,
            range_=range_,
            value=value,
            value_in=value_in,
        )

        criteria_term_schema.additional_properties = d
        return criteria_term_schema

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
