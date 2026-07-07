from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingCreditsSchema")


@_attrs_define
class BillingCreditsSchema:
    """
    Attributes:
        credits_ (int):
        auto_pay (bool | Unset):
        country (str | Unset):
        currency (str | Unset):
        custom_message (str | Unset):
        system_domain_id (UUID | Unset):
        total (str | Unset):
        vat (int | Unset):
    """

    credits_: int
    auto_pay: bool | Unset = UNSET
    country: str | Unset = UNSET
    currency: str | Unset = UNSET
    custom_message: str | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    total: str | Unset = UNSET
    vat: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        auto_pay = self.auto_pay

        country = self.country

        currency = self.currency

        custom_message = self.custom_message

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        total = self.total

        vat = self.vat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
            }
        )
        if auto_pay is not UNSET:
            field_dict["auto_pay"] = auto_pay
        if country is not UNSET:
            field_dict["country"] = country
        if currency is not UNSET:
            field_dict["currency"] = currency
        if custom_message is not UNSET:
            field_dict["custom_message"] = custom_message
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if total is not UNSET:
            field_dict["total"] = total
        if vat is not UNSET:
            field_dict["vat"] = vat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_ = d.pop("credits")

        auto_pay = d.pop("auto_pay", UNSET)

        country = d.pop("country", UNSET)

        currency = d.pop("currency", UNSET)

        custom_message = d.pop("custom_message", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        total = d.pop("total", UNSET)

        vat = d.pop("vat", UNSET)

        billing_credits_schema = cls(
            credits_=credits_,
            auto_pay=auto_pay,
            country=country,
            currency=currency,
            custom_message=custom_message,
            system_domain_id=system_domain_id,
            total=total,
            vat=vat,
        )

        billing_credits_schema.additional_properties = d
        return billing_credits_schema

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
