from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_customer_shipping import BillingCustomerShipping


T = TypeVar("T", bound="BillingCustomerSchema")


@_attrs_define
class BillingCustomerSchema:
    """
    Attributes:
        shipping (BillingCustomerShipping):
        business_vat_id (str | Unset):
        email (str | Unset):
        enable_subscription (bool | Unset):
    """

    shipping: BillingCustomerShipping
    business_vat_id: str | Unset = UNSET
    email: str | Unset = UNSET
    enable_subscription: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipping = self.shipping.to_dict()

        business_vat_id = self.business_vat_id

        email = self.email

        enable_subscription = self.enable_subscription

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipping": shipping,
            }
        )
        if business_vat_id is not UNSET:
            field_dict["business_vat_id"] = business_vat_id
        if email is not UNSET:
            field_dict["email"] = email
        if enable_subscription is not UNSET:
            field_dict["enable_subscription"] = enable_subscription

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_customer_shipping import BillingCustomerShipping

        d = dict(src_dict)
        shipping = BillingCustomerShipping.from_dict(d.pop("shipping"))

        business_vat_id = d.pop("business_vat_id", UNSET)

        email = d.pop("email", UNSET)

        enable_subscription = d.pop("enable_subscription", UNSET)

        billing_customer_schema = cls(
            shipping=shipping,
            business_vat_id=business_vat_id,
            email=email,
            enable_subscription=enable_subscription,
        )

        billing_customer_schema.additional_properties = d
        return billing_customer_schema

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
