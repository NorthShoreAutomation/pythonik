from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditsSchema")


@_attrs_define
class CreditsSchema:
    """
    Attributes:
        credits_ (int):
        country (str | Unset):
        currency (str | Unset):
        total (float | Unset):
        vat (int | Unset):
    """

    credits_: int
    country: str | Unset = UNSET
    currency: str | Unset = UNSET
    total: float | Unset = UNSET
    vat: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        country = self.country

        currency = self.currency

        total = self.total

        vat = self.vat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total is not UNSET:
            field_dict["total"] = total
        if vat is not UNSET:
            field_dict["vat"] = vat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_ = d.pop("credits")

        country = d.pop("country", UNSET)

        currency = d.pop("currency", UNSET)

        total = d.pop("total", UNSET)

        vat = d.pop("vat", UNSET)

        credits_schema = cls(
            credits_=credits_,
            country=country,
            currency=currency,
            total=total,
            vat=vat,
        )

        credits_schema.additional_properties = d
        return credits_schema

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
