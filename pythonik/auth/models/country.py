from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Country")


@_attrs_define
class Country:
    """
    Attributes:
        name (str):
        alpha2 (None | str | Unset):
        alpha3 (None | str | Unset):
        apolitical_name (None | str | Unset):
        numeric (None | str | Unset):
    """

    name: str
    alpha2: None | str | Unset = UNSET
    alpha3: None | str | Unset = UNSET
    apolitical_name: None | str | Unset = UNSET
    numeric: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alpha2: None | str | Unset
        if isinstance(self.alpha2, Unset):
            alpha2 = UNSET
        else:
            alpha2 = self.alpha2

        alpha3: None | str | Unset
        if isinstance(self.alpha3, Unset):
            alpha3 = UNSET
        else:
            alpha3 = self.alpha3

        apolitical_name: None | str | Unset
        if isinstance(self.apolitical_name, Unset):
            apolitical_name = UNSET
        else:
            apolitical_name = self.apolitical_name

        numeric: None | str | Unset
        if isinstance(self.numeric, Unset):
            numeric = UNSET
        else:
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

        def _parse_alpha2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alpha2 = _parse_alpha2(d.pop("alpha2", UNSET))

        def _parse_alpha3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alpha3 = _parse_alpha3(d.pop("alpha3", UNSET))

        def _parse_apolitical_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        apolitical_name = _parse_apolitical_name(d.pop("apolitical_name", UNSET))

        def _parse_numeric(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numeric = _parse_numeric(d.pop("numeric", UNSET))

        country = cls(
            name=name,
            alpha2=alpha2,
            alpha3=alpha3,
            apolitical_name=apolitical_name,
            numeric=numeric,
        )

        country.additional_properties = d
        return country

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
