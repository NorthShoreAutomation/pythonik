from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_schema_currency import BillingSchemaCurrency
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSchema")


@_attrs_define
class BillingSchema:
    """
    Attributes:
        label (str):
        system_domain_id (UUID):
        value (float):
        balance (float | None | Unset):
        consumption_subtype (None | str | Unset):
        consumption_type (None | str | Unset):
        currency (BillingSchemaCurrency | None | Unset):
        date (datetime.datetime | None | Unset):
        expiration_date (datetime.datetime | None | Unset):
        id (None | Unset | UUID):
        price_list (None | str | Unset):
    """

    label: str
    system_domain_id: UUID
    value: float
    balance: float | None | Unset = UNSET
    consumption_subtype: None | str | Unset = UNSET
    consumption_type: None | str | Unset = UNSET
    currency: BillingSchemaCurrency | None | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET
    expiration_date: datetime.datetime | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    price_list: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        system_domain_id = str(self.system_domain_id)

        value = self.value

        balance: float | None | Unset
        if isinstance(self.balance, Unset):
            balance = UNSET
        else:
            balance = self.balance

        consumption_subtype: None | str | Unset
        if isinstance(self.consumption_subtype, Unset):
            consumption_subtype = UNSET
        else:
            consumption_subtype = self.consumption_subtype

        consumption_type: None | str | Unset
        if isinstance(self.consumption_type, Unset):
            consumption_type = UNSET
        else:
            consumption_type = self.consumption_type

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        elif isinstance(self.currency, BillingSchemaCurrency):
            currency = self.currency.value
        else:
            currency = self.currency

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        expiration_date: None | str | Unset
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        price_list: None | str | Unset
        if isinstance(self.price_list, Unset):
            price_list = UNSET
        else:
            price_list = self.price_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "system_domain_id": system_domain_id,
                "value": value,
            }
        )
        if balance is not UNSET:
            field_dict["balance"] = balance
        if consumption_subtype is not UNSET:
            field_dict["consumption_subtype"] = consumption_subtype
        if consumption_type is not UNSET:
            field_dict["consumption_type"] = consumption_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if date is not UNSET:
            field_dict["date"] = date
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if id is not UNSET:
            field_dict["id"] = id
        if price_list is not UNSET:
            field_dict["price_list"] = price_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        system_domain_id = UUID(d.pop("system_domain_id"))

        value = d.pop("value")

        def _parse_balance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        balance = _parse_balance(d.pop("balance", UNSET))

        def _parse_consumption_subtype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consumption_subtype = _parse_consumption_subtype(
            d.pop("consumption_subtype", UNSET)
        )

        def _parse_consumption_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consumption_type = _parse_consumption_type(d.pop("consumption_type", UNSET))

        def _parse_currency(data: object) -> BillingSchemaCurrency | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                currency_type_1 = BillingSchemaCurrency(data)

                return currency_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BillingSchemaCurrency | None | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.datetime.fromisoformat(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = datetime.datetime.fromisoformat(data)

                return expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date = _parse_expiration_date(d.pop("expiration_date", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_price_list(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_list = _parse_price_list(d.pop("price_list", UNSET))

        billing_schema = cls(
            label=label,
            system_domain_id=system_domain_id,
            value=value,
            balance=balance,
            consumption_subtype=consumption_subtype,
            consumption_type=consumption_type,
            currency=currency,
            date=date,
            expiration_date=expiration_date,
            id=id,
            price_list=price_list,
        )

        billing_schema.additional_properties = d
        return billing_schema

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
