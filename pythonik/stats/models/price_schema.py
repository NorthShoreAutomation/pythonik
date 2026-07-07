from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.price_schema_currency import PriceSchemaCurrency

if TYPE_CHECKING:
    from ..models.price_schema_prices import PriceSchemaPrices


T = TypeVar("T", bound="PriceSchema")


@_attrs_define
class PriceSchema:
    """
    Attributes:
        currency (PriceSchemaCurrency):
        name (str):
        prices (PriceSchemaPrices):
    """

    currency: PriceSchemaCurrency
    name: str
    prices: PriceSchemaPrices
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency.value

        name = self.name

        prices = self.prices.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "name": name,
                "prices": prices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price_schema_prices import PriceSchemaPrices

        d = dict(src_dict)
        currency = PriceSchemaCurrency(d.pop("currency"))

        name = d.pop("name")

        prices = PriceSchemaPrices.from_dict(d.pop("prices"))

        price_schema = cls(
            currency=currency,
            name=name,
            prices=prices,
        )

        price_schema.additional_properties = d
        return price_schema

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
