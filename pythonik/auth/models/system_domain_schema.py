from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_domain_schema_billing_tier import SystemDomainSchemaBillingTier
from ..models.system_domain_schema_industry import SystemDomainSchemaIndustry
from ..models.system_domain_schema_status import SystemDomainSchemaStatus
from ..models.system_domain_schema_type import SystemDomainSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_limits_schema import BillingLimitsSchema


T = TypeVar("T", bound="SystemDomainSchema")


@_attrs_define
class SystemDomainSchema:
    """
    Attributes:
        base_url (str):
        name (str):
        billing_limits (BillingLimitsSchema | None | Unset):
        billing_tier (SystemDomainSchemaBillingTier | Unset):
        contract_end_date (datetime.datetime | Unset):
        country (str | Unset):
        creating_user_id (UUID | Unset):
        custom_terms (bool | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        deactivate_date (datetime.datetime | Unset):
        description (str | Unset):
        disable_billing_page (bool | Unset):
        disable_cc_purchase (bool | Unset):
        discount_percent (float | Unset):
        do_not_charge_edge_transcoder (bool | Unset):
        do_not_charge_remote_proxies (bool | Unset):
        do_not_charge_shield (bool | Unset):
        features (list[str] | Unset):
        freeze_date (datetime.datetime | Unset):
        has_preloaded_assets (bool | Unset):
        id (UUID | Unset):
        industry (SystemDomainSchemaIndustry | Unset):
        invoice_end_of_month (bool | Unset):
        is_plg (bool | Unset):
        is_template (bool | Unset):
        licensed_user_billing (bool | Unset):
        marketplace_customer_id (str | Unset):
        marketplace_entitlement_id (str | Unset):
        ordway_customer_id (str | Unset):
        ordway_subscription_id (str | Unset):
        platform_name (str | Unset):
        price_list (str | Unset):
        primary_region (str | Unset):
        referral_code (str | Unset):
        sales_force_id (str | Unset):
        status (SystemDomainSchemaStatus | Unset):
        stripe_id (str | Unset):
        type_ (SystemDomainSchemaType | Unset):
        warning_message (str | Unset):
    """

    base_url: str
    name: str
    billing_limits: BillingLimitsSchema | None | Unset = UNSET
    billing_tier: SystemDomainSchemaBillingTier | Unset = UNSET
    contract_end_date: datetime.datetime | Unset = UNSET
    country: str | Unset = UNSET
    creating_user_id: UUID | Unset = UNSET
    custom_terms: bool | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    deactivate_date: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    disable_billing_page: bool | Unset = UNSET
    disable_cc_purchase: bool | Unset = UNSET
    discount_percent: float | Unset = UNSET
    do_not_charge_edge_transcoder: bool | Unset = UNSET
    do_not_charge_remote_proxies: bool | Unset = UNSET
    do_not_charge_shield: bool | Unset = UNSET
    features: list[str] | Unset = UNSET
    freeze_date: datetime.datetime | Unset = UNSET
    has_preloaded_assets: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    industry: SystemDomainSchemaIndustry | Unset = UNSET
    invoice_end_of_month: bool | Unset = UNSET
    is_plg: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    licensed_user_billing: bool | Unset = UNSET
    marketplace_customer_id: str | Unset = UNSET
    marketplace_entitlement_id: str | Unset = UNSET
    ordway_customer_id: str | Unset = UNSET
    ordway_subscription_id: str | Unset = UNSET
    platform_name: str | Unset = UNSET
    price_list: str | Unset = UNSET
    primary_region: str | Unset = UNSET
    referral_code: str | Unset = UNSET
    sales_force_id: str | Unset = UNSET
    status: SystemDomainSchemaStatus | Unset = UNSET
    stripe_id: str | Unset = UNSET
    type_: SystemDomainSchemaType | Unset = UNSET
    warning_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_limits_schema import BillingLimitsSchema

        base_url = self.base_url

        name = self.name

        billing_limits: dict[str, Any] | None | Unset
        if isinstance(self.billing_limits, Unset):
            billing_limits = UNSET
        elif isinstance(self.billing_limits, BillingLimitsSchema):
            billing_limits = self.billing_limits.to_dict()
        else:
            billing_limits = self.billing_limits

        billing_tier: str | Unset = UNSET
        if not isinstance(self.billing_tier, Unset):
            billing_tier = self.billing_tier.value

        contract_end_date: str | Unset = UNSET
        if not isinstance(self.contract_end_date, Unset):
            contract_end_date = self.contract_end_date.isoformat()

        country = self.country

        creating_user_id: str | Unset = UNSET
        if not isinstance(self.creating_user_id, Unset):
            creating_user_id = str(self.creating_user_id)

        custom_terms = self.custom_terms

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        deactivate_date: str | Unset = UNSET
        if not isinstance(self.deactivate_date, Unset):
            deactivate_date = self.deactivate_date.isoformat()

        description = self.description

        disable_billing_page = self.disable_billing_page

        disable_cc_purchase = self.disable_cc_purchase

        discount_percent = self.discount_percent

        do_not_charge_edge_transcoder = self.do_not_charge_edge_transcoder

        do_not_charge_remote_proxies = self.do_not_charge_remote_proxies

        do_not_charge_shield = self.do_not_charge_shield

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        freeze_date: str | Unset = UNSET
        if not isinstance(self.freeze_date, Unset):
            freeze_date = self.freeze_date.isoformat()

        has_preloaded_assets = self.has_preloaded_assets

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        industry: str | Unset = UNSET
        if not isinstance(self.industry, Unset):
            industry = self.industry.value

        invoice_end_of_month = self.invoice_end_of_month

        is_plg = self.is_plg

        is_template = self.is_template

        licensed_user_billing = self.licensed_user_billing

        marketplace_customer_id = self.marketplace_customer_id

        marketplace_entitlement_id = self.marketplace_entitlement_id

        ordway_customer_id = self.ordway_customer_id

        ordway_subscription_id = self.ordway_subscription_id

        platform_name = self.platform_name

        price_list = self.price_list

        primary_region = self.primary_region

        referral_code = self.referral_code

        sales_force_id = self.sales_force_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        stripe_id = self.stripe_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        warning_message = self.warning_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_url": base_url,
                "name": name,
            }
        )
        if billing_limits is not UNSET:
            field_dict["billing_limits"] = billing_limits
        if billing_tier is not UNSET:
            field_dict["billing_tier"] = billing_tier
        if contract_end_date is not UNSET:
            field_dict["contract_end_date"] = contract_end_date
        if country is not UNSET:
            field_dict["country"] = country
        if creating_user_id is not UNSET:
            field_dict["creating_user_id"] = creating_user_id
        if custom_terms is not UNSET:
            field_dict["custom_terms"] = custom_terms
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if deactivate_date is not UNSET:
            field_dict["deactivate_date"] = deactivate_date
        if description is not UNSET:
            field_dict["description"] = description
        if disable_billing_page is not UNSET:
            field_dict["disable_billing_page"] = disable_billing_page
        if disable_cc_purchase is not UNSET:
            field_dict["disable_cc_purchase"] = disable_cc_purchase
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if do_not_charge_edge_transcoder is not UNSET:
            field_dict["do_not_charge_edge_transcoder"] = do_not_charge_edge_transcoder
        if do_not_charge_remote_proxies is not UNSET:
            field_dict["do_not_charge_remote_proxies"] = do_not_charge_remote_proxies
        if do_not_charge_shield is not UNSET:
            field_dict["do_not_charge_shield"] = do_not_charge_shield
        if features is not UNSET:
            field_dict["features"] = features
        if freeze_date is not UNSET:
            field_dict["freeze_date"] = freeze_date
        if has_preloaded_assets is not UNSET:
            field_dict["has_preloaded_assets"] = has_preloaded_assets
        if id is not UNSET:
            field_dict["id"] = id
        if industry is not UNSET:
            field_dict["industry"] = industry
        if invoice_end_of_month is not UNSET:
            field_dict["invoice_end_of_month"] = invoice_end_of_month
        if is_plg is not UNSET:
            field_dict["is_plg"] = is_plg
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if licensed_user_billing is not UNSET:
            field_dict["licensed_user_billing"] = licensed_user_billing
        if marketplace_customer_id is not UNSET:
            field_dict["marketplace_customer_id"] = marketplace_customer_id
        if marketplace_entitlement_id is not UNSET:
            field_dict["marketplace_entitlement_id"] = marketplace_entitlement_id
        if ordway_customer_id is not UNSET:
            field_dict["ordway_customer_id"] = ordway_customer_id
        if ordway_subscription_id is not UNSET:
            field_dict["ordway_subscription_id"] = ordway_subscription_id
        if platform_name is not UNSET:
            field_dict["platform_name"] = platform_name
        if price_list is not UNSET:
            field_dict["price_list"] = price_list
        if primary_region is not UNSET:
            field_dict["primary_region"] = primary_region
        if referral_code is not UNSET:
            field_dict["referral_code"] = referral_code
        if sales_force_id is not UNSET:
            field_dict["sales_force_id"] = sales_force_id
        if status is not UNSET:
            field_dict["status"] = status
        if stripe_id is not UNSET:
            field_dict["stripe_id"] = stripe_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if warning_message is not UNSET:
            field_dict["warning_message"] = warning_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_limits_schema import BillingLimitsSchema

        d = dict(src_dict)
        base_url = d.pop("base_url")

        name = d.pop("name")

        def _parse_billing_limits(data: object) -> BillingLimitsSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_limits_type_1 = BillingLimitsSchema.from_dict(data)

                return billing_limits_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BillingLimitsSchema | None | Unset, data)

        billing_limits = _parse_billing_limits(d.pop("billing_limits", UNSET))

        _billing_tier = d.pop("billing_tier", UNSET)
        billing_tier: SystemDomainSchemaBillingTier | Unset
        if isinstance(_billing_tier, Unset):
            billing_tier = UNSET
        else:
            billing_tier = SystemDomainSchemaBillingTier(_billing_tier)

        _contract_end_date = d.pop("contract_end_date", UNSET)
        contract_end_date: datetime.datetime | Unset
        if isinstance(_contract_end_date, Unset):
            contract_end_date = UNSET
        else:
            contract_end_date = datetime.datetime.fromisoformat(_contract_end_date)

        country = d.pop("country", UNSET)

        _creating_user_id = d.pop("creating_user_id", UNSET)
        creating_user_id: UUID | Unset
        if isinstance(_creating_user_id, Unset):
            creating_user_id = UNSET
        else:
            creating_user_id = UUID(_creating_user_id)

        custom_terms = d.pop("custom_terms", UNSET)

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

        _deactivate_date = d.pop("deactivate_date", UNSET)
        deactivate_date: datetime.datetime | Unset
        if isinstance(_deactivate_date, Unset):
            deactivate_date = UNSET
        else:
            deactivate_date = datetime.datetime.fromisoformat(_deactivate_date)

        description = d.pop("description", UNSET)

        disable_billing_page = d.pop("disable_billing_page", UNSET)

        disable_cc_purchase = d.pop("disable_cc_purchase", UNSET)

        discount_percent = d.pop("discount_percent", UNSET)

        do_not_charge_edge_transcoder = d.pop("do_not_charge_edge_transcoder", UNSET)

        do_not_charge_remote_proxies = d.pop("do_not_charge_remote_proxies", UNSET)

        do_not_charge_shield = d.pop("do_not_charge_shield", UNSET)

        features = cast(list[str], d.pop("features", UNSET))

        _freeze_date = d.pop("freeze_date", UNSET)
        freeze_date: datetime.datetime | Unset
        if isinstance(_freeze_date, Unset):
            freeze_date = UNSET
        else:
            freeze_date = datetime.datetime.fromisoformat(_freeze_date)

        has_preloaded_assets = d.pop("has_preloaded_assets", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _industry = d.pop("industry", UNSET)
        industry: SystemDomainSchemaIndustry | Unset
        if isinstance(_industry, Unset):
            industry = UNSET
        else:
            industry = SystemDomainSchemaIndustry(_industry)

        invoice_end_of_month = d.pop("invoice_end_of_month", UNSET)

        is_plg = d.pop("is_plg", UNSET)

        is_template = d.pop("is_template", UNSET)

        licensed_user_billing = d.pop("licensed_user_billing", UNSET)

        marketplace_customer_id = d.pop("marketplace_customer_id", UNSET)

        marketplace_entitlement_id = d.pop("marketplace_entitlement_id", UNSET)

        ordway_customer_id = d.pop("ordway_customer_id", UNSET)

        ordway_subscription_id = d.pop("ordway_subscription_id", UNSET)

        platform_name = d.pop("platform_name", UNSET)

        price_list = d.pop("price_list", UNSET)

        primary_region = d.pop("primary_region", UNSET)

        referral_code = d.pop("referral_code", UNSET)

        sales_force_id = d.pop("sales_force_id", UNSET)

        _status = d.pop("status", UNSET)
        status: SystemDomainSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SystemDomainSchemaStatus(_status)

        stripe_id = d.pop("stripe_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SystemDomainSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SystemDomainSchemaType(_type_)

        warning_message = d.pop("warning_message", UNSET)

        system_domain_schema = cls(
            base_url=base_url,
            name=name,
            billing_limits=billing_limits,
            billing_tier=billing_tier,
            contract_end_date=contract_end_date,
            country=country,
            creating_user_id=creating_user_id,
            custom_terms=custom_terms,
            date_created=date_created,
            date_modified=date_modified,
            deactivate_date=deactivate_date,
            description=description,
            disable_billing_page=disable_billing_page,
            disable_cc_purchase=disable_cc_purchase,
            discount_percent=discount_percent,
            do_not_charge_edge_transcoder=do_not_charge_edge_transcoder,
            do_not_charge_remote_proxies=do_not_charge_remote_proxies,
            do_not_charge_shield=do_not_charge_shield,
            features=features,
            freeze_date=freeze_date,
            has_preloaded_assets=has_preloaded_assets,
            id=id,
            industry=industry,
            invoice_end_of_month=invoice_end_of_month,
            is_plg=is_plg,
            is_template=is_template,
            licensed_user_billing=licensed_user_billing,
            marketplace_customer_id=marketplace_customer_id,
            marketplace_entitlement_id=marketplace_entitlement_id,
            ordway_customer_id=ordway_customer_id,
            ordway_subscription_id=ordway_subscription_id,
            platform_name=platform_name,
            price_list=price_list,
            primary_region=primary_region,
            referral_code=referral_code,
            sales_force_id=sales_force_id,
            status=status,
            stripe_id=stripe_id,
            type_=type_,
            warning_message=warning_message,
        )

        system_domain_schema.additional_properties = d
        return system_domain_schema

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
