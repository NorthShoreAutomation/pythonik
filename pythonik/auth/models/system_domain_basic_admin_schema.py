from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_domain_basic_admin_schema_billing_tier import (
    SystemDomainBasicAdminSchemaBillingTier,
)
from ..models.system_domain_basic_admin_schema_type import (
    SystemDomainBasicAdminSchemaType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemDomainBasicAdminSchema")


@_attrs_define
class SystemDomainBasicAdminSchema:
    """
    Attributes:
        name (str):
        billing_tier (SystemDomainBasicAdminSchemaBillingTier | Unset):
        contract_end_date (datetime.datetime | Unset):
        country (str | Unset):
        date_created (datetime.datetime | Unset):
        features (list[str] | Unset):
        freeze_date (datetime.datetime | Unset):
        id (UUID | Unset):
        is_plg (bool | Unset):
        type_ (SystemDomainBasicAdminSchemaType | Unset):
    """

    name: str
    billing_tier: SystemDomainBasicAdminSchemaBillingTier | Unset = UNSET
    contract_end_date: datetime.datetime | Unset = UNSET
    country: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    features: list[str] | Unset = UNSET
    freeze_date: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    is_plg: bool | Unset = UNSET
    type_: SystemDomainBasicAdminSchemaType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        billing_tier: str | Unset = UNSET
        if not isinstance(self.billing_tier, Unset):
            billing_tier = self.billing_tier.value

        contract_end_date: str | Unset = UNSET
        if not isinstance(self.contract_end_date, Unset):
            contract_end_date = self.contract_end_date.isoformat()

        country = self.country

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        freeze_date: str | Unset = UNSET
        if not isinstance(self.freeze_date, Unset):
            freeze_date = self.freeze_date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_plg = self.is_plg

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if billing_tier is not UNSET:
            field_dict["billing_tier"] = billing_tier
        if contract_end_date is not UNSET:
            field_dict["contract_end_date"] = contract_end_date
        if country is not UNSET:
            field_dict["country"] = country
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if features is not UNSET:
            field_dict["features"] = features
        if freeze_date is not UNSET:
            field_dict["freeze_date"] = freeze_date
        if id is not UNSET:
            field_dict["id"] = id
        if is_plg is not UNSET:
            field_dict["is_plg"] = is_plg
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _billing_tier = d.pop("billing_tier", UNSET)
        billing_tier: SystemDomainBasicAdminSchemaBillingTier | Unset
        if isinstance(_billing_tier, Unset):
            billing_tier = UNSET
        else:
            billing_tier = SystemDomainBasicAdminSchemaBillingTier(_billing_tier)

        _contract_end_date = d.pop("contract_end_date", UNSET)
        contract_end_date: datetime.datetime | Unset
        if isinstance(_contract_end_date, Unset):
            contract_end_date = UNSET
        else:
            contract_end_date = datetime.datetime.fromisoformat(_contract_end_date)

        country = d.pop("country", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        features = cast(list[str], d.pop("features", UNSET))

        _freeze_date = d.pop("freeze_date", UNSET)
        freeze_date: datetime.datetime | Unset
        if isinstance(_freeze_date, Unset):
            freeze_date = UNSET
        else:
            freeze_date = datetime.datetime.fromisoformat(_freeze_date)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_plg = d.pop("is_plg", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SystemDomainBasicAdminSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SystemDomainBasicAdminSchemaType(_type_)

        system_domain_basic_admin_schema = cls(
            name=name,
            billing_tier=billing_tier,
            contract_end_date=contract_end_date,
            country=country,
            date_created=date_created,
            features=features,
            freeze_date=freeze_date,
            id=id,
            is_plg=is_plg,
            type_=type_,
        )

        system_domain_basic_admin_schema.additional_properties = d
        return system_domain_basic_admin_schema

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
