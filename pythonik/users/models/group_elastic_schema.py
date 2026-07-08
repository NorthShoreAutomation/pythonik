from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_elastic_schema_default_user_type_type_1 import (
        GroupElasticSchemaDefaultUserTypeType1,
    )
    from ..models.group_elastic_schema_group_type_type_1 import (
        GroupElasticSchemaGroupTypeType1,
    )


T = TypeVar("T", bound="GroupElasticSchema")


@_attrs_define
class GroupElasticSchema:
    """
    Attributes:
        name (str):
        alias (None | str | Unset):
        date_created (None | str | Unset):
        date_modified (None | str | Unset):
        default_user_type (GroupElasticSchemaDefaultUserTypeType1 | None | Unset):
        description (None | str | Unset):
        external_id (None | str | Unset):
        group_type (GroupElasticSchemaGroupTypeType1 | None | Unset):
        id (None | Unset | UUID):
        is_legacy_everyone (bool | None | Unset):
        is_saml_group (bool | None | Unset):
        saml_primary_group_priority (int | None | Unset):
    """

    name: str
    alias: None | str | Unset = UNSET
    date_created: None | str | Unset = UNSET
    date_modified: None | str | Unset = UNSET
    default_user_type: GroupElasticSchemaDefaultUserTypeType1 | None | Unset = UNSET
    description: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    group_type: GroupElasticSchemaGroupTypeType1 | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_legacy_everyone: bool | None | Unset = UNSET
    is_saml_group: bool | None | Unset = UNSET
    saml_primary_group_priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.group_elastic_schema_default_user_type_type_1 import (
            GroupElasticSchemaDefaultUserTypeType1,
        )
        from ..models.group_elastic_schema_group_type_type_1 import (
            GroupElasticSchemaGroupTypeType1,
        )

        name = self.name

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = self.date_modified

        default_user_type: dict[str, Any] | None | Unset
        if isinstance(self.default_user_type, Unset):
            default_user_type = UNSET
        elif isinstance(self.default_user_type, GroupElasticSchemaDefaultUserTypeType1):
            default_user_type = self.default_user_type.to_dict()
        else:
            default_user_type = self.default_user_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        group_type: dict[str, Any] | None | Unset
        if isinstance(self.group_type, Unset):
            group_type = UNSET
        elif isinstance(self.group_type, GroupElasticSchemaGroupTypeType1):
            group_type = self.group_type.to_dict()
        else:
            group_type = self.group_type

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_legacy_everyone: bool | None | Unset
        if isinstance(self.is_legacy_everyone, Unset):
            is_legacy_everyone = UNSET
        else:
            is_legacy_everyone = self.is_legacy_everyone

        is_saml_group: bool | None | Unset
        if isinstance(self.is_saml_group, Unset):
            is_saml_group = UNSET
        else:
            is_saml_group = self.is_saml_group

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
        if saml_primary_group_priority is not UNSET:
            field_dict["saml_primary_group_priority"] = saml_primary_group_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_elastic_schema_default_user_type_type_1 import (
            GroupElasticSchemaDefaultUserTypeType1,
        )
        from ..models.group_elastic_schema_group_type_type_1 import (
            GroupElasticSchemaGroupTypeType1,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_date_created(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_default_user_type(
            data: object,
        ) -> GroupElasticSchemaDefaultUserTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_user_type_type_1 = (
                    GroupElasticSchemaDefaultUserTypeType1.from_dict(data)
                )

                return default_user_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GroupElasticSchemaDefaultUserTypeType1 | None | Unset, data)

        default_user_type = _parse_default_user_type(d.pop("default_user_type", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_group_type(
            data: object,
        ) -> GroupElasticSchemaGroupTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_type_1 = GroupElasticSchemaGroupTypeType1.from_dict(data)

                return group_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GroupElasticSchemaGroupTypeType1 | None | Unset, data)

        group_type = _parse_group_type(d.pop("group_type", UNSET))

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

        def _parse_is_legacy_everyone(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_legacy_everyone = _parse_is_legacy_everyone(
            d.pop("is_legacy_everyone", UNSET)
        )

        def _parse_is_saml_group(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_saml_group = _parse_is_saml_group(d.pop("is_saml_group", UNSET))

        def _parse_saml_primary_group_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        saml_primary_group_priority = _parse_saml_primary_group_priority(
            d.pop("saml_primary_group_priority", UNSET)
        )

        group_elastic_schema = cls(
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
            saml_primary_group_priority=saml_primary_group_priority,
        )

        group_elastic_schema.additional_properties = d
        return group_elastic_schema

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
