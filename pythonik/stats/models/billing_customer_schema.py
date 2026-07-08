from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        business_vat_id (None | str | Unset):
        email (None | str | Unset):
        enable_subscription (bool | None | Unset):
    """

    shipping: BillingCustomerShipping
    business_vat_id: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    enable_subscription: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipping = self.shipping.to_dict()

        business_vat_id: None | str | Unset
        if isinstance(self.business_vat_id, Unset):
            business_vat_id = UNSET
        else:
            business_vat_id = self.business_vat_id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        enable_subscription: bool | None | Unset
        if isinstance(self.enable_subscription, Unset):
            enable_subscription = UNSET
        else:
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

        def _parse_business_vat_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_vat_id = _parse_business_vat_id(d.pop("business_vat_id", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_enable_subscription(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_subscription = _parse_enable_subscription(
            d.pop("enable_subscription", UNSET)
        )

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
