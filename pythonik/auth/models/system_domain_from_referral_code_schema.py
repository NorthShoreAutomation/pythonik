from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_domain_from_referral_code_schema_billing_tier import (
    SystemDomainFromReferralCodeSchemaBillingTier,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemDomainFromReferralCodeSchema")


@_attrs_define
class SystemDomainFromReferralCodeSchema:
    """
    Attributes:
        country_code (str):
        name (str):
        admin_email (str | Unset):
        admin_first_name (str | Unset):
        admin_last_name (str | Unset):
        admin_password (str | Unset):
        billing_tier (SystemDomainFromReferralCodeSchemaBillingTier | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        id (UUID | Unset):
    """

    country_code: str
    name: str
    admin_email: str | Unset = UNSET
    admin_first_name: str | Unset = UNSET
    admin_last_name: str | Unset = UNSET
    admin_password: str | Unset = UNSET
    billing_tier: SystemDomainFromReferralCodeSchemaBillingTier | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        name = self.name

        admin_email = self.admin_email

        admin_first_name = self.admin_first_name

        admin_last_name = self.admin_last_name

        admin_password = self.admin_password

        billing_tier: str | Unset = UNSET
        if not isinstance(self.billing_tier, Unset):
            billing_tier = self.billing_tier.value

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country_code": country_code,
                "name": name,
            }
        )
        if admin_email is not UNSET:
            field_dict["admin_email"] = admin_email
        if admin_first_name is not UNSET:
            field_dict["admin_first_name"] = admin_first_name
        if admin_last_name is not UNSET:
            field_dict["admin_last_name"] = admin_last_name
        if admin_password is not UNSET:
            field_dict["admin_password"] = admin_password
        if billing_tier is not UNSET:
            field_dict["billing_tier"] = billing_tier
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("country_code")

        name = d.pop("name")

        admin_email = d.pop("admin_email", UNSET)

        admin_first_name = d.pop("admin_first_name", UNSET)

        admin_last_name = d.pop("admin_last_name", UNSET)

        admin_password = d.pop("admin_password", UNSET)

        _billing_tier = d.pop("billing_tier", UNSET)
        billing_tier: SystemDomainFromReferralCodeSchemaBillingTier | Unset
        if isinstance(_billing_tier, Unset):
            billing_tier = UNSET
        else:
            billing_tier = SystemDomainFromReferralCodeSchemaBillingTier(_billing_tier)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        system_domain_from_referral_code_schema = cls(
            country_code=country_code,
            name=name,
            admin_email=admin_email,
            admin_first_name=admin_first_name,
            admin_last_name=admin_last_name,
            admin_password=admin_password,
            billing_tier=billing_tier,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            id=id,
        )

        system_domain_from_referral_code_schema.additional_properties = d
        return system_domain_from_referral_code_schema

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
