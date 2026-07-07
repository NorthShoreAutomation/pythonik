from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.referral_code_schema_billing_tier import ReferralCodeSchemaBillingTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferralCodeSchema")


@_attrs_define
class ReferralCodeSchema:
    """
    Attributes:
        code (str):
        valid_to (datetime.datetime):
        value (float):
        billing_tier (ReferralCodeSchemaBillingTier | Unset):
        credit_expiry_days (int | None | Unset):
        do_not_delete (bool | None | Unset):
        freeze_date (datetime.datetime | None | Unset):
        is_plg (bool | None | Unset):
        manage_system_domain_id (None | Unset | UUID):
        ordway_customer_id (None | str | Unset):
        sales_force_id (None | str | Unset):
    """

    code: str
    valid_to: datetime.datetime
    value: float
    billing_tier: ReferralCodeSchemaBillingTier | Unset = UNSET
    credit_expiry_days: int | None | Unset = UNSET
    do_not_delete: bool | None | Unset = UNSET
    freeze_date: datetime.datetime | None | Unset = UNSET
    is_plg: bool | None | Unset = UNSET
    manage_system_domain_id: None | Unset | UUID = UNSET
    ordway_customer_id: None | str | Unset = UNSET
    sales_force_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        valid_to = self.valid_to.isoformat()

        value = self.value

        billing_tier: str | Unset = UNSET
        if not isinstance(self.billing_tier, Unset):
            billing_tier = self.billing_tier.value

        credit_expiry_days: int | None | Unset
        if isinstance(self.credit_expiry_days, Unset):
            credit_expiry_days = UNSET
        else:
            credit_expiry_days = self.credit_expiry_days

        do_not_delete: bool | None | Unset
        if isinstance(self.do_not_delete, Unset):
            do_not_delete = UNSET
        else:
            do_not_delete = self.do_not_delete

        freeze_date: None | str | Unset
        if isinstance(self.freeze_date, Unset):
            freeze_date = UNSET
        elif isinstance(self.freeze_date, datetime.datetime):
            freeze_date = self.freeze_date.isoformat()
        else:
            freeze_date = self.freeze_date

        is_plg: bool | None | Unset
        if isinstance(self.is_plg, Unset):
            is_plg = UNSET
        else:
            is_plg = self.is_plg

        manage_system_domain_id: None | str | Unset
        if isinstance(self.manage_system_domain_id, Unset):
            manage_system_domain_id = UNSET
        elif isinstance(self.manage_system_domain_id, UUID):
            manage_system_domain_id = str(self.manage_system_domain_id)
        else:
            manage_system_domain_id = self.manage_system_domain_id

        ordway_customer_id: None | str | Unset
        if isinstance(self.ordway_customer_id, Unset):
            ordway_customer_id = UNSET
        else:
            ordway_customer_id = self.ordway_customer_id

        sales_force_id: None | str | Unset
        if isinstance(self.sales_force_id, Unset):
            sales_force_id = UNSET
        else:
            sales_force_id = self.sales_force_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "valid_to": valid_to,
                "value": value,
            }
        )
        if billing_tier is not UNSET:
            field_dict["billing_tier"] = billing_tier
        if credit_expiry_days is not UNSET:
            field_dict["credit_expiry_days"] = credit_expiry_days
        if do_not_delete is not UNSET:
            field_dict["do_not_delete"] = do_not_delete
        if freeze_date is not UNSET:
            field_dict["freeze_date"] = freeze_date
        if is_plg is not UNSET:
            field_dict["is_plg"] = is_plg
        if manage_system_domain_id is not UNSET:
            field_dict["manage_system_domain_id"] = manage_system_domain_id
        if ordway_customer_id is not UNSET:
            field_dict["ordway_customer_id"] = ordway_customer_id
        if sales_force_id is not UNSET:
            field_dict["sales_force_id"] = sales_force_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        valid_to = datetime.datetime.fromisoformat(d.pop("valid_to"))

        value = d.pop("value")

        _billing_tier = d.pop("billing_tier", UNSET)
        billing_tier: ReferralCodeSchemaBillingTier | Unset
        if isinstance(_billing_tier, Unset):
            billing_tier = UNSET
        else:
            billing_tier = ReferralCodeSchemaBillingTier(_billing_tier)

        def _parse_credit_expiry_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credit_expiry_days = _parse_credit_expiry_days(
            d.pop("credit_expiry_days", UNSET)
        )

        def _parse_do_not_delete(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        do_not_delete = _parse_do_not_delete(d.pop("do_not_delete", UNSET))

        def _parse_freeze_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                freeze_date_type_0 = datetime.datetime.fromisoformat(data)

                return freeze_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        freeze_date = _parse_freeze_date(d.pop("freeze_date", UNSET))

        def _parse_is_plg(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_plg = _parse_is_plg(d.pop("is_plg", UNSET))

        def _parse_manage_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manage_system_domain_id_type_0 = UUID(data)

                return manage_system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        manage_system_domain_id = _parse_manage_system_domain_id(
            d.pop("manage_system_domain_id", UNSET)
        )

        def _parse_ordway_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ordway_customer_id = _parse_ordway_customer_id(
            d.pop("ordway_customer_id", UNSET)
        )

        def _parse_sales_force_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sales_force_id = _parse_sales_force_id(d.pop("sales_force_id", UNSET))

        referral_code_schema = cls(
            code=code,
            valid_to=valid_to,
            value=value,
            billing_tier=billing_tier,
            credit_expiry_days=credit_expiry_days,
            do_not_delete=do_not_delete,
            freeze_date=freeze_date,
            is_plg=is_plg,
            manage_system_domain_id=manage_system_domain_id,
            ordway_customer_id=ordway_customer_id,
            sales_force_id=sales_force_id,
        )

        referral_code_schema.additional_properties = d
        return referral_code_schema

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
