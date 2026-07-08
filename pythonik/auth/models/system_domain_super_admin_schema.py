from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_limits_schema import BillingLimitsSchema
    from ..models.system_domain_super_admin_schema_billing_tier_type_1 import (
        SystemDomainSuperAdminSchemaBillingTierType1,
    )
    from ..models.system_domain_super_admin_schema_industry_type_1 import (
        SystemDomainSuperAdminSchemaIndustryType1,
    )
    from ..models.system_domain_super_admin_schema_status_type_1 import (
        SystemDomainSuperAdminSchemaStatusType1,
    )
    from ..models.system_domain_super_admin_schema_type_type_1 import (
        SystemDomainSuperAdminSchemaTypeType1,
    )


T = TypeVar("T", bound="SystemDomainSuperAdminSchema")


@_attrs_define
class SystemDomainSuperAdminSchema:
    """
    Attributes:
        base_url (str):
        name (str):
        billing_limits (BillingLimitsSchema | None | Unset):
        billing_tier (None | SystemDomainSuperAdminSchemaBillingTierType1 | Unset):
        contract_end_date (datetime.datetime | None | Unset):
        country (None | str | Unset):
        creating_user_id (None | Unset | UUID):
        custom_terms (bool | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        deactivate_date (datetime.datetime | None | Unset):
        description (None | str | Unset):
        disable_billing_page (bool | None | Unset):
        disable_cc_purchase (bool | None | Unset):
        discount_percent (float | None | Unset):
        do_not_charge_edge_transcoder (bool | None | Unset):
        do_not_charge_remote_proxies (bool | None | Unset):
        do_not_charge_shield (bool | None | Unset):
        features (list[str] | None | Unset):
        freeze_date (datetime.datetime | None | Unset):
        has_preloaded_assets (bool | None | Unset):
        id (None | Unset | UUID):
        industry (None | SystemDomainSuperAdminSchemaIndustryType1 | Unset):
        invoice_end_of_month (bool | None | Unset):
        is_plg (bool | None | Unset):
        is_template (bool | None | Unset):
        licensed_user_billing (bool | None | Unset):
        marketplace_customer_id (None | str | Unset):
        marketplace_entitlement_id (None | str | Unset):
        ordway_customer_id (None | str | Unset):
        ordway_subscription_id (None | str | Unset):
        platform_name (None | str | Unset):
        price_list (None | str | Unset):
        referral_code (None | str | Unset):
        sales_force_id (None | str | Unset):
        status (None | SystemDomainSuperAdminSchemaStatusType1 | Unset):
        stripe_id (None | str | Unset):
        type_ (None | SystemDomainSuperAdminSchemaTypeType1 | Unset):
        warning_message (None | str | Unset):
    """

    base_url: str
    name: str
    billing_limits: BillingLimitsSchema | None | Unset = UNSET
    billing_tier: None | SystemDomainSuperAdminSchemaBillingTierType1 | Unset = UNSET
    contract_end_date: datetime.datetime | None | Unset = UNSET
    country: None | str | Unset = UNSET
    creating_user_id: None | Unset | UUID = UNSET
    custom_terms: bool | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    deactivate_date: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    disable_billing_page: bool | None | Unset = UNSET
    disable_cc_purchase: bool | None | Unset = UNSET
    discount_percent: float | None | Unset = UNSET
    do_not_charge_edge_transcoder: bool | None | Unset = UNSET
    do_not_charge_remote_proxies: bool | None | Unset = UNSET
    do_not_charge_shield: bool | None | Unset = UNSET
    features: list[str] | None | Unset = UNSET
    freeze_date: datetime.datetime | None | Unset = UNSET
    has_preloaded_assets: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    industry: None | SystemDomainSuperAdminSchemaIndustryType1 | Unset = UNSET
    invoice_end_of_month: bool | None | Unset = UNSET
    is_plg: bool | None | Unset = UNSET
    is_template: bool | None | Unset = UNSET
    licensed_user_billing: bool | None | Unset = UNSET
    marketplace_customer_id: None | str | Unset = UNSET
    marketplace_entitlement_id: None | str | Unset = UNSET
    ordway_customer_id: None | str | Unset = UNSET
    ordway_subscription_id: None | str | Unset = UNSET
    platform_name: None | str | Unset = UNSET
    price_list: None | str | Unset = UNSET
    referral_code: None | str | Unset = UNSET
    sales_force_id: None | str | Unset = UNSET
    status: None | SystemDomainSuperAdminSchemaStatusType1 | Unset = UNSET
    stripe_id: None | str | Unset = UNSET
    type_: None | SystemDomainSuperAdminSchemaTypeType1 | Unset = UNSET
    warning_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_limits_schema import BillingLimitsSchema
        from ..models.system_domain_super_admin_schema_billing_tier_type_1 import (
            SystemDomainSuperAdminSchemaBillingTierType1,
        )
        from ..models.system_domain_super_admin_schema_industry_type_1 import (
            SystemDomainSuperAdminSchemaIndustryType1,
        )
        from ..models.system_domain_super_admin_schema_status_type_1 import (
            SystemDomainSuperAdminSchemaStatusType1,
        )
        from ..models.system_domain_super_admin_schema_type_type_1 import (
            SystemDomainSuperAdminSchemaTypeType1,
        )

        base_url = self.base_url

        name = self.name

        billing_limits: dict[str, Any] | None | Unset
        if isinstance(self.billing_limits, Unset):
            billing_limits = UNSET
        elif isinstance(self.billing_limits, BillingLimitsSchema):
            billing_limits = self.billing_limits.to_dict()
        else:
            billing_limits = self.billing_limits

        billing_tier: dict[str, Any] | None | Unset
        if isinstance(self.billing_tier, Unset):
            billing_tier = UNSET
        elif isinstance(
            self.billing_tier, SystemDomainSuperAdminSchemaBillingTierType1
        ):
            billing_tier = self.billing_tier.to_dict()
        else:
            billing_tier = self.billing_tier

        contract_end_date: None | str | Unset
        if isinstance(self.contract_end_date, Unset):
            contract_end_date = UNSET
        elif isinstance(self.contract_end_date, datetime.datetime):
            contract_end_date = self.contract_end_date.isoformat()
        else:
            contract_end_date = self.contract_end_date

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        creating_user_id: None | str | Unset
        if isinstance(self.creating_user_id, Unset):
            creating_user_id = UNSET
        elif isinstance(self.creating_user_id, UUID):
            creating_user_id = str(self.creating_user_id)
        else:
            creating_user_id = self.creating_user_id

        custom_terms: bool | None | Unset
        if isinstance(self.custom_terms, Unset):
            custom_terms = UNSET
        else:
            custom_terms = self.custom_terms

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

        deactivate_date: None | str | Unset
        if isinstance(self.deactivate_date, Unset):
            deactivate_date = UNSET
        elif isinstance(self.deactivate_date, datetime.datetime):
            deactivate_date = self.deactivate_date.isoformat()
        else:
            deactivate_date = self.deactivate_date

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        disable_billing_page: bool | None | Unset
        if isinstance(self.disable_billing_page, Unset):
            disable_billing_page = UNSET
        else:
            disable_billing_page = self.disable_billing_page

        disable_cc_purchase: bool | None | Unset
        if isinstance(self.disable_cc_purchase, Unset):
            disable_cc_purchase = UNSET
        else:
            disable_cc_purchase = self.disable_cc_purchase

        discount_percent: float | None | Unset
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent

        do_not_charge_edge_transcoder: bool | None | Unset
        if isinstance(self.do_not_charge_edge_transcoder, Unset):
            do_not_charge_edge_transcoder = UNSET
        else:
            do_not_charge_edge_transcoder = self.do_not_charge_edge_transcoder

        do_not_charge_remote_proxies: bool | None | Unset
        if isinstance(self.do_not_charge_remote_proxies, Unset):
            do_not_charge_remote_proxies = UNSET
        else:
            do_not_charge_remote_proxies = self.do_not_charge_remote_proxies

        do_not_charge_shield: bool | None | Unset
        if isinstance(self.do_not_charge_shield, Unset):
            do_not_charge_shield = UNSET
        else:
            do_not_charge_shield = self.do_not_charge_shield

        features: list[str] | None | Unset
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, list):
            features = self.features

        else:
            features = self.features

        freeze_date: None | str | Unset
        if isinstance(self.freeze_date, Unset):
            freeze_date = UNSET
        elif isinstance(self.freeze_date, datetime.datetime):
            freeze_date = self.freeze_date.isoformat()
        else:
            freeze_date = self.freeze_date

        has_preloaded_assets: bool | None | Unset
        if isinstance(self.has_preloaded_assets, Unset):
            has_preloaded_assets = UNSET
        else:
            has_preloaded_assets = self.has_preloaded_assets

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        industry: dict[str, Any] | None | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        elif isinstance(self.industry, SystemDomainSuperAdminSchemaIndustryType1):
            industry = self.industry.to_dict()
        else:
            industry = self.industry

        invoice_end_of_month: bool | None | Unset
        if isinstance(self.invoice_end_of_month, Unset):
            invoice_end_of_month = UNSET
        else:
            invoice_end_of_month = self.invoice_end_of_month

        is_plg: bool | None | Unset
        if isinstance(self.is_plg, Unset):
            is_plg = UNSET
        else:
            is_plg = self.is_plg

        is_template: bool | None | Unset
        if isinstance(self.is_template, Unset):
            is_template = UNSET
        else:
            is_template = self.is_template

        licensed_user_billing: bool | None | Unset
        if isinstance(self.licensed_user_billing, Unset):
            licensed_user_billing = UNSET
        else:
            licensed_user_billing = self.licensed_user_billing

        marketplace_customer_id: None | str | Unset
        if isinstance(self.marketplace_customer_id, Unset):
            marketplace_customer_id = UNSET
        else:
            marketplace_customer_id = self.marketplace_customer_id

        marketplace_entitlement_id: None | str | Unset
        if isinstance(self.marketplace_entitlement_id, Unset):
            marketplace_entitlement_id = UNSET
        else:
            marketplace_entitlement_id = self.marketplace_entitlement_id

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

        platform_name: None | str | Unset
        if isinstance(self.platform_name, Unset):
            platform_name = UNSET
        else:
            platform_name = self.platform_name

        price_list: None | str | Unset
        if isinstance(self.price_list, Unset):
            price_list = UNSET
        else:
            price_list = self.price_list

        referral_code: None | str | Unset
        if isinstance(self.referral_code, Unset):
            referral_code = UNSET
        else:
            referral_code = self.referral_code

        sales_force_id: None | str | Unset
        if isinstance(self.sales_force_id, Unset):
            sales_force_id = UNSET
        else:
            sales_force_id = self.sales_force_id

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SystemDomainSuperAdminSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        stripe_id: None | str | Unset
        if isinstance(self.stripe_id, Unset):
            stripe_id = UNSET
        else:
            stripe_id = self.stripe_id

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, SystemDomainSuperAdminSchemaTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        warning_message: None | str | Unset
        if isinstance(self.warning_message, Unset):
            warning_message = UNSET
        else:
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
        from ..models.system_domain_super_admin_schema_billing_tier_type_1 import (
            SystemDomainSuperAdminSchemaBillingTierType1,
        )
        from ..models.system_domain_super_admin_schema_industry_type_1 import (
            SystemDomainSuperAdminSchemaIndustryType1,
        )
        from ..models.system_domain_super_admin_schema_status_type_1 import (
            SystemDomainSuperAdminSchemaStatusType1,
        )
        from ..models.system_domain_super_admin_schema_type_type_1 import (
            SystemDomainSuperAdminSchemaTypeType1,
        )

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

        def _parse_billing_tier(
            data: object,
        ) -> None | SystemDomainSuperAdminSchemaBillingTierType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_tier_type_1 = (
                    SystemDomainSuperAdminSchemaBillingTierType1.from_dict(data)
                )

                return billing_tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | SystemDomainSuperAdminSchemaBillingTierType1 | Unset, data
            )

        billing_tier = _parse_billing_tier(d.pop("billing_tier", UNSET))

        def _parse_contract_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contract_end_date_type_0 = datetime.datetime.fromisoformat(data)

                return contract_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        contract_end_date = _parse_contract_end_date(d.pop("contract_end_date", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_creating_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creating_user_id_type_0 = UUID(data)

                return creating_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        creating_user_id = _parse_creating_user_id(d.pop("creating_user_id", UNSET))

        def _parse_custom_terms(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        custom_terms = _parse_custom_terms(d.pop("custom_terms", UNSET))

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

        def _parse_deactivate_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deactivate_date_type_0 = datetime.datetime.fromisoformat(data)

                return deactivate_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deactivate_date = _parse_deactivate_date(d.pop("deactivate_date", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_disable_billing_page(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disable_billing_page = _parse_disable_billing_page(
            d.pop("disable_billing_page", UNSET)
        )

        def _parse_disable_cc_purchase(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disable_cc_purchase = _parse_disable_cc_purchase(
            d.pop("disable_cc_purchase", UNSET)
        )

        def _parse_discount_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        discount_percent = _parse_discount_percent(d.pop("discount_percent", UNSET))

        def _parse_do_not_charge_edge_transcoder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        do_not_charge_edge_transcoder = _parse_do_not_charge_edge_transcoder(
            d.pop("do_not_charge_edge_transcoder", UNSET)
        )

        def _parse_do_not_charge_remote_proxies(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        do_not_charge_remote_proxies = _parse_do_not_charge_remote_proxies(
            d.pop("do_not_charge_remote_proxies", UNSET)
        )

        def _parse_do_not_charge_shield(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        do_not_charge_shield = _parse_do_not_charge_shield(
            d.pop("do_not_charge_shield", UNSET)
        )

        def _parse_features(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                features_type_0 = cast(list[str], data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        features = _parse_features(d.pop("features", UNSET))

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

        def _parse_has_preloaded_assets(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_preloaded_assets = _parse_has_preloaded_assets(
            d.pop("has_preloaded_assets", UNSET)
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

        def _parse_industry(
            data: object,
        ) -> None | SystemDomainSuperAdminSchemaIndustryType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                industry_type_1 = SystemDomainSuperAdminSchemaIndustryType1.from_dict(
                    data
                )

                return industry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainSuperAdminSchemaIndustryType1 | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_invoice_end_of_month(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        invoice_end_of_month = _parse_invoice_end_of_month(
            d.pop("invoice_end_of_month", UNSET)
        )

        def _parse_is_plg(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_plg = _parse_is_plg(d.pop("is_plg", UNSET))

        def _parse_is_template(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_template = _parse_is_template(d.pop("is_template", UNSET))

        def _parse_licensed_user_billing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        licensed_user_billing = _parse_licensed_user_billing(
            d.pop("licensed_user_billing", UNSET)
        )

        def _parse_marketplace_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marketplace_customer_id = _parse_marketplace_customer_id(
            d.pop("marketplace_customer_id", UNSET)
        )

        def _parse_marketplace_entitlement_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marketplace_entitlement_id = _parse_marketplace_entitlement_id(
            d.pop("marketplace_entitlement_id", UNSET)
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

        def _parse_platform_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform_name = _parse_platform_name(d.pop("platform_name", UNSET))

        def _parse_price_list(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_list = _parse_price_list(d.pop("price_list", UNSET))

        def _parse_referral_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referral_code = _parse_referral_code(d.pop("referral_code", UNSET))

        def _parse_sales_force_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sales_force_id = _parse_sales_force_id(d.pop("sales_force_id", UNSET))

        def _parse_status(
            data: object,
        ) -> None | SystemDomainSuperAdminSchemaStatusType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = SystemDomainSuperAdminSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainSuperAdminSchemaStatusType1 | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_stripe_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_id = _parse_stripe_id(d.pop("stripe_id", UNSET))

        def _parse_type_(
            data: object,
        ) -> None | SystemDomainSuperAdminSchemaTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = SystemDomainSuperAdminSchemaTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainSuperAdminSchemaTypeType1 | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_warning_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        warning_message = _parse_warning_message(d.pop("warning_message", UNSET))

        system_domain_super_admin_schema = cls(
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
            referral_code=referral_code,
            sales_force_id=sales_force_id,
            status=status,
            stripe_id=stripe_id,
            type_=type_,
            warning_message=warning_message,
        )

        system_domain_super_admin_schema.additional_properties = d
        return system_domain_super_admin_schema

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
