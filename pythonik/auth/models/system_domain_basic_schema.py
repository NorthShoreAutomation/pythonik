from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_domain_basic_schema_billing_tier_type_1 import (
        SystemDomainBasicSchemaBillingTierType1,
    )
    from ..models.system_domain_basic_schema_type_type_1 import (
        SystemDomainBasicSchemaTypeType1,
    )


T = TypeVar("T", bound="SystemDomainBasicSchema")


@_attrs_define
class SystemDomainBasicSchema:
    """
    Attributes:
        name (str):
        billing_tier (None | SystemDomainBasicSchemaBillingTierType1 | Unset):
        country (None | str | Unset):
        date_created (datetime.datetime | None | Unset):
        features (list[str] | None | Unset):
        id (None | Unset | UUID):
        is_plg (bool | None | Unset):
        type_ (None | SystemDomainBasicSchemaTypeType1 | Unset):
    """

    name: str
    billing_tier: None | SystemDomainBasicSchemaBillingTierType1 | Unset = UNSET
    country: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    features: list[str] | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_plg: bool | None | Unset = UNSET
    type_: None | SystemDomainBasicSchemaTypeType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_domain_basic_schema_billing_tier_type_1 import (
            SystemDomainBasicSchemaBillingTierType1,
        )
        from ..models.system_domain_basic_schema_type_type_1 import (
            SystemDomainBasicSchemaTypeType1,
        )

        name = self.name

        billing_tier: dict[str, Any] | None | Unset
        if isinstance(self.billing_tier, Unset):
            billing_tier = UNSET
        elif isinstance(self.billing_tier, SystemDomainBasicSchemaBillingTierType1):
            billing_tier = self.billing_tier.to_dict()
        else:
            billing_tier = self.billing_tier

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        features: list[str] | None | Unset
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, list):
            features = self.features

        else:
            features = self.features

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_plg: bool | None | Unset
        if isinstance(self.is_plg, Unset):
            is_plg = UNSET
        else:
            is_plg = self.is_plg

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, SystemDomainBasicSchemaTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if billing_tier is not UNSET:
            field_dict["billing_tier"] = billing_tier
        if country is not UNSET:
            field_dict["country"] = country
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if features is not UNSET:
            field_dict["features"] = features
        if id is not UNSET:
            field_dict["id"] = id
        if is_plg is not UNSET:
            field_dict["is_plg"] = is_plg
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_domain_basic_schema_billing_tier_type_1 import (
            SystemDomainBasicSchemaBillingTierType1,
        )
        from ..models.system_domain_basic_schema_type_type_1 import (
            SystemDomainBasicSchemaTypeType1,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_billing_tier(
            data: object,
        ) -> None | SystemDomainBasicSchemaBillingTierType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_tier_type_1 = SystemDomainBasicSchemaBillingTierType1.from_dict(
                    data
                )

                return billing_tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainBasicSchemaBillingTierType1 | Unset, data)

        billing_tier = _parse_billing_tier(d.pop("billing_tier", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

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

        def _parse_is_plg(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_plg = _parse_is_plg(d.pop("is_plg", UNSET))

        def _parse_type_(
            data: object,
        ) -> None | SystemDomainBasicSchemaTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = SystemDomainBasicSchemaTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainBasicSchemaTypeType1 | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        system_domain_basic_schema = cls(
            name=name,
            billing_tier=billing_tier,
            country=country,
            date_created=date_created,
            features=features,
            id=id,
            is_plg=is_plg,
            type_=type_,
        )

        system_domain_basic_schema.additional_properties = d
        return system_domain_basic_schema

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
