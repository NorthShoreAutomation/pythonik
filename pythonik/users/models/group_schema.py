from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_schema_default_user_type import GroupSchemaDefaultUserType
from ..models.group_schema_group_type import GroupSchemaGroupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_categories import RoleCategories


T = TypeVar("T", bound="GroupSchema")


@_attrs_define
class GroupSchema:
    """
    Attributes:
        name (str):
        alias (str | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        default_user_type (GroupSchemaDefaultUserType | Unset):
        description (str | Unset):
        external_id (None | str | Unset):
        group_type (GroupSchemaGroupType | Unset):
        id (UUID | Unset):
        is_legacy_everyone (bool | Unset):
        is_saml_group (bool | Unset):
        logo (str | Unset):
        role_categories (None | RoleCategories | Unset):
        roles (list[str] | Unset):
        saml_primary_group_priority (int | None | Unset):
    """

    name: str
    alias: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    default_user_type: GroupSchemaDefaultUserType | Unset = UNSET
    description: str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    group_type: GroupSchemaGroupType | Unset = UNSET
    id: UUID | Unset = UNSET
    is_legacy_everyone: bool | Unset = UNSET
    is_saml_group: bool | Unset = UNSET
    logo: str | Unset = UNSET
    role_categories: None | RoleCategories | Unset = UNSET
    roles: list[str] | Unset = UNSET
    saml_primary_group_priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.role_categories import RoleCategories

        name = self.name

        alias = self.alias

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        default_user_type: str | Unset = UNSET
        if not isinstance(self.default_user_type, Unset):
            default_user_type = self.default_user_type.value

        description = self.description

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        group_type: str | Unset = UNSET
        if not isinstance(self.group_type, Unset):
            group_type = self.group_type.value

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_legacy_everyone = self.is_legacy_everyone

        is_saml_group = self.is_saml_group

        logo = self.logo

        role_categories: dict[str, Any] | None | Unset
        if isinstance(self.role_categories, Unset):
            role_categories = UNSET
        elif isinstance(self.role_categories, RoleCategories):
            role_categories = self.role_categories.to_dict()
        else:
            role_categories = self.role_categories

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        saml_primary_group_priority: int | None | Unset
        if isinstance(self.saml_primary_group_priority, Unset):
            saml_primary_group_priority = UNSET
        else:
            saml_primary_group_priority = self.saml_primary_group_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if default_user_type is not UNSET:
            field_dict["default_user_type"] = default_user_type
        if description is not UNSET:
            field_dict["description"] = description
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if group_type is not UNSET:
            field_dict["group_type"] = group_type
        if id is not UNSET:
            field_dict["id"] = id
        if is_legacy_everyone is not UNSET:
            field_dict["is_legacy_everyone"] = is_legacy_everyone
        if is_saml_group is not UNSET:
            field_dict["is_saml_group"] = is_saml_group
        if logo is not UNSET:
            field_dict["logo"] = logo
        if role_categories is not UNSET:
            field_dict["role_categories"] = role_categories
        if roles is not UNSET:
            field_dict["roles"] = roles
        if saml_primary_group_priority is not UNSET:
            field_dict["saml_primary_group_priority"] = saml_primary_group_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_categories import RoleCategories

        d = dict(src_dict)
        name = d.pop("name")

        alias = d.pop("alias", UNSET)

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

        _default_user_type = d.pop("default_user_type", UNSET)
        default_user_type: GroupSchemaDefaultUserType | Unset
        if isinstance(_default_user_type, Unset):
            default_user_type = UNSET
        else:
            default_user_type = GroupSchemaDefaultUserType(_default_user_type)

        description = d.pop("description", UNSET)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        _group_type = d.pop("group_type", UNSET)
        group_type: GroupSchemaGroupType | Unset
        if isinstance(_group_type, Unset):
            group_type = UNSET
        else:
            group_type = GroupSchemaGroupType(_group_type)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_legacy_everyone = d.pop("is_legacy_everyone", UNSET)

        is_saml_group = d.pop("is_saml_group", UNSET)

        logo = d.pop("logo", UNSET)

        def _parse_role_categories(data: object) -> None | RoleCategories | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_categories_type_1 = RoleCategories.from_dict(data)

                return role_categories_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RoleCategories | Unset, data)

        role_categories = _parse_role_categories(d.pop("role_categories", UNSET))

        roles = cast(list[str], d.pop("roles", UNSET))

        def _parse_saml_primary_group_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        saml_primary_group_priority = _parse_saml_primary_group_priority(
            d.pop("saml_primary_group_priority", UNSET)
        )

        group_schema = cls(
            name=name,
            alias=alias,
            date_created=date_created,
            date_modified=date_modified,
            default_user_type=default_user_type,
            description=description,
            external_id=external_id,
            group_type=group_type,
            id=id,
            is_legacy_everyone=is_legacy_everyone,
            is_saml_group=is_saml_group,
            logo=logo,
            role_categories=role_categories,
            roles=roles,
            saml_primary_group_priority=saml_primary_group_priority,
        )

        group_schema.additional_properties = d
        return group_schema

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
