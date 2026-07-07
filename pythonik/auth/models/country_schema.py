from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CountrySchema")


@_attrs_define
class CountrySchema:
    """
    Attributes:
        name (str):
        alpha2 (str | Unset):
        alpha3 (str | Unset):
        apolitical_name (str | Unset):
        numeric (str | Unset):
    """

    name: str
    alpha2: str | Unset = UNSET
    alpha3: str | Unset = UNSET
    apolitical_name: str | Unset = UNSET
    numeric: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alpha2 = self.alpha2

        alpha3 = self.alpha3

        apolitical_name = self.apolitical_name

        numeric = self.numeric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if alpha2 is not UNSET:
            field_dict["alpha2"] = alpha2
        if alpha3 is not UNSET:
            field_dict["alpha3"] = alpha3
        if apolitical_name is not UNSET:
            field_dict["apolitical_name"] = apolitical_name
        if numeric is not UNSET:
            field_dict["numeric"] = numeric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        alpha2 = d.pop("alpha2", UNSET)

        alpha3 = d.pop("alpha3", UNSET)

        apolitical_name = d.pop("apolitical_name", UNSET)

        numeric = d.pop("numeric", UNSET)

        country_schema = cls(
            name=name,
            alpha2=alpha2,
            alpha3=alpha3,
            apolitical_name=apolitical_name,
            numeric=numeric,
        )

        country_schema.additional_properties = d
        return country_schema

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
