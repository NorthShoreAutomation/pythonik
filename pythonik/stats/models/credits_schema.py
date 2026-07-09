from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditsSchema")


@_attrs_define
class CreditsSchema:
    """
    Attributes:
        credits_ (int):
        country (None | str | Unset):
        currency (None | str | Unset):
        total (float | None | Unset):
        vat (int | None | Unset):
    """

    credits_: int
    country: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    total: float | None | Unset = UNSET
    vat: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

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

        total: float | None | Unset
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

        def _parse_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        def _parse_vat(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vat = _parse_vat(d.pop("vat", UNSET))

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
