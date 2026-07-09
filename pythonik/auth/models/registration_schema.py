from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistrationSchema")


@_attrs_define
class RegistrationSchema:
    """
    Attributes:
        country (str):
        email (str):
        first_name (str):
        last_name (str):
        password (str):
        base_url (None | str | Unset):
        company_name (None | str | Unset):
        date_created (datetime.datetime | None | Unset):
        email_marketing_consent (bool | None | Unset):
        id (None | Unset | UUID):
        marketplace_signup_nonce (None | str | Unset):
        ordway_customer_id (None | str | Unset):
        ordway_subscription_id (None | str | Unset):
        referral_code (None | str | Unset):
        stripe_id (None | str | Unset):
    """

    country: str
    email: str
    first_name: str
    last_name: str
    password: str
    base_url: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    email_marketing_consent: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    marketplace_signup_nonce: None | str | Unset = UNSET
    ordway_customer_id: None | str | Unset = UNSET
    ordway_subscription_id: None | str | Unset = UNSET
    referral_code: None | str | Unset = UNSET
    stripe_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        password = self.password

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        email_marketing_consent: bool | None | Unset
        if isinstance(self.email_marketing_consent, Unset):
            email_marketing_consent = UNSET
        else:
            email_marketing_consent = self.email_marketing_consent

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        marketplace_signup_nonce: None | str | Unset
        if isinstance(self.marketplace_signup_nonce, Unset):
            marketplace_signup_nonce = UNSET
        else:
            marketplace_signup_nonce = self.marketplace_signup_nonce

        ordway_customer_id: None | str | Unset
        if isinstance(self.ordway_customer_id, Unset):
            ordway_customer_id = UNSET
        else:
            ordway_customer_id = self.ordway_customer_id

        ordway_subscription_id: None | str | Unset
        if isinstance(self.ordway_subscription_id, Unset):
            ordway_subscription_id = UNSET
        else:
            ordway_subscription_id = self.ordway_subscription_id

        referral_code: None | str | Unset
        if isinstance(self.referral_code, Unset):
            referral_code = UNSET
        else:
            referral_code = self.referral_code

        stripe_id: None | str | Unset
        if isinstance(self.stripe_id, Unset):
            stripe_id = UNSET
        else:
            stripe_id = self.stripe_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
            }
        )
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if email_marketing_consent is not UNSET:
            field_dict["email_marketing_consent"] = email_marketing_consent
        if id is not UNSET:
            field_dict["id"] = id
        if marketplace_signup_nonce is not UNSET:
            field_dict["marketplace_signup_nonce"] = marketplace_signup_nonce
        if ordway_customer_id is not UNSET:
            field_dict["ordway_customer_id"] = ordway_customer_id
        if ordway_subscription_id is not UNSET:
            field_dict["ordway_subscription_id"] = ordway_subscription_id
        if referral_code is not UNSET:
            field_dict["referral_code"] = referral_code
        if stripe_id is not UNSET:
            field_dict["stripe_id"] = stripe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = d.pop("country")

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        password = d.pop("password")

        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

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

        def _parse_email_marketing_consent(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        email_marketing_consent = _parse_email_marketing_consent(
            d.pop("email_marketing_consent", UNSET)
        )

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

        def _parse_marketplace_signup_nonce(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marketplace_signup_nonce = _parse_marketplace_signup_nonce(
            d.pop("marketplace_signup_nonce", UNSET)
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

        def _parse_ordway_subscription_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ordway_subscription_id = _parse_ordway_subscription_id(
            d.pop("ordway_subscription_id", UNSET)
        )

        def _parse_referral_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referral_code = _parse_referral_code(d.pop("referral_code", UNSET))

        def _parse_stripe_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_id = _parse_stripe_id(d.pop("stripe_id", UNSET))

        registration_schema = cls(
            country=country,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            base_url=base_url,
            company_name=company_name,
            date_created=date_created,
            email_marketing_consent=email_marketing_consent,
            id=id,
            marketplace_signup_nonce=marketplace_signup_nonce,
            ordway_customer_id=ordway_customer_id,
            ordway_subscription_id=ordway_subscription_id,
            referral_code=referral_code,
            stripe_id=stripe_id,
        )

        registration_schema.additional_properties = d
        return registration_schema

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
