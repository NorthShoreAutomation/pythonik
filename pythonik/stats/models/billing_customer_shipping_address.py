from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingCustomerShippingAddress")


@_attrs_define
class BillingCustomerShippingAddress:
    """
    Attributes:
        city (str):
        country (str):
        line1 (str):
        postal_code (str):
        line2 (None | str | Unset):
        state (None | str | Unset):
    """

    city: str
    country: str
    line1: str
    postal_code: str
    line2: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country = self.country

        line1 = self.line1

        postal_code = self.postal_code

        line2: None | str | Unset
        if isinstance(self.line2, Unset):
            line2 = UNSET
        else:
            line2 = self.line2

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "country": country,
                "line1": line1,
                "postal_code": postal_code,
            }
        )
        if line2 is not UNSET:
            field_dict["line2"] = line2
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city")

        country = d.pop("country")

        line1 = d.pop("line1")

        postal_code = d.pop("postal_code")

        def _parse_line2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line2 = _parse_line2(d.pop("line2", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        billing_customer_shipping_address = cls(
            city=city,
            country=country,
            line1=line1,
            postal_code=postal_code,
            line2=line2,
            state=state,
        )

        billing_customer_shipping_address.additional_properties = d
        return billing_customer_shipping_address

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
