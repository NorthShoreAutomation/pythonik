from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        admin_email (None | str | Unset):
        admin_first_name (None | str | Unset):
        admin_last_name (None | str | Unset):
        admin_password (None | str | Unset):
        billing_tier (None | SystemDomainFromReferralCodeSchemaBillingTier | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        description (None | str | Unset):
        id (None | Unset | UUID):
    """

    country_code: str
    name: str
    admin_email: None | str | Unset = UNSET
    admin_first_name: None | str | Unset = UNSET
    admin_last_name: None | str | Unset = UNSET
    admin_password: None | str | Unset = UNSET
    billing_tier: None | SystemDomainFromReferralCodeSchemaBillingTier | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        name = self.name

        admin_email: None | str | Unset
        if isinstance(self.admin_email, Unset):
            admin_email = UNSET
        else:
            admin_email = self.admin_email

        admin_first_name: None | str | Unset
        if isinstance(self.admin_first_name, Unset):
            admin_first_name = UNSET
        else:
            admin_first_name = self.admin_first_name

        admin_last_name: None | str | Unset
        if isinstance(self.admin_last_name, Unset):
            admin_last_name = UNSET
        else:
            admin_last_name = self.admin_last_name

        admin_password: None | str | Unset
        if isinstance(self.admin_password, Unset):
            admin_password = UNSET
        else:
            admin_password = self.admin_password

        billing_tier: None | str | Unset
        if isinstance(self.billing_tier, Unset):
            billing_tier = UNSET
        elif isinstance(
            self.billing_tier, SystemDomainFromReferralCodeSchemaBillingTier
        ):
            billing_tier = self.billing_tier.value
        else:
            billing_tier = self.billing_tier

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        def _parse_admin_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_email = _parse_admin_email(d.pop("admin_email", UNSET))

        def _parse_admin_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_first_name = _parse_admin_first_name(d.pop("admin_first_name", UNSET))

        def _parse_admin_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_last_name = _parse_admin_last_name(d.pop("admin_last_name", UNSET))

        def _parse_admin_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_password = _parse_admin_password(d.pop("admin_password", UNSET))

        def _parse_billing_tier(
            data: object,
        ) -> None | SystemDomainFromReferralCodeSchemaBillingTier | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                billing_tier_type_1 = SystemDomainFromReferralCodeSchemaBillingTier(
                    data
                )

                return billing_tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | SystemDomainFromReferralCodeSchemaBillingTier | Unset, data
            )

        billing_tier = _parse_billing_tier(d.pop("billing_tier", UNSET))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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
