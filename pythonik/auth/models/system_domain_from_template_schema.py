from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
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
        admin_email (str | Unset):
        admin_first_name (str | Unset):
        admin_id (UUID | Unset):
        admin_last_name (str | Unset):
        admin_password (str | Unset):
        base_url (str | Unset):
        billing_tier (SystemDomainFromTemplateSchemaBillingTier | Unset):
        custom_terms (bool | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        id (UUID | Unset):
        status (SystemDomainFromTemplateSchemaStatus | Unset):
        type_ (SystemDomainFromTemplateSchemaType | Unset):
    """

    name: str
    admin_email: str | Unset = UNSET
    admin_first_name: str | Unset = UNSET
    admin_id: UUID | Unset = UNSET
    admin_last_name: str | Unset = UNSET
    admin_password: str | Unset = UNSET
    base_url: str | Unset = UNSET
    billing_tier: SystemDomainFromTemplateSchemaBillingTier | Unset = UNSET
    custom_terms: bool | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    status: SystemDomainFromTemplateSchemaStatus | Unset = UNSET
    type_: SystemDomainFromTemplateSchemaType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        admin_email = self.admin_email

        admin_first_name = self.admin_first_name

        admin_id: str | Unset = UNSET
        if not isinstance(self.admin_id, Unset):
            admin_id = str(self.admin_id)

        admin_last_name = self.admin_last_name

        admin_password = self.admin_password

        base_url = self.base_url

        billing_tier: str | Unset = UNSET
        if not isinstance(self.billing_tier, Unset):
            billing_tier = self.billing_tier.value

        custom_terms = self.custom_terms

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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

        admin_email = d.pop("admin_email", UNSET)

        admin_first_name = d.pop("admin_first_name", UNSET)

        _admin_id = d.pop("admin_id", UNSET)
        admin_id: UUID | Unset
        if isinstance(_admin_id, Unset):
            admin_id = UNSET
        else:
            admin_id = UUID(_admin_id)

        admin_last_name = d.pop("admin_last_name", UNSET)

        admin_password = d.pop("admin_password", UNSET)

        base_url = d.pop("base_url", UNSET)

        _billing_tier = d.pop("billing_tier", UNSET)
        billing_tier: SystemDomainFromTemplateSchemaBillingTier | Unset
        if isinstance(_billing_tier, Unset):
            billing_tier = UNSET
        else:
            billing_tier = SystemDomainFromTemplateSchemaBillingTier(_billing_tier)

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

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _status = d.pop("status", UNSET)
        status: SystemDomainFromTemplateSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SystemDomainFromTemplateSchemaStatus(_status)

        _type_ = d.pop("type", UNSET)
        type_: SystemDomainFromTemplateSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SystemDomainFromTemplateSchemaType(_type_)

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
