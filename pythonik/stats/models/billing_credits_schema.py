from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        auto_pay (bool | None | Unset):
        country (None | str | Unset):
        currency (None | str | Unset):
        custom_message (None | str | Unset):
        system_domain_id (None | Unset | UUID):
        total (None | str | Unset):
        vat (int | None | Unset):
    """

    credits_: int
    auto_pay: bool | None | Unset = UNSET
    country: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    custom_message: None | str | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    total: None | str | Unset = UNSET
    vat: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        auto_pay: bool | None | Unset
        if isinstance(self.auto_pay, Unset):
            auto_pay = UNSET
        else:
            auto_pay = self.auto_pay

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        custom_message: None | str | Unset
        if isinstance(self.custom_message, Unset):
            custom_message = UNSET
        else:
            custom_message = self.custom_message

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        total: None | str | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        vat: int | None | Unset
        if isinstance(self.vat, Unset):
            vat = UNSET
        else:
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

        def _parse_auto_pay(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_pay = _parse_auto_pay(d.pop("auto_pay", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_custom_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_message = _parse_custom_message(d.pop("custom_message", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        def _parse_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        def _parse_vat(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vat = _parse_vat(d.pop("vat", UNSET))

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
