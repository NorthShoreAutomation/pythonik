from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_customer_shipping_address import (
        BillingCustomerShippingAddress,
    )


T = TypeVar("T", bound="BillingCustomerShipping")


@_attrs_define
class BillingCustomerShipping:
    """
    Attributes:
        address (BillingCustomerShippingAddress):
        name (str):
        phone (None | str | Unset):
    """

    address: BillingCustomerShippingAddress
    name: str
    phone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address.to_dict()

        name = self.name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "name": name,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_customer_shipping_address import (
            BillingCustomerShippingAddress,
        )

        d = dict(src_dict)
        address = BillingCustomerShippingAddress.from_dict(d.pop("address"))

        name = d.pop("name")

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        billing_customer_shipping = cls(
            address=address,
            name=name,
            phone=phone,
        )

        billing_customer_shipping.additional_properties = d
        return billing_customer_shipping

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
