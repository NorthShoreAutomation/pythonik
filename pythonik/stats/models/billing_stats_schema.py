from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_stats_schema_system_domain_status_type_1 import (
        BillingStatsSchemaSystemDomainStatusType1,
    )


T = TypeVar("T", bound="BillingStatsSchema")


@_attrs_define
class BillingStatsSchema:
    """
    Attributes:
        system_domain_type (str):
        system_domain_warning_message (str):
        current_balance (float | None | Unset):
        invoice_end_of_month (bool | None | Unset):
        new_billing_enabled (bool | None | Unset):
        stripe_id (bool | None | Unset):
        system_domain_status (BillingStatsSchemaSystemDomainStatusType1 | None | Unset):
    """

    system_domain_type: str
    system_domain_warning_message: str
    current_balance: float | None | Unset = UNSET
    invoice_end_of_month: bool | None | Unset = UNSET
    new_billing_enabled: bool | None | Unset = UNSET
    stripe_id: bool | None | Unset = UNSET
    system_domain_status: BillingStatsSchemaSystemDomainStatusType1 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_stats_schema_system_domain_status_type_1 import (
            BillingStatsSchemaSystemDomainStatusType1,
        )

        system_domain_type = self.system_domain_type

        system_domain_warning_message = self.system_domain_warning_message

        current_balance: float | None | Unset
        if isinstance(self.current_balance, Unset):
            current_balance = UNSET
        else:
            current_balance = self.current_balance

        invoice_end_of_month: bool | None | Unset
        if isinstance(self.invoice_end_of_month, Unset):
            invoice_end_of_month = UNSET
        else:
            invoice_end_of_month = self.invoice_end_of_month

        new_billing_enabled: bool | None | Unset
        if isinstance(self.new_billing_enabled, Unset):
            new_billing_enabled = UNSET
        else:
            new_billing_enabled = self.new_billing_enabled

        stripe_id: bool | None | Unset
        if isinstance(self.stripe_id, Unset):
            stripe_id = UNSET
        else:
            stripe_id = self.stripe_id

        system_domain_status: dict[str, Any] | None | Unset
        if isinstance(self.system_domain_status, Unset):
            system_domain_status = UNSET
        elif isinstance(
            self.system_domain_status, BillingStatsSchemaSystemDomainStatusType1
        ):
            system_domain_status = self.system_domain_status.to_dict()
        else:
            system_domain_status = self.system_domain_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "system_domain_type": system_domain_type,
                "system_domain_warning_message": system_domain_warning_message,
            }
        )
        if current_balance is not UNSET:
            field_dict["current_balance"] = current_balance
        if invoice_end_of_month is not UNSET:
            field_dict["invoice_end_of_month"] = invoice_end_of_month
        if new_billing_enabled is not UNSET:
            field_dict["new_billing_enabled"] = new_billing_enabled
        if stripe_id is not UNSET:
            field_dict["stripe_id"] = stripe_id
        if system_domain_status is not UNSET:
            field_dict["system_domain_status"] = system_domain_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_stats_schema_system_domain_status_type_1 import (
            BillingStatsSchemaSystemDomainStatusType1,
        )

        d = dict(src_dict)
        system_domain_type = d.pop("system_domain_type")

        system_domain_warning_message = d.pop("system_domain_warning_message")

        def _parse_current_balance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_balance = _parse_current_balance(d.pop("current_balance", UNSET))

        def _parse_invoice_end_of_month(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        invoice_end_of_month = _parse_invoice_end_of_month(
            d.pop("invoice_end_of_month", UNSET)
        )

        def _parse_new_billing_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        new_billing_enabled = _parse_new_billing_enabled(
            d.pop("new_billing_enabled", UNSET)
        )

        def _parse_stripe_id(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        stripe_id = _parse_stripe_id(d.pop("stripe_id", UNSET))

        def _parse_system_domain_status(
            data: object,
        ) -> BillingStatsSchemaSystemDomainStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                system_domain_status_type_1 = (
                    BillingStatsSchemaSystemDomainStatusType1.from_dict(data)
                )

                return system_domain_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BillingStatsSchemaSystemDomainStatusType1 | None | Unset, data)

        system_domain_status = _parse_system_domain_status(
            d.pop("system_domain_status", UNSET)
        )

        billing_stats_schema = cls(
            system_domain_type=system_domain_type,
            system_domain_warning_message=system_domain_warning_message,
            current_balance=current_balance,
            invoice_end_of_month=invoice_end_of_month,
            new_billing_enabled=new_billing_enabled,
            stripe_id=stripe_id,
            system_domain_status=system_domain_status,
        )

        billing_stats_schema.additional_properties = d
        return billing_stats_schema

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
