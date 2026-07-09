from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_domain_from_template_schema_billing_tier import (
    SystemDomainFromTemplateSchemaBillingTier,
)
from ..models.system_domain_from_template_schema_status import (
    SystemDomainFromTemplateSchemaStatus,
)
from ..models.system_domain_from_template_schema_type import (
    SystemDomainFromTemplateSchemaType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemDomainFromTemplateSchema")


@_attrs_define
class SystemDomainFromTemplateSchema:
    """
    Attributes:
        name (str):
        admin_email (None | str | Unset):
        admin_first_name (None | str | Unset):
        admin_id (None | Unset | UUID):
        admin_last_name (None | str | Unset):
        admin_password (None | str | Unset):
        base_url (None | str | Unset):
        billing_tier (None | SystemDomainFromTemplateSchemaBillingTier | Unset):
        custom_terms (bool | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        description (None | str | Unset):
        id (None | Unset | UUID):
        status (None | SystemDomainFromTemplateSchemaStatus | Unset):
        type_ (None | SystemDomainFromTemplateSchemaType | Unset):
    """

    name: str
    admin_email: None | str | Unset = UNSET
    admin_first_name: None | str | Unset = UNSET
    admin_id: None | Unset | UUID = UNSET
    admin_last_name: None | str | Unset = UNSET
    admin_password: None | str | Unset = UNSET
    base_url: None | str | Unset = UNSET
    billing_tier: None | SystemDomainFromTemplateSchemaBillingTier | Unset = UNSET
    custom_terms: bool | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    status: None | SystemDomainFromTemplateSchemaStatus | Unset = UNSET
    type_: None | SystemDomainFromTemplateSchemaType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        admin_id: None | str | Unset
        if isinstance(self.admin_id, Unset):
            admin_id = UNSET
        elif isinstance(self.admin_id, UUID):
            admin_id = str(self.admin_id)
        else:
            admin_id = self.admin_id

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

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        billing_tier: None | str | Unset
        if isinstance(self.billing_tier, Unset):
            billing_tier = UNSET
        elif isinstance(self.billing_tier, SystemDomainFromTemplateSchemaBillingTier):
            billing_tier = self.billing_tier.value
        else:
            billing_tier = self.billing_tier

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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SystemDomainFromTemplateSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, SystemDomainFromTemplateSchemaType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if admin_email is not UNSET:
            field_dict["admin_email"] = admin_email
        if admin_first_name is not UNSET:
            field_dict["admin_first_name"] = admin_first_name
        if admin_id is not UNSET:
            field_dict["admin_id"] = admin_id
        if admin_last_name is not UNSET:
            field_dict["admin_last_name"] = admin_last_name
        if admin_password is not UNSET:
            field_dict["admin_password"] = admin_password
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if billing_tier is not UNSET:
            field_dict["billing_tier"] = billing_tier
        if custom_terms is not UNSET:
            field_dict["custom_terms"] = custom_terms
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        def _parse_admin_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                admin_id_type_0 = UUID(data)

                return admin_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        admin_id = _parse_admin_id(d.pop("admin_id", UNSET))

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

        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))

        def _parse_billing_tier(
            data: object,
        ) -> None | SystemDomainFromTemplateSchemaBillingTier | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                billing_tier_type_1 = SystemDomainFromTemplateSchemaBillingTier(data)

                return billing_tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainFromTemplateSchemaBillingTier | Unset, data)

        billing_tier = _parse_billing_tier(d.pop("billing_tier", UNSET))

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

        def _parse_status(
            data: object,
        ) -> None | SystemDomainFromTemplateSchemaStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = SystemDomainFromTemplateSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainFromTemplateSchemaStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_type_(
            data: object,
        ) -> None | SystemDomainFromTemplateSchemaType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = SystemDomainFromTemplateSchemaType(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainFromTemplateSchemaType | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        system_domain_from_template_schema = cls(
            name=name,
            admin_email=admin_email,
            admin_first_name=admin_first_name,
            admin_id=admin_id,
            admin_last_name=admin_last_name,
            admin_password=admin_password,
            base_url=base_url,
            billing_tier=billing_tier,
            custom_terms=custom_terms,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            id=id,
            status=status,
            type_=type_,
        )

        system_domain_from_template_schema.additional_properties = d
        return system_domain_from_template_schema

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
