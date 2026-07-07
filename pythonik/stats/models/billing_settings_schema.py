from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSettingsSchema")


@_attrs_define
class BillingSettingsSchema:
    """
    Attributes:
        auto_refill_amount (int | None | Unset):
        enable_auto_top_up (bool | Unset):
        low_balance_trigger (int | None | Unset):
    """

    auto_refill_amount: int | None | Unset = UNSET
    enable_auto_top_up: bool | Unset = UNSET
    low_balance_trigger: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_refill_amount: int | None | Unset
        if isinstance(self.auto_refill_amount, Unset):
            auto_refill_amount = UNSET
        else:
            auto_refill_amount = self.auto_refill_amount

        enable_auto_top_up = self.enable_auto_top_up

        low_balance_trigger: int | None | Unset
        if isinstance(self.low_balance_trigger, Unset):
            low_balance_trigger = UNSET
        else:
            low_balance_trigger = self.low_balance_trigger

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_refill_amount is not UNSET:
            field_dict["auto_refill_amount"] = auto_refill_amount
        if enable_auto_top_up is not UNSET:
            field_dict["enable_auto_top_up"] = enable_auto_top_up
        if low_balance_trigger is not UNSET:
            field_dict["low_balance_trigger"] = low_balance_trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_auto_refill_amount(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_refill_amount = _parse_auto_refill_amount(
            d.pop("auto_refill_amount", UNSET)
        )

        enable_auto_top_up = d.pop("enable_auto_top_up", UNSET)

        def _parse_low_balance_trigger(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        low_balance_trigger = _parse_low_balance_trigger(
            d.pop("low_balance_trigger", UNSET)
        )

        billing_settings_schema = cls(
            auto_refill_amount=auto_refill_amount,
            enable_auto_top_up=enable_auto_top_up,
            low_balance_trigger=low_balance_trigger,
        )

        billing_settings_schema.additional_properties = d
        return billing_settings_schema

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
