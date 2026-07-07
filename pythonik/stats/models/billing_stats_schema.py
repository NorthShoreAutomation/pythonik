from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_stats_schema_system_domain_status import (
    BillingStatsSchemaSystemDomainStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingStatsSchema")


@_attrs_define
class BillingStatsSchema:
    """
    Attributes:
        system_domain_type (str):
        system_domain_warning_message (str):
        current_balance (float | Unset):
        invoice_end_of_month (bool | Unset):
        new_billing_enabled (bool | Unset):
        stripe_id (bool | Unset):
        system_domain_status (BillingStatsSchemaSystemDomainStatus | Unset):
    """

    system_domain_type: str
    system_domain_warning_message: str
    current_balance: float | Unset = UNSET
    invoice_end_of_month: bool | Unset = UNSET
    new_billing_enabled: bool | Unset = UNSET
    stripe_id: bool | Unset = UNSET
    system_domain_status: BillingStatsSchemaSystemDomainStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_domain_type = self.system_domain_type

        system_domain_warning_message = self.system_domain_warning_message

        current_balance = self.current_balance

        invoice_end_of_month = self.invoice_end_of_month

        new_billing_enabled = self.new_billing_enabled

        stripe_id = self.stripe_id

        system_domain_status: str | Unset = UNSET
        if not isinstance(self.system_domain_status, Unset):
            system_domain_status = self.system_domain_status.value

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
        d = dict(src_dict)
        system_domain_type = d.pop("system_domain_type")

        system_domain_warning_message = d.pop("system_domain_warning_message")

        current_balance = d.pop("current_balance", UNSET)

        invoice_end_of_month = d.pop("invoice_end_of_month", UNSET)

        new_billing_enabled = d.pop("new_billing_enabled", UNSET)

        stripe_id = d.pop("stripe_id", UNSET)

        _system_domain_status = d.pop("system_domain_status", UNSET)
        system_domain_status: BillingStatsSchemaSystemDomainStatus | Unset
        if isinstance(_system_domain_status, Unset):
            system_domain_status = UNSET
        else:
            system_domain_status = BillingStatsSchemaSystemDomainStatus(
                _system_domain_status
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
