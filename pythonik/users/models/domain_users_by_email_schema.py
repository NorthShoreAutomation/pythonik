from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_users_by_email_schema_mfa_methods_item import (
    DomainUsersByEmailSchemaMfaMethodsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_users_by_email_schema_facets import (
        DomainUsersByEmailSchemaFacets,
    )
    from ..models.user_elastic import UserElastic


T = TypeVar("T", bound="DomainUsersByEmailSchema")


@_attrs_define
class DomainUsersByEmailSchema:
    """
    Attributes:
        facets (DomainUsersByEmailSchemaFacets | Unset):
        first_url (str | Unset):
        last_url (str | Unset):
        mfa_methods (list[DomainUsersByEmailSchemaMfaMethodsItem] | Unset):
        mfa_required (bool | Unset):
        next_url (str | Unset):
        objects (list[UserElastic] | Unset):
        page (int | Unset):
        pages (int | Unset):
        per_page (int | Unset):
        prev_url (str | Unset):
        total (int | Unset):
    """

    facets: DomainUsersByEmailSchemaFacets | Unset = UNSET
    first_url: str | Unset = UNSET
    last_url: str | Unset = UNSET
    mfa_methods: list[DomainUsersByEmailSchemaMfaMethodsItem] | Unset = UNSET
    mfa_required: bool | Unset = UNSET
    next_url: str | Unset = UNSET
    objects: list[UserElastic] | Unset = UNSET
    page: int | Unset = UNSET
    pages: int | Unset = UNSET
    per_page: int | Unset = UNSET
    prev_url: str | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.facets, Unset):
            facets = self.facets.to_dict()

        first_url = self.first_url

        last_url = self.last_url

        mfa_methods: list[str] | Unset = UNSET
        if not isinstance(self.mfa_methods, Unset):
            mfa_methods = []
            for mfa_methods_item_data in self.mfa_methods:
                mfa_methods_item = mfa_methods_item_data.value
                mfa_methods.append(mfa_methods_item)

        mfa_required = self.mfa_required

        next_url = self.next_url

        objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()
                objects.append(objects_item)

        page = self.page

        pages = self.pages

        per_page = self.per_page

        prev_url = self.prev_url

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if facets is not UNSET:
            field_dict["facets"] = facets
        if first_url is not UNSET:
            field_dict["first_url"] = first_url
        if last_url is not UNSET:
            field_dict["last_url"] = last_url
        if mfa_methods is not UNSET:
            field_dict["mfa_methods"] = mfa_methods
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required
        if next_url is not UNSET:
            field_dict["next_url"] = next_url
        if objects is not UNSET:
            field_dict["objects"] = objects
        if page is not UNSET:
            field_dict["page"] = page
        if pages is not UNSET:
            field_dict["pages"] = pages
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if prev_url is not UNSET:
            field_dict["prev_url"] = prev_url
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_users_by_email_schema_facets import (
            DomainUsersByEmailSchemaFacets,
        )
        from ..models.user_elastic import UserElastic

        d = dict(src_dict)
        _facets = d.pop("facets", UNSET)
        facets: DomainUsersByEmailSchemaFacets | Unset
        if isinstance(_facets, Unset):
            facets = UNSET
        else:
            facets = DomainUsersByEmailSchemaFacets.from_dict(_facets)

        first_url = d.pop("first_url", UNSET)

        last_url = d.pop("last_url", UNSET)

        _mfa_methods = d.pop("mfa_methods", UNSET)
        mfa_methods: list[DomainUsersByEmailSchemaMfaMethodsItem] | Unset = UNSET
        if _mfa_methods is not UNSET:
            mfa_methods = []
            for mfa_methods_item_data in _mfa_methods:
                mfa_methods_item = DomainUsersByEmailSchemaMfaMethodsItem(
                    mfa_methods_item_data
                )

                mfa_methods.append(mfa_methods_item)

        mfa_required = d.pop("mfa_required", UNSET)

        next_url = d.pop("next_url", UNSET)

        _objects = d.pop("objects", UNSET)
        objects: list[UserElastic] | Unset = UNSET
        if _objects is not UNSET:
            objects = []
            for objects_item_data in _objects:
                objects_item = UserElastic.from_dict(objects_item_data)

                objects.append(objects_item)

        page = d.pop("page", UNSET)

        pages = d.pop("pages", UNSET)

        per_page = d.pop("per_page", UNSET)

        prev_url = d.pop("prev_url", UNSET)

        total = d.pop("total", UNSET)

        domain_users_by_email_schema = cls(
            facets=facets,
            first_url=first_url,
            last_url=last_url,
            mfa_methods=mfa_methods,
            mfa_required=mfa_required,
            next_url=next_url,
            objects=objects,
            page=page,
            pages=pages,
            per_page=per_page,
            prev_url=prev_url,
            total=total,
        )

        domain_users_by_email_schema.additional_properties = d
        return domain_users_by_email_schema

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
